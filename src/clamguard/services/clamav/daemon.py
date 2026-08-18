import logging
import os
import time

import pyclamd
from PySide6.QtCore import QThread, Signal

from clamguard.core.initialise import init_clamd, init_freshclam, scan_file

logger = logging.getLogger(__name__)


class FreshClamInit(QThread):
    """Thread to run freshclam and update virus definitions."""

    outputReceived = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self._freshclam_process = None
        self._stop_requested = False

    def _terminate_process(self, process):
        """Helper to safely terminate a subprocess without hanging the thread."""
        if process and process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=3)
            except Exception:
                process.kill()

    def stop_run(self):
        """Request the thread to stop and terminate the process."""
        self._stop_requested = True
        self._terminate_process(self._freshclam_process)

    def run(self):
        logger.info("Starting FreshClam update process...")
        self._freshclam_process = init_freshclam()

        if not self._freshclam_process or self._freshclam_process.stdout is None:
            logger.error("Failed to start freshclam process.")
            return

        try:
            while not self._stop_requested:
                line = self._freshclam_process.stdout.readline()
                if not line:
                    break  # EOF reached

                # Safely decode if the process returns bytes instead of strings
                if isinstance(line, bytes):
                    line = line.decode("utf-8", errors="ignore").strip()
                else:
                    line = line.strip()

                if line:
                    self.outputReceived.emit(line)
        finally:
            self._terminate_process(self._freshclam_process)
            self._freshclam_process = None
            logger.info("FreshClam update process finished.")
            # Note: No need to emit self.finished.emit(), QThread does this automatically.


class ClamDInit(QThread):
    """Thread to start clamd and wait for it to become responsive."""

    status = Signal(dict)  # Fixed syntax from `status: Signal = Signal(dict)`

    def __init__(self) -> None:
        super().__init__()
        self._counter = 1
        self._max_retries = 15
        self._handler: pyclamd.ClamdNetworkSocket | pyclamd.ClamdUnixSocket | None = (
            None
        )
        self._clamd_process = None
        self._stop_requested = False

        if os.name == "nt":
            self._host = "127.0.0.1"
            self._port = 3310
        else:
            from clamguard.core.default import socket_path

            self._socket_path = socket_path

    def _terminate_process(self, process):
        """Helper to safely terminate a subprocess without hanging the thread."""
        if process and process.poll() is None:
            process.terminate()
            try:
                # Wait up to 3 seconds for it to close gracefully
                process.wait(timeout=3)
            except Exception:
                # If it refuses to close, force kill it
                process.kill()

    def stop(self):
        """Stop the thread and terminate the clamd process."""
        self._stop_requested = True
        self._terminate_process(self._clamd_process)

    def run(self):
        logger.info("Starting ClamAV Daemon...")
        self._clamd_process = init_clamd()

        if not self._clamd_process:
            self._emit_status(False, True, "Failed to start ClamAV Daemon process.", 0)
            return

        time.sleep(2)  # Give the daemon a moment to initialize

        while self._counter <= self._max_retries and not self._stop_requested:
            progress = int((self._counter / self._max_retries) * 100)
            self._emit_status(
                False,
                False,
                f"Connecting to ClamAV (Attempt {self._counter}/{self._max_retries})...",
                progress,
            )

            try:
                if os.name == "nt":
                    self._handler = pyclamd.ClamdNetworkSocket(
                        host=self._host, port=self._port
                    )
                else:
                    self._handler = pyclamd.ClamdUnixSocket(
                        self._socket_path.as_posix()
                    )

                if self._handler.ping():
                    logger.info("ClamAV Daemon is online and responsive.")
                    self._emit_status(True, True, "ClamAV Daemon is online.", 100)
                    return  # Success, exit run()

            except pyclamd.ConnectionError as e:
                logger.warning(f"Connection attempt {self._counter} failed: {e}")
            except Exception as e:
                logger.error(f"Unexpected error during ClamAV connection: {e}")

            self._counter += 1

            # Interruptible sleep: checks for cancellation every 0.1s
            for _ in range(20):
                if self._stop_requested:
                    break
                time.sleep(0.1)

        # If we exit the loop, it means we failed to connect or were stopped
        if self._stop_requested:
            self._emit_status(False, True, "Connection cancelled.", 0)
        else:
            logger.error("Couldn't connect to ClamAV Daemon after max retries.")
            self._emit_status(False, True, "Failed to connect to ClamAV.", 0)

        self.stop()  # Terminate the daemon if we couldn't connect

    def _emit_status(self, success: bool, end: bool, message: str, progress: int):
        self.status.emit(
            {
                "success": success,
                "end": end,
                "message": message,
                "progress": progress,
            }
        )


class ClamAVScanner(QThread):
    """Thread to run clamscan on specified paths."""

    outputReceived = Signal(str)

    def __init__(self, paths: list[str], parent=None):
        super().__init__(parent)
        self.paths = paths
        self._scan_process = None
        self._stop_requested = False

    def stop(self):
        """Request the scan to stop and terminate the process."""
        self._stop_requested = True
        self._terminate_process(self._scan_process)

    def run(self):
        logger.info(f"Starting scan for paths: {self.paths}")

        try:
            self._scan_process = scan_file(self.paths)

            if not self._scan_process or self._scan_process.stdout is None:
                logger.error("Failed to start clamscan process.")
                return

            for line in self._scan_process.stdout:
                if self._stop_requested:
                    break

                if isinstance(line, bytes):
                    line = line.decode("utf-8", errors="ignore").rstrip()
                else:
                    line = line.rstrip()

                if line:
                    self.outputReceived.emit(line)

            return_code = self._scan_process.wait()
            logger.info(f"Scan finished with return code: {return_code}")

        except Exception as e:
            logger.error(f"Error during scan: {e}")
        finally:
            self._terminate_process(self._scan_process)
            self._scan_process = None
            logger.info("Scan process cleaned up.")

    def _terminate_process(self, process):
        """Helper to safely terminate a subprocess without hanging the thread."""
        if process and process.poll() is None:
            process.terminate()
            try:
                # Wait up to 3 seconds for it to close gracefully
                process.wait(timeout=3)
            except Exception:
                # If it refuses to close, force kill it
                process.kill()

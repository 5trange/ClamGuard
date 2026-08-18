import logging
import subprocess
import time

import pyclamd
from PySide6.QtCore import QThread, Signal

from clamguard.core.initialise import init_clamd, init_freshclam, scan_file
from clamguard.services.platform import platform_service

logger = logging.getLogger(__name__)


class FreshClamInit(QThread):
    """Thread to run freshclam and update virus definitions."""

    outputReceived = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self._freshclam_process = None
        self._stop_requested = False

    def _terminate_process(self, process):
        if process and process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                process.kill()

    def stop_run(self):
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
                    break

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


class ClamDInit(QThread):
    """Thread to start clamd and wait for it to become responsive."""

    status = Signal(dict)

    def __init__(self) -> None:
        super().__init__()
        self._counter = 1
        self._max_retries = 15
        self._handler = None
        self._clamd_process = None
        self._stop_requested = False

        self._connection_info = platform_service.get_clamav_connection()

    def _terminate_process(self, process):
        if process and process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                process.kill()

    def stop(self):
        self._stop_requested = True
        self._terminate_process(self._clamd_process)

    def run(self):
        logger.info("Starting ClamAV Daemon...")
        self._clamd_process = init_clamd()

        if not self._clamd_process:
            self._emit_status(False, True, "Failed to start ClamAV Daemon process.", 0)
            return

        time.sleep(2)

        while self._counter <= self._max_retries and not self._stop_requested:
            progress = int((self._counter / self._max_retries) * 100)
            self._emit_status(
                False,
                False,
                f"Connecting to ClamAV (Attempt {self._counter}/{self._max_retries})...",
                progress,
            )

            try:
                if self._connection_info["type"] == "tcp":
                    self._handler = pyclamd.ClamdNetworkSocket(
                        host=self._connection_info["host"],
                        port=int(self._connection_info["port"]),
                    )
                else:
                    self._handler = pyclamd.ClamdUnixSocket(
                        self._connection_info["path"]
                    )

                if self._handler.ping():
                    logger.info("ClamAV Daemon is online and responsive.")
                    self._emit_status(True, True, "ClamAV Daemon is online.", 100)
                    return

            except pyclamd.ConnectionError as e:
                logger.warning(f"Connection attempt {self._counter} failed: {e}")
            except Exception as e:
                logger.error(f"Unexpected error during ClamAV connection: {e}")

            self._counter += 1

            for _ in range(20):
                if self._stop_requested:
                    break
                time.sleep(0.1)

        if self._stop_requested:
            self._emit_status(False, True, "Connection cancelled.", 0)
        else:
            logger.error("Couldn't connect to ClamAV Daemon after max retries.")
            self._emit_status(False, True, "Failed to connect to ClamAV.", 0)

        self.stop()

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
        if process and process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=3)
            except Exception:
                process.kill()

import os
import time

import pyclamd
from PySide6.QtCore import QThread, Signal

from clamguard.core.initialise import init_clamd, init_freshclam, scan_file


class FreshClamInit(QThread):
    outputReceived = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.freshclam_process = None
        self._stop_requested = False

    def stop_run(self):
        self._stop_requested = True
        if self.freshclam_process and self.freshclam_process.poll() is None:
            self.freshclam_process.terminate()

    def run(self):
        self.freshclam_process = init_freshclam()

        while not self._stop_requested:
            if self.freshclam_process is None or self.freshclam_process.stdout is None:
                return
            line = self.freshclam_process.stdout.readline()
            if not line:
                break
            self.outputReceived.emit(line.strip())

        if self.freshclam_process and self.freshclam_process.poll() is None:
            self.freshclam_process.terminate()

        self.finished.emit()


# ClamAV in window uses tcp to access the details
# but linux and others uses socket
class ClamDInit(QThread):
    status = Signal(dict)

    def __init__(self) -> None:
        print("ClamDInit created", id(self))
        super().__init__()
        self.counter = 1
        self.max_retries = 10
        self.handler = None
        self.clamd_process = None

        if os.name == "nt":
            self.host = "127.0.0.1"
            self.port = 3310
        else:
            from clamguard.core.default import socket_path

            self.socket_path = socket_path

    def stop(self):
        if self.clamd_process and self.clamd_process.poll() is None:
            self.clamd_process.terminate()

    def run(self):
        print("ClamD run started")
        self.clamd_process = init_clamd()
        time.sleep(2)
        while self.counter <= self.max_retries:
            self.status.emit(
                {
                    "success": False,
                    "end": False,
                    "message": "Connecting with ClamAV",
                    "progress": 50,
                }
            )
            try:
                if os.name == "nt":
                    self.handler = pyclamd.ClamdNetworkSocket(
                        host=self.host,
                        port=self.port,
                    )
                else:
                    self.handler = pyclamd.ClamdUnixSocket(
                        self.socket_path.as_posix(),
                    )

                if self.handler.ping():
                    print("ClamAV Daemon is online")
                    self.status.emit(
                        {
                            "success": True,
                            "end": True,
                            "message": "ClamAV Daemon is online.",
                            "progress": 100,
                        }
                    )
                    return
            except pyclamd.ConnectionError as e:
                print(type(e), e)
            finally:
                print("ClamD run ended")

            print(f"Connection failed. Retries left: {self.max_retries - self.counter}")

            self.counter += 1
            time.sleep(2)

        print("Couldn't connect to ClamAV Daemon!")

        self.stop()

        self.status.emit(
            {
                "success": False,
                "end": True,
                "message": "Failed to connect to ClamAV.",
                "progress": 0,
            }
        )


class ClamAVScanner(QThread):
    outputReceived = Signal(str)

    def __init__(self, paths: list[str], parent=None):
        super().__init__(parent)

        self.paths = paths
        self.clamscan_process = None

    def run(self):
        process = None

        try:
            process = scan_file(self.paths)
            self.clamscan_process = process

            if process is None or process.stdout is None:
                return

            for line in process.stdout:
                self.outputReceived.emit(line.rstrip())

            return_code = process.wait()

            print(
                f"Scan finished with return code: {return_code}"
            )

        finally:
            if process is not None and process.poll() is None:
                    process.terminate()
                    process.wait()

            self.clamscan_process = None

    def stop(self):
        process = self.clamscan_process

        if process is not None and process.poll() is None:
            process.terminate()

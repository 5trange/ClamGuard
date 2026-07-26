import os
import time

import pyclamd
from PySide6.QtCore import QThread, Signal

from core.initialise import init_clamd, init_freshclam


class FreshClamInit(QThread):
    outputReceived = Signal(str)
    finished = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.freshclam_process = None

    def stop_run(self):
        if self.freshclam_process:
            self.freshclam_process.terminate()
            self.freshclam_process = None

    def run(self):
        self.freshclam_process = init_freshclam()
        if self.freshclam_process is None or self.freshclam_process.stdout is None:
            return
        while line := self.freshclam_process.stdout.readline():
            self.outputReceived.emit(line.strip())
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
            from core.default import socket_path

            self.socket_path = socket_path

    def __del__(self):
        print("ClamDInit destroyed")
        if self.clamd_process:
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

            except Exception as e:
                print(f"Connection failed: {e}")
            finally:
                print("ClamD run ended")

            print(f"Connection failed. Retries left: {self.max_retries - self.counter}")

            self.counter += 1
            time.sleep(2)

        print("Couldn't connect to ClamAV Daemon!")

        if self.clamd_process:
            self.clamd_process.terminate()

        self.status.emit(
            {
                "success": False,
                "end": True,
                "message": "Failed to connect to ClamAV.",
                "progress": 0,
            }
        )

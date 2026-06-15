import os
import time

from PySide6.QtCore import QThread, Signal
from .initialise import init_clamd
from .default import socket_path

import pyclamd


# ClamAV in window uses tcp to access the details
# but linux and others uses socket
class ClamDInit(QThread):
    status = Signal(dict)

    def __init__(self) -> None:
        super().__init__()
        self.clamd_process = init_clamd()
        self.counter = 1
        self.max_retries = 10
        self.handler = None

        if os.name == "nt":
            self.host = "127.0.0.1"
            self.port = 3310
        else:
            self.socket_path = socket_path

    def run(self):
        while self.counter <= self.max_retries:
            self.status.emit(
                {
                    "success": False,
                    "end": False,
                    "message": "Connecting with ClamAV",
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
                        }
                    )
                    return

            except Exception as e:
                print(f"Connection failed: {e}")

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
            }
        )

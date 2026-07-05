import os
import time

from PySide6.QtCore import QThread, Signal
from .initialise import init_clamd, init_freshclam

import pyclamd


class FreshClamInit(QThread):
    status = Signal(dict)

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        self.status.emit(
            {
                "success": False,
                "end": False,
                "message": "Updating ClamAV database with Freshclam",
                "progress": 0,
            }
        )
        self.freshclam_process = init_freshclam()
        self.status.emit(
            {
                "success": False,
                "end": False,
                "message": "Updating ClamAV database with Freshclam",
                "progress": 10,
            }
        )
        return_code = self.freshclam_process.wait()
        if return_code == 0:
            self.status.emit(
                {
                    "success": True,
                    "end": True,
                    "message": "Freshclam update completed successfully.",
                    "progress": 20,
                }
            )
        else:
            self.status.emit(
                {
                    "success": False,
                    "end": True,
                    "message": f"Freshclam update failed with return code {return_code}.",
                    "progress": 0,
                }
            )


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

        if os.name == "nt":
            self.host = "127.0.0.1"
            self.port = 3310
        else:
            from .default import socket_path

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

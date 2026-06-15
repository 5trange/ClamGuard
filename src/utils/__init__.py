import os
import signal
import socket
import time

from PySide6.QtCore import QThread, Signal
from .initialise import init_clamd
from .default import socket_path

import pyclamd


# ClamAV in window uses tcp to access the details
# but linux and others uses socket
class ClamDInit(QThread):
    failed = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.clamd_process = init_clamd()
        self.counter = 1
        self.max_retries = 50

        if os.name == "nt":
            self.host = "127.0.0.1"
            self.port = 3310
        else:
            self.socket_path = socket_path

    def run(self):
        result = None
        while self.counter <= self.max_retries:
            try:
                if os.name == "nt":
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((self.host, self.port))
                else:
                    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                    result = sock.connect_ex(self.socket_path.as_posix())
                if result == 0:
                    print("ClamAV Daemon is online")
                    sock.close()
                    break
            except socket.error:
                raise
            print(
                f"Connection failed. Retrying... Retries left: {self.max_retries - self.counter}"
            )
            time.sleep(2)
            self.counter = self.counter + 1
        if result and result != 0:
            print("Couldn't connect to ClamAV Daemon!")
            if self.clamd_process:
                os.kill(self.clamd_process.pid, signal.SIGTERM)
                self.failed.emit()
                return

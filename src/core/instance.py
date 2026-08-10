
from PySide6.QtCore import QObject
from PySide6.QtNetwork import QLocalServer, QLocalSocket


class InstanceManager(QObject):

    SERVER_NAME = "clamguard-instance"

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self.server = QLocalServer(self)

    def is_running(self) -> bool:
        socket = QLocalSocket()
        socket.connectToServer(self.SERVER_NAME)

        if socket.waitForConnected(100):
            socket.disconnectFromServer()
            return True

        return False

    def start_server(self) -> bool:
        if self.is_running():
            return False

        QLocalServer.removeServer(self.SERVER_NAME)
        if not self.server.listen(self.SERVER_NAME):
            print(f"Failed to listen: {self.server.errorString()}")
            return False

        return True

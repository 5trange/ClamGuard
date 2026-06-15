from PySide6.QtCore import QObject, Signal, Property, Slot
from utils import ClamDInit


class SplashScreenBackend(QObject):
    progressChanged = Signal()
    startupFinished = Signal()
    statusChanged = Signal()

    def __init__(self):
        super().__init__()
        self._progress = 0
        self._status = "Starting modules.."

    def getProgress(self):
        return self._progress

    def setProgress(self, value):
        self._progress = value
        self.progressChanged.emit()

    @Property(str, notify=statusChanged)
    def status(self):
        return self._status

    def setStatus(self, value):
        self._status = value
        self.statusChanged.emit()

    @Slot(dict)
    def on_change(self, message):
        self.setStatus(message.get("message"))
        if not message.get("success") and not message.get("end"):
            self.setProgress(50)
        elif not message.get("success") and message.get("end"):
            self.setProgress(0)
        else:
            self.setProgress(100)

    @Property(int, notify=progressChanged)
    def progress(self):
        return self._progress

    @Slot()
    def start(self):
        self.clamav_thread = ClamDInit()
        self.clamav_thread.finished.connect(self.startupFinished)
        self.clamav_thread.status.connect(self.on_change)
        self.clamav_thread.start()

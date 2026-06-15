from PySide6.QtCore import QObject, Signal, Property, Slot
from utils import ClamDInit


class SplashScreenBackend(QObject):
    progressChanged = Signal()
    startupFinished = Signal()

    def __init__(self):
        super().__init__()
        self._progress = 0

    def getProgress(self):
        return self._progress

    def setProgress(self, value):
        self._progress = value
        self.progressChanged.emit()

    @Slot()
    def start(self):
        self.clamav_thread = ClamDInit()
        self.clamav_thread.finished.connect(self.startupFinished)
        self.clamav_thread.failed.connect(lambda: print("ClamAV Failed to Startup"))
        self.clamav_thread.start()

    @Property(int, notify=progressChanged)
    def progress(self):
        return self._progress

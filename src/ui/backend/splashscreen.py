from PySide6.QtCore import QObject, Signal, Property, Slot
from services.clamav.daemon import FreshClamInit, ClamDInit

class SplashScreenBackend(QObject):
    progressChanged = Signal()
    statusChanged = Signal()
    fatalError = Signal()
    startupFinished = Signal()

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
            self.setProgress(message.get("progress", 0))
        elif not message.get("success") and message.get("end"):
            self.setProgress(message.get("progress", 0))
            self.fatalError.emit()
        elif message.get("success") and message.get("end"):
            self.setProgress(100)
            self.startupFinished.emit()

    @Property(int, notify=progressChanged)
    def progress(self):
        return self._progress

    @Slot(dict)
    def on_freshclam_status(self, message):
        if not message["end"]:
            return

        # Don't continue if FreshClam failed
        if not message["success"]:
            self.setProgress(0)
            self.fatalError.emit()
            return

        self.clamav_thread = ClamDInit()
        self.clamav_thread.status.connect(self.on_change)
        self.clamav_thread.finished.connect(lambda: print("ClamD thread finished"))
        self.clamav_thread.start()

    @Slot()
    def start(self):
        self.freshclam_thread = FreshClamInit()
        self.freshclam_thread.status.connect(self.on_freshclam_status)
        self.freshclam_thread.finished.connect(
            lambda: print("FreshClam thread finished")
        )
        self.freshclam_thread.start()

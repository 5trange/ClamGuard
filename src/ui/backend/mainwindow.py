from PySide6.QtCore import Property, QObject, QUrl, Signal, Slot
from PySide6.QtQuick import QQuickWindow

from core.paths import get_full_scan_path, get_quick_scan_path
from services.clamav.daemon import ClamAVScanner, FreshClamInit


class MainWindowBackend(QObject):
    windowTitleChanged = Signal()
    windowWidthChanged = Signal()
    windowHeightChanged = Signal()
    engineVersionChanged = Signal()
    updateStarted = Signal()
    updateFinished = Signal()
    updateOutputReceived = Signal(str)
    runStarted = Signal()
    runFinished = Signal()
    runOutputReceived = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._window_title = "ClamGuard Antivirus"
        self._window_width = 800
        self._window_height = 600
        self._engine_version = "Engine Version 1.3.0"
        self.update_worker: FreshClamInit | None = None
        self.scan_worker: ClamAVScanner | None = None

    @Property(str, notify=windowTitleChanged)
    def windowTitle(self):
        return self._window_title

    @Property(int, notify=windowWidthChanged)
    def windowWidth(self):
        return self._window_width

    @Property(int, notify=windowHeightChanged)
    def windowHeight(self):
        return self._window_height

    @Property(str, notify=engineVersionChanged)
    def engineVersion(self):
        return self._engine_version

    @Slot(QQuickWindow)
    def minimizeWindow(self, window: QQuickWindow):
        window.showMinimized()

    @Slot(QQuickWindow)
    def hideToTray(self, window: QQuickWindow):
        window.hide()

    @Slot()
    def cancelUpdate(self):
        if self.update_worker:
            self.update_worker.stop_run()
            self.update_worker = None

    @Slot()
    def checkForUpdates(self):
        self.update_worker = FreshClamInit()
        self.update_worker.started.connect(self.updateStarted)
        self.update_worker.outputReceived.connect(self.updateOutputReceived)
        self.update_worker.finished.connect(self.updateFinished)
        self.update_worker.start()

    @Slot()
    def quickScan(self):
        paths = get_quick_scan_path()
        paths = [str(path) for path in paths]
        self.scan_worker = ClamAVScanner(paths)
        self.scan_worker.started.connect(self.runStarted)
        self.scan_worker.outputReceived.connect(self.runOutputReceived.emit)
        self.scan_worker.finished.connect(self.runFinished)
        self.scan_worker.start()
        self.runOutputReceived.emit("Scan started for " + str(paths))

    @Slot()
    def fullScan(self):
        paths = get_full_scan_path()
        paths = [str(path) for path in paths]
        self.scan_worker = ClamAVScanner(paths)
        self.scan_worker.started.connect(self.runStarted)
        self.scan_worker.outputReceived.connect(self.runOutputReceived.emit)
        self.scan_worker.finished.connect(self.runFinished)
        self.scan_worker.start()
        self.runOutputReceived.emit("Scan started for " + str(paths))

    @Slot(QUrl)
    def customScan(self, path: QUrl):
        self.scan_worker = ClamAVScanner([path.toLocalFile()])
        self.scan_worker.started.connect(self.runStarted)
        self.scan_worker.outputReceived.connect(self.runOutputReceived.emit)
        self.scan_worker.finished.connect(self.runFinished)
        self.scan_worker.start()
        self.runOutputReceived.emit("Scan started for " + path.toLocalFile())

    @Slot()
    def cancelScan(self):
        if self.scan_worker:
            self.scan_worker.stop()
            self.runOutputReceived.emit("Scan cancelled")

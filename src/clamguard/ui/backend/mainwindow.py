import re

from PySide6.QtCore import Property, QObject, QUrl, Signal, Slot
from PySide6.QtQuick import QQuickWindow

from clamguard.core.paths import get_full_scan_path, get_quick_scan_path
from clamguard.models.quarantine import QuarantineItem
from clamguard.services.clamav.daemon import ClamAVScanner, FreshClamInit

DICT_FORMAT = re.compile(
    r"^(?P<file_path>.+/)"
    r"(?P<file_name>[^/]+):"
    r"(?:\s+(?P<type>.+?))?"
    r"\s+(?P<status>FOUND|OK)$"
)


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

    def __init__(self, quarantineModel, parent=None):
        super().__init__(parent)
        self._window_title = "ClamGuard Antivirus"
        self._window_width = 800
        self._window_height = 600
        self._engine_version = "Engine Version 1.3.0"
        self.update_worker: FreshClamInit | None = None
        self.scan_worker: ClamAVScanner | None = None
        self.quarantine_model = quarantineModel

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
        if self.update_worker is not None and self.update_worker.isRunning():
            return

        self.update_worker = FreshClamInit()
        self.update_worker.started.connect(self.updateStarted)
        self.update_worker.outputReceived.connect(self.updateOutputReceived)
        self.update_worker.finished.connect(self.updateFinished)
        self.update_worker.finished.connect(self.updateWorkerFinished)
        self.update_worker.start()

    def updateWorkerFinished(self):
        if self.update_worker is None:
            return

        self.update_worker.deleteLater()
        self.update_worker = None

    @Slot(str)
    def findVirus(self, file_path: str):
        match = DICT_FORMAT.match(file_path)
        if not match:
            return

        if match:
            file_path = match.group("file_path")
            file_name = match.group("file_name")
            file_type = match.group("type")
            status = match.group("status")
            if status == "FOUND":
                self.quarantine_model.addItem(file_name, file_type, file_path)
                self.runOutputReceived.emit(f"Quarantined: {file_name}")
            else:
                del match

    def scanFinished(self):
        if self.scan_worker is None:
            return

        self.scan_worker.deleteLater()
        self.scan_worker = None

    def _scanInProgress(self) -> bool:
        return self.scan_worker is not None and self.scan_worker.isRunning()

    @Slot()
    def quickScan(self):
        if self._scanInProgress():
            return

        paths = get_quick_scan_path()
        paths = [str(path) for path in paths]
        self.scan_worker = ClamAVScanner(paths)
        self.scan_worker.started.connect(self.runStarted)
        self.scan_worker.started.connect(
            lambda: self.runOutputReceived.emit("Scan started for " + str(paths))
        )
        self.scan_worker.outputReceived.connect(self.runOutputReceived.emit)
        self.scan_worker.outputReceived.connect(self.findVirus)
        self.scan_worker.finished.connect(self.runFinished)
        self.scan_worker.finished.connect(self.scanFinished)
        self.scan_worker.start()

    @Slot()
    def fullScan(self):
        if self._scanInProgress():
            return

        paths = get_full_scan_path()
        paths = [str(path) for path in paths]
        self.scan_worker = ClamAVScanner(paths)
        self.scan_worker.started.connect(self.runStarted)
        self.scan_worker.started.connect(
            lambda: self.runOutputReceived.emit("Scan started for " + str(paths))
        )
        self.scan_worker.outputReceived.connect(self.runOutputReceived.emit)
        self.scan_worker.outputReceived.connect(self.findVirus)
        self.scan_worker.finished.connect(self.runFinished)
        self.scan_worker.finished.connect(self.scanFinished)
        self.scan_worker.start()

    @Slot(QUrl)
    def customScan(self, path: QUrl):
        if self._scanInProgress():
            return

        self.scan_worker = ClamAVScanner([path.toLocalFile()])
        self.scan_worker.started.connect(self.runStarted)
        self.scan_worker.started.connect(
            lambda: self.runOutputReceived.emit(
                "Scan started for " + str(path.toLocalFile())
            )
        )
        # self.scan_worker.outputReceived.connect(self.runOutputReceived.emit)
        self.scan_worker.outputReceived.connect(self.findVirus)
        self.scan_worker.finished.connect(self.runFinished)
        self.scan_worker.finished.connect(self.scanFinished)
        self.scan_worker.start()

    @Slot()
    def cancelScan(self):
        if self.scan_worker:
            self.scan_worker.stop()
            self.runOutputReceived.emit("Scan cancelled")

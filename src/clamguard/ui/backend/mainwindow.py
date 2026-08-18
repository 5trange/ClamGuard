import re

from PySide6.QtCore import Property, QObject, QUrl, Signal, Slot
from PySide6.QtQuick import QQuickWindow

from clamguard.core.paths import get_full_scan_path, get_quick_scan_path
from clamguard.services.clamav.daemon import ClamAVScanner, FreshClamInit

DICT_FORMAT = re.compile(
    r"^(?P<file_path>.+/)(?P<file_name>[^/]+):\s+(?:(?P<type>.+?)\s+)?(?P<status>FOUND|OK)$"
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
        self._engine_version = "Engine Version 1.3.0"

        self.update_worker = None
        self.scan_worker = None
        self.quarantine_model = quarantineModel

    @Property(str, notify=engineVersionChanged)
    def engineVersion(self):
        return self._engine_version

    @Slot(QQuickWindow)
    def minimizeWindow(self, window: QQuickWindow):
        window.showMinimized()

    @Slot(QQuickWindow)
    def hideToTray(self, window: QQuickWindow):
        window.hide()

    # ==========================================
    # UPDATE LOGIC
    # ==========================================
    @Slot()
    def checkForUpdates(self):
        if self.update_worker and self.update_worker.isRunning():
            return

        self.update_worker = FreshClamInit()
        self._connect_worker(
            self.update_worker,
            self.updateStarted,
            self.updateFinished,
            self.updateOutputReceived,
        )
        self.update_worker.finished.connect(self._cleanup_update_worker)
        self.update_worker.start()

    @Slot()
    def cancelUpdate(self):
        if self.update_worker:
            self.update_worker.stop_run()

    def _cleanup_update_worker(self):
        if self.update_worker:
            self.update_worker.deleteLater()
            self.update_worker = None

    # ==========================================
    # SCAN LOGIC
    # ==========================================
    def _start_scan(self, paths: list[str]):
        if self.scan_worker and self.scan_worker.isRunning():
            return

        self.scan_worker = ClamAVScanner(paths)
        self._connect_worker(
            self.scan_worker, self.runStarted, self.runFinished, self.runOutputReceived
        )

        # Scan-specific connections
        self.scan_worker.started.connect(
            lambda: self.runOutputReceived.emit(f"Scan started for {paths}")
        )
        self.scan_worker.outputReceived.connect(self._process_scan_output)
        self.scan_worker.finished.connect(self._cleanup_scan_worker)
        self.scan_worker.finished.connect(
            lambda: self.runOutputReceived.emit("Scan has ended")
        )

        self.scan_worker.start()

    def _connect_worker(self, worker, started_sig, finished_sig, output_sig):
        """Helper to avoid repeating signal connections."""
        worker.started.connect(started_sig)
        worker.finished.connect(finished_sig)
        worker.outputReceived.connect(output_sig)

    def _process_scan_output(self, output: str):
        """Parses ClamAV output and handles quarantining."""
        match = DICT_FORMAT.match(output)
        if match:
            status = match.group("status")
            if status == "FOUND":
                file_path = match.group("file_path")
                file_name = match.group("file_name")
                file_type = match.group("type") or "Unknown"

                self.quarantine_model.addItem(file_name, file_type, file_path)
                self.runOutputReceived.emit(f"Quarantined: {file_name}")

    def _cleanup_scan_worker(self):
        if self.scan_worker:
            self.scan_worker.deleteLater()
            self.scan_worker = None

    @Slot()
    def quickScan(self):
        paths = [str(p) for p in get_quick_scan_path()]
        self._start_scan(paths)

    @Slot()
    def fullScan(self):
        paths = [str(p) for p in get_full_scan_path()]
        self._start_scan(paths)

    @Slot(QUrl)
    def customScan(self, path: QUrl):
        self._start_scan([path.toLocalFile()])

    @Slot()
    def cancelScan(self):
        if self.scan_worker:
            self.scan_worker.stop()
            self.runOutputReceived.emit("Scan cancelled")

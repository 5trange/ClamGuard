import time

from PySide6.QtCore import Property, QObject, Signal, Slot
from PySide6.QtQuick import QQuickWindow

from services.clamav.daemon import UpdateWorker


class MainWindowBackend(QObject):
    windowTitleChanged = Signal()
    windowWidthChanged = Signal()
    windowHeightChanged = Signal()
    engineVersionChanged = Signal()
    updateStarted = Signal()
    updateFinished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._window_title = "ClamGuard Antivirus"
        self._window_width = 800
        self._window_height = 600
        self._engine_version = "Engine Version 1.3.0"
        self.update_worker = None

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

    @Slot()
    def checkForUpdates(self):
        self.update_worker = UpdateWorker()
        self.update_worker.started.connect(self.updateStarted)
        self.update_worker.finished.connect(self.updateFinished)
        self.update_worker.start()

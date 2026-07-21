from PySide6.QtCore import QObject, Signal, Property, Slot
from PySide6.QtQuick import QQuickWindow

class MainWindowBackend(QObject):

    windowTitleChanged = Signal()
    windowWidthChanged = Signal()
    windowHeightChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._window_title = "ClamGuard Antivirus"
        self._window_width = 800
        self._window_height = 600

    @Property(str, notify=windowTitleChanged)
    def windowTitle(self):
        return self._window_title

    @Property(int, notify=windowWidthChanged)
    def windowWidth(self):
        return self._window_width

    @Property(int, notify=windowHeightChanged)
    def windowHeight(self):
        return self._window_height

    @Slot(QQuickWindow)
    def minimizeWindow(self, window: QQuickWindow):
        window.showMinimized()

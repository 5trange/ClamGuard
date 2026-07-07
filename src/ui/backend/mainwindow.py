from PySide6.QtCore import QObject, Signal, Property, Slot


class MainWindowBackend(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._window_title = "ClamGuard"
        self._window_width = 800
        self._window_height = 600

    @Property(str)
    def windowTitle(self):
        return self._window_title

    @Property(int)
    def windowWidth(self):
        return self._window_width

    @Property(int)
    def windowHeight(self):
        return self._window_height
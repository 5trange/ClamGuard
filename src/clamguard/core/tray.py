from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMenu, QSystemTrayIcon


class SystemTray:
    def __init__(self, app, engine, window, show_window_callback):
        self.app = app
        self.engine = engine
        self.window = window
        self.show_window_callback = show_window_callback

        self.tray = QSystemTrayIcon(app)

        self.tray.setIcon(QIcon(":/img/clamguard.ico"))

        menu = QMenu()

        open_action = QAction("Open", menu)
        open_action.triggered.connect(lambda: self.show_window_callback(self.window))

        quit_action = QAction("Quit", menu)
        quit_action.triggered.connect(self.quit)

        menu.addAction(open_action)
        menu.addSeparator()
        menu.addAction(quit_action)

        self.tray.setContextMenu(menu)
        self.tray.show()

    def quit(self):
        self.tray.hide()
        self.app.quit()

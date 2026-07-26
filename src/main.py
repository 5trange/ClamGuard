import os
import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication

import core.resources_rc
from core.initialise import initialise_config_folder
from ui import show_main_window
from ui.backend.mainwindow import MainWindowBackend
from ui.backend.splashscreen import SplashScreenBackend


def main():
    if os.name == "nt":
        import ctypes

        myappid = "com.clamguard.app"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    initialise_config_folder()

    app = QApplication(sys.argv)
    app.setDesktopFileName("clamguard")

    app.setWindowIcon(QIcon("qrc:/img/clamguard.ico"))
    engine = QQmlApplicationEngine()

    splashscreen_backend = SplashScreenBackend()
    main_window_backend = MainWindowBackend()
    splashscreen_backend.fatalError.connect(engine.quit)
    splashscreen_backend.startupFinished.connect(lambda: show_main_window(engine))

    engine.rootContext().setContextProperty("splashscreen", splashscreen_backend)
    engine.rootContext().setContextProperty("mainwindow", main_window_backend)

    engine.load(QUrl("qrc:/qml/SplashScreen.qml"))

    if not engine.rootObjects():
        print("Error: No root objects loaded. Exiting application.")
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

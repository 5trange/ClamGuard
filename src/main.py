import os
import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication

import core.resources_rc
from core.initialise import initialise_config_folder
from core.instance import InstanceManager
from models.quarantine import QuarantineModel
from ui import create_main_window
from ui.backend.mainwindow import MainWindowBackend
from ui.backend.splashscreen import SplashScreenBackend

instance_manager = InstanceManager()


def set_app_id(app_id: str):
    import ctypes

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)


def main():

    app = QApplication(sys.argv)
    if os.name == "nt":
        set_app_id("com.clamguard.app")
    elif os.name == "linux":
        app.setDesktopFileName("clamguard")

    initialise_config_folder()

    if not instance_manager.start_server():
        print("Failed to start server. Exiting.")
        print(f"already running: {instance_manager.is_running()}")
        sys.exit(0)

    app.setWindowIcon(QIcon("qrc:/img/clamguard.ico"))
    engine = QQmlApplicationEngine()

    quarantineModel = QuarantineModel()

    splashscreen_backend = SplashScreenBackend()
    main_window_backend = MainWindowBackend(quarantineModel)
    splashscreen_backend.fatalError.connect(engine.quit)
    splashscreen_backend.startupFinished.connect(
        lambda: create_main_window(app, engine)
    )

    engine.rootContext().setContextProperty("splashscreen", splashscreen_backend)
    engine.rootContext().setContextProperty("mainwindow", main_window_backend)
    engine.rootContext().setContextProperty("quarantineModel", quarantineModel)

    engine.load(QUrl("qrc:/qml/SplashScreen.qml"))

    if not engine.rootObjects():
        print("Error: No root objects loaded. Exiting application.")
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

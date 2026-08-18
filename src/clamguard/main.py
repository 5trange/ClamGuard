import os
import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication

import clamguard.resources_rc
from clamguard.core.initialise import initialise_config_folder
from clamguard.core.instance import InstanceManager
from clamguard.models.quarantine import QuarantineModel
from clamguard.ui import create_main_window
from clamguard.ui.backend.mainwindow import MainWindowBackend
from clamguard.ui.backend.splashscreen import SplashScreenBackend


def set_app_id(app_id: str):
    import ctypes

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)


def stop_running_processes(splashscreen_backend, main_window_backend):
    """Terminate orphaned processes on exit."""
    splashscreen_backend.stop_clamd()
    if main_window_backend.update_worker:
        main_window_backend.update_worker.stop_run()
    if main_window_backend.scan_worker:
        main_window_backend.scan_worker.stop()


def main():
    app = QApplication(sys.argv)

    if os.name == "nt":
        set_app_id("com.clamguard.app")
    elif os.name == "linux":
        app.setDesktopFileName("clamguard")

    initialise_config_folder()

    instance_manager = InstanceManager()
    if not instance_manager.start_server():
        print("Failed to start server. App already running?")
        sys.exit(0)

    app.setWindowIcon(QIcon("qrc:/img/clamguard.ico"))

    engine = QQmlApplicationEngine()
    quarantineModel = QuarantineModel()
    splashscreen_backend = SplashScreenBackend()
    main_window_backend = MainWindowBackend(quarantineModel)

    # Connect signals
    splashscreen_backend.fatalError.connect(engine.quit)
    splashscreen_backend.startupFinished.connect(
        lambda: create_main_window(app, engine)
    )
    app.aboutToQuit.connect(
        lambda: stop_running_processes(splashscreen_backend, main_window_backend)
    )

    engine.rootContext().setContextProperty("splashscreen", splashscreen_backend)
    engine.rootContext().setContextProperty("mainwindow", main_window_backend)
    engine.rootContext().setContextProperty("quarantineModel", quarantineModel)

    engine.load(QUrl("qrc:/qml/SplashScreen.qml"))

    if not engine.rootObjects():
        print("Error: No root objects loaded. Exiting application.")
        sys.exit(-1)

    sys.exit(app.exec())

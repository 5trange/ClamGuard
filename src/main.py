import os
import sys
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle
from PySide6.QtWidgets import QApplication

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

    QQuickStyle.setStyle("Fusion")
    app = QApplication(sys.argv)

    icon_path = Path(__file__).parent / "ui/qml/img/clamguard.png"
    app.setWindowIcon(QIcon(str(icon_path)))

    engine = QQmlApplicationEngine()

    splashscreen_backend = SplashScreenBackend()
    splashscreen_backend.fatalError.connect(engine.quit)
    splashscreen_backend.startupFinished.connect(lambda: show_main_window(engine))
    engine.rootContext().setContextProperty("splashscreen", splashscreen_backend)

    main_window_backend = MainWindowBackend()
    engine.rootContext().setContextProperty("mainwindow", main_window_backend)

    main_window_path = Path(__file__).parent / "ui/qml/SplashScreen.qml"
    engine.load(str(main_window_path))

    if not engine.rootObjects():
        print("Error: No root objects loaded. Exiting application.")
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

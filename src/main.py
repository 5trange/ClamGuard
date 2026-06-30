from pathlib import Path
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from ui.mainwindow import MainWindowBackend
from utils.initialise import initialise_config_folder
from ui.splashscreen import SplashScreenBackend


def main():
    initialise_config_folder()
    app = QApplication(sys.argv)

    icon_path = Path(__file__).parent / "ui/qml/img/clamguard.png"
    app.setWindowIcon(QIcon(str(icon_path)))

    engine = QQmlApplicationEngine()
    
    splashscreen_backend = SplashScreenBackend()
    engine.rootContext().setContextProperty("splashscreen", splashscreen_backend)

    main_window_backend = MainWindowBackend()
    engine.rootContext().setContextProperty("mainwindow", main_window_backend)

    main_window_path = Path(__file__).parent / "ui/qml/MainWindow.qml"
    engine.load(str(main_window_path))

    if not engine.rootObjects():
        print("Error: No root objects loaded. Exiting application.")
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

from pathlib import Path

from .backend.mainwindow import MainWindowBackend
from PySide6.QtQml import QQmlApplicationEngine


def show_main_window(engine: QQmlApplicationEngine):
    print("show_main_window called")
    main_window_backend = MainWindowBackend()
    engine.rootContext().setContextProperty("mainwindow", main_window_backend)
    main_window_path = Path(__file__).parent / "qml" / "MainWindow.qml"
    engine.load(str(main_window_path))


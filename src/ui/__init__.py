from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine

from .backend.mainwindow import MainWindowBackend


def show_main_window(engine: QQmlApplicationEngine):
    print("show_main_window called")
    main_window_backend = MainWindowBackend()
    engine.rootContext().setContextProperty("mainwindow", main_window_backend)
    engine.load(QUrl("qrc:/qml/MainWindow.qml"))

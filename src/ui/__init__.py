from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine


def show_main_window(engine: QQmlApplicationEngine):
    print("show_main_window called")
    engine.load(QUrl("qrc:/qml/MainWindow.qml"))
    if not engine.rootObjects():
        print("Failed to load MainWindow.qml")

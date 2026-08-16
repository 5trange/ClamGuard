from typing import cast

from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick import QQuickWindow
from PySide6.QtWidgets import QApplication

from clamguard.core.tray import SystemTray


def show_main_window(window: QQuickWindow):
    if window is None:
        return

    window.show()
    window.raise_()
    window.requestActivate()

def create_main_window(app: QApplication, engine: QQmlApplicationEngine):
    before = set(engine.rootObjects())
    engine.load(QUrl("qrc:/qml/MainWindow.qml"))
    after = set(engine.rootObjects())
    new_objects = after - before
    if not new_objects:
        print("Failed to load MainWindow.qml")
        return

    window = new_objects.pop()
    window = cast(QQuickWindow, window)
    window.setIcon(QIcon(":/img/clamguard.ico"))

    SystemTray(app=app, engine=engine, window=window, show_window_callback=show_main_window)

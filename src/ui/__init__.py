from typing import cast

from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick import QQuickWindow


def show_main_window(engine: QQmlApplicationEngine):
    print("show_main_window called")
    engine.load(QUrl("qrc:/qml/MainWindow.qml"))
    if not engine.rootObjects():
        print("Failed to load MainWindow.qml")
    window = engine.rootObjects()[0]
    window = cast(QQuickWindow, engine.rootObjects()[0])
    window.setIcon(QIcon(":/img/clamguard.png"))

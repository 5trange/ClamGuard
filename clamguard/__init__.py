from PySide6.QtWidgets import QApplication
import start_clamguard
import sys

class ClamGuard:

    def __init__(self):
        app = QApplication(sys.argv)
        window = start_clamguard.SplashScreen()
        sys.exit(app.exec())

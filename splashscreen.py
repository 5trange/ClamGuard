from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import sys
from time import sleep


class splashscreen():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.img = QPixmap('resource/ss.jpg')
        self.ss = QSplashScreen(self.img)
        self.ss.show()
        sleep(2)
    def __del__(self):
        try:
            self.ss.flush()
            sys.exit(self.app.exec_())
        except:
            print("Have Error")
s = splashscreen()

import sys
import platform
import sys
import time
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.QtCore import *
from process import *

#Importing UI File
from mainWindow import Ui_mainWindow

class WorkerThread(QThread):
    # Create a worker thread
    out_string = pyqtSignal(str)  # Using String type for emitter.
    # finish_function = pyqtSignal(str)
    runobj = RunProcess()

    def run(self):
        buffer = self.runobj.run_command('clamscan.exe')
        for i in buffer:
            self.out_string.emit(i)

    def stop(self):
        self.runobj.kill_command()
        self.terminate()

class MainWindow(QMainWindow):
    def __init__(self):
        ## Setting Shadow and other UI definitions
        QMainWindow.__init__(self)
        self.ui=Ui_mainWindow()
        self.ui.setupUi(self)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.dropshadowFrame.setGraphicsEffect(self.shadow)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## scanStatus modifiers

        self.ui.scanStatus.setBackgroundVisible(True)
        self.ui.scanStatus.setReadOnly(True)

        ## Moving Window when dragged on Titlebar
        self.ui.titleBar.mouseMoveEvent = self.moveWindow

        ## Page Switching
        ## To ScanPage
        self.ui.scanFrame.mousePressEvent = self.switch_scan
        ## To Homepage from Scanpage
        self.ui.backButton.clicked.connect(self.switch_home)

        #SCANBUTTONS
        self.ui.quickscanButton.clicked.connect(self.startThread)

        ## Window Control Buttons
        self.ui.minButton.clicked.connect(lambda: self.showMinimized())
        self.ui.closeButton.clicked.connect(lambda: self.close())

    ## Mouse Drag Event Handler Code
    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def switch_scan(self, event):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageScan)

    def switch_home(self):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageHome)

    ## THREAD FUNCTIONS

    def startThread(self):
        # Starting worker thread
        self.thread = WorkerThread()
        self.thread.out_string.connect(self.setValue)
        self.thread.start()

    def setValue(self, val):
        # Setting value for plaintext
        self.ui.scanStatus.appendPlainText(val)

    def stopThread(self):
        self.thread.terminate()
        self.ui.scanStatus.clear()
        self.ui.scanStatus.setPlainText("Scan stopped!")



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

# -----------------------------------------------------------------------------
# ui_start.py [Starts UI]

# -----------------------------------------------------------------------------
# Name:        ui_start.py
# Product:     ClamGuard
#
# Authors:      Adith, Bilal, Vinayak
#   ________                ______                     __
#  / ____/ /___ _____ ___  / ____/_  ______ __________/ /
# / /   / / __ `/ __ `__ \/ / __/ / / / __ `/ ___/ __  /
#/ /___/ / /_/ / / / / / / /_/ / /_/ / /_/ / /  / /_/ /
#\____/_/\__,_/_/ /_/ /_/\____/\__,_/\__,_/_/   \__,_/
#
#
#
# Created:     2021/Mar/05
# Copyright:
# Licence:
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

##IMPORTS

import sys
import platform
import sys
import time
import os
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
        buffer = self.runobj.run_command('clamdscan.exe')
        for i in buffer:
            self.out_string.emit(i)

    def stop_thread(self):
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
        self.ui.cancelscanButton.clicked.connect(self.stopThread)

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
        self.ui.scanStatus.clear()

    def setValue(self, val):
        # Setting value for plaintext
        self.ui.scanStatus.appendPlainText(val)

    def stopThread(self):
        try:
            self.thread.stop_thread()
            self.ui.scanStatus.clear()
            self.ui.scanStatus.setPlainText("Scan stopped!")
            os.system("taskkill /f /im clamscan.exe")
        except:
            print('Process is not alive!')



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

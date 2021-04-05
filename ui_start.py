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

#IMPORTS
import sys
import platform
import time
import os
import threading
import signal
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PyQt5.QtCore import *
from process import *
from mainWindow import Ui_mainWindow #IMPORTING MAINWINDOW.PY

#MAINWINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self):
        #SETTING SHADOW AND OTHER WINDOW DEFINITIONS
        QMainWindow.__init__(self)
        self.ui=Ui_mainWindow()
        self.ui.setupUi(self)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.dropshadowFrame.setGraphicsEffect(self.shadow)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) #SETTING FRAMELESS WINDOW
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) #SETTING FRAMEBORDER TO TRANSLUCENT

        #WINDOW CONTROL BUTTONS
        self.ui.minButton.clicked.connect(lambda: self.showMinimized()) #MINIMIZE ON CLICK
        self.ui.closeButton.clicked.connect(lambda: self.close()) #CLOSE ON CLICK

        #TITLEBAR DRAGGING
        self.ui.titleBar.mouseMoveEvent = self.moveWindow

        #SCANSTATUS AND UPDATESTATUS MODIFIERS
        self.ui.scanStatus.setBackgroundVisible(True)
        self.ui.scanStatus.setReadOnly(True)
        self.ui.updateStatus.setBackgroundVisible(True)
        self.ui.updateStatus.setReadOnly(True)

        #ADDING PAGESWITCHING FUNCTIONS TO BUTTONS AND FRAMES
        #TO SCANPAGE FROM HOMEPAGE
        self.ui.scanFrame.mousePressEvent = self.switch_scan
        #TO HOMEPAGE FROM SCANPAGE
        self.ui.homeButton.clicked.connect(self.switch_home)
        #TO UPDATEPAGE FROM HOMEPAGE
        self.ui.updateFrame.mousePressEvent = self.switch_update
        #TO HOMEPAGE FROM UPDATEPAGE
        self.ui.updatehomeButton.clicked.connect(self.switch_home)

        #SCANPAGE FUNCTIONS
        ##QUICKSCAN
        self.ui.quickscanButton.clicked.connect(self.start_quickscan) #STARTS THREAD
        ##FULLSCAN
        self.ui.fullscanButton.clicked.connect(self.start_fullscan) #STARTS THREAD
        #CANCELBUTTON
        self.ui.cancelscanButton.setEnabled(False) #SETS CANCEL BUTTON TO DISABLED UNTIL A SCAN FUNCTION IS STARTED
        self.ui.cancelscanButton.clicked.connect(self.stopscan) #STOPS SUBPROCESS INTURN STOPPING THREAD?


    #MOUSE DRAG EVENT HANDLER
    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    #STACKEDWIDGET PAGE SWITCHING FUNCTIONS
    def switch_scan(self, event):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageScan)

    def switch_update(self, event):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageUpdate)

    def switch_home(self):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageHome)

    #SCAN FUNCTIONS; TWO FUNCTIONS NEEDED TO START EACH SCAN TYPE?
    ##QUICKSCAN
    def start_quickscan(self):
        self.SingleThread = threading.Thread(target = self.quickscan)
        self.SingleThread.start()

    def quickscan(self):
        self.ui.cancelscanButton.setEnabled(True) #SETS CANCEL BUTTON TO ENABLED
        self.ui.quickscanButton.setEnabled(False) #SETS QUICKSCAN BUTTON TO DISABLED
        self.ui.fullscanButton.setEnabled(False) #SETS FULLSCAN BUTTON TO DISABLED
        self.ui.customscanButton.setEnabled(False) #SETS CUSTOMSCAN BUTTON TO DISABLED
        self.ui.homeButton.setEnabled(False) #SETS HOME BUTTON TO DISABLED
        self.ui.scanStatus.setPlainText('Scan started, Please wait...')
        self.process = Popen(['clamdscan.exe','--multiscan'], stdout = PIPE, encoding = 'utf-8')
        while(True):
            buffer = self.process.stdout.readline()
            if buffer == '':
                self.ui.cancelscanButton.setEnabled(False) #SETS CANCEL BUTTON TO DISABLED AFTER ENDING THE FUNCTION
                self.ui.cancelscanButton.setEnabled(False) #SETS CANCEL BUTTON TO DISABLED AFTER ENDING THE FUNCTION
                self.ui.quickscanButton.setEnabled(True) #SETS QUICKSCAN BUTTON TO ENABLED
                self.ui.fullscanButton.setEnabled(True) #SETS FULLSCAN BUTTON TO ENABLED
                self.ui.customscanButton.setEnabled(True) #SETS CUSTOMSCAN BUTTON TO ENABLED
                self.ui.homeButton.setEnabled(True) #SETS HOME BUTTON TO ENABLED
                break
            else:
                self.ui.scanStatus.appendPlainText(buffer)

    ##FULLSCAN
    def start_fullscan(self):
        self.SingleThread = threading.Thread(target = self.fullscan)
        self.SingleThread.start()

    def fullscan(self):
        self.ui.cancelscanButton.setEnabled(True) #SETS CANCEL BUTTON TO ENABLED
        self.ui.quickscanButton.setEnabled(False) #SETS QUICKSCAN BUTTON TO DISABLED
        self.ui.fullscanButton.setEnabled(False) #SETS FULLSCAN BUTTON TO DISABLED
        self.ui.customscanButton.setEnabled(False) #SETS CUSTOMSCAN BUTTON TO DISABLED
        self.ui.homeButton.setEnabled(False) #SETS HOME BUTTON TO DISABLED
        self.ui.scanStatus.setPlainText('Full system scan started. Please note that this might take some time to complete. ')
        self.process = Popen(['clamdscan.exe','--multiscan'], stdout = PIPE, encoding = 'utf-8')
        while(True):
            buffer = self.process.stdout.readline()
            if buffer == '':
                self.ui.cancelscanButton.setEnabled(False) #SETS CANCEL BUTTON TO DISABLED AFTER ENDING THE FUNCTION
                self.ui.quickscanButton.setEnabled(True) #SETS QUICKSCAN BUTTON TO ENABLED
                self.ui.fullscanButton.setEnabled(True) #SETS FULLSCAN BUTTON TO ENABLED
                self.ui.customscanButton.setEnabled(True) #SETS CUSTOMSCAN BUTTON TO ENABLED
                self.ui.homeButton.setEnabled(True) #SETS HOME BUTTON TO ENABLED
                break
            else:
                self.ui.scanStatus.appendPlainText(buffer)

    #GENERAL FUNCTION TO KILL POPEN PROCESS WITH SIGTERM FOR A CLEAN EXIT; THREAD SHOULD STOP BY THEN
    def stopscan(self):
        try:
            os.kill(self.process.pid, signal.SIGTERM)
            self.ui.scanStatus.clear()
            self.ui.scanStatus.appendPlainText('Scan stopped.')
            print('Thread stopped.')
            self.ui.cancelscanButton.setEnabled(False) #SETS CANCEL SCAN BUTTON TO DISABLED AFTER SUCESSFUL TERMINATION OF THREAD
            self.ui.quickscanButton.setEnabled(True) #SETS QUICKSCAN BUTTON TO ENABLED
            self.ui.fullscanButton.setEnabled(True) #SETS FULLSCAN BUTTON TO ENABLED
            self.ui.customscanButton.setEnabled(True) #SETS CUSTOMSCAN BUTTON TO ENABLED
            self.ui.homeButton.setEnabled(True) #SETS HOME BUTTON TO ENABLED
        except Exception as e:
            print(f'Something went wrong. Error code: {e}')
            self.ui.cancelscanButton.setEnabled(True) #SETS CANCEL BUTTON TO ENABLED TO TRY AGAIN

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

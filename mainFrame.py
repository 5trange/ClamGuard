# -----------------------------------------------------------------------------
# mainFrame.py [Main Frame]

# -----------------------------------------------------------------------------
# Name:        mainFrame.py
# Product:     ClamGuard
#
# Authors:      Adith, Bilal, Vinayak
#
# Created:     2021/Feb/09
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

# Imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from process import *
import sys
import time
import qdarkstyle


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


class MainFrame(QMainWindow):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("ClamGuard Test SubSystem")
        self.setStyleSheet(qdarkstyle.load_stylesheet())
        self.setFixedSize(800, 600)
        self.initui()

    def initui(self):
        self.scanStatus = QPlainTextEdit(self)
        self.scanStatus.setFixedSize(723, 367)
        self.scanStatus.move(40, 196)
        # self.scanStatus.appendPlainText() Function to append plain text.

        # Setting same function for both buttons for testing purposes.
        self.scanButton = QPushButton(self)
        self.scanButton.setText("Scan Now")
        self.scanButton.move(40, 72)
        self.scanButton.setFixedSize(117, 40)
        self.scanButton.clicked.connect(self.startThread)

        self.stopScan = QPushButton(self)
        self.stopScan.setText("Stop Scan")
        self.stopScan.move(646, 72)
        self.stopScan.setFixedSize(117, 40)
        # Testing thread termination
        self.stopScan.clicked.connect(self.stopThread)

    def startThread(self):
        # Starting worker thread
        self.thread = WorkerThread()
        self.thread.out_string.connect(self.setValue)
        self.thread.start()

    def setValue(self, val):
        # Setting value for plaintext
        self.scanStatus.appendPlainText(val)

    def stopThread(self):
        self.thread.terminate()
        self.scanStatus.clear()
        self.scanStatus.setPlainText("Scan stopped!")


App = QApplication(sys.argv)
window = MainFrame()
window.show()
sys.exit(App.exec())

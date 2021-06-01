# -----------------------------------------------------------------------------
# Name          :   start_clamguard.py
# Product       :   ClamGuard
# Authors       :   Adith, Bilal, Vinayak
# Created       :   May-08-2021
# -----------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------

# Imports
import sys
import platform
import time
import os
import threading
import signal
import webbrowser
import socket
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from subprocess import *
from mainWindow import Ui_mainWindow  # Importing mainWindow.py
from SplashScreen import Ui_SplashScreen  # Importing SplashScreen.py
from filesystemMonitor import * # Importing filesystemMonitor.py

# Globals vars + env path
appdata_dir = os.environ['APPDATA']
win_dir = os.environ['SYSTEMROOT']
root_drive = os.environ['SYSTEMDRIVE']
drivers_dir = win_dir + '\\System32\\Drivers\\'
system32_dir = win_dir + '\\System32\\'


# Splashscreen class
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.main_window = MainWindow()
        self.ui.setupUi(self)

        # Remove titlebar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Dropshadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.show()

        # Start clamd
        try:
            self.clamd_process = Popen(['clamd.exe'], creationflags = CREATE_NO_WINDOW)
        except Exception as e:
            print(f"Debug: Error:{e}")
            raise

        self.init_thread = clamd_init()
        self.init_thread.start()
        self.init_thread.finished.connect(lambda: self.ui.progressBar.setValue(75))
        self.init_thread.finished.connect(lambda: self.start_watchdog())
        self.init_thread.finished.connect(lambda: self.close())
        self.init_thread.finished.connect(lambda: self.main_window.show())

    def start_watchdog(self):
        self.event_handler = SystemHandler()
        self.observer = watchdog.observers.Observer()
        self.observer.schedule(self.event_handler, root_drive, recursive=True)
        print("Debug: ClamGuard WatchDog Started.")

# MainWindow class
class MainWindow(QMainWindow):
    def __init__(self):
        # Shadow+Other functions
        QMainWindow.__init__(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.dropshadowFrame.setGraphicsEffect(self.shadow)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # Setting frameless window
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Setting frame border

        # Window control buttons
        self.ui.minButton.clicked.connect(lambda: self.showMinimized())  # Minimize on click
        self.ui.closeButton.clicked.connect(lambda: self.close())  # Close on click

        # Titlebar dragging
        self.ui.titleBar.mouseMoveEvent = self.moveWindow

        # About page functions
        self.ui.AboutGithub.mousePressEvent = self.openGithub

        # ScanStatus and UpdateStatus modifiers
        self.ui.scanStatus.setBackgroundVisible(True)
        self.ui.scanStatus.setReadOnly(True)
        self.ui.updateStatus.setBackgroundVisible(True)
        self.ui.updateStatus.setReadOnly(True)

        # Page swap functions
        # To scanpage from homepage
        self.ui.scanFrame.mousePressEvent = self.switch_scan
        # To homepage from scanpage
        self.ui.homeButton.clicked.connect(self.switch_home)
        # To updatepage from homepage
        self.ui.updateFrame.mousePressEvent = self.switch_update
        # To homepage from updatepage
        self.ui.updatehomeButton.clicked.connect(self.switch_home)
        # To aboutpage from homepage
        self.ui.aboutLabel.mousePressEvent = self.switch_about
        # To homepage from aboutpage
        self.ui.homeButtonAbout.clicked.connect(self.switch_home)
        # To quarantine from homepage
        self.ui.quarantineLabel.mousePressEvent = self.switch_quarantine
        # To homepage from quarantine
        self.ui.quarantineHomeButton.clicked.connect(self.switch_home)

        # Scan page functions
        self.ui.quickscanButton.clicked.connect(self.launch_quickscan)
        self.ui.fullscanButton.clicked.connect(self.launch_fullscan)
        self.ui.customscanButton.clicked.connect(self.launch_customscan)
        self.ui.cancelscanButton.setEnabled(False)
        self.ui.cancelscanButton.clicked.connect(self.stop_scan)

        # Update page functions
        self.ui.checkUpdate.clicked.connect(self.launch_update)
        self.ui.cancelUpdate.setEnabled(False)
        self.ui.cancelUpdate.clicked.connect(self.stop_update)

        # Quarantine functions
        self.ui.quarantineRefresh.clicked.connect(self.start_quarantine)

    # Mouse drag event handler
    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # Stacked widget functions
    def switch_scan(self, event):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageScan)

    def switch_update(self, event):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageUpdate)

    def switch_home(self):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageHome)

    def switch_about(self, event):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageAbout)

    def switch_quarantine(self, event):
        self.ui.stackedHome.setCurrentWidget(self.ui.pageQuarantine)

    # Quickscan threads and slots
    def launch_quickscan(self):
        self.ui.cancelscanButton.setEnabled(True)
        self.ui.quickscanButton.setEnabled(False)
        self.ui.fullscanButton.setEnabled(False)
        self.ui.customscanButton.setEnabled(False)
        self.ui.homeButton.setEnabled(False)
        self.ui.scanStatus.clear()
        self.ui.scanStatus.appendPlainText(
            "Quick scan started. Please wait...\n\nNOTE: Quick scan is very CPU Intensive, It is recommended to close all programs before scanning.\n\n")
        self.sthread = QuickScan()
        self.sthread.ret.connect(self.set_scan_value)
        self.sthread.start()
        self.sthread.finished.connect(lambda: self.ui.cancelscanButton.setEnabled(False))
        self.sthread.finished.connect(lambda: self.ui.quickscanButton.setEnabled(True))
        self.sthread.finished.connect(lambda: self.ui.fullscanButton.setEnabled(True))
        self.sthread.finished.connect(lambda: self.ui.customscanButton.setEnabled(True))
        self.sthread.finished.connect(lambda: self.ui.homeButton.setEnabled(True))

    # Fullscan threads and slots
    def launch_fullscan(self):
        self.ui.cancelscanButton.setEnabled(True)
        self.ui.quickscanButton.setEnabled(False)
        self.ui.fullscanButton.setEnabled(False)
        self.ui.customscanButton.setEnabled(False)
        self.ui.homeButton.setEnabled(False)
        self.ui.scanStatus.clear()
        self.ui.scanStatus.appendPlainText(
            f"Full scan started.\n\nScanning {root_drive}.\n\nPlease note that full scan might take a long time to complete.\n\nIt is recommended to close all programs before scanning.\n\n")
        self.sthread = FullScan()
        self.sthread.ret.connect(self.set_scan_value)
        self.sthread.start()
        self.sthread.finished.connect(lambda: self.ui.cancelscanButton.setEnabled(False))
        self.sthread.finished.connect(lambda: self.ui.quickscanButton.setEnabled(True))
        self.sthread.finished.connect(lambda: self.ui.fullscanButton.setEnabled(True))
        self.sthread.finished.connect(lambda: self.ui.customscanButton.setEnabled(True))
        self.sthread.finished.connect(lambda: self.ui.homeButton.setEnabled(True))

    # Customscan threads and slots
    def launch_customscan(self):
        self.ui.cancelscanButton.setEnabled(True)
        self.ui.quickscanButton.setEnabled(False)
        self.ui.fullscanButton.setEnabled(False)
        self.ui.customscanButton.setEnabled(False)
        self.ui.homeButton.setEnabled(False)
        self.ui.scanStatus.clear()
        self.scan_dir = QFileDialog.getExistingDirectory(self,self.tr("Choose a folder to scan."),self.tr('/'))
        self.scan_dir = self.scan_dir.replace("/","\\") # Shindows likes to use backslashes hhhh
        print("Debug: "+self.scan_dir)
        self.sthread = CustomScan(self.scan_dir)
        self.sthread.ret.connect(self.set_scan_value)
        self.sthread.start()
        self.sthread.finished.connect(lambda: self.ui.cancelscanButton.setEnabled(False))
        self.sthread.finished.connect(lambda: self.ui.quickscanButton.setEnabled(True))
        self.sthread.finished.connect(lambda: self.ui.fullscanButton.setEnabled(True))
        self.sthread.finished.connect(lambda: self.ui.customscanButton.setEnabled(True))
        self.sthread.finished.connect(lambda: self.ui.homeButton.setEnabled(True))

    def set_scan_value(self, scanstring):
        self.ui.scanStatus.appendPlainText(scanstring)

    def stop_scan(self):
        self.SingleThread = threading.Thread(target=self.stop_scan_thread)
        self.SingleThread.start()

    def stop_scan_thread(self):
        self.sthread.abort = True
        os.kill(self.sthread.process.pid, signal.SIGTERM)
        self.ui.cancelscanButton.setEnabled(False)
        time.sleep(5)

    # Update threads and slots
    def launch_update(self):
        self.ui.cancelUpdate.setEnabled(True)
        self.ui.updatehomeButton.setEnabled(False)
        self.ui.checkUpdate.setEnabled(False)
        self.ui.updateStatus.clear()
        self.ui.updateStatus.appendPlainText("Refreshing database...\n\n")
        self.thread = Updater()
        self.thread.ret.connect(self.set_update_value)
        self.thread.start()
        self.thread.finished.connect(lambda: self.ui.cancelUpdate.setEnabled(False))
        self.thread.finished.connect(lambda: self.ui.checkUpdate.setEnabled(True))
        self.thread.finished.connect(lambda: self.ui.updatehomeButton.setEnabled(True))

    def set_update_value(self, updatestring):
        self.ui.updateStatus.appendPlainText(updatestring)

    def stop_update(self):
        self.SingleThread = threading.Thread(target=self.stop_update_thread)
        self.SingleThread.start()

    def stop_update_thread(self):
        self.thread.abort = True
        os.kill(self.thread.process.pid, signal.SIGTERM)
        self.ui.cancelUpdate.setEnabled(False)
        time.sleep(5)

    # Quarantine file population threads.
    def start_quarantine(self):
        self.QuarantineThread = threading.Thread(target=self.populate_quarantine)
        self.QuarantineThread.start()

    def populate_quarantine(self):
        WorkingDirectory = os.getcwd()
        QuarantineDirectory = WorkingDirectory + "\\quarantine\\"
        lines = os.listdir(QuarantineDirectory)
        entries = 0
        for line in lines:
            size = os.path.getsize(str(QuarantineDirectory+line))
            if entries == 0:
                self.ui.quarantineView.setRowCount(0)
            self.ui.quarantineView.insertRow(entries)
            self.ui.quarantineView.setItem(entries, 0, QTableWidgetItem(line))
            self.ui.quarantineView.setItem(entries, 1, QTableWidgetItem(f'{size} Bytes'))
            entries = entries + 1

    # Opening github repo page.
    def openGithub(self, event):
        webbrowser.open("https://github.com/5trange/ClamGuard")


class Updater(QThread):
    ret = Signal(str)
    abort = False

    def printing(self):
        print("Debug: Hello, I'm a worker class!")

    def run(self):
        try:
            self.process = Popen(['freshclam.exe'], stdout=PIPE, encoding='utf-8', creationflags = CREATE_NO_WINDOW)
            while self.process.poll() is None:
                if (self.abort == True):
                    try:
                        self.ret.emit("\n\nStopping update...")
                        break
                    except Exception as e:
                        print(f"Debug: Error!:{e}")
                else:
                    self.updatebuffer = str(self.process.stdout.readline())
                    self.updatebuffer = os.linesep.join([s for s in self.updatebuffer.splitlines() if s])
                    if self.updatebuffer != '':
                        self.ret.emit(self.updatebuffer)

            if (self.abort == False):
                self.ret.emit("\nDatabase refreshed.")
            elif (self.abort == True):
                self.ret.emit("\n\nDatabase update cancelled.")
        except Exception as e:
            print(f"Debug: Error!:{e}")


class QuickScan(QThread):
    ret = Signal(str)
    abort = False

    def run(self):
        try:
            self.process = Popen(
                ['clamdscan.exe', appdata_dir, drivers_dir, '--infected', '--multiscan', '--move=quarantine'],
                stdout=PIPE, encoding='utf-8', creationflags = CREATE_NO_WINDOW)
            while self.process.poll() is None:
                if (self.abort == True):
                    try:
                        self.ret.emit("\n\nStopping scan...")
                        break
                    except Exception as e:
                        print(f"Debug: Error!:{e}")
                else:
                    self.scanbuffer = self.process.stdout.readline()
                    self.scanbuffer = os.linesep.join([s for s in self.scanbuffer.splitlines() if s])
                    if self.scanbuffer != '':
                        self.ret.emit(self.scanbuffer)

            if (self.abort == False):
                self.ret.emit("\nQuick scan complete.")
            elif (self.abort == True):
                self.ret.emit("\n\nScan cancelled.")
        except Exception as e:
            print(f"Debug: Error!:{e}")

class FullScan(QThread):
    ret = Signal(str)
    abort = False

    def run(self):
        try:
            self.process = Popen(
                ['clamdscan.exe', root_drive, '--infected', '--move=quarantine'],
                stdout=PIPE, encoding='utf-8', creationflags = CREATE_NO_WINDOW)
            while self.process.poll() is None:
                if (self.abort == True):
                    try:
                        self.ret.emit("\n\nStopping scan...")
                        break
                    except Exception as e:
                        print(f"Debug: Error!:{e}")
                else:
                    self.scanbuffer = self.process.stdout.readline()
                    self.scanbuffer = os.linesep.join([s for s in self.scanbuffer.splitlines() if s])
                    if self.scanbuffer != '':
                        self.ret.emit(self.scanbuffer)

            if (self.abort == False):
                self.ret.emit("\nFull scan complete.")
            elif (self.abort == True):
                self.ret.emit("\n\nFull scan cancelled.")
        except Exception as e:
            print(f"Debug: Error!:{e}")

class CustomScan(QThread):
    ret = Signal(str)
    abort = False
    scan_dir = ''

    # Constructor modification to pass scan_dir
    def __init__(self, scan_dir, parent=None):
        QThread.__init__(self, parent)
        self.scan_dir = scan_dir

    def run(self):
        if self.scan_dir == '':
            self.abort = True
            print("Debug: Scan directory empty!")
            self.ret.emit("No directory selected. Scan cancelled.")
        else:
            print("Debug: "+self.scan_dir)
            self.ret.emit(f"Directory selected: {self.scan_dir}")
            self.ret.emit(f"Scanning {self.scan_dir}\n\n")
            try:
                self.process = Popen(
                    ['clamdscan.exe', self.scan_dir, '--infected', '--move=quarantine'],
                    stdout=PIPE, encoding='utf-8', creationflags = CREATE_NO_WINDOW)
                while self.process.poll() is None:
                    if (self.abort == True):
                        try:
                            self.ret.emit("\n\nStopping scan...")
                            break
                        except Exception as e:
                            print(f"Debug: Error!:{e}")
                    else:
                        self.scanbuffer = self.process.stdout.readline()
                        self.scanbuffer = os.linesep.join([s for s in self.scanbuffer.splitlines() if s])
                        if self.scanbuffer != '':
                            self.ret.emit(self.scanbuffer)

                if (self.abort == False):
                    self.ret.emit("\nCustom scan complete.")
                elif (self.abort == True):
                    self.ret.emit("\n\nCustom scan cancelled.")

            except Exception as e:
                print(f"Debug: Error!:{e}")

class clamd_init(QThread):
    def run(self):
        self.host = '127.0.0.1'
        self.port = 3310
        self.timeout = None
        self.counter = 1
        self.max_retries = 10
        self.clamd_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while (self.counter <= self.max_retries):
            try:
                self.result = self.clamd_socket.connect_ex((self.host, self.port))
                if self.result == 0:
                    print('ClamAV Daemon is online')
                    self.clamd_socket.close()
                    break
            except socket.error:
                raise
            print(f'Connection failed. Retrying... Retries left: {self.max_retries - self.counter}')
            self.counter = self.counter+1
        if (self.result != 0):
            print("Couldn't connect to ClamAV Daemon!")
            sys.exit(1) # Prolly not very safe

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())

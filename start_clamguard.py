import sys
import platform
import time
import os
import threading
import signal
import webbrowser
from PySide2 import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from subprocess import *
from mainWindow import Ui_mainWindow #IMPORTING MAINWINDOW.PY
from SplashScreen import Ui_SplashScreen #IMPORTING SPLASHSCREEN.PY

# Splashscreen class
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.counter = 0

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

        # Dummy splashscreen
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)
        self.center() #CENTERING
        self.show()

    def progress(self):
        # Start clamd then ping it
        # Change progress according to that

        # Dummy value
        self.ui.progressBar.setValue(self.counter)

        # End splash and start ClamGuard
        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()
            self.close()
            self.main_window=MainWindow()
            self.main_window.show()

        # Increase counter
        self.counter += 1

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# MainWindow class
class MainWindow(QMainWindow):
    def __init__(self):
        # Shadow+Other functions
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

        # Window control buttons
        self.ui.minButton.clicked.connect(lambda: self.showMinimized()) #MINIMIZE ON CLICK
        self.ui.closeButton.clicked.connect(lambda: self.close()) #CLOSE ON CLICK

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
        #TO SCANPAGE FROM HOMEPAGE
        self.ui.scanFrame.mousePressEvent = self.switch_scan
        #TO HOMEPAGE FROM SCANPAGE
        self.ui.homeButton.clicked.connect(self.switch_home)
        #TO UPDATEPAGE FROM HOMEPAGE
        self.ui.updateFrame.mousePressEvent = self.switch_update
        #TO HOMEPAGE FROM UPDATEPAGE
        self.ui.updatehomeButton.clicked.connect(self.switch_home)
        #TO ABOUTPAGE FROM HOMEPAGE
        self.ui.aboutLabel.mousePressEvent = self.switch_about
        #TO HOMEPAGE FROM ABOUTPAGE
        self.ui.homeButtonAbout.clicked.connect(self.switch_home)
        #TO QUARANTINE FROM HOMEPAGE
        self.ui.quarantineLabel.mousePressEvent = self.switch_quarantine
        #TO HOMEPAGE FROM QUARANTINE
        self.ui.quarantineHomeButton.clicked.connect(self.switch_home)


        # Scan page functions
        #self.ui.quickscanButton.clicked.connect(self.start_quickscan)
        #self.ui.fullscanButton.clicked.connect(self.start_fullscan)
        #self.ui.customscanButton.clicked.connect(self.start_customscan)
        self.ui.cancelscanButton.setEnabled(False)
        #self.ui.cancelscanButton.clicked.connect(self.stopscan)

        # Update page functions
        self.ui.checkUpdate.clicked.connect(self.launch_update)
        self.ui.cancelUpdate.setEnabled(False)
        #self.ui.cancelUpdate.clicked.connect(self.stop_update)


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

    # Update threads and slots
    def launch_update(self):
        self.ui.cancelUpdate.setEnabled(True)
        self.ui.updatehomeButton.setEnabled(False)
        self.ui.checkUpdate.setEnabled(False)
        self.ui.updateStatus.clear()
        self.ui.updateStatus.appendPlainText("Refreshing database...\n\n")
        self.thread = Updater()
        self.thread.ref.connect(self.set_update_value)
        self.thread.start()
        self.thread.finished.connect(lambda: self.ui.cancelUpdate.setEnabled(False))
        self.thread.finished.connect(lambda: self.ui.checkUpdate.setEnabled(True))
        self.thread.finished.connect(lambda: self.ui.updatehomeButton.setEnabled(True))

    def set_update_value(self, updatestring):
        self.ui.updateStatus.appendPlainText(updatestring)

    # Quarantine file population threads.
    def start_quarantine(self):
        self.QuarantineThread = threading.Thread(target = self.populate_quarantine)
        self.QuarantineThread.start()

    def populate_quarantine(self):
        WorkingDirectory = os.getcwd()
        QuarantineDirectory = WorkingDirectory+"\\quarantine\\"
        lines = os.listdir(QuarantineDirectory)
        entries = 0
        for line in lines:
            if entries == 0:
                self.ui.quarantineView.setRowCount(0)
            self.ui.quarantineView.insertRow(entries)
            self.ui.quarantineView.setItem(entries,0,QTableWidgetItem(line))
            entries = entries+1

    #Opening github repo page.
    def openGithub(self, event):
        webbrowser.open("https://github.com/5trange/ClamGuard")

class Updater(QThread):
    ref = Signal(str)

    def printing(self):
        print("Hello, I'm a worker class!")

    def run(self):
        try:
            self.process =  Popen(['freshclam.exe'], stdout = PIPE, encoding = 'utf-8')
            while self.process.poll() is None:
                self.updatebuffer = str(self.process.stdout.readline())
                self.updatebuffer = os.linesep.join([s for s in self.updatebuffer.splitlines() if s])
                if self.updatebuffer != '':
                    self.ref.emit(self.updatebuffer)
            self.ref.emit("\n\nDatabase refreshed.")
        except Exception as f:
            print(f)


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

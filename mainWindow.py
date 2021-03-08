# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowmfkkrs.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setMinimumSize(QSize(800, 600))
        mainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
        self.dropshadowFrame = QFrame(self.centralwidget)
        self.dropshadowFrame.setObjectName(u"dropshadowFrame")
        self.dropshadowFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(55, 56, 59, 255));\n"
"border-radius: 5px;")
        self.dropshadowFrame.setFrameShape(QFrame.NoFrame)
        self.dropshadowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.dropshadowFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.dropshadowFrame)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 30))
        self.titleBar.setStyleSheet(u"background-color:none;")
        self.titleBar.setFrameShape(QFrame.NoFrame)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleFrame = QFrame(self.titleBar)
        self.titleFrame.setObjectName(u"titleFrame")
        font = QFont()
        font.setFamily(u"SF Pro Display")
        self.titleFrame.setFont(font)
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.title_label = QLabel(self.titleFrame)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setFamily(u"SF Pro Display")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"color: rgb(0, 255, 38);")

        self.horizontalLayout_2.addWidget(self.title_label)


        self.horizontalLayout.addWidget(self.titleFrame)

        self.titleButtons = QFrame(self.titleBar)
        self.titleButtons.setObjectName(u"titleButtons")
        self.titleButtons.setMaximumSize(QSize(70, 16777215))
        self.titleButtons.setFrameShape(QFrame.StyledPanel)
        self.titleButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.titleButtons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.minButton = QPushButton(self.titleButtons)
        self.minButton.setObjectName(u"minButton")
        self.minButton.setMinimumSize(QSize(16, 16))
        self.minButton.setMaximumSize(QSize(16, 16))
        self.minButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(176, 109, 16);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: rgb(255, 128, 0);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.minButton)

        self.closeButton = QPushButton(self.titleButtons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(16, 16))
        self.closeButton.setMaximumSize(QSize(16, 16))
        self.closeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color: rgb(161, 0, 2);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: rgb(255, 0, 4);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout.addWidget(self.titleButtons)


        self.verticalLayout.addWidget(self.titleBar)

        self.mainInterface = QFrame(self.dropshadowFrame)
        self.mainInterface.setObjectName(u"mainInterface")
        font2 = QFont()
        font2.setFamily(u"SF Pro Text")
        self.mainInterface.setFont(font2)
        self.mainInterface.setStyleSheet(u"background-color:none;")
        self.mainInterface.setFrameShape(QFrame.NoFrame)
        self.mainInterface.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mainInterface)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedHome = QStackedWidget(self.mainInterface)
        self.stackedHome.setObjectName(u"stackedHome")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.verticalLayout_4 = QVBoxLayout(self.pageHome)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.pageHome)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_content_home)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scanFrame = QFrame(self.frame_content_home)
        self.scanFrame.setObjectName(u"scanFrame")
        self.scanFrame.setMinimumSize(QSize(160, 160))
        self.scanFrame.setMaximumSize(QSize(160, 160))
        self.scanFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.scanFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: 5px solid rgb(0, 182, 24);\n"
"	border-radius: 80px;\n"
"}\n"
"QFrame:hover\n"
"{\n"
"	border: 5px solid rgb(0, 255, 38);\n"
"}\n"
"	")
        self.scanFrame.setFrameShape(QFrame.StyledPanel)
        self.scanFrame.setFrameShadow(QFrame.Raised)
        self.scanlabel = QLabel(self.scanFrame)
        self.scanlabel.setObjectName(u"scanlabel")
        self.scanlabel.setGeometry(QRect(50, 110, 61, 21))
        font3 = QFont()
        font3.setFamily(u"SF Pro Text")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(75)
        self.scanlabel.setFont(font3)
        self.scanlabel.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(0, 255, 38);\n"
"	border:none;\n"
"}\n"
"\n"
"	")
        self.scanlabel.setAlignment(Qt.AlignCenter)
        self.scanImg = QLabel(self.scanFrame)
        self.scanImg.setObjectName(u"scanImg")
        self.scanImg.setGeometry(QRect(30, 10, 100, 100))
        self.scanImg.setMinimumSize(QSize(100, 100))
        self.scanImg.setMaximumSize(QSize(100, 100))
        self.scanImg.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(0, 255, 38);\n"
"	border:none;\n"
"}\n"
"")
        self.scanImg.setPixmap(QPixmap(u"img/search_green.png"))
        self.scanImg.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.scanFrame)

        self.updateFrame = QFrame(self.frame_content_home)
        self.updateFrame.setObjectName(u"updateFrame")
        self.updateFrame.setMinimumSize(QSize(160, 160))
        self.updateFrame.setMaximumSize(QSize(160, 160))
        self.updateFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: 5px solid rgb(0, 182, 24);\n"
"	border-radius: 80px;\n"
"}\n"
"QFrame:hover\n"
"{\n"
"	border: 5px solid rgb(0, 255, 38);\n"
"}\n"
"	")
        self.updateFrame.setFrameShape(QFrame.StyledPanel)
        self.updateFrame.setFrameShadow(QFrame.Raised)
        self.updateImg = QLabel(self.updateFrame)
        self.updateImg.setObjectName(u"updateImg")
        self.updateImg.setGeometry(QRect(30, 10, 100, 100))
        self.updateImg.setMinimumSize(QSize(100, 100))
        self.updateImg.setMaximumSize(QSize(100, 100))
        self.updateImg.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(0, 255, 38);\n"
"	border:none;\n"
"}\n"
"")
        self.updateImg.setPixmap(QPixmap(u"img/update_green.png"))
        self.updateImg.setScaledContents(True)
        self.updateLabel = QLabel(self.updateFrame)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setGeometry(QRect(45, 110, 71, 21))
        font4 = QFont()
        font4.setFamily(u"SF Pro Display")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.updateLabel.setFont(font4)
        self.updateLabel.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(0, 255, 38);\n"
"	border:none;\n"
"}\n"
"\n"
"	")

        self.horizontalLayout_4.addWidget(self.updateFrame)


        self.verticalLayout_4.addWidget(self.frame_content_home)

        self.stackedHome.addWidget(self.pageHome)
        self.pageScan = QWidget()
        self.pageScan.setObjectName(u"pageScan")
        self.verticalLayout_5 = QVBoxLayout(self.pageScan)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frameHome = QFrame(self.pageScan)
        self.frameHome.setObjectName(u"frameHome")
        self.frameHome.setFrameShape(QFrame.StyledPanel)
        self.frameHome.setFrameShadow(QFrame.Raised)
        self.homeButton = QPushButton(self.frameHome)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(9, 20, 182, 120))
        self.homeButton.setMinimumSize(QSize(120, 120))
        self.homeButton.setFont(font4)
        self.homeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 2px solid rgb(0, 182, 24);\n"
"	color: rgb(0,255,38);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 5px solid rgb(0, 255, 38);\n"
"}\n"
"	")
        icon = QIcon()
        icon.addFile(u"img/home_green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(50, 50))

        self.verticalLayout_5.addWidget(self.frameHome)

        self.frameScanButtons = QFrame(self.pageScan)
        self.frameScanButtons.setObjectName(u"frameScanButtons")
        self.frameScanButtons.setFrameShape(QFrame.StyledPanel)
        self.frameScanButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frameScanButtons)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.quickscanButton = QPushButton(self.frameScanButtons)
        self.quickscanButton.setObjectName(u"quickscanButton")
        self.quickscanButton.setMinimumSize(QSize(0, 120))
        self.quickscanButton.setFont(font4)
        self.quickscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 2px solid rgb(0, 182, 24);\n"
"	color: rgb(0,255,38);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 5px solid rgb(0, 255, 38);\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.quickscanButton)

        self.fullscanButton = QPushButton(self.frameScanButtons)
        self.fullscanButton.setObjectName(u"fullscanButton")
        self.fullscanButton.setMinimumSize(QSize(0, 120))
        self.fullscanButton.setFont(font4)
        self.fullscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 2px solid rgb(0, 182, 24);\n"
"	color: rgb(0,255,38);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 5px solid rgb(0, 255, 38);\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.fullscanButton)

        self.customscanButton = QPushButton(self.frameScanButtons)
        self.customscanButton.setObjectName(u"customscanButton")
        self.customscanButton.setMinimumSize(QSize(0, 120))
        self.customscanButton.setFont(font4)
        self.customscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 2px solid rgb(0, 182, 24);\n"
"	color: rgb(0,255,38);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 5px solid rgb(0, 255, 38);\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.customscanButton)

        self.cancelscanButton = QPushButton(self.frameScanButtons)
        self.cancelscanButton.setObjectName(u"cancelscanButton")
        self.cancelscanButton.setMinimumSize(QSize(0, 120))
        self.cancelscanButton.setFont(font4)
        self.cancelscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 2px solid rgb(0, 182, 24);\n"
"	color: rgb(0,255,38);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 5px solid rgb(255,0,4);\n"
"	color: rgb(255,0,4);\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.cancelscanButton)


        self.verticalLayout_5.addWidget(self.frameScanButtons)

        self.frameScanStatus = QFrame(self.pageScan)
        self.frameScanStatus.setObjectName(u"frameScanStatus")
        self.frameScanStatus.setMaximumSize(QSize(16777215, 175))
        self.frameScanStatus.setFrameShape(QFrame.StyledPanel)
        self.frameScanStatus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frameScanStatus)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scanStatus = QPlainTextEdit(self.frameScanStatus)
        self.scanStatus.setObjectName(u"scanStatus")
        font5 = QFont()
        font5.setFamily(u"Consolas")
        self.scanStatus.setFont(font5)
        self.scanStatus.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"	 \n"
"	background-color: rgb(33, 33, 33);\n"
"	color: rgb(0,255,38);\n"
"}\n"
"	")

        self.verticalLayout_6.addWidget(self.scanStatus)


        self.verticalLayout_5.addWidget(self.frameScanStatus)

        self.stackedHome.addWidget(self.pageScan)

        self.verticalLayout_3.addWidget(self.stackedHome)


        self.verticalLayout.addWidget(self.mainInterface)

        self.statusBar = QFrame(self.dropshadowFrame)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setMaximumSize(QSize(16777215, 30))
        self.statusBar.setStyleSheet(u"background-color:none;")
        self.statusBar.setFrameShape(QFrame.NoFrame)
        self.statusBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.statusBar)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.engineVer = QLabel(self.statusBar)
        self.engineVer.setObjectName(u"engineVer")
        font6 = QFont()
        font6.setFamily(u"SF Pro Display")
        font6.setPointSize(8)
        font6.setBold(True)
        font6.setWeight(75)
        self.engineVer.setFont(font6)
        self.engineVer.setStyleSheet(u"color: rgb(0, 255, 38);")

        self.horizontalLayout_6.addWidget(self.engineVer)


        self.verticalLayout.addWidget(self.statusBar)


        self.drop_shadow_layout.addWidget(self.dropshadowFrame)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.stackedHome.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"ClamGuard", None))
        self.title_label.setText(QCoreApplication.translate("mainWindow", u"ClamGuard", None))
        self.minButton.setText("")
        self.closeButton.setText("")
        self.scanlabel.setText(QCoreApplication.translate("mainWindow", u"SCAN", None))
        self.scanImg.setText("")
        self.updateImg.setText("")
        self.updateLabel.setText(QCoreApplication.translate("mainWindow", u"UPDATE", None))
        self.homeButton.setText("")
        self.quickscanButton.setText(QCoreApplication.translate("mainWindow", u"Quick Scan", None))
        self.fullscanButton.setText(QCoreApplication.translate("mainWindow", u"Full Scan", None))
        self.customscanButton.setText(QCoreApplication.translate("mainWindow", u"Custom Scan", None))
        self.cancelscanButton.setText(QCoreApplication.translate("mainWindow", u"Cancel Scan", None))
        self.engineVer.setText(QCoreApplication.translate("mainWindow", u"Engine Version: ", None))
    # retranslateUi


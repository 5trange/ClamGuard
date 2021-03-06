# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowBptFpj.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
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
        self.dropshadowFrame.setStyleSheet(u"background-color: #2e3440;\n"
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
        self.titleFrame.setFont(font)
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.title_label = QLabel(self.titleFrame)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.title_label.setFont(font1)
        self.title_label.setStyleSheet(u"color: #81a1c1;")

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
"	background-color: #ebcb8b;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: #a3be8c;\n"
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
"	background-color: #d08770;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: #bf616a;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout.addWidget(self.titleButtons)


        self.verticalLayout.addWidget(self.titleBar)

        self.mainInterface = QFrame(self.dropshadowFrame)
        self.mainInterface.setObjectName(u"mainInterface")
        self.mainInterface.setFont(font)
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
        self.scanFrame = QFrame(self.frame_content_home)
        self.scanFrame.setObjectName(u"scanFrame")
        self.scanFrame.setGeometry(QRect(155, 181, 160, 160))
        self.scanFrame.setMinimumSize(QSize(160, 160))
        self.scanFrame.setMaximumSize(QSize(160, 160))
        self.scanFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.scanFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: 5px solid #81a1c1;\n"
"	border-radius: 80px;\n"
"}\n"
"QFrame:hover\n"
"{\n"
"	border: 5px solid #b48ead;\n"
"}\n"
"	")
        self.scanFrame.setFrameShape(QFrame.StyledPanel)
        self.scanFrame.setFrameShadow(QFrame.Raised)
        self.scanlabel = QLabel(self.scanFrame)
        self.scanlabel.setObjectName(u"scanlabel")
        self.scanlabel.setGeometry(QRect(50, 110, 61, 21))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.scanlabel.setFont(font2)
        self.scanlabel.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
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
        self.scanImg.setPixmap(QPixmap(u"img/search.png"))
        self.scanImg.setScaledContents(True)
        self.updateFrame = QFrame(self.frame_content_home)
        self.updateFrame.setObjectName(u"updateFrame")
        self.updateFrame.setGeometry(QRect(467, 181, 160, 160))
        self.updateFrame.setMinimumSize(QSize(160, 160))
        self.updateFrame.setMaximumSize(QSize(160, 160))
        self.updateFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateFrame.setStyleSheet(u"QFrame\n"
"{\n"
"	border: 5px solid #81a1c1;\n"
"	border-radius: 80px;\n"
"}\n"
"QFrame:hover\n"
"{\n"
"	border: 5px solid #b48ead;\n"
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
        self.updateImg.setPixmap(QPixmap(u"img/update.png"))
        self.updateImg.setScaledContents(True)
        self.updateLabel = QLabel(self.updateFrame)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setGeometry(QRect(45, 110, 71, 21))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.updateLabel.setFont(font3)
        self.updateLabel.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"\n"
"	")
        self.aboutLabel = QLabel(self.frame_content_home)
        self.aboutLabel.setObjectName(u"aboutLabel")
        self.aboutLabel.setGeometry(QRect(50, 480, 31, 31))
        self.aboutLabel.setFont(font1)
        self.aboutLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutLabel.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(0, 182, 24);\n"
"	border:none;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:rgb(0, 255, 38);\n"
"	border:1px solid rgb(255, 255, 255);\n"
"}")
        self.aboutLabel.setPixmap(QPixmap(u"img/info.png"))
        self.aboutLabel.setScaledContents(True)
        self.quarantineLabel = QLabel(self.frame_content_home)
        self.quarantineLabel.setObjectName(u"quarantineLabel")
        self.quarantineLabel.setGeometry(QRect(10, 480, 31, 31))
        self.quarantineLabel.setFont(font1)
        self.quarantineLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.quarantineLabel.setStyleSheet(u"QLabel\n"
"{\n"
"	color:rgb(0, 182, 24);\n"
"	border:none;\n"
"}\n"
"QLabel:hover\n"
"{\n"
"	color:rgb(0, 255, 38);\n"
"	border:1px solid rgb(255, 255, 255);\n"
"}")
        self.quarantineLabel.setPixmap(QPixmap(u"img/warning.png"))
        self.quarantineLabel.setScaledContents(True)
        self.voyagerHome = QLabel(self.frame_content_home)
        self.voyagerHome.setObjectName(u"voyagerHome")
        self.voyagerHome.setGeometry(QRect(0, 0, 801, 551))
        self.voyagerHome.setPixmap(QPixmap(u"img/voyager.png"))
        self.voyagerHome.setScaledContents(True)
        self.voyagerHome.raise_()
        self.scanFrame.raise_()
        self.updateFrame.raise_()
        self.aboutLabel.raise_()
        self.quarantineLabel.raise_()

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
        self.homeButton.setFont(font3)
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 3px solid #b48ead;\n"
"}\n"
"	")
        icon = QIcon()
        icon.addFile(u"img/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(50, 50))
        self.moonG = QLabel(self.frameHome)
        self.moonG.setObjectName(u"moonG")
        self.moonG.setGeometry(QRect(630, 0, 191, 171))
        self.moonG.setPixmap(QPixmap(u"img/pixelmoon.png"))
        self.moonG.setScaledContents(True)

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
        self.quickscanButton.setFont(font3)
        self.quickscanButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.quickscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 3px solid #b48ead;\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.quickscanButton)

        self.fullscanButton = QPushButton(self.frameScanButtons)
        self.fullscanButton.setObjectName(u"fullscanButton")
        self.fullscanButton.setMinimumSize(QSize(0, 120))
        self.fullscanButton.setFont(font3)
        self.fullscanButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.fullscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 3px solid #b48ead;\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.fullscanButton)

        self.customscanButton = QPushButton(self.frameScanButtons)
        self.customscanButton.setObjectName(u"customscanButton")
        self.customscanButton.setMinimumSize(QSize(0, 120))
        self.customscanButton.setFont(font3)
        self.customscanButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.customscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 3px solid #b48ead;\n"
"}\n"
"	")

        self.horizontalLayout_5.addWidget(self.customscanButton)

        self.cancelscanButton = QPushButton(self.frameScanButtons)
        self.cancelscanButton.setObjectName(u"cancelscanButton")
        self.cancelscanButton.setMinimumSize(QSize(0, 120))
        self.cancelscanButton.setFont(font3)
        self.cancelscanButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelscanButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #bf616a;\n"
"	border: 3px solid #b48ead;\n"
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
        self.scanStatus.setFont(font)
        self.scanStatus.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"	 \n"
"	background-color: #2e3440;\n"
"	color: #d8dee9;\n"
"}\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    \n"
"	background-color: #3b4252;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	\n"
"	background-color: #3b4252;\n"
"	height: 15px;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	\n"
"	background-color: rgb(80, 80, 122);\n"
"}\n"
"QScrol"
                        "lBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	\n"
"	background-color: #3b4252;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	\n"
"	background-color: rgb(78, 78, 119);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"	")
        self.scanStatus.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.scanStatus)


        self.verticalLayout_5.addWidget(self.frameScanStatus)

        self.stackedHome.addWidget(self.pageScan)
        self.pageUpdate = QWidget()
        self.pageUpdate.setObjectName(u"pageUpdate")
        self.verticalLayout_2 = QVBoxLayout(self.pageUpdate)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frameGoHome = QFrame(self.pageUpdate)
        self.frameGoHome.setObjectName(u"frameGoHome")
        self.frameGoHome.setMinimumSize(QSize(764, 159))
        self.frameGoHome.setMaximumSize(QSize(764, 159))
        self.frameGoHome.setFrameShape(QFrame.StyledPanel)
        self.frameGoHome.setFrameShadow(QFrame.Raised)
        self.updatehomeButton = QPushButton(self.frameGoHome)
        self.updatehomeButton.setObjectName(u"updatehomeButton")
        self.updatehomeButton.setGeometry(QRect(9, 20, 182, 120))
        self.updatehomeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.updatehomeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 3px solid #b48ead;\n"
"}\n"
"	")
        self.updatehomeButton.setIcon(icon)
        self.updatehomeButton.setIconSize(QSize(50, 50))
        self.moonG2 = QLabel(self.frameGoHome)
        self.moonG2.setObjectName(u"moonG2")
        self.moonG2.setGeometry(QRect(630, 0, 191, 171))
        self.moonG2.setPixmap(QPixmap(u"img/pixelmoon.png"))
        self.moonG2.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.frameGoHome)

        self.frameUpdateButtons = QFrame(self.pageUpdate)
        self.frameUpdateButtons.setObjectName(u"frameUpdateButtons")
        self.frameUpdateButtons.setMinimumSize(QSize(764, 158))
        self.frameUpdateButtons.setMaximumSize(QSize(764, 158))
        self.frameUpdateButtons.setFrameShape(QFrame.StyledPanel)
        self.frameUpdateButtons.setFrameShadow(QFrame.Raised)
        self.checkUpdate = QPushButton(self.frameUpdateButtons)
        self.checkUpdate.setObjectName(u"checkUpdate")
        self.checkUpdate.setGeometry(QRect(9, 19, 182, 120))
        self.checkUpdate.setMinimumSize(QSize(182, 120))
        self.checkUpdate.setMaximumSize(QSize(182, 120))
        self.checkUpdate.setFont(font3)
        self.checkUpdate.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkUpdate.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 3px solid #b48ead;\n"
"}\n"
"	")
        self.cancelUpdate = QPushButton(self.frameUpdateButtons)
        self.cancelUpdate.setObjectName(u"cancelUpdate")
        self.cancelUpdate.setGeometry(QRect(573, 19, 182, 120))
        self.cancelUpdate.setMinimumSize(QSize(182, 120))
        self.cancelUpdate.setMaximumSize(QSize(182, 120))
        self.cancelUpdate.setFont(font3)
        self.cancelUpdate.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelUpdate.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: #bf616a;\n"
"	border: 3px solid #b48ead;\n"
"}\n"
"	")

        self.verticalLayout_2.addWidget(self.frameUpdateButtons)

        self.frameUpdateStatus = QFrame(self.pageUpdate)
        self.frameUpdateStatus.setObjectName(u"frameUpdateStatus")
        self.frameUpdateStatus.setMinimumSize(QSize(764, 175))
        self.frameUpdateStatus.setMaximumSize(QSize(764, 175))
        self.frameUpdateStatus.setFrameShape(QFrame.StyledPanel)
        self.frameUpdateStatus.setFrameShadow(QFrame.Raised)
        self.updateStatus = QPlainTextEdit(self.frameUpdateStatus)
        self.updateStatus.setObjectName(u"updateStatus")
        self.updateStatus.setGeometry(QRect(9, 9, 746, 157))
        self.updateStatus.setMinimumSize(QSize(746, 157))
        self.updateStatus.setMaximumSize(QSize(746, 157))
        self.updateStatus.setFont(font)
        self.updateStatus.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"	 \n"
"	background-color: #2e3440;\n"
"	color: #d8dee9;\n"
"}\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    \n"
"	background-color: #3b4252;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	\n"
"	background-color: #3b4252;\n"
"	height: 15px;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	\n"
"	background-color: rgb(80, 80, 122);\n"
"}\n"
"QScrol"
                        "lBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	\n"
"	background-color: #3b4252;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	\n"
"	background-color: rgb(78, 78, 119);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"	")
        self.updateStatus.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.frameUpdateStatus)

        self.stackedHome.addWidget(self.pageUpdate)
        self.pageAbout = QWidget()
        self.pageAbout.setObjectName(u"pageAbout")
        self.verticalLayout_7 = QVBoxLayout(self.pageAbout)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frameHomeAbout = QFrame(self.pageAbout)
        self.frameHomeAbout.setObjectName(u"frameHomeAbout")
        self.frameHomeAbout.setMinimumSize(QSize(764, 169))
        self.frameHomeAbout.setMaximumSize(QSize(764, 169))
        self.frameHomeAbout.setFrameShape(QFrame.StyledPanel)
        self.frameHomeAbout.setFrameShadow(QFrame.Raised)
        self.homeButtonAbout = QPushButton(self.frameHomeAbout)
        self.homeButtonAbout.setObjectName(u"homeButtonAbout")
        self.homeButtonAbout.setGeometry(QRect(9, 20, 182, 120))
        self.homeButtonAbout.setMinimumSize(QSize(120, 120))
        self.homeButtonAbout.setFont(font3)
        self.homeButtonAbout.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButtonAbout.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 3px solid #b48ead;\n"
"}\n"
"	")
        self.homeButtonAbout.setIcon(icon)
        self.homeButtonAbout.setIconSize(QSize(50, 50))
        self.moonG3 = QLabel(self.frameHomeAbout)
        self.moonG3.setObjectName(u"moonG3")
        self.moonG3.setGeometry(QRect(630, 0, 191, 171))
        self.moonG3.setPixmap(QPixmap(u"img/pixelmoon.png"))
        self.moonG3.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.frameHomeAbout)

        self.frameAboutContent = QFrame(self.pageAbout)
        self.frameAboutContent.setObjectName(u"frameAboutContent")
        self.frameAboutContent.setFrameShape(QFrame.StyledPanel)
        self.frameAboutContent.setFrameShadow(QFrame.Raised)
        self.ProjectTitle = QLabel(self.frameAboutContent)
        self.ProjectTitle.setObjectName(u"ProjectTitle")
        self.ProjectTitle.setGeometry(QRect(10, 20, 171, 21))
        self.ProjectTitle.setMinimumSize(QSize(0, 21))
        self.ProjectTitle.setMaximumSize(QSize(16777215, 21))
        self.ProjectTitle.setFont(font3)
        self.ProjectTitle.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"\n"
"	")
        self.ProjectTitle.setAlignment(Qt.AlignCenter)
        self.AboutGithub = QLabel(self.frameAboutContent)
        self.AboutGithub.setObjectName(u"AboutGithub")
        self.AboutGithub.setGeometry(QRect(10, 280, 101, 41))
        self.AboutGithub.setCursor(QCursor(Qt.PointingHandCursor))
        self.AboutGithub.setStyleSheet(u"")
        self.AboutGithub.setPixmap(QPixmap(u"img/GitHub.png"))
        self.AboutGithub.setScaledContents(True)
        self.AboutGPL = QLabel(self.frameAboutContent)
        self.AboutGPL.setObjectName(u"AboutGPL")
        self.AboutGPL.setGeometry(QRect(140, 280, 91, 41))
        self.AboutGPL.setPixmap(QPixmap(u"img/gpl.png"))
        self.AboutGPL.setScaledContents(True)
        self.label = QLabel(self.frameAboutContent)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 381, 16))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"")
        self.label_2 = QLabel(self.frameAboutContent)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 741, 161))
        font5 = QFont()
        font5.setBold(True)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"")
        self.label_3 = QLabel(self.frameAboutContent)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 230, 571, 16))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.frameAboutContent)

        self.stackedHome.addWidget(self.pageAbout)
        self.pageQuarantine = QWidget()
        self.pageQuarantine.setObjectName(u"pageQuarantine")
        self.verticalLayout_8 = QVBoxLayout(self.pageQuarantine)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frameQuarantineNav = QFrame(self.pageQuarantine)
        self.frameQuarantineNav.setObjectName(u"frameQuarantineNav")
        self.frameQuarantineNav.setMinimumSize(QSize(764, 169))
        self.frameQuarantineNav.setMaximumSize(QSize(764, 169))
        self.frameQuarantineNav.setFrameShape(QFrame.StyledPanel)
        self.frameQuarantineNav.setFrameShadow(QFrame.Raised)
        self.quarantineHomeButton = QPushButton(self.frameQuarantineNav)
        self.quarantineHomeButton.setObjectName(u"quarantineHomeButton")
        self.quarantineHomeButton.setGeometry(QRect(9, 20, 182, 120))
        self.quarantineHomeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.quarantineHomeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 3px solid #b48ead;\n"
"}\n"
"	")
        self.quarantineHomeButton.setIcon(icon)
        self.quarantineHomeButton.setIconSize(QSize(50, 50))
        self.moonG4 = QLabel(self.frameQuarantineNav)
        self.moonG4.setObjectName(u"moonG4")
        self.moonG4.setGeometry(QRect(630, 0, 191, 171))
        self.moonG4.setPixmap(QPixmap(u"img/pixelmoon.png"))
        self.moonG4.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.frameQuarantineNav)

        self.frameQuarantineContent = QFrame(self.pageQuarantine)
        self.frameQuarantineContent.setObjectName(u"frameQuarantineContent")
        self.frameQuarantineContent.setFrameShape(QFrame.StyledPanel)
        self.frameQuarantineContent.setFrameShadow(QFrame.Raised)
        self.quarantineRefresh = QPushButton(self.frameQuarantineContent)
        self.quarantineRefresh.setObjectName(u"quarantineRefresh")
        self.quarantineRefresh.setGeometry(QRect(680, 9, 71, 30))
        self.quarantineRefresh.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        self.quarantineRefresh.setFont(font6)
        self.quarantineRefresh.setCursor(QCursor(Qt.PointingHandCursor))
        self.quarantineRefresh.setStyleSheet(u"QPushButton\n"
"{\n"
"	border: 1px solid #b48ead;\n"
"	border-radius: 5px;\n"
"	color: #81a1c1;\n"
"	background-color: #2e3440;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border: 3px solid #b48ead;\n"
"}\n"
"	")
        self.quarantineView = QTableWidget(self.frameQuarantineContent)
        if (self.quarantineView.columnCount() < 2):
            self.quarantineView.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.quarantineView.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.quarantineView.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.quarantineView.setObjectName(u"quarantineView")
        self.quarantineView.setGeometry(QRect(9, 45, 745, 275))
        self.quarantineView.setStyleSheet(u"QTableWidget\n"
"{ \n"
"	background-color: #2e3440;\n"
"	color: #d8dee9;\n"
"}\n"
"	")
        self.quarantineView.horizontalHeader().setMinimumSectionSize(50)
        self.quarantineView.horizontalHeader().setDefaultSectionSize(200)
        self.quarantineView.horizontalHeader().setStretchLastSection(True)
        self.quarantineView.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.frameQuarantineContent)

        self.stackedHome.addWidget(self.pageQuarantine)

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
        font7 = QFont()
        font7.setPointSize(7)
        font7.setBold(True)
        self.engineVer.setFont(font7)
        self.engineVer.setStyleSheet(u"color: #81a1c1;")

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
        self.title_label.setText(QCoreApplication.translate("mainWindow", u"ClamGuard Security", None))
        self.minButton.setText("")
        self.closeButton.setText("")
#if QT_CONFIG(tooltip)
        self.scanFrame.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.scanlabel.setText(QCoreApplication.translate("mainWindow", u"SCAN", None))
        self.scanImg.setText("")
#if QT_CONFIG(tooltip)
        self.updateFrame.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.updateImg.setText("")
        self.updateLabel.setText(QCoreApplication.translate("mainWindow", u"UPDATE", None))
#if QT_CONFIG(tooltip)
        self.aboutLabel.setToolTip(QCoreApplication.translate("mainWindow", u"About ClamGuard Project", None))
#endif // QT_CONFIG(tooltip)
        self.aboutLabel.setText("")
#if QT_CONFIG(tooltip)
        self.quarantineLabel.setToolTip(QCoreApplication.translate("mainWindow", u"View Quarantine", None))
#endif // QT_CONFIG(tooltip)
        self.quarantineLabel.setText("")
        self.voyagerHome.setText("")
        self.homeButton.setText("")
        self.moonG.setText("")
#if QT_CONFIG(tooltip)
        self.quickscanButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.quickscanButton.setText(QCoreApplication.translate("mainWindow", u"Quick Scan", None))
#if QT_CONFIG(tooltip)
        self.fullscanButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.fullscanButton.setText(QCoreApplication.translate("mainWindow", u"Full Scan", None))
#if QT_CONFIG(tooltip)
        self.customscanButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.customscanButton.setText(QCoreApplication.translate("mainWindow", u"Custom Scan", None))
        self.cancelscanButton.setText(QCoreApplication.translate("mainWindow", u"Cancel Scan", None))
        self.updatehomeButton.setText("")
        self.moonG2.setText("")
#if QT_CONFIG(tooltip)
        self.checkUpdate.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.checkUpdate.setText(QCoreApplication.translate("mainWindow", u"Check for Updates", None))
        self.cancelUpdate.setText(QCoreApplication.translate("mainWindow", u"Cancel Update", None))
        self.homeButtonAbout.setText("")
        self.moonG3.setText("")
        self.ProjectTitle.setText(QCoreApplication.translate("mainWindow", u"ClamGuard Project", None))
        self.AboutGithub.setText("")
        self.AboutGPL.setText("")
        self.label.setText(QCoreApplication.translate("mainWindow", u"An opensource antivirus solution based on ClamAV.", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Developed by: \n"
"Adith K. Murali, Bilal Jafar, Vinayak Bhat S.\n"
"\n"
"Artwork and design by:\n"
"Jisin Thomas\n"
"\n"
"This software is free software, you can modify or redistribute it under the terms of GNU General Public License version 2\n"
"or later.", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Developed using PySide6 and Python3. The full source code is available in our GitHub repository.", None))
        self.quarantineHomeButton.setText("")
        self.moonG4.setText("")
        self.quarantineRefresh.setText(QCoreApplication.translate("mainWindow", u"Refresh", None))
        ___qtablewidgetitem = self.quarantineView.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.quarantineView.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"Size", None));
        self.engineVer.setText(QCoreApplication.translate("mainWindow", u"ClamGuard Version: 0.7.7-rc", None))
    # retranslateUi


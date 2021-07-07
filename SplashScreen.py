# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplashScreenCyuhVA.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #2e3440;\n"
"    border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 130, 661, 81))
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 280, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: #2e3440;\n"
"	color: #b48ead;\n"
"	border-style: none;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: color: #a3be8c;\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 320, 661, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_loading.setFont(font1)
        self.label_loading.setStyleSheet(u"QLabel\n"
"{\n"
"	color: #81a1c1;\n"
"	border:none;\n"
"}\n"
"")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.pix = QLabel(self.dropShadowFrame)
        self.pix.setObjectName(u"pix")
        self.pix.setGeometry(QRect(-10, 0, 681, 491))
        self.pix.setPixmap(QPixmap(u"img/voyager.png"))
        self.pix.setScaledContents(True)
        self.pix.raise_()
        self.label_title.raise_()
        self.progressBar.raise_()
        self.label_loading.raise_()

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"Starting ClamGuard", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\">CLAMGUARD</p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"Starting modules..", None))
        self.pix.setText("")
    # retranslateUi


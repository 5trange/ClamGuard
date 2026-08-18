import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "pages"

ApplicationWindow {
    id: root
    width: 800
    height: 600
    minimumWidth: 800
    minimumHeight: 600
    maximumWidth: 800
    maximumHeight: 600
    flags: Qt.FramelessWindowHint
    visible: true
    title: "ClamGuard Security"
    color: "#2e3440"

    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        Rectangle {
            id: titleBar
            Layout.fillWidth: true
            Layout.preferredHeight: 30
            color: "transparent"

            MouseArea {
                anchors.fill: parent
                acceptedButtons: Qt.LeftButton
                onPressed: root.startSystemMove()
                z: -1
            }

            RowLayout {
                anchors.fill: parent
                anchors.rightMargin: 12
                spacing: 8

                Label {
                    text: "ClamGuard Security"
                    color: "#81a1c1"
                    font.bold: true
                    Layout.fillWidth: true
                    leftPadding: 15
                }

                // Minimize Button
                Rectangle {
                    id: minButton
                    width: 16
                    height: 16
                    radius: 8
                    color: minMouse.containsMouse ? "#A3BE8C" : "#EBCB8B"

                    Behavior on color {
                        ColorAnimation { duration: 120 }
                    }

                    MouseArea {
                        id: minMouse
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor

                        onClicked: {
                            if (mainwindow) {
                                mainwindow.minimizeWindow(root);
                            }
                        }
                    }
                }

                // Close/Hide Button
                Rectangle {
                    id: closeButton
                    width: 16
                    height: 16
                    radius: 8
                    color: closeMouse.containsMouse ? "#BF616A" : "#D08770"

                    Behavior on color {
                        ColorAnimation { duration: 120 }
                    }

                    MouseArea {
                        id: closeMouse
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor

                        onClicked: {
                            if (mainwindow) {
                                mainwindow.hideToTray(root);
                            }
                        }
                    }
                }
            }
        }

        StackLayout {
            id: pages
            Layout.fillWidth: true
            Layout.fillHeight: true
            currentIndex: 0

            HomePage {
                id: home
                onOpenScanPage: pages.currentIndex = 1
                onOpenUpdatePage: pages.currentIndex = 2
                onOpenAboutPage: pages.currentIndex = 3
                onOpenQuarantinePage: pages.currentIndex = 4
            }

            ScanPage {
                id: scanPage
                onGoToHome: pages.currentIndex = 0
            }

            UpdatePage {
                id: updatePage
                onGoToHome: pages.currentIndex = 0
            }

            AboutPage {
                id: aboutPage
                onGoToHome: pages.currentIndex = 0
            }

            QuarantinePage {
                id: quarantinePage
                onGoToHome: pages.currentIndex = 0
            }
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 25
            color: "#3b4252"

            Label {
                anchors.centerIn: parent
                text: mainwindow ? mainwindow.engineVersion : "Engine Version 1.3.0"
                color: "#eceff4"
            }
        }
    }
}

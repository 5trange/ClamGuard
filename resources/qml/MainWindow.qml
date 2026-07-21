import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "pages"

ApplicationWindow {
    id: root

    width: mainwindow.windowWidth
    height: mainwindow.windowHeight
    minimumWidth: 800
    minimumHeight: 600
    maximumWidth: 800
    maximumHeight: 600

    visible: true
    title: mainwindow.windowTitle

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
                onPressed: {
                    root.startSystemMove()
                }
                z: -1
            }

            RowLayout {
                anchors.fill: parent
                anchors.top: parent.top
                anchors.right: parent.right
                anchors.rightMargin: 12
                spacing: 8

                Label {
                    text: "ClamGuard Security"
                    color: "#81a1c1"
                    font.bold: true

                    Layout.fillWidth: true
                    leftPadding: 15
                }

                Rectangle {
                    id: minButton
                    width: 16
                    height: 16
                    radius: 8
                    color: mouse.containsMouse ? "#A3BE8C" : "#EBCB8B"

                    Behavior on color {
                        ColorAnimation { duration: 120 }
                    }

                    MouseArea {
                        id: mouse
                        anchors.fill: parent
                        hoverEnabled: true
                        cursorShape: Qt.PointingHandCursor

                        onClicked: mainwindow.minimizeWindow(root)
                    }
                }

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

                        onClicked: Qt.quit()
                    }
                }
            }
        }

        StackLayout {
            id: pages
            Layout.fillWidth: true
            Layout.fillHeight: true

            HomePage {}
            ScanPage {}
            UpdatePage {}
            AboutPage {}
            QuarantinePage {}
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 25

            color: "#3b4252"

            Label {
                anchors.centerIn: parent

                text: "Engine Version"
                color: "#eceff4"
            }
        }
    }
}

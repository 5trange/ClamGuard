import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Page {
    id: pageAbout

    signal aboutGoHome()

    background: Rectangle {
        color: "transparent"
    }

    ColumnLayout {
        anchors.fill: parent
        spacing: 16

        Rectangle {
            id: frameAboutNav

            Layout.fillWidth: true
            Layout.preferredHeight: 160

            color: "transparent"

            Button {
                id: aboutHomeButton

                anchors.left: parent.left
                anchors.leftMargin: 10
                anchors.verticalCenter: parent.verticalCenter

                width: 182
                height: 120

                text: ""

                icon.source: "qrc:/img/home.png"
                icon.width: 50
                icon.height: 50

                hoverEnabled: true

                background: Rectangle {
                    radius: 5
                    color: aboutHomeButton.hovered ? "#3b4252" : "#2e3440"
                    border.width: aboutHomeButton.hovered ? 3 : 1
                    border.color: "#b48ead"
                }

                onClicked: pageAbout.aboutGoHome()
            }

            Image {
                id: moonG3

                anchors.top: parent.top
                anchors.right: parent.right

                width: 191
                height: 171

                source: "qrc:/img/pixelmoon.png"
                fillMode: Image.PreserveAspectFit
            }
        }

        Rectangle {
            id: aboutFrame

            Layout.fillWidth: true
            Layout.fillHeight: true

            color: "#2e3440"
            radius: 8
            border.color: "#434c5e"

            ScrollView {
                anchors.fill: parent
                anchors.margins: 20

                Column {
                    width: parent.width
                    spacing: 18

                    Image {
                        id: appLogo

                        Layout.alignment: Qt.AlignHCenter

                        width: 96
                        height: 96

                        source: "qrc:/img/clamguard.png"
                        fillMode: Image.PreserveAspectFit
                    }

                    Label {
                        id: appName

                        Layout.alignment: Qt.AlignHCenter

                        text: qsTr("ClamGuard")
                        color: "#81a1c1"

                        font.pixelSize: 28
                        font.bold: true
                    }

                    Label {
                        id: appVersion

                        Layout.alignment: Qt.AlignHCenter

                        text: qsTr("Version 1.3.0")
                        color: "#d8dee9"

                        font.pixelSize: 16
                    }

                    Rectangle {
                        Layout.fillWidth: true
                        height: 1
                        color: "#434c5e"
                    }

                    Text {
                        id: description
                        width: parent.width

                        Layout.fillWidth: false

                        text:
                            qsTr("ClamGuard is a modern graphical frontend for ClamAV. "
                                 + "It provides an easy way to scan files, update virus "
                                 + "definitions, and manage quarantined files through a "
                                 + "simple Qt Quick interface.")

                        wrapMode: Text.WordWrap

                        color: "#d8dee9"
                        font.pixelSize: 15
                    }

                    Rectangle {
                        Layout.fillWidth: true
                        height: 1
                        color: "#434c5e"
                    }

                    GridLayout {
                        Layout.fillWidth: true

                        columns: 2
                        rowSpacing: 8
                        columnSpacing: 12

                        Label {
                            text: qsTr("Developer")
                            color: "#81a1c1"
                            font.bold: true
                        }

                        Label {
                            id: developerLabel
                            text: qsTr("Bilal Jafar, Adith K Murali, Vinayakan S")
                            color: "#d8dee9"
                        }

                        Label {
                            text: qsTr("Backend")
                            color: "#81a1c1"
                            font.bold: true
                        }

                        Label {
                            text: qsTr("ClamAV")
                            color: "#d8dee9"
                        }

                        Label {
                            text: qsTr("Framework")
                            color: "#81a1c1"
                            font.bold: true
                        }

                        Label {
                            text: qsTr("Qt 6 / PySide6")
                            color: "#d8dee9"
                        }

                        Label {
                            text: qsTr("License")
                            color: "#81a1c1"
                            font.bold: true
                        }

                        Label {
                            text: qsTr("GPL v3")
                            color: "#d8dee9"
                        }
                    }

                    Rectangle {
                        Layout.fillWidth: true
                        height: 1
                        color: "#434c5e"
                    }

                    RowLayout {
                        Layout.alignment: Qt.AlignHCenter
                        spacing: 12

                        Button {
                            id: githubButton

                            text: qsTr("GitHub")

                            hoverEnabled: true

                            background: Rectangle {
                                radius: 5
                                color: githubButton.hovered ? "#3b4252" : "#2e3440"
                                border.color: "#b48ead"
                                border.width: githubButton.hovered ? 3 : 1
                            }

                            contentItem: Label {
                                text: githubButton.text
                                color: "#81a1c1"
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                            }

                            onClicked: Qt.openUrlExternally("https://github.com/5trange/ClamGuard")
                        }

                        Button {
                            id: websiteButton

                            text: qsTr("Website")

                            hoverEnabled: true

                            background: Rectangle {
                                radius: 5
                                color: websiteButton.hovered ? "#3b4252" : "#2e3440"
                                border.color: "#b48ead"
                                border.width: websiteButton.hovered ? 3 : 1
                            }

                            contentItem: Label {
                                text: websiteButton.text
                                color: "#81a1c1"
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                            }

                            onClicked: Qt.openUrlExternally("https://sourceforge.net/projects/clamguard/")
                        }
                    }
                }
            }
        }
    }
}

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Page {
    id: pageScan

    signal scanGoToHome

    background: Rectangle {
        color: "transparent"
    }

    ColumnLayout {
        anchors.fill: parent
        spacing: 16

        Rectangle {
            id: frameHome

            Layout.fillWidth: true
            Layout.preferredHeight: 160

            color: "transparent"

            Button {
                id: homeButton

                anchors.left: parent.left
                anchors.leftMargin: 10
                anchors.verticalCenter: parent.verticalCenter

                width: 182
                height: 120

                icon.source: "qrc:/img/home.png"
                icon.width: 50
                icon.height: 50

                text: ""

                font.pixelSize: 18
                font.bold: true

                hoverEnabled: true

                background: Rectangle {
                    radius: 5
                    color: homeButton.hovered ? "#3b4252" : "#2e3440"
                    border.width: homeButton.hovered ? 3 : 1
                    border.color: "#b48ead"
                }
                onClicked: pageScan.scanGoToHome()
            }

            Image {
                id: moonG

                anchors.right: parent.right
                anchors.top: parent.top

                width: 191
                height: 171

                source: "qrc:/img/pixelmoon.png"
                fillMode: Image.PreserveAspectFit
            }
        }

        //
        // Scan Buttons
        //
        RowLayout {
            id: frameScanButtons

            Layout.fillWidth: true
            Layout.preferredHeight: 120

            spacing: 10

            Button {
                id: quickscanButton

                Layout.fillWidth: true
                Layout.fillHeight: true

                text: "Quick Scan"

                font.pixelSize: 18
                font.bold: true

                hoverEnabled: true

                background: Rectangle {
                    radius: 5
                    color: quickscanButton.hovered ? "#3b4252" : "#2e3440"
                    border.width: quickscanButton.hovered ? 3 : 1
                    border.color: "#b48ead"
                }

                contentItem: Label {
                    text: quickscanButton.text
                    color: "#81a1c1"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font: quickscanButton.font
                }
            }

            Button {
                id: fullscanButton

                Layout.fillWidth: true
                Layout.fillHeight: true

                text: "Full Scan"

                font.pixelSize: 18
                font.bold: true

                hoverEnabled: true

                background: Rectangle {
                    radius: 5
                    color: fullscanButton.hovered ? "#3b4252" : "#2e3440"
                    border.width: fullscanButton.hovered ? 3 : 1
                    border.color: "#b48ead"
                }

                contentItem: Label {
                    text: fullscanButton.text
                    color: "#81a1c1"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font: fullscanButton.font
                }
            }

            Button {
                id: customscanButton

                Layout.fillWidth: true
                Layout.fillHeight: true

                text: "Custom Scan"

                font.pixelSize: 18
                font.bold: true

                hoverEnabled: true

                background: Rectangle {
                    radius: 5
                    color: customscanButton.hovered ? "#3b4252" : "#2e3440"
                    border.width: customscanButton.hovered ? 3 : 1
                    border.color: "#b48ead"
                }

                contentItem: Label {
                    text: customscanButton.text
                    color: "#81a1c1"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font: customscanButton.font
                }
            }

            Button {
                id: cancelscanButton

                Layout.fillWidth: true
                Layout.fillHeight: true

                text: "Cancel Scan"

                font.pixelSize: 18
                font.bold: true

                hoverEnabled: true

                background: Rectangle {
                    radius: 5
                    color: cancelscanButton.hovered ? "#bf616a" : "#2e3440"
                    border.width: cancelscanButton.hovered ? 3 : 1
                    border.color: "#b48ead"
                }

                contentItem: Label {
                    text: cancelscanButton.text
                    color: "#81a1c1"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    font: cancelscanButton.font
                }
            }
        }

        //
        // Scan Output
        //
        Rectangle {
            id: frameScanStatus

            Layout.fillWidth: true
            Layout.preferredHeight: 175

            color: "#2e3440"
            border.color: "#434c5e"
            radius: 5

            ScrollView {
                anchors.fill: parent
                anchors.margins: 5

                TextArea {
                    id: scanStatus

                    readOnly: true
                    wrapMode: TextArea.Wrap

                    color: "#d8dee9"
                    selectionColor: "#5e81ac"
                    selectedTextColor: "white"

                    text: ""

                    background: Rectangle {
                        color: "#2e3440"
                    }
                }
            }
        }
    }
}

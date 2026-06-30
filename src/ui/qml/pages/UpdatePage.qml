import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Page {
    id: pageUpdate

    background: Rectangle {
        color: "transparent"
    }

    ColumnLayout {
        anchors.fill: parent
        spacing: 16

        //
        // Header
        //
        Rectangle {
            id: frameGoHome

            Layout.fillWidth: true
            Layout.preferredHeight: 159

            color: "transparent"

            Button {
                id: updatehomeButton

                anchors.left: parent.left
                anchors.leftMargin: 9
                anchors.verticalCenter: parent.verticalCenter

                width: 182
                height: 120

                text: ""

                icon.source: "../img/home.png"
                icon.width: 50
                icon.height: 50

                hoverEnabled: true

                background: Rectangle {
                    radius: 5
                    color: updatehomeButton.hovered ? "#3b4252" : "#2e3440"
                    border.width: updatehomeButton.hovered ? 3 : 1
                    border.color: "#b48ead"
                }
            }

            Image {
                id: moonG2

                anchors.top: parent.top
                anchors.right: parent.right

                width: 191
                height: 171

                source: "../img/pixelmoon.png"
                fillMode: Image.PreserveAspectFit
            }
        }

        //
        // Update Buttons
        //
        RowLayout {
            id: frameUpdateButtons

            Layout.fillWidth: true
            Layout.preferredHeight: 158

            spacing: 10

            Button {
                id: checkUpdate

                Layout.preferredWidth: 182
                Layout.preferredHeight: 120

                text: "Check for Updates"

                font.pixelSize: 18
                font.bold: true

                hoverEnabled: true

                background: Rectangle {
                    radius: 5
                    color: checkUpdate.hovered ? "#3b4252" : "#2e3440"
                    border.width: checkUpdate.hovered ? 3 : 1
                    border.color: "#b48ead"
                }

                contentItem: Label {
                    text: checkUpdate.text
                    color: "#81a1c1"
                    font: checkUpdate.font
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
            }

            Item {
                Layout.fillWidth: true
            }

            Button {
                id: cancelUpdate

                Layout.preferredWidth: 182
                Layout.preferredHeight: 120

                text: "Cancel Update"

                font.pixelSize: 18
                font.bold: true

                hoverEnabled: true

                background: Rectangle {
                    radius: 5
                    color: cancelUpdate.hovered ? "#bf616a" : "#2e3440"
                    border.width: cancelUpdate.hovered ? 3 : 1
                    border.color: "#b48ead"
                }

                contentItem: Label {
                    text: cancelUpdate.text
                    color: "#81a1c1"
                    font: cancelUpdate.font
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
            }
        }

        //
        // Update Log
        //
        Rectangle {
            id: frameUpdateStatus

            Layout.fillWidth: true
            Layout.fillHeight: true

            color: "#2e3440"
            radius: 5
            border.color: "#434c5e"

            ScrollView {
                anchors.fill: parent
                anchors.margins: 9

                TextArea {
                    id: updateStatus

                    readOnly: true
                    wrapMode: TextArea.Wrap

                    color: "#d8dee9"
                    selectionColor: "#5e81ac"
                    selectedTextColor: "white"

                    background: Rectangle {
                        color: "#2e3440"
                    }
                }
            }
        }
    }
}
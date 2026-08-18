import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Dialogs

Page {
    id: pageScan
    signal goToHome

    Connections {
        target: mainwindow
        function onRunStarted() {
            scanLog.clear();
            homeButton.enabled = false;
            quickscanButton.enabled = false;
            fullscanButton.enabled = false;
            customscanButton.enabled = false;
            cancelscanButton.enabled = true;
        }
        function onRunFinished() {
            homeButton.enabled = true;
            quickscanButton.enabled = true;
            fullscanButton.enabled = true;
            customscanButton.enabled = true;
            cancelscanButton.enabled = false;
        }

        function onRunOutputReceived(output) {
            scanLog.appendLimited(output);
        }
    }

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

                onClicked: pageScan.goToHome()
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

                onClicked: mainwindow.quickScan()
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

                onClicked: mainwindow.fullScan()
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

                onClicked: folderDialog.open()

                FolderDialog {
                    id: folderDialog
                    title: "Select a Folder"
                    onAccepted: {
                        scanLog.appendLimited("Scanning... " + selectedFolder + "\n");
                        mainwindow.customScan(selectedFolder);
                    }
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

                onClicked: mainwindow.cancelScan()
            }
        }

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

                ListView {
                    id: scanLog
                    anchors.fill: parent
                    anchors.margins: 5
                    clip: true
                    spacing: 2
                    property bool userAtBottom: true
                    model: ListModel { id: logModel }

                    delegate: Text {
                        text: message
                        color: "#d8dee9"
                        width: ListView.view.width
                        wrapMode: Text.Wrap
                        lineHeight: 1.2
                        lineHeightMode: Text.ProportionalHeight
                    }

                    onContentYChanged: {
                        userAtBottom = (contentHeight - contentY - height) < 50;
                    }

                    Rectangle {
                        anchors.fill: parent
                        color: "#2e3440"
                        z: -1
                    }

                    function clear(){
                        logModel.clear();
                    }

                    function appendLimited(text) {
                        logModel.append({ message: text });
                        while (logModel.count > 500) {
                            logModel.remove(0);
                        }
                        scanLog.forceLayout();
                        scanLog.positionViewAtEnd();
                    }
                }
            }
        }
    }
}

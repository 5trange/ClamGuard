import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Page {
    id: pageQuarantine

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
            id: frameQuarantineNav

            Layout.fillWidth: true
            Layout.preferredHeight: 160

            color: "transparent"

            Button {
                id: quarantineHomeButton

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
                    color: quarantineHomeButton.hovered ? "#3b4252" : "#2e3440"
                    border.width: quarantineHomeButton.hovered ? 3 : 1
                    border.color: "#b48ead"
                }
            }

            Image {
                id: moonG4

                anchors.top: parent.top
                anchors.right: parent.right

                width: 191
                height: 171

                source: "qrc:/img/pixelmoon.png"
                fillMode: Image.PreserveAspectFit
            }
        }

        //
        // Content
        //
        Rectangle {
            id: frameQuarantineContent

            Layout.fillWidth: true
            Layout.fillHeight: true

            color: "#2e3440"
            radius: 5
            border.color: "#434c5e"

            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 12
                spacing: 12

                RowLayout {
                    Layout.fillWidth: true

                    Label {
                        text: qsTr("Quarantine")
                        color: "#81a1c1"
                        font.pixelSize: 24
                        font.bold: true
                    }

                    Item {
                        Layout.fillWidth: true
                    }

                    Button {
                        id: quarantineRefresh

                        text: qsTr("Refresh")

                        hoverEnabled: true

                        background: Rectangle {
                            radius: 5
                            color: quarantineRefresh.hovered ? "#3b4252" : "#2e3440"
                            border.width: quarantineRefresh.hovered ? 3 : 1
                            border.color: "#b48ead"
                        }

                        contentItem: Label {
                            text: quarantineRefresh.text
                            color: "#81a1c1"
                            font: quarantineRefresh.font
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter
                        }
                    }
                }

                TableView {
                    id: quarantineView

                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    clip: true

                    columnSpacing: 1
                    rowSpacing: 1

                    boundsBehavior: Flickable.StopAtBounds

                    delegate: Rectangle {
                        implicitHeight: 34
                        color: styleData.selected ? "#5e81ac" : "#2e3440"
                        border.color: "#434c5e"

                        Text {
                            anchors.fill: parent
                            anchors.margins: 8

                            text: display
                            color: "#d8dee9"
                            verticalAlignment: Text.AlignVCenter
                            elide: Text.ElideRight
                        }
                    }

                    ScrollBar.vertical: ScrollBar {}
                    ScrollBar.horizontal: ScrollBar {}
                }
            }
        }
    }
}

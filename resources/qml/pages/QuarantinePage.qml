import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Page {
    id: pageQuarantine

    Component.onCompleted: {
        quarantineModel.load()
    }

    signal quarantineGoHome

    background: Rectangle {
        color: "transparent"
    }

    ColumnLayout {
        anchors.fill: parent
        spacing: 16

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

                onClicked: pageQuarantine.quarantineGoHome()
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

                        onClicked: quarantineModel.load()
                    }
                }

                HorizontalHeaderView {
                    id: quarantineHeader

                    Layout.fillWidth: true
                    Layout.preferredHeight: 35

                    syncView: quarantineView

                    delegate: Rectangle {
                        implicitHeight: 35

                        color: "#3b4252"
                        border.color: "#434c5e"

                        Text {
                            anchors.fill: parent
                            anchors.leftMargin: 8

                            text: model.display

                            color: "#81a1c1"
                            font.bold: true

                            verticalAlignment: Text.AlignVCenter
                            elide: Text.ElideRight
                        }
                    }
                }

                TableView {
                    id: quarantineView

                    property int hoveredColumn: -1

                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    clip: true

                    model: quarantineModel

                    property var normalColumnWidths: [180, 220, 400, 180]

                    property var expandedColumnWidths: [280, 350, 600, 250]

                    columnSpacing: 1
                    rowSpacing: 1

                    boundsBehavior: Flickable.StopAtBounds

                    columnWidthProvider: function (column) {
                        switch (column) {
                        case 0:
                            return quarantineView.width * 0.20;
                        case 1:
                            return quarantineView.width * 0.25;
                        case 2:
                            return quarantineView.width * 0.35;
                        case 3:
                            return quarantineView.width * 0.20;
                        default:
                            return 100;
                        }
                    }

                    rowHeightProvider: function (row) {
                        return 40;
                    }

                    delegate: Rectangle {
                        implicitWidth: 200
                        implicitHeight: 40

                        color: "#2e3440"
                        border.width: 1
                        border.color: "#434c5e"

                        Text {
                            id: cellText
                            anchors.fill: parent
                            anchors.margins: 8

                            text: display
                            color: "#d8dee9"

                            verticalAlignment: Text.AlignVCenter
                            elide: Text.ElideRight
                        }

                        MouseArea {
                            id: mouseArea

                            anchors.fill: parent
                            hoverEnabled: true

                            onEntered: {
                                quarantineView.hoveredColumn = column;
                                quarantineView.forceLayout();
                            }

                            onExited: {
                                quarantineView.hoveredColumn = -1;
                                quarantineView.forceLayout();
                            }
                        }

                        ToolTip.visible: mouseArea.containsMouse && cellText.truncated
                        ToolTip.text: display
                        ToolTip.delay: 500
                    }

                    ScrollBar.vertical: ScrollBar {}
                    ScrollBar.horizontal: ScrollBar {}
                }
            }
        }
    }
}

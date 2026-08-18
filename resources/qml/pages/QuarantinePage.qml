import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Page {
    id: pageQuarantine

    Component.onCompleted: {
        quarantineModel.load();
    }

    signal goToHome

    background: Rectangle {
        color: "transparent"
    }

    ColumnLayout {
        anchors.fill: parent
        spacing: 16

        // --- Navigation Header ---
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

                onClicked: pageQuarantine.goToHome()
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

        // --- Main Content Area ---
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

                // Top Bar: Title + Refresh
                RowLayout {
                    Layout.fillWidth: true

                    Label {
                        text: qsTr("Quarantine")
                        color: "#81a1c1"
                        font.pixelSize: 24
                        font.bold: true
                    }

                    Item { Layout.fillWidth: true }

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

                // Table Header
                HorizontalHeaderView {
                    id: quarantineHeader
                    syncView: quarantineView
                    resizableColumns: true
                    visible: quarantineModel && quarantineModel.count > 0

                    model: [
                        "Name",
                        "Type",
                        "Original Location",
                        "Date",
                        "Actions"
                    ]

                    delegate: Rectangle {
                        implicitWidth: index === 4 ? 140 : 150
                        implicitHeight: 35
                        color: "#3b4252"
                        border.color: "#434c5e"

                        Text {
                            anchors.fill: parent
                            anchors.leftMargin: 8
                            text: modelData
                            color: "#81a1c1"
                            font.bold: true
                            verticalAlignment: Text.AlignVCenter
                            elide: Text.ElideRight
                        }
                    }
                }

                // Table View
                Item {
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    TableView {
                        id: quarantineView
                        anchors.fill: parent
                        visible: quarantineModel && quarantineModel.count > 0
                        clip: true
                        model: quarantineModel
                        columnSpacing: 1
                        rowSpacing: 1
                        boundsBehavior: Flickable.StopAtBounds

                        delegate: Rectangle {
                            id: cell
                            implicitWidth: column === 4 ? 140 : 150
                            implicitHeight: 40

                            required property int column
                            required property int row
                            required property string display

                            color: mouseArea.containsMouse ? "#3b4252" : "#2e3440"
                            border.width: 1
                            border.color: "#434c5e"

                            Loader {
                                anchors.fill: parent
                                anchors.margins: 4
                                active: cell.column === 4
                                sourceComponent: actionsComponent
                            }

                            Text {
                                id: cellText
                                visible: cell.column !== 4
                                anchors.fill: parent
                                anchors.margins: 8
                                text: cell.display
                                color: "#d8dee9"
                                verticalAlignment: Text.AlignVCenter
                                elide: Text.ElideRight

                                ToolTip {
                                    visible: mouseArea.containsMouse && cellText.truncated
                                    text: cell.display
                                    delay: 500
                                }
                            }

                            MouseArea {
                                id: mouseArea
                                anchors.fill: parent
                                hoverEnabled: true
                            }
                        }

                        ScrollBar.vertical: ScrollBar { policy: ScrollBar.AsNeeded }
                        ScrollBar.horizontal: ScrollBar { policy: ScrollBar.AsNeeded }
                    }

                    Rectangle {
                        anchors.fill: parent
                        color: "#2e3440"
                        visible: quarantineModel && quarantineModel.count > 0

                        Column {
                            anchors.centerIn: parent
                            spacing: 12

                            Text {
                                anchors.horizontalCenter: parent.horizontalCenter
                                text: qsTr("No Virus Found")
                                color: "#81a1c1"
                                font.pixelSize: 22
                                font.bold: true
                            }

                            Text {
                                anchors.horizontalCenter: parent.horizontalCenter
                                text: qsTr("Your quarantine folder is empty")
                                color: "#d8dee9"
                                font.pixelSize: 14
                                opacity: 0.6
                            }
                        }
                    }
                }
            }
        }
    }

    // --- Component: Action Buttons for TableView ---
    Component {
        id: actionsComponent
        Row {
            spacing: 8
            anchors.centerIn: parent

            Button {
                text: "Restore"
                width: 60
                height: 28
                hoverEnabled: true

                background: Rectangle {
                    radius: 4
                    color: parent.hovered ? "#A3BE8C" : "#2e3440"
                    border.width: 1
                    border.color: "#A3BE8C"
                }

                contentItem: Text {
                    text: parent.text
                    color: parent.hovered ? "#2e3440" : "#A3BE8C"
                    font.bold: true
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }

                onClicked: {
                    if (quarantineModel.restoreItem(cell.row)) {
                        console.log("Restored successfully")
                    }
                }
            }

            Button {
                text: "Delete"
                width: 60
                height: 28
                hoverEnabled: true

                background: Rectangle {
                    radius: 4
                    color: parent.hovered ? "#BF616A" : "#2e3440"
                    border.width: 1
                    border.color: "#BF616A"
                }

                contentItem: Text {
                    text: parent.text
                    color: parent.hovered ? "#2e3440" : "#BF616A"
                    font.bold: true
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }

                onClicked: {
                    if (quarantineModel.deleteItem(cell.row)) {
                        console.log("Deleted successfully")
                    }
                }
            }
        }
    }
}

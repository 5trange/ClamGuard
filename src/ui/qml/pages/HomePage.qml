import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Page {
    id: homePage

    background: Rectangle {
        color: "transparent"
    }

    Item {
        id: content
        anchors.fill: parent

        Image {
            id: voyagerHome
            anchors.fill: parent
            source: "../img/voyager.png"
            fillMode: Image.PreserveAspectCrop
        }

        Rectangle {
            id: scanFrame

            x: 155
            y: 181
            width: 160
            height: 160

            color: "transparent"

            radius: 20
            border.width: 5
            border.color: "#81a1c1"

            Image {
                id: scanImg

                anchors.horizontalCenter: parent.horizontalCenter
                y: 10

                width: 100
                height: 100

                source: "../img/search.png"
                fillMode: Image.PreserveAspectFit
            }

            Label {
                id: scanlabel

                anchors.horizontalCenter: parent.horizontalCenter
                y: 115

                text: "SCAN"

                color: "#81a1c1"

                font.pixelSize: 20
                font.bold: true
            }

            MouseArea {
                anchors.fill: parent
                hoverEnabled: true
                cursorShape: Qt.PointingHandCursor

                // Connect later
                // onClicked: ...
            }
        }

        Rectangle {
            id: updateFrame

            x: 467
            y: 181
            width: 160
            height: 160

            color: "transparent"

            radius: 20
            border.width: 5
            border.color: "#81a1c1"

            Image {
                id: updateImg

                anchors.horizontalCenter: parent.horizontalCenter
                y: 10

                width: 100
                height: 100

                source: "../img/update.png"
                fillMode: Image.PreserveAspectFit
            }

            Label {
                id: updateLabel

                anchors.horizontalCenter: parent.horizontalCenter
                y: 115

                text: "UPDATE"

                color: "#81a1c1"

                font.pixelSize: 20
                font.bold: true
            }

            MouseArea {
                anchors.fill: parent
                hoverEnabled: true
                cursorShape: Qt.PointingHandCursor

                // onClicked: ...
            }
        }

        Image {
            id: quarantineLabel

            x: 10
            y: 480

            width: 32
            height: 32

            source: "../img/warning.png"

            fillMode: Image.PreserveAspectFit

            ToolTip.visible: quarantineMouse.containsMouse
            ToolTip.text: qsTr("View Quarantine")

            MouseArea {
                id: quarantineMouse
                anchors.fill: parent
                hoverEnabled: true
                cursorShape: Qt.PointingHandCursor

                // onClicked: ...
            }
        }

        Image {
            id: aboutLabel

            x: 50
            y: 480

            width: 32
            height: 32

            source: "../img/info.png"

            fillMode: Image.PreserveAspectFit

            ToolTip.visible: aboutMouse.containsMouse
            ToolTip.text: qsTr("About ClamGuard Project")

            MouseArea {
                id: aboutMouse
                anchors.fill: parent
                hoverEnabled: true
                cursorShape: Qt.PointingHandCursor

                // onClicked: ...
            }
        }
    }
}
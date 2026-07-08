import QtQuick
import QtQuick.Controls

ApplicationWindow {
    id: splashScreenwindow

    width: 680
    height: 400
    visible: true
    title: "Starting ClamGuard"

    Connections {
        target: splashscreen

        function onStartupFinished() {
            splashScreenwindow.close()
        }
    }

    Component.onCompleted: {
      splashscreen.start()
    }

    Rectangle {
        anchors.fill: parent
        color: "transparent"

        Rectangle {
            id: dropShadowFrame

            anchors.fill: parent

            color: "#2e3440"
            radius: 10

            Image {
                id: pix

                anchors.fill: parent
                source: "qrc:/img/voyager.png"
                fillMode: Image.Stretch
            }

            Label {
                id: labelTitle

                anchors.horizontalCenter: parent.horizontalCenter
                y: 130
                width: parent.width
                height: 81

                text: "CLAMGUARD"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter

                font.pixelSize: 40
                font.bold: true

                color: "#81a1c1"
            }

            ProgressBar {
                id: progressBar

                x: 50
                y: 280
                width: 561
                height: 23

                from: 0
                to: 100
                value: splashscreen ? splashscreen.progress : 1
                
                background: Rectangle {
                    color: "#2e3440"
                }

                contentItem: Item {
                    Rectangle {
                        width: progressBar.visualPosition * progressBar.width
                        height: progressBar.height
                        color: "#a3be8c"
                    }
                }
            }

            Label {
                id: labelLoading

                anchors.horizontalCenter: parent.horizontalCenter
                y: 320
                width: parent.width
                height: 21

                text: splashscreen?.status ?? ""

                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter

                font.pixelSize: 12
                color: "#81a1c1"
            }
        }
    }
}

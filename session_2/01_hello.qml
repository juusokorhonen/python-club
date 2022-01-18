import QtQuick
import QtQuick.Window
import QtQuick.Controls.Material

Window {

    id: root
    visible: true
    width: 720
    height: 540
    x: 100
    y: 100
    title: qsTr("Hello from the PySide")

    Text {

        text: qsTr("Hello from the PySide!")
        font.pixelSize: 56
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter

    }

    Button {

        text: qsTr("Exit")
        anchors.horizontalCenter: parent.horizontalCenter
        y: 400
        onClicked: root.close();

    }

}
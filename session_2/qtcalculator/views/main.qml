import QtQuick
import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls.Material
import "components"

Window {

    id: root
    visible: true
    width: 540
    height: 540
    x: 100
    y: 100

    Material.theme: Material.Light
    Material.accent: Material.Cyan

    Window {

        visible: true
        width: 300
        height: 200
        x: 200
        y: 200

    }

    ColumnLayout {
        spacing: 32
        width: parent.width
        height: parent.height

        Display {

            id: display
            Layout.alignment: Qt.AlignCenter

        }

        NumberPad {

            id: pad
            Layout.alignment: Qt.AlignCenter

        }    

    }

    

}
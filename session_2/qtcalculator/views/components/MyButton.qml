import QtQuick
import QtQuick.Controls.Material

Button {

    id: button
    text: "?"
    
    Material.foreground: Material.Primary

    states: [
        State {

            name: "pressed"
            when: button.pressed
            PropertyChanges {

            }

        }
    ]

}
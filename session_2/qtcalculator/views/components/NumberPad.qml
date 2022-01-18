import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

GridLayout {

    columns: 3
    columnSpacing: 32
    rowSpacing: 16

    Layout.preferredHeight: 450

    component DigitButton: MyButton {
        onPressed: function() {
            display.text += this.text
        }
    }

    component OperatorButton: MyButton {
        Material.background: Material.Teal
        onPressed: function() {
            window.operatorPressed(text)
        }
    }

    DigitButton {
        text: "7"
    }
    DigitButton {
        text: "8"
    }
    DigitButton {
        text: "9"
    }
    DigitButton {
        text: "4"
    }
    DigitButton {
        text: "5"
    }
    DigitButton {
        text: "6"
    }
    DigitButton {
        text: "1"
    }
    DigitButton {
        text: "2"
    }
    DigitButton {
        text: "3"
    }
    DigitButton {
        text: "0"
    }

    DigitButton {
        text: "."
    }
    DigitButton {
        text: " "
    }
    
    OperatorButton {
        text: " "
    }
    OperatorButton {
        text: "-"
    }
    OperatorButton {
        text: "+"
    }
    OperatorButton {
        text: " "
    }
    OperatorButton {
        text: "/"
    }
    OperatorButton {
        text: "*"
    }
    OperatorButton {
        text: "C"
    }
    OperatorButton {
        text: " "
    }
    OperatorButton {
        text: "="
    }

}
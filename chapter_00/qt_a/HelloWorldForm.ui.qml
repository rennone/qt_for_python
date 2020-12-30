import QtQuick 2.4
import QtQuick.Layouts 1.0
import QtQuick.Controls 2.0

Item {
    width: col_layout.width
    height: col_layout.height
    property bool isWorld: false
    property alias text1: first_text
    property alias button: button

    ColumnLayout {
        id: col_layout
        x: 0
        y: 0

        BorderImage {
            id: borderImage
            source: "stamp01.png"
            Layout.preferredHeight: 100
            Layout.preferredWidth: 100
        }

        Text {
            id: first_text
            text: qsTr("Text")
            font.pixelSize: 12
            Layout.preferredHeight: 33
            Layout.preferredWidth: 109
        }

        Text {
            id: text2
            text: qsTr("Text")
            font.pixelSize: 12
            Layout.preferredWidth: 109
            Layout.preferredHeight: 33
        }
        Button {
            id: button
            text: qsTr("Button")
        }
    }
}

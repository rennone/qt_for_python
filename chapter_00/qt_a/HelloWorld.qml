import QtQuick 2.4
import FromPythonTextLibrary 1.0

HelloWorldForm {
    FromPythonText{
        id : from_python_text

        onValue_changed : {
            print( "QML(onValueChanged) : " + text)
        }
    }

    button.onClicked: {
        print('QML(onClicked) : ' + from_python_text.text)
        text1.text = from_python_text.text
        from_python_text.text = 'from QML'
}
}

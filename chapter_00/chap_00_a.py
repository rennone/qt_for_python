
import PySide2
from PySide2.QtWidgets import QApplication 
from PySide2.QtQuick import QQuickView 
from PySide2.QtCore import QUrl, QObject, Property, Signal
from PySide2.QtQml import qmlRegisterType
import sys

class PythonText(QObject):
    value_changed = Signal(str)
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        #QObject.connect(self, SIGNAL('valueChanged()'), self.on_value_changed)
        self._text = 'World from python'

    @Property(str, notify=value_changed)
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        print(text)
        self.value_changed.emit(self._text)

if __name__ == '__main__':
    print(PySide2.__version__)
    app = QApplication([])
    view = QQuickView()
    qmlRegisterType(PythonText, 'FromPythonTextLibrary', 1, 0, 'FromPythonText')
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    python_text = PythonText()
    context = view.rootContext()

    # #NOTE 絶対パスだとNetwork Errorで失敗する
    #url = QUrl('G:/Work/home_cmd/qt/scan_book_man/HelloWorld.qml')
    url = QUrl('qt/HelloWorld.qml')
    view.setSource(url)
    context.setContextProperty('from_python_text', python_text)
    if view.status() != QQuickView.Error:
        view.show()
        python_text.text = 'world from python'
        ret = app.exec_()
        del view
        sys.exit(ret)

    #import time
    #import argparse
    #parser = argparse.ArgumentParser('image to pdf')

    #parser.add_argument('i', nargs='*',  help='src pdf path list')
    #parser.add_argument('--gamma', action='store_false', help='apply gamma correction')
    #args = parser.parse_args()
    #tp.init()
    
    #files = {}
    #for p in args.i:
    #    key = os.path.dirname(p)
    #    if key not in files:
    #        files[key] = []
    #    files[key].append(p)

    #for key in files.keys:
    #    p = ScanPdfProcessor(key, files[key])
    #    p.merge_and_save()
    #    p.convert_to_png()
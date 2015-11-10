__author__ = 'Lucas'

import sys
from PyQt4 import QtCore, QtGui
from my_first_gui import Ui_Form

class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.writetext)

    def writetext(self):
        self.ui.label.setText(self.ui.lineEdit.text())
        print "Hello World"

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
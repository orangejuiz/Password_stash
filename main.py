import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QIcon
from sneakyapp import Ui_MainWindow


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEdit.setPlaceholderText("Sneaky pass")
        self.ui.lineEdit_2.setPlaceholderText("Sneaky pass")
        self.ui.pushButton.clicked.connect(lambda: self.btnClicked())

    def btnClicked(self):
        self.ui.label_6.setText("Успешно!")
        self.ui.label_6.adjustSize()
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())


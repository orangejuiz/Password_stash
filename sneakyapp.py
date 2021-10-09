# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sneakyapp.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(2, 0, 460, 150))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 110, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(24)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(-50, 0, 451, 141))
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 35)")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../Desktop/3 копия.png"))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 190, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(130, 134, 255)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 270, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(130, 134, 255)")
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(19, 150, 421, 2))
        self.frame_2.setStyleSheet("background-color: rgba(90, 93, 255, 158)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 400, 60, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(188, 440, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(130, 134, 255)")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255,255,255);\n"
"border: 2px solid rgb(130, 134, 255);\n"
"border-radius: 15;\n"
"color: black")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 300, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255,255,255);\n"
"border: 2px solid rgb(130, 134, 255);\n"
"border-radius: 15;\n"
"color: black")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 391, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: rgba(0, 0, 255, 204);\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"\n"
"    background-color: rgba(0, 255, 255, 144)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Новый пароль"))
        self.label_2.setText(_translate("MainWindow", "Название"))
        self.label_3.setText(_translate("MainWindow", "Пароль"))
        self.label_6.setText((_translate("MainWindow", "")))
        self.pushButton.setText(_translate("MainWindow", "СОЗДАТЬ"))

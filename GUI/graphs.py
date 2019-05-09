# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graphs.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from buysell import Ui_Buysell
class Ui_Graphs(object):

    def openbuysell(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Buysell()
        self.ui.setupUi(self.window)
        self.window.show()


    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(930, 605)
        Dialog.setStyleSheet("background-color: rgb(189, 255, 231);\n"
"")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(570, 60, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 110, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 160, 75, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 390, 171, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")


        self.pushButton_4.clicked.connect(self.openbuysell)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "1 hour"))
        self.pushButton_2.setText(_translate("Dialog", "24 hours"))
        self.pushButton_3.setText(_translate("Dialog", "7 days"))
        self.pushButton_4.setText(_translate("Dialog", "Buy/Sell"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Graphs()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orders.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Orders(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(671, 487)
        Dialog.setStyleSheet("background-color: rgb(189, 255, 231);\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(86, 50, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(430, 50, 91, 16))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(50, 80, 201, 371))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(410, 80, 201, 371))
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Ordres ouverts"))
        self.label_2.setText(_translate("Dialog", "Trades terminés"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Orders()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


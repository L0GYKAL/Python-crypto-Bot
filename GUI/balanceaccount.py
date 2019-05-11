
from PyQt5 import QtCore, QtGui, QtWidgets
from accountEditor import Ui_AccountEditor


class Ui_balanceaccount(object):

    def openAccount(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AccountEditor()
        self.ui.setupUi(self.window)
        self.window.show()
    


    
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Account")
        Dialog.resize(692, 535)
        Dialog.setStyleSheet("background-color: rgb(189, 255, 231);\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 60, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(500, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(60, 90, 211, 311))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(410, 90, 211, 311))
        self.listWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(290, 440, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 490, 281, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.openAccount)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Exchanges"))
        self.label_2.setText(_translate("Dialog", "Adresses"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "binance..."))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Dialog", "doge..."))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setText(_translate("Dialog", "Total Balance: "))
        self.pushButton.setText(_translate("Dialog", "Edit exchanges and addresses"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_balanceaccount()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

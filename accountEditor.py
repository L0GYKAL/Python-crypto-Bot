# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\accountEditor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..") # Adds higher directory to python modules path.
import APIkeys_fetching, fetchAddresses
from BasicFonctionalities import getAllCurrencies

class Ui_Account(object):
    def setupUi(self, Account):
        Account.setObjectName("Account")
        Account.resize(572, 508)
        self.textBrowser = QtWidgets.QTextBrowser(Account)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 581, 51))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(Account)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 551, 81))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.nameLine = QtWidgets.QPlainTextEdit(self.groupBox)
        self.nameLine.setGeometry(QtCore.QRect(80, 50, 111, 21))
        self.nameLine.setObjectName("nameLine")
        self.surnameLine = QtWidgets.QPlainTextEdit(self.groupBox)
        self.surnameLine.setGeometry(QtCore.QRect(80, 20, 111, 21))
        self.surnameLine.setObjectName("surnameLine")
        self.groupBox_2 = QtWidgets.QGroupBox(Account)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 551, 341))
        self.groupBox_2.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(29, 30, 201, 271))
        self.groupBox_3.setObjectName("groupBox_3")
        self.idLine = QtWidgets.QLineEdit(self.groupBox_3)
        self.idLine.setGeometry(QtCore.QRect(20, 110, 113, 20))
        self.idLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idLine.setObjectName("idLine")
        self.apikeyline = QtWidgets.QLineEdit(self.groupBox_3)
        self.apikeyline.setGeometry(QtCore.QRect(20, 150, 113, 20))
        self.apikeyline.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.apikeyline.setObjectName("apikeyline")
        self.secretLine = QtWidgets.QLineEdit(self.groupBox_3)
        self.secretLine.setGeometry(QtCore.QRect(20, 190, 113, 20))
        self.secretLine.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.secretLine.setObjectName("secretLine")
        self.addButton = QtWidgets.QPushButton(self.groupBox_3)
        self.addButton.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.addButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.addAnExchange)
        self.modifierButton = QtWidgets.QPushButton(self.groupBox_3)
        self.modifierButton.setGeometry(QtCore.QRect(110, 230, 75, 23))
        self.modifierButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.modifierButton.setObjectName("modifierButton")
        self.modifierButton.clicked.connect(self.addAnExchange)
        self.Exchangeliste = QtWidgets.QComboBox(self.groupBox_3)
        self.Exchangeliste.setGeometry(QtCore.QRect(30, 40, 131, 31))
        self.Exchangeliste.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Exchangeliste.setObjectName("Exchangeliste")
        self.Exchangeliste.addItem("")
        self.Exchangeliste.addItem("")
        self.Exchangeliste.addItem("")
        self.Exchangeliste.addItem("")
        self.Exchangeliste.addItem("")
        self.Exchangeliste.addItem("")
        self.Exchangeliste.addItem("")
        self.Exchangeliste.setCurrentRow(0)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(290, 30, 201, 271))
        self.groupBox_4.setObjectName("groupBox_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 40, 131, 31))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        symbols = getAllCurrencies()
        for symbol in symbols:
            self.comboBox_2.addItem(symbol)
        self.comboBox_2.currentIndex(0)
        self.addressline = QtWidgets.QLineEdit(self.groupBox_4)
        self.addressline.setGeometry(QtCore.QRect(30, 110, 113, 20))
        self.addressline.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.addressline.setObjectName("addressline")
        self.addAddressepush = QtWidgets.QPushButton(self.groupBox_4)
        self.addAddressepush.setGeometry(QtCore.QRect(70, 190, 75, 23))
        self.addAddressepush.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.addAddressepush.setObjectName("addAddressepush")
        self.addAddressepush.clicked.connect(self.addAnAddresse)

        self.retranslateUi(Account)
        QtCore.QMetaObject.connectSlotsByName(Account)
        
    def addAnExchange(self):
        api = APIkeys_fetching.APIkeys()
        exchange = self.Exchangeliste.currentItem().text()
        Id = self.nameLine.text()
        apikey = self.apikeyline.text()
        secret = self.secretLine.text()
        api.APIkeys_fetching.editKeys(exchange, Id, apikey, secret)
        
    def addAnAddresse(self):
        addresses = fetchAddresses.addresses()
        addresse = self.addressline.text()
        symbol = self.comboBox_2.currentText()
        addresses.add(addresse, symbol)
        

    def retranslateUi(self, Account):
        _translate = QtCore.QCoreApplication.translate
        Account.setWindowTitle(_translate("Account", "AccountEditor"))
        self.textBrowser.setHtml(_translate("Account", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000;\">Welcome to your account!</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Account", "Personnal Informations"))
        self.label.setText(_translate("Account", "Surname"))
        self.label_2.setText(_translate("Account", "Name"))
        self.groupBox_2.setTitle(_translate("Account", "Wallet"))
        self.groupBox_3.setTitle(_translate("Account", "Exchange"))
        self.idLine.setText(_translate("Account", "Nom"))
        self.apikeyline.setText(_translate("Account", "Clé publique"))
        self.secretLine.setText(_translate("Account", "Clé privé"))
        self.addButton.setText(_translate("Account", "Ajouter"))
        self.modifierButton.setText(_translate("Account", "Modifier"))
        self.Exchangeliste.setItemText(0, _translate("Account", "binance"))
        self.Exchangeliste.setItemText(1, _translate("Account", "upbit"))
        self.Exchangeliste.setItemText(2, _translate("Account", "kucoin"))
        self.Exchangeliste.setItemText(3, _translate("Account", "kraken"))
        self.Exchangeliste.setItemText(4, _translate("Account", "coss"))
        self.Exchangeliste.setItemText(5, _translate("Account", "bittrex"))
        self.Exchangeliste.setItemText(6, _translate("Account", "bitfinex"))
        self.groupBox_4.setTitle(_translate("Account", "Adresse"))
        self.comboBox_2.setItemText(0, _translate("Account", "BTC"))
        self.addressline.setText(_translate("Account", "Adresse"))
        self.addAddressepush.setText(_translate("Account", "Ajouter"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account = QtWidgets.QDialog()
    ui = Ui_Account()
    ui.setupUi(Account)
    Account.show()
    sys.exit(app.exec_())


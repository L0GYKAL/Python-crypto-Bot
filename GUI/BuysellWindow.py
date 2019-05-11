# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Buysell.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("..")  # Adds higher directory to python modules path.
import orders

class Ui_Dialog(object):
    def setupUi(self, Dialog, exchange, ticker):
        self.exchange = exchange
        self.ticker = ticker
        self.tickerList = ticker.split('/')
        Dialog.setObjectName("Dialog")
        Dialog.resize(301, 521)
        Dialog.setStyleSheet("background-color: rgb(189, 255, 231);\n"
"")
        self.exchangeAndTicker = QtWidgets.QLabel(Dialog)
        self.exchangeAndTicker.setGeometry(QtCore.QRect(80, 30, 101, 20))
        self.exchangeAndTicker.setObjectName("exchangeAndTicker")
        self.PriceText = QtWidgets.QLabel(Dialog)
        self.PriceText.setGeometry(QtCore.QRect(70, 100, 47, 21))
        self.PriceText.setObjectName("PriceText")
        self.AmountText = QtWidgets.QLabel(Dialog)
        self.AmountText.setGeometry(QtCore.QRect(70, 190, 47, 13))
        self.AmountText.setObjectName("AmountText")
        self.totalAmountAndSymbol = QtWidgets.QLabel(Dialog)
        self.totalAmountAndSymbol.setGeometry(QtCore.QRect(70, 280, 111, 16))
        self.totalAmountAndSymbol.setObjectName("totalAmountAndSymbol")
        self.Buy = QtWidgets.QPushButton(Dialog)
        self.Buy.setGeometry(QtCore.QRect(20, 420, 101, 31))
        self.Buy.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Buy.setObjectName("Buy")
        self.Buy.clicked.connect(self.buyOrder)
        self.Sell = QtWidgets.QPushButton(Dialog)
        self.Sell.setGeometry(QtCore.QRect(150, 420, 101, 31))
        self.Sell.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Sell.setObjectName("Sell")
        self.Sell.clicked.connect(self.sellOrder)
        self.Price = QtWidgets.QLineEdit(Dialog)
        self.Price.setGeometry(QtCore.QRect(70, 130, 113, 20))
        self.Price.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Price.setObjectName("Price")
        self.Amount = QtWidgets.QLineEdit(Dialog)
        self.Amount.setGeometry(QtCore.QRect(70, 220, 113, 20))
        self.Amount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Amount.setObjectName("Amount")
        self.totalAmount = QtWidgets.QLineEdit(Dialog)
        self.totalAmount.setGeometry(QtCore.QRect(70, 310, 113, 20))
        self.totalAmount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.totalAmount.setObjectName("totalAmount")
        self.tickerSymbol2 = QtWidgets.QLabel(Dialog)
        self.tickerSymbol2.setGeometry(QtCore.QRect(190, 130, 47, 21))
        self.tickerSymbol2.setObjectName("tickerSymbol2")
        #assignement du texte
        self.tickerSymbol2.setText(self.tickerList[1])
        
        self.tickerSymbol1 = QtWidgets.QLabel(Dialog)
        self.tickerSymbol1.setGeometry(QtCore.QRect(190, 220, 47, 21))
        self.tickerSymbol1.setObjectName("tickerSymbol1")
        #assignement du texte
        self.tickerSymbol1.setText(self.tickerList[0])

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        
    def buyOrder(self):
        orders.createOrder(self.exchange, self.ticker, float(self.Amount.text()), float(self.Price.text()), 'buy', 'limit')
    
    def sellOrder(self):
        orders.createOrder(self.exchange, self.ticker, float(self.Amount.text()), float(self.Price.text()), 'sell', 'limit')
    
    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.exchangeAndTicker.setText(_translate("Dialog", "Binance: BTC/USDT"))
        self.PriceText.setText(_translate("Dialog", "Price:"))
        self.AmountText.setText(_translate("Dialog", "Amount:"))
        self.totalAmountAndSymbol.setText(_translate("Dialog", "Total amount in USDT:"))
        self.Buy.setText(_translate("Dialog", "Buy"))
        self.Sell.setText(_translate("Dialog", "Sell"))
        self.tickerSymbol2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">USDT</span></p></body></html>"))
        self.tickerSymbol1.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">BTC</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


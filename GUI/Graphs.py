# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Graphs.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import BuysellWindow
sys.path.append("..")  # Adds higher directory to python modules path.
import graphics

class Ui_Dialog(object):
    def setupUi(self, Dialog, exchange: str, ticker: str):
        #récupération du chemin
        self.mypath = os.path.dirname(__file__)
        self.exchange = exchange
        self.ticker = ticker
        graphics.chart(self.exchange, self.ticker, '1h', self.mypath)
        Dialog.setObjectName("Dialog")
        Dialog.resize(1800, 1000)
        Dialog.setStyleSheet("background-color: rgb(189, 255, 231);\n"
"")
        self.graphTo1h = QtWidgets.QPushButton(Dialog)
        self.graphTo1h.setGeometry(QtCore.QRect(1590, 60, 141, 23))
        self.graphTo1h.setWhatsThis("")
        self.graphTo1h.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphTo1h.setObjectName("graphTo1h")
        self.graphTo1h.clicked.connect(self.GraphTo1h)
        self.graphTo24h = QtWidgets.QPushButton(Dialog)
        self.graphTo24h.setGeometry(QtCore.QRect(1590, 110, 141, 23))
        self.graphTo24h.setWhatsThis("")
        self.graphTo24h.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphTo24h.setObjectName("graphTo24h")
        self.graphTo24h.clicked.connect(self.GraphTo24h)
        self.graphTo7d = QtWidgets.QPushButton(Dialog)
        self.graphTo7d.setGeometry(QtCore.QRect(1590, 160, 141, 23))
        self.graphTo7d.setWhatsThis("")
        self.graphTo7d.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graphTo7d.setObjectName("graphTo7d")
        self.graphTo7d.clicked.connect(self.GraphTo7d)
        self.BUY_SELL = QtWidgets.QPushButton(Dialog)
        self.BUY_SELL.setGeometry(QtCore.QRect(1610, 440, 171, 31))
        self.BUY_SELL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BUY_SELL.setObjectName("BUY_SELL")
        self.BUY_SELL.clicked.connect(self.openBuySell)
        self.Htmlreader_graph = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.Htmlreader_graph.setGeometry(QtCore.QRect(20, 20, 1541, 961))
        self.Htmlreader_graph.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.Htmlreader_graph.setWhatsThis("")
        self.Htmlreader_graph.setAutoFillBackground(False)
        #récupération du chemin
        self.Htmlreader_graph.setUrl(QtCore.QUrl("file:///"+ self.mypath + "/plotlyGraph.html"))
        self.Htmlreader_graph.setObjectName("Htmlreader_graph")
        self.Timeframe = QtWidgets.QLabel(Dialog)
        self.Timeframe.setGeometry(QtCore.QRect(1600, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Timeframe.setFont(font)
        self.Timeframe.setObjectName("Timeframe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    #fonction pour changer le timeframe du graph:
    #1h
    def GraphTo1h(Ui_Dialog):
        graphics.chart(Ui_Dialog.exchange, Ui_Dialog.ticker, '1h', Ui_Dialog.mypath)
        Ui_Dialog.Htmlreader_graph.reload()
        
    #24h
    def GraphTo24h(Ui_Dialog):
        graphics.chart(Ui_Dialog.exchange, Ui_Dialog.ticker, '1d', Ui_Dialog.mypath)
        Ui_Dialog.Htmlreader_graph.reload()
        
    #7d
    def GraphTo7d(Ui_Dialog):
        graphics.chart(Ui_Dialog.exchange, Ui_Dialog.ticker, '7d', Ui_Dialog.mypath)
        Ui_Dialog.Htmlreader_graph.reload()
    
    #•ouvre la fenetre BUY/SELL
    def openBuySell(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = BuysellWindow.Ui_Dialog()
        self.ui.setupUi(self.window, self.exchange, self.ticker)
        self.window.show()
    
    
    
    
    
    
    
    
    
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.graphTo1h.setText(_translate("Dialog", "1 hour"))
        self.graphTo24h.setText(_translate("Dialog", "24 hours"))
        self.graphTo7d.setText(_translate("Dialog", "7 days"))
        self.BUY_SELL.setText(_translate("Dialog", "Buy/Sell"))
        self.Timeframe.setText(_translate("Dialog", "Timeframe:"))
        

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


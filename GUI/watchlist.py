# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\watchlist.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
from .GUI import Graphs
#import Buysell
sys.path.append("..")  # Adds higher directory to python modules path.
from BasicFonctionalities import tickerFinder, marketPercent
from graphics import chart

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(930, 607)
        Dialog.setStyleSheet("background-color: rgb(189, 255, 231);\n"
"")
        self.liste = QtWidgets.QListWidget(Dialog)
        self.liste.setGeometry(QtCore.QRect(265, 31, 271, 521))
        self.liste.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.liste.setObjectName("liste")
        self.liste.setCurrentRow(0)
        self.searchBar = QtWidgets.QLineEdit(Dialog)
        self.searchBar.setGeometry(QtCore.QRect(20, 39, 161, 31))
        self.searchBar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchBar.setObjectName("searchBar")
        self.search = QtWidgets.QPushButton(Dialog)
        self.search.setGeometry(QtCore.QRect(50, 90, 81, 31))
        self.search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search.setObjectName("search")
        self.search.clicked.connect(self.searching)  #boutton relié à la fonction
        self.Graph = QtWidgets.QPushButton(Dialog)
        self.Graph.setGeometry(QtCore.QRect(360, 570, 75, 23))
        self.Graph.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Graph.setObjectName("Graph")
        self.Graph.clicked.connect(self.graph)  #boutton relié à la fonction
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(570, 30, 256, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.depuis2 = QtWidgets.QLabel(Dialog)
        self.depuis2.setGeometry(QtCore.QRect(570, 150, 81, 16))
        self.depuis2.setObjectName("depuis2")
        self.depuis3 = QtWidgets.QLabel(Dialog)
        self.depuis3.setGeometry(QtCore.QRect(570, 180, 81, 16))
        self.depuis3.setObjectName("depuis3")
        self.depuis1 = QtWidgets.QLabel(Dialog)
        self.depuis1.setGeometry(QtCore.QRect(570, 120, 81, 16))
        self.depuis1.setObjectName("depuis1")
        self.since7dpercent = QtWidgets.QLineEdit(Dialog)
        self.since7dpercent.setGeometry(QtCore.QRect(670, 120, 113, 20))
        self.since7dpercent.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.since7dpercent.setObjectName("since7dpercent")
        self.since24hpercent = QtWidgets.QLineEdit(Dialog)
        self.since24hpercent.setGeometry(QtCore.QRect(670, 150, 113, 20))
        self.since24hpercent.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.since24hpercent.setObjectName("since24hpercent")
        self.since1hpercent = QtWidgets.QLineEdit(Dialog)
        self.since1hpercent.setGeometry(QtCore.QRect(670, 180, 113, 20))
        self.since1hpercent.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.since1hpercent.setObjectName("since1hpercent")
        
        #récupération des pourcentages
        percents = marketPercent()
        self.since7dpercent.setText(percents[0])
        self.since24hpercent.setText(percents[1])
        self.since1hpercent.setText(percents[2])
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(790, 120, 47, 13))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(790, 150, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(790, 180, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 50, 31, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #création de la fonction de recherche
    def searching(self):
        _translate = QtCore.QCoreApplication.translate
        self.exchanges = tickerFinder()
        tickersList = []
        for exchange in self.exchanges.keys():
            for ticker in self.exchanges[exchange]:
                text = exchange + ' : ' + ticker
                tickersList.append(text)
        i=0
        for text in tickersList:
            item = QtWidgets.QListWidgetItem()
            self.liste.addItem(item)
            item = self.liste.item(i)
            item.setText(_translate("Dialog", text))
            i+=1
            
    def graph(self):
        i = self.liste.currentRow().text()
        t = 0
        ticker1 = ''
        exchange1 = ''
        for exchange in self.exchanges.keys():
            for ticker in self.exchanges[exchange]: 
                if t==i:
                    ticker1 = ticker
                    exchange1 = exchange
                    break
                else:
                    t+=1

        #open the Graphs window
        self.window = QtWidgets.QMainWindow()
        self.ui = Graphs.Ui_Dialog()
        self.ui.setupUi(self.window, exchange1, ticker1)
        self.window.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.liste.isSortingEnabled()
        self.liste.setSortingEnabled(False)
        self.liste.setSortingEnabled(__sortingEnabled)
        self.search.setText(_translate("Dialog", "Search"))
        self.Graph.setText(_translate("Dialog", "Graph"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:14pt; color:#000000; background-color:transparent;\">Average percentages of the 100 largest crypto:</span></p></body></html>"))
        self.depuis2.setText(_translate("Dialog", "Since 24 hours"))
        self.depuis3.setText(_translate("Dialog", "Since 1 hour"))
        self.depuis1.setText(_translate("Dialog", "Since 7 days"))
        self.label.setText(_translate("Dialog", "%"))
        self.label_5.setText(_translate("Dialog", "%"))
        self.label_6.setText(_translate("Dialog", "%"))
        mypath = os.path.dirname(__file__)
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><img src=\""+ mypath + ":/images/loupe.png\" width=30 height=30/></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\BTC_LiveGraph.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.
import graphics 

class Ui_BTC_LiveGraph(object):
    def setupUi(self, BTC_LiveGraph):
        BTC_LiveGraph.setObjectName("BTC_LiveGraph")
        BTC_LiveGraph.resize(1650, 900)
        BTC_LiveGraph.setAccessibleDescription("")
        self.htmlreader_BTCLiveGraph = QtWebEngineWidgets.QWebEngineView(BTC_LiveGraph)
        self.htmlreader_BTCLiveGraph.setGeometry(QtCore.QRect(10, 10, 1771, 981))
        self.htmlreader_BTCLiveGraph.setAccessibleDescription("")
        #récupération du chemin absolu du fichier
        mypath = os.path.dirname(__file__)
        self.htmlreader_BTCLiveGraph.setUrl(QtCore.QUrl(str("file:///"+ mypath + "/BTC_liveGraph.html")))
        self.htmlreader_BTCLiveGraph.setObjectName("htmlreader_BTCLiveGraph")

        self.retranslateUi(BTC_LiveGraph)
        QtCore.QMetaObject.connectSlotsByName(BTC_LiveGraph)

    def retranslateUi(self, BTC_LiveGraph):
        _translate = QtCore.QCoreApplication.translate
        BTC_LiveGraph.setWindowTitle(_translate("BTC_LiveGraph", "BTC Live Graph"))
        graphics.BTC_liveGraph(self.htmlreader_BTCLiveGraph)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BTC_LiveGraph = QtWidgets.QDialog()
    ui = Ui_BTC_LiveGraph()
    ui.setupUi(BTC_LiveGraph)
    BTC_LiveGraph.show()
    sys.exit(app.exec_())


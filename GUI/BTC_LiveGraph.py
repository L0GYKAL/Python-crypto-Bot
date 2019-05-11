from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
from PyQt5.Qt import QApplication, QMainWindow
from PyQt5.QtCore import QThread, QRect, QUrl, QCoreApplication, QMetaObject, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView


class updator(QtCore.QThread):
    def __init__(self, window):
        QtCore.QThread.__init__(self)



    def run(self):
        while True:
            self.sleep(2000 * 2 / 1000)
            self.window.htmlreader_BTCLiveGraph.reload()


class Ui_BTC_LiveGraph(object):
    def setupUi(self, widget):
        self.mypath = os.path.dirname(__file__)
        widget.setObjectName("BTC_LiveGraph")
        widget.resize(1600, 900)
        widget.setAccessibleDescription("")
        self.htmlreader_BTCLiveGraph = QWebEngineView(widget)
        self.htmlreader_BTCLiveGraph.setGeometry(QRect(10, 10, 1500, 800))
        self.htmlreader_BTCLiveGraph.setAccessibleDescription("")
        self.htmlreader_BTCLiveGraph.setObjectName("htmlreader_BTCLiveGraph")

        self.retranslateUi(widget)
        QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QCoreApplication.translate
        widget.setWindowTitle(_translate("BTC_LiveGraph", "BTC Live Graph"))


class MainWindow(Ui_BTC_LiveGraph, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # You can do this here, just keep the Ui class for UI stuff
        self.mypath = os.path.dirname(__file__)
        self.htmlreader_BTCLiveGraph.setUrl(QUrl(self.mypath + 'BTC_liveGraph.html'))

        self._updator = QTimer(self)
        self._updator.setSingleShot(False)
        self._updator.timeout.connect(self.reload)
        # Reload every 4 seconds
        self._updator.start(4000)

    def reload(self):
        self.htmlreader_BTCLiveGraph.reload()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    BTC_LiveGraph = MainWindow()
    BTC_LiveGraph.show()

    sys.exit(app.exec_())

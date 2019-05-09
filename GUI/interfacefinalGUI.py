from PyQt5 import QtCore, QtGui, QtWidgets
from TutorialGUI import Ui_Dialogue
from accountGUI import Ui_Account
from newsGUI import Ui_News
from watchlistGUI import Ui_Watchlist
from orders import Ui_Orders

class Ui_Dialog(object):

    def openOrders(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Orders()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def openWatchlist(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Watchlist()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def openNews(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_News()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAccount(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Account()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialogue()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(703, 395)
        Dialog.setStyleSheet("image: url(:/newPrefix/Interface 2.jpg);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.openAccount)
        
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.openWatchlist)
        
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 180, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.openNews)
        
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 230, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(self.openOrders)

        
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 370, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 10, 141, 21))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_6.clicked.connect(self.openWindow)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Account"))
        self.pushButton_2.setText(_translate("Dialog", "Watchlist"))
        self.pushButton_3.setText(_translate("Dialog", "News"))
        self.pushButton_4.setText(_translate("Dialog", "Orders"))
        self.pushButton_5.setText(_translate("Dialog", "Settings"))
        self.pushButton_6.setText(_translate("Dialog", "How to use SIR ?"))

import image


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



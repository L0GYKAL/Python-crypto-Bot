
from PyQt5 import QtCore, QtGui, QtWidgets
from graphs import Ui_Graphs


class Ui_Watchlist(object):

    def opengraphs(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Graphs()
        self.ui.setupUi(self.window)
        self.window.show()


    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(930, 607)
        Dialog.setStyleSheet("background-color: rgb(189, 255, 231);\n"
"")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(265, 31, 271, 521))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(180, 30, 31, 31))
        self.toolButton.setStyleSheet("image: url(:/newPrefix/search-icon-png-1.png);\n"
"background-color: rgb(199, 255, 243);")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 570, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.opengraphs)
        
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(570, 30, 256, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(570, 150, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(570, 180, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(570, 120, 81, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(670, 120, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(670, 150, 113, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(670, 180, 113, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(790, 120, 47, 13))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(790, 150, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(790, 180, 47, 13))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "crypto1"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.pushButton_2.setText(_translate("Dialog", "Graph"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-3fda06ab-7fff-90a4-dabb-d275b2e36340\"></a><span style=\" font-family:\'Arial\'; font-size:9pt; color:#000000; background-color:transparent;\">M</span><span style=\" font-family:\'Arial\'; font-size:9pt; color:#000000; background-color:transparent;\">oyenne des pourcentages des 100 plus grosses crypto:</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "depuis 24 heures"))
        self.label_4.setText(_translate("Dialog", "depuis 1 heure"))
        self.label_3.setText(_translate("Dialog", "depuis 7 jours"))
        self.label.setText(_translate("Dialog", "%"))
        self.label_5.setText(_translate("Dialog", "%"))
        self.label_6.setText(_translate("Dialog", "%"))

import image

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Watchlist()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


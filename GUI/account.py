# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Account(object):
    def setupUi(self, Account):
        Account.setObjectName("Account")
        Account.resize(400, 300)
        self.textBrowser = QtWidgets.QTextBrowser(Account)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 401, 51))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Account)
        QtCore.QMetaObject.connectSlotsByName(Account)

    def retranslateUi(self, Account):
        _translate = QtCore.QCoreApplication.translate
        Account.setWindowTitle(_translate("Account", "Dialog"))
        self.textBrowser.setHtml(_translate("Account", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000;\">Welcome to your account!</span></p></body></html>"))

import image

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account = QtWidgets.QDialog()
    ui = Ui_Account()
    ui.setupUi(Account)
    Account.show()
    sys.exit(app.exec_())


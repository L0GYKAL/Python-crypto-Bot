# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstboot.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialogue(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(819, 309)
        Dialog.setStyleSheet("image: url(:/newPrefix/firstboot.jpg);")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 131, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 200, 141, 161))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(670, 20, 141, 131))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><a name=\"tw-target-text\"></a><span style=\" font-family:\'inherit\'; font-size:6pt; color:#212121;\">T</span><span style=\" font-family:\'inherit\'; font-size:6pt; color:#212121;\">he </span><span style=\" font-family:\'inherit\'; font-size:6pt; font-weight:600; text-decoration: underline; color:#212121;\">account</span><span style=\" font-family:\'inherit\'; font-size:6pt; color:#212121;\"> allows you to see your personal data</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:transparent;\"><a name=\"tw-target-text-container\"></a><span style=\" font-family:\'inherit\'; font-size:6pt; color:#212121;\">T</span><span style=\" font-family:\'inherit\'; font-size:6pt; color:#212121;\">he </span><span style=\" font-family:\'inherit\'; font-size:6pt; font-weight:600; text-decoration: underline; color:#212121;\">news</span><span style=\" font-family:\'inherit\'; font-size:6pt; color:#212121;\"> page allows you to keep up to date with the latest news</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; font-family:\'inherit\'; font-size:6pt; color:#212121; background-color:transparent;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\"><br /></span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,sans-serif\'; font-size:6pt; color:#545454; background-color:#ffffff;\">A </span><span style=\" font-family:\'arial,sans-serif\'; font-size:6pt; font-weight:600; text-decoration: underline; color:#6a6a6a; background-color:#ffffff;\">watchlist</span><span style=\" font-family:\'arial,sans-serif\'; font-size:6pt; color:#545454; background-color:#ffffff;\"> is list of securities being monitored for potential </span><span style=\" font-family:\'arial,sans-serif\'; font-size:6pt; font-weight:600; color:#6a6a6a; background-color:#ffffff;\">trading</span><span style=\" font-family:\'arial,sans-serif\'; font-size:6pt; color:#545454; background-color:#ffffff;\"> or investing opportunities.</span></p></body></html>"))

import image

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialogue()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


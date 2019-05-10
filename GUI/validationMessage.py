# -*- coding: utf-8 -*-
#final version
# Form implementation generated from reading ui file 'F:\validationMessage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Responsemessage(object):
    def setupUi(self, Responsemessage):
        Responsemessage.setObjectName("Responsemessage")
        Responsemessage.resize(469, 198)
        Responsemessage.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        Responsemessage.setFocusPolicy(QtCore.Qt.StrongFocus)
        Responsemessage.setStyleSheet("background-color: rgb(170, 255, 255);")
        Responsemessage.setModal(True)
        self.okButton = QtWidgets.QDialogButtonBox(Responsemessage)
        self.okButton.setGeometry(QtCore.QRect(200, 160, 81, 32))
        self.okButton.setOrientation(QtCore.Qt.Horizontal)
        self.okButton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.okButton.setCenterButtons(True)
        self.okButton.setObjectName("okButton")
        self.message = QtWidgets.QLabel(Responsemessage)
        self.message.setGeometry(QtCore.QRect(10, 10, 459, 101))
        self.message.setAccessibleDescription("")
        self.message.setObjectName("message")
        self.image = QtWidgets.QLabel(Responsemessage)
        self.image.setGeometry(QtCore.QRect(220, 90, 61, 61))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.message.raise_()
        self.okButton.raise_()
        self.image.raise_()

        self.retranslateUi(Responsemessage)
        self.okButton.accepted.connect(Responsemessage.accept)
        self.okButton.rejected.connect(Responsemessage.reject)
        QtCore.QMetaObject.connectSlotsByName(Responsemessage)

    def retranslateUi(self, Responsemessage):
        _translate = QtCore.QCoreApplication.translate
        Responsemessage.setWindowTitle(_translate("Responsemessage", "Response message"))
        self.message.setText(_translate("Responsemessage", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ff0000;\">Congratulation!</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ff0000;\">Your action was effected</span></p></body></html>"))
        mypath = os.path.dirname(__file__)
        self.image.setText(_translate("Responsemessage", "<html><head/><body><p><img src=\"" + mypath + "/images/validation.png\" width=\"50\" height=\"50\"/></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Responsemessage = QtWidgets.QDialog()
    ui = Ui_Responsemessage()
    ui.setupUi(Responsemessage)
    Responsemessage.show()
    sys.exit(app.exec_())


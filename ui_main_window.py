# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 283)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.myButton = QtWidgets.QPushButton(self.centralwidget)
        self.myButton.setGeometry(QtCore.QRect(240, 190, 75, 23))
        self.myButton.setObjectName("myButton")
        self._infoLabel = QtWidgets.QLabel(self.centralwidget)
        self._infoLabel.setGeometry(QtCore.QRect(250, 90, 54, 12))
        self._infoLabel.setObjectName("_infoLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.myButton.setText(_translate("MainWindow", "PushButton"))
        self._infoLabel.setText(_translate("MainWindow", "TextLabel"))


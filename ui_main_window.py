# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(298, 228)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self._webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self._webView.setUrl(QtCore.QUrl("about:blank"))
        self._webView.setObjectName("_webView")
        self.verticalLayout.addWidget(self._webView)
        self._infoLabel = QtWidgets.QLabel(self.centralwidget)
        self._infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self._infoLabel.setObjectName("_infoLabel")
        self.verticalLayout.addWidget(self._infoLabel)
        self.myButton = QtWidgets.QPushButton(self.centralwidget)
        self.myButton.setObjectName("myButton")
        self.verticalLayout.addWidget(self.myButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._infoLabel.setText(_translate("MainWindow", "TextLabel"))
        self.myButton.setText(_translate("MainWindow", "PushButton"))

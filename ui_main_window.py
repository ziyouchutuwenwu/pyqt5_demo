# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._main_layout = QtWidgets.QHBoxLayout()
        self._main_layout.setObjectName("_main_layout")
        self._left_layout = QtWidgets.QVBoxLayout()
        self._left_layout.setObjectName("_left_layout")
        self._webview = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self._webview.setObjectName("_webview")
        self._left_layout.addWidget(self._webview)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._left_layout.addItem(spacerItem)
        self._main_layout.addLayout(self._left_layout)
        self._right_layout = QtWidgets.QVBoxLayout()
        self._right_layout.setObjectName("_right_layout")
        self._info_label = QtWidgets.QLabel(self.centralwidget)
        self._info_label.setAlignment(QtCore.Qt.AlignCenter)
        self._info_label.setObjectName("_info_label")
        self._right_layout.addWidget(self._info_label)
        self._demo_button = QtWidgets.QPushButton(self.centralwidget)
        self._demo_button.setObjectName("_demo_button")
        self._right_layout.addWidget(self._demo_button)
        self._load_webview_button = QtWidgets.QPushButton(self.centralwidget)
        self._load_webview_button.setObjectName("_load_webview_button")
        self._right_layout.addWidget(self._load_webview_button)
        self._main_layout.addLayout(self._right_layout)
        self.horizontalLayout.addLayout(self._main_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._info_label.setText(_translate("MainWindow", "TextLabel"))
        self._demo_button.setText(_translate("MainWindow", "demo_button"))
        self._load_webview_button.setText(_translate("MainWindow", "load webview"))
from PyQt5 import QtWebEngineWidgets

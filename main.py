#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt5 import QtWidgets
from custom_ui.main_window import MainWindow
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
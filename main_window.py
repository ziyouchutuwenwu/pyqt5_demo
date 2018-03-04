from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main_window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.myButton.clicked.connect(self.myButtonClicked)

    def myButtonClicked(self, remark):
        self._infoLabel.setText("Hello World")
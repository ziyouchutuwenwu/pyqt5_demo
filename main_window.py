from PyQt5 import QtWidgets
from ui_main_window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.myButton.clicked.connect(self.my_button_clicked)

    def my_button_clicked(self):
        self._infoLabel.setText("Hello World")
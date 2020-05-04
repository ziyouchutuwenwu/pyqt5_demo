from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from demo_thread import DemoThread
from ui_main_window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self._demo_thread = DemoThread()
        self._demo_button.clicked.connect(self.on_demo_button_clicked)

        self._load_webview_button.clicked.connect(self.on_webview_button_clicked)

    def on_demo_button_clicked(self):
        self._demo_thread = DemoThread()
        self._demo_thread.set_callback(self.on_demo_thread_started, self.on_demo_thread_stopped)
        self._demo_thread.start()

    def on_webview_button_clicked(self):
        self._webview.load(QUrl("http://www.baidu.com"))

    def on_demo_thread_started(self):
        self._info_label.setText("on demo thread started")

    def on_demo_thread_stopped(self, result_info):
        self._info_label.setText("on demo thread stopped, info is " + result_info)
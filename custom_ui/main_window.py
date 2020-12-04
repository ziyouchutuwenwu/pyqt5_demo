import os

import PyQt5.QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl, PYQT_VERSION_STR

from custom_ui import webview_intercepter
from demo_thread import DemoThread
from ui.ui_main_window import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self.setWindowIcon(PyQt5.QtGui.QIcon(project_path + '/res/ico.ico'))

        self._demo_thread = DemoThread()
        self._demo_button.clicked.connect(self.on_demo_button_clicked)

        # 使用self引用，防止gc
        self._intercepter = webview_intercepter.WebEngineUrlRequestInterceptor()
        self._webview.page().profile().setUrlRequestInterceptor(self._intercepter)

        self._load_webview_button.clicked.connect(self.on_webview_button_clicked)

    def on_webview_button_clicked(self):
        self._webview.load(QUrl("http://www.baidu.com"))

    def on_demo_button_clicked(self):
        self._demo_thread = DemoThread()
        self._demo_thread.set_callback(self.on_demo_thread_started, self.on_demo_thread_stopped)
        self._demo_thread.start()

    def on_demo_thread_started(self):
        self._info_label.setText("on demo thread started")

    def on_demo_thread_stopped(self, result_info):
        version_info = PYQT_VERSION_STR
        info = "on demo thread stopped, info is %s, pyqt %s" % (result_info, version_info)
        self._info_label.setText(info)

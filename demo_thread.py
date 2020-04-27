#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal
import time

class DemoThread(QThread):
    _start_signal = pyqtSignal()
    _finish_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

    def set_callback(self, on_started, on_finished):
        if on_started != None:
            self._start_signal.connect(on_started)
        if on_finished != None:
            self._finish_signal.connect(on_finished)

    def run(self):
        self._start_signal.emit()

        time.sleep(5)

        self._finish_signal.emit("ok")
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import PyQt5.QtWebEngineCore


class WebEngineUrlRequestInterceptor(PyQt5.QtWebEngineCore.QWebEngineUrlRequestInterceptor):
    def __init__(self, parent=None):
        super().__init__(parent)

    def interceptRequest(self, info):
        print(info.requestUrl(), info.requestMethod(), info.resourceType(), info.firstPartyUrl())
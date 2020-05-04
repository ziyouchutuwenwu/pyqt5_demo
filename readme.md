- 如果在windows下，打包提示找不到sip，那么在main.py里面添加
```
from PyQt5 import sip
```

- 打包
```
pyinstaller -F -w ./main.py
```

- 关于QWebEngineView
```text
qtDesigner里面没有QWebEngineView，需要使用QWidget，然后右键，提升为QWebEngineView
linux下不能输入中文输入法，windows下没有问题
```

- 测试代码
```python
self._webview.load(QUrl("http://www.baidu.com"))
```
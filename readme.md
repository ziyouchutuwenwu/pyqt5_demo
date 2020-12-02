# 说明

## windows 下

如果在 windows 下，打包提示找不到 sip，那么在 main.py 里面添加

```python
from PyQt5 import sip
```

打包

```sh
pyinstaller -F -w ./main.py
```

## 关于 QWebEngineView

```text
qtDesigner里面没有QWebEngineView，需要使用QWidget，然后右键，提升为QWebEngineView
```

### 测试代码

```python
self._webview.load(QUrl("http://www.baidu.com"))
```

### linux 下输入中文输入法

缺的是 fcitx 的库

```sh
pip show PyQt5
找到带有`site-packages`的路径
```

复制 `libfcitxplatforminputcontextplugin.so` 到 pyqt 的目录，注意 pyenv 安装好的 python 版本号

```sh
cp /usr/lib/x86_64-linux-gnu/qt5/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so ~/.pyenv/versions/3.9.0/lib/python3.9/site-packages/PyQt5/Qt/plugins/platforminputcontexts/
```

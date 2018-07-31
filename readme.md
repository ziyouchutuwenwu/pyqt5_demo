- 如果在windows下，打包提示找不到sip，那么在main.py里面添加
```
from PyQt5 import sip
```

- 打包
```
pyinstaller -F -w ./main.py
```

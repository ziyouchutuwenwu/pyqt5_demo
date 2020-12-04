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

## designer上修改自定义控件

```text
designer里面ui使用自定义的类，在控件上右击，选择提升
需要填写新的类名字
头文件填写这个类所在的文件名
```
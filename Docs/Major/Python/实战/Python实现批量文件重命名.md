# Python实现批量文件重命名

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Python实现批量文件重命名](#python实现批量文件重命名)
  - [使用说明](#使用说明)
  - [脚本代码](#脚本代码)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 使用说明

将下面的脚本写入命名为rename.py的文件并，放到要批量修改文件名的文件夹下
使用如下命令

```py3
python3 rename.py [测试名字]
# 或直接输入
# python3 rename.py
```
    

## 脚本代码

```python
# rename.py
# 导入os库
import os
import sys

# 文件存放的路径
path = r"./"
# 将命令中第二个参数作为输入，多个参数空格隔开
if len(sys.argv) >= 2:
    base = sys.argv[1]
else:
    # 控制台输入
    base = input('Please input base name: ')  

print("You inputted ", base)

# 遍历更改文件名
num = 1

for old in os.listdir(path):
    if old == 'rename.py':
        print('Skip script!')
    else:
        new = base + '_' + str(num) + os.path.splitext(old)[-1]
        os.rename(os.path.join(path, old),
                  os.path.join(path, new))
        print('Rename', old, 'to', new)
    num = num + 1

print('Succeed!!!')

# 获取文件名后缀 os.path.splitext(name)[-1]
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️


> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Python实现批量文件重命名.html](http://www.skyline.show/Python实现批量文件重命名.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

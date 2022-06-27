# Shell 中 grep 的使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 中 grep 的使用](#shell-中-grep-的使用)
  - [使用](#使用)
    - [基础使用](#基础使用)
    - [正则](#正则)
    - [递归查找子目录](#递归查找子目录)
    - [忽略大小写](#忽略大小写)
    - [匹配次数](#匹配次数)
    - [静默查找](#静默查找)
  - [选项](#选项)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 使用

### 基础使用

grep 是一个字符搜索命令，使用的基础语法为

```sh
grep [options] pattern [files]
```

### 正则

^ 匹配的字符在行首
$ 匹配的字符在行尾

```sh
grep ^grep Docs/Major/Shell/Commands/Shell中grep的使用.md
grep shell$ Docs/Major/Shell/Commands/Shell中grep的使用.md
```

可通过 -e 来开启正则匹配模式，-e 参数在使用多次时很有用

```sh
# 搜索包含shell 和grep的行
grep -e shell -e grep Docs/Major/Shell/Commands/Shell中grep的使用.md
```

### 递归查找子目录

-r 选项
在项目根目录尝试输入如下命令

```sh
grep -r shell -e grep Docs/Major/Shell/
```

### 忽略大小写

-i 选项
在项目根目录尝试输入如下命令

```sh
grep -i shell Docs/Major/Shell/Commands/Shell中grep的使用.md
```

### 匹配次数

-c 选项，获取匹配次数
在项目根目录尝试输入如下命令

```sh
grep -c shell Docs/Major/Shell/Commands/Shell中grep的使用.md
# 6
```

### 静默查找

-q 选项
静默查找，不做打印输出，只有运行结果状态。
常用语条件判定等情况
不指定时即为关闭静默。
关闭静默

```sh
STR='GNU/Linux is an operating system'
SUB='Linux'

if grep "$SUB" <<< "$STR"; then
  echo "It's there"
fi
# GNU/Linux is an operating system
# It's there
```

开启静默

```sh
STR='GNU/Linux is an operating system'
SUB='Linux'

if grep -q "$SUB" <<< "$STR"; then
  echo "It's there"
fi
# It's there
```

## 选项

| 选项 | 描述                                               |
| ---- | -------------------------------------------------- |
| q    | 静默查找，不做输出，常用语条件判定等情况           |
| r    | 递归查找子目录文件                                 |
| n    | 列出行标                                           |
| i    | 忽略大小写                                         |
| e    | 搜索时启用正则匹配，可使用多次                     |
| w    | 精确指定单词，需要为单词，英文单词前后有字母不匹配 |
| l    | 只输出匹配的文件名                                 |
| c    | 输出匹配字符次数                                   |
| o    | 只输出的匹配字符，多个匹配换行输出                 |
| v    | 反转输出，输出不匹配该字符的行                     |

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Shell 中 grep 的使用.html](http://www.skyline.show/Shell中grep的使用.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

# Shell 中 xargs 使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 中 xargs 使用](#shell-中-xargs-使用)
  - [概述](#概述)
  - [基础使用示例](#基础使用示例)
    - [echo](#echo)
    - [wc](#wc)
    - [mkdir](#mkdir)
  - [参数](#参数)
    - [-L](#-l)
    - [-n](#-n)
    - [-d](#-d)
    - [-t](#-t)
    - [-p](#-p)
  - [BMW WARNING](#bmw-warning)
    - [NOTICE](#notice)
    - [Material](#Material)
    - [Warrant](#Warrant)

<!-- /code_chunk_output -->

## 概述

Shell 中只有部分命令支持标准输入，例如 wc、grep、xargs 等，通过管道 | 很容易将前置命令的标准输出传递给这些命令。但是部分命令不支持标准输入，不能通过管道 | 直接操作，例如 echo rm mkdir 等。这需要 xargs 为那些不支持标准输入的命令提供管道操作。
通过 xargs 将标准输入转换成参数来完成后续命令。如果转换成的参数有多个（通过标准输入空符分割），后续命令重复执行。

> The xargs command in UNIX is a command line utility for building an execution pipeline from standard input. Whilst tools like grep can accept standard input as a parameter, many other tools cannot. Using xargs allows tools like echo and rm and mkdir to accept standard input as arguments.

## 基础使用示例

### echo

```
# input
echo skyline | echo
#output

```

```
# input
echo skyline | xargs echo
# output
skyline
```

在未指定后续操作的情况下，xargs 默认执行 echo 操作

```
# input
echo skyline | xargs
# output
skyline
```

通常 xargs 与管道符一起使用，但其也可以从其他方式指定标准输入。
通过键盘指定标准输入
![Shell中xargs使用QQ20210922-174329-HD](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E4%B8%ADxargs%E4%BD%BF%E7%94%A8QQ20210922-174329-HD.gif)

```
# input
xargs # 输入 xargs 输入 ⏎
skyline # 输入 skyline 输入 ⏎ 输入 ^ + D
# output
skyline # 输出
```

与如下命令等价

```
# input
xargs echo # 输入 xargs echo 输入 ⏎
skyline # 输入 skyline 输入 ⏎ 输入 ^ + D
# output
skyline # 输出
```

### wc

```
# input
find . -name "*.md"
# output
./Major/Mobile/Flutter/Flutter基础使用汇总.md
./Major/Mobile/Flutter/Flutter基础控件使用.md
./Major/Shell/Shell中xargs使用.md
./Major/Shell/Shell中的符号.md
./Major/Shell/Shell常见操作汇总.md
./README.md
./Tools/DEVs/VSCode/Extensions/PicGo.md
./Tools/OS/ipadOS使用.md
```

```
# input
find . -name "*.md" | wc -l
# output
       8
```

```
# input
find . -name "*.md" | xargs wc -l
# output
      84 ./Major/Mobile/Flutter/Flutter基础使用汇总.md
     109 ./Major/Mobile/Flutter/Flutter基础控件使用.md
       0 ./Major/Shell/Shell中xargs使用.md
     131 ./Major/Shell/Shell中的符号.md
      13 ./Major/Shell/Shell常见操作汇总.md
       4 ./README.md
      44 ./Tools/DEVs/VSCode/Extensions/PicGo.md
       5 ./Tools/OS/ipadOS使用.md
     390 total
```

### mkdir

```
# input
echo 1 2 3 | xargs mkdir
ls
# output
1 2 3
```

## 参数

### -0

用 null 作为分隔符，与 find 中 -print0 意义一致，且需一起使用

### -I

将标准输入以指定字符缓存，方便后续使用。类似于正则中()的作用。

将当前目录下文件统一加后缀

```
# input
ls
# output
one           two         three
# input
find . -type f -name '*' -print0 | xargs -0 -I{} mv {} {}.txt && ls


one.txt           two.txt         three.txt
# input
ls | xargs -I_ mv _ _.bak && ls
# output
one.txt.bak   three.txt.bak two.txt.bak
```

### -L

number 类型，解决多行输入问题，将标准输入按照该数字指定的行数进行分隔，假设为 -L 2，则每次执行取两行作为标准输入，
执行多次，直到多行执行结束。
多数命令不支持多行参数，通常直接指定 -L1

```
# input
echo -e "She*\nFlu*" | xargs -L 1 find  . -name
# output
./Major/Shell
./Major/Shell/Shell中xargs使用.md
./Major/Shell/Shell中的符号.md
./Major/Shell/Shell常见操作汇总.md
./Major/Mobile/Flutter
./Major/Mobile/Flutter/Flutter基础使用汇总.md
./Major/Mobile/Flutter/Flutter基础控件使用.md
```

![Shell中xargs使用QQ20210923-105617-HD](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E4%B8%ADxargs%E4%BD%BF%E7%94%A8QQ20210923-105617-HD.gif)

### -n

number 类型，解决同行多项参数问题。与-L 参数互斥，同时指定选后指定的选项。

```
# input
echo -e "She* Flu*" | xargs -n 1 find . -name
# output
./Major/Shell
./Major/Shell/Shell中xargs使用.md
./Major/Shell/Shell中的符号.md
./Major/Shell/Shell常见操作汇总.md
./Major/Mobile/Flutter
./Major/Mobile/Flutter/Flutter基础使用汇总.md
./Major/Mobile/Flutter/Flutter基础控件使用.md
```

### -d

指定分隔符
这在处理有空格等特殊符号的输入中很有用

### -t

打印执行日志

```
# input
echo skyline | xargs -t echo
# output
echo skyline
skyline
```

### -p

打印实际操作并让用户选择是否执行

```
# input
ls
# output
one   three two
# input
echo 'one two three' | xargs -p rm -rf
# input & output
rm -rf one two three?...y
# input
ls
# output

```

上述确认操作中除了输入 y，其他任何输入都不会进行删除操作

![Shell中xargs使用QQ20210923-170939-HD](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E4%B8%ADxargs%E4%BD%BF%E7%94%A8QQ20210923-170939-HD.gif)

## BMW WARNING

### Bulletin

I am a bucolic migrant worker but I never walk backwards.

### Material

> [Linux and Unix xargs command tutorial with examples](https://shapeshed.com/unix-xargs/) > [8 Practical Examples of Linux Xargs Command for Beginners](https://www.howtoforge.com/tutorial/linux-xargs-command/)

### Warrant

> 本文作者： Skyline(lty)
> 版权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

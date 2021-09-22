# Shell 中 xargs 使用

## 概述

Shell 中只有部分命令支持标准输入，例如 wc、grep、xargs 等，通过管道 | 很容易将前置命令的标准输出传递给这些命令。但是部分命令不支持标准输入，不能通过管道 | 直接操作，例如 echo rm mkdir 等。这需要 xargs 为那些不支持标准输入的命令提供管道操作。
通过 xargs 将标准输入转换成参数来完成后续命令，如果转换成的参数有多个（通过标准输入空符分割），后续命令重复执行。

> The xargs command in UNIX is a command line utility for building an execution pipeline from standard input. Whilst tools like grep can accept standard input as a parameter, many other tools cannot. Using xargs allows tools like echo and rm and mkdir to accept standard input as arguments.

## 基础使用示例

### echo

```
echo skyline | echo
```

```
echo skyline | xargs echo
skyline
```

在指定后续操作的情况下，xargs 默认执行 echo 操作

```
echo skyline | xargs
skyline
```

通过键盘指定标准输入
![Shell中xargs使用QQ20210922-174329-HD](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E4%B8%ADxargs%E4%BD%BF%E7%94%A8QQ20210922-174329-HD.gif)

```
xargs # 输入 xargs 输入 ⏎
skyline # 输入 skyline 输入 ⏎ 输入 ^ + D
skyline # 输出
```

与如下命令等价

```
xargs echo # 输入 xargs echo 输入 ⏎
skyline # 输入 skyline 输入 ⏎ 输入 ^ + D
skyline # 输出
```

### wc

```
find . -name "*.md"
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
find . -name "*.md" | wc -l
       8
```

```
find . -name "*.md" | xargs wc -l
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
echo 1 2 3 | xargs mkdir
ls
1 2 3
```

## 参数

### -d

## BMW WARNING

### NOTICE

All bucolic migrant workers must fight against capitalism together

### 参考资料

> [Linux and Unix xargs command tutorial with examples](https://shapeshed.com/unix-xargs/)

### 许可协议

> 本文作者： Skyline(lty)
> 版权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 许可协议。 转载请注明出处！

# sed 的使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [sed 的使用](#sed-的使用)
  - [简介](#简介)
  - [选项参数](#选项参数)
    - [-n](#-n)
    - [-e](#-e)
    - [-i](#-i)
  - [命令参数](#命令参数)
    - [i/a](#ia)
    - [d](#d)
    - [p](#p)
    - [s/c](#sc)
  - [常见用法](#常见用法)
    - [文末插入](#文末插入)
    - [替换字符](#替换字符)
    - [行数](#行数)
    - [字符行号](#字符行号)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 简介

流编辑器，sed 用于读取指定文件或标准输入。
如果没有文件被指定，可由命令列表来指定输入，进行相应修改后写入到标准输出。

## 选项参数

### -n

默认情况下，在所有的标准输出都会被打印到屏幕上。 -n 选项用于指定输出内容。

```sh
# 输出100到200行
sed -n '100,200p' skyline.txt
# 输出文件行数
sed -n '$=' skyline.txt
```

多个地址用逗号隔开

### -e

-e 是编辑命令，用于执行多个编辑任务。
`sed -e '1,10d' -e 's/skyline/lty/g' skyline.txt`
skyline.txt 将依次执行之后的命令，删除一到十行，并且全局替换'skyline'为'lty'

### -i

-i 指定备份，指定空字符串或不指定内容直接修改源文件(linux 下可以不指定，mac 下需指定空字符)。
没有指定该选项将直接标准输出，不进行任何实质修改

```sh
# 指定skyline.txt.bak的备份
sed -i '.bak' 's/skyline/lty/g' ./skyline.txt
```

skyline.txt 源文件内容将会备份到 skyline.txt.bak 文件中

```sh
sed -i '' 's/skyline/lty/g' ./skyline.txt
```

将不备份直接修改源文件

```sh
sed -i 's/skyline/lty/g' ./skyline.txt
```

linux 可以直接执行修改源文件，mac 下需要如上指定空字符方可
在 Mac 上，sed 命令直接操作文件的时候，必须指定备份的格式，而在 linux 上，却并没有这个要求

## 命令参数

### i/a

i 与 a 都是插入参数，后面可以接字串，用 a 插入的字串会在行的下一行行首出现，用 i 插入的字串会在当前行的行首，出现单独一行需要在字符后加上\n

```sh
# Mac/Linux
sed -i '' '9i\
6666666' skyline.txt
# Linux
sed -i '' '9a\6666666' skyline.txt
```

- 注意 mac 下\后需要换行

### d

删除，之后不接内容
`sed -i '' '1,2d' skyline.txt`

### p

标准输出内容

`sed -n '3p' skyline`

### s/c

替换部分内容，s 来替换，通常这个 s 搭配正则表达式。 c 替换通常指定行，之后用这些字串取代 n1,n2 之间的行内容

```sh
# 替换1到5行的内容为lalala
sed -i '' '1,5c\
lalala' skyline.txt
# 替换
sed -i '' 's/666/222/g' skyline.txt
```

## 常见用法

### 文末插入

注意 mac 下\后需要换行

```sh
sed -i '' '$a\skyline' skyline.txt
```

### 替换字符

替换第 n 个匹配的字符

```sh
echo sksksksksksk | sed 's/sk/SK/3'
```

### 行数

输出文件行数

```sh
sed -n '$=' skyline.txt
```

### 字符行号

输出文件第 n 个匹配字符所在行号

```sh
sed -n /skyline/= skyline.txt | sed -n 2p #匹配第二个skyline，打印其所在行号
```

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

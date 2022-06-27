# sed 的使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [sed 的使用](#sed-的使用)
  - [sed 简介](#sed-简介)
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
    - [获取行数](#获取行数)
    - [获取字符行号](#获取字符行号)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## sed 简介

sed 是一种流文本编辑器，用于读取指定文件或标准输入。
如果没有文件被指定，可由命令列表来指定输入，进行相应修改后写入到标准输出。
本文后续内容以[skyline.txt](https://github.com/skylinety/Blog/blob/main/Demos/Major/Shell/skyline.txt)示例，可在根目录执行下述脚本。
其文本内容为

```js
test
skyline
test2
skyline test
```

## 选项参数

### -n

默认情况下，在所有的标准输出都会被打印到屏幕上。 -n 选项用于指定输出内容。

```sh
# 输出1到3行
sed -n '1,3p' Demos/Major/Shell/skyline.txt
# test
# skyline
# test2

# 输出文件总行数
sed -n '$=' Demos/Major/Shell/skyline.txt
# 4
# 获取文件行数，也可使用cat Demos/Major/Shell/skyline.txt  | wc -l
```

连续的行数用逗号隔开。

### -e

-e 是编辑命令，用于执行多个编辑任务。

```sh
sed -e '1,2d' -e 's/skyline/lty/g' Demos/Major/Shell/skyline.txt
# test2
# lty test
```

skyline.txt 将依次执行之后的命令，删除 1 到 2 行，并且全局替换'skyline'为'lty'
上述操作不会影响 skyline.txt 源文件，只做标准输出，可使用>将结果重定向到另一个文件。

### -i

-i 指定备份

可指定字符后缀为备份文件

```sh
# 指定会在skyline.txt同级目录生产skyline.txt.bak备份，skyline.txt内容将会变更
# skyline.txt 源文件内容将会备份到 skyline.txt.bak 文件中
sed -i '.bak' 's/skyline/lty/g' Demos/Major/Shell/skyline.txt
cat Demos/Major/Shell/skyline.txt.bak
# test
# skyline
# test2
# skyline test
cat Demos/Major/Shell/skyline.txt
# test
# lty
# test2
# lty test
```

指定空字符串或不指定内容直接修改源文件(linux 下可以不指定，mac 下需指定空字符)

```sh
sed -i '' 's/skyline/lty/g' Demos/Major/Shell/skyline.txt
# 将不备份直接修改skyline.txt源文件
cat Demos/Major/Shell/skyline.txt
# test
# lty
# test2
# lty test
```

```sh
sed -i 's/skyline/lty/g' Demos/Major/Shell/skyline.txt
# mac下不可执行，linux 可以直接执行修改源文件，mac 下需要如上指定空字符方可
# 在 Mac 上，sed 命令直接操作文件的时候，必须指定备份的格式，而在 linux 上，却并没有这个要求
```

## 命令参数

### i/a

i 与 a 都是插入参数，后面可以接字串，用 a 插入的字串会在行的下一行行首出现，用 i 插入的字串会在当前行的行首。
插入的字符用\隔开，注意，在 mac 下\后需要换行

```sh
# Mac/Linux
sed -i '' '3i\
test3' Demos/Major/Shell/skyline.txt
cat Demos/Major/Shell/skyline.txt
# test
# skyline
# test3test2
# skyline test
sed -i '' '3a\
test3' Demos/Major/Shell/skyline.txt
# test
# skyline
# test2
# test3skyline test

# Linux
sed -i '' '3a\test3' Demos/Major/Shell/skyline.txt
```

### d

- 简单使用

删除命令，之后不接内容。

```sh
sed -i '' '1,3d' Demos/Major/Shell/skyline.txt
# 删除文件的1，2，3行
sed -i '' '1d;3d' Demos/Major/Shell/skyline.txt
# 删除文件的1行3行
sed -i '' '$d' Demos/Major/Shell/skyline.txt
# 删除文件的尾行
sed -i '' '1,3d!' Demos/Major/Shell/skyline.txt
# 删除其他行，只保留1-3行
```

- 使用正则

删除空行

```sh
# 删除文件中的空行
sed -i '' '/^$/d' Demos/Major/Shell/skyline.txt
# 开始与结束衔接，表示该行没有任何内容，即空行
```

删除有匹配成功对应的行

```sh
sed -i '' '/skyline/d' Demos/Major/Shell/skyline.txt
cat Demos/Major/Shell/skyline.txt
# test
# test2
```

删除有匹配成功对应的行

```sh
sed -i '' '/^skyline$/d' Demos/Major/Shell/skyline.txt
cat Demos/Major/Shell/skyline.txt
# test
# test2
# skyline test
```

删除特殊匹配的行

```sh
# 删除有空格的行
sed -i '' '/[[:space:]]/d' Demos/Major/Shell/skyline.txt
cat Demos/Major/Shell/skyline.txt
# test
# skyline
# test2

# 删除有数字的行
sed -i '' '/[[:digit:]]/d' Demos/Major/Shell/skyline.txt
cat Demos/Major/Shell/skyline.txt
# test
# skyline
# skyline test

# 删除有小写字母的行
sed -i '' '/[[:lower:]]/d' Demos/Major/Shell/skyline.txt
cat Demos/Major/Shell/skyline.txt
#
```

### p

标准输出内容

```sh
# 输出1到3行
sed -n '1,3p' Demos/Major/Shell/skyline.txt
# test
# skyline
# test2
```

### s/c

使用 s/c 来替换部分内容。
这个 s 通常搭配正则表达式， c 通常替换指定行。

替换行

```sh
# 替换1到5行的内容为lalala
sed -i '' '1,5c\
lalala' Demos/Major/Shell/skyline.txt
cat Demos/Major/Shell/skyline.txt
# lalala
```

替换文本

```sh
sed -i '' 's/skyline/lty/g' Demos/Major/Shell/skyline.txt
# 将不备份直接修改skyline.txt源文件
cat Demos/Major/Shell/skyline.txt
# test
# lty
# test2
# lty test
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
# skskSKsksksk
```

### 获取行数

输出文件行数

```sh

# 输出文件总行数
sed -n '$=' Demos/Major/Shell/skyline.txt
# 4
# 获取文件行数，也可使用cat Demos/Major/Shell/skyline.txt  | wc -l
```

### 获取字符行号

输出文件第 n 个匹配字符所在行号

```sh
# 输出所有skyline的行号
sed -n /skyline/=  Demos/Major/Shell/skyline.txt
# 2
# 4

#输出第2个skyline所在行号
sed -n /skyline/= Demos/Major/Shell/skyline.txt | sed -n 2p
# 4
```

![Shell中sed的使用20220609113948](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E4%B8%ADsed%E7%9A%84%E4%BD%BF%E7%94%A820220609113948.png)

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

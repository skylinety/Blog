# Shell 中字符串相关操作

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 中字符串相关操作](#shell-中字符串相关操作)
  - [字符替换](#字符替换)
  - [字符包含判定](#字符包含判定)
    - [==](#)
    - [正则=~](#正则)
    - [grep](#grep)
  - [将字符串作为命令执行](#将字符串作为命令执行)
  - [获取子串（字符串切割）](#获取子串字符串切割)
    - [cut](#cut)
    - [截取语法](#截取语法)
  - [字符串转数组](#字符串转数组)
    - [read](#read)
    - [字符替换](#字符替换-1)
    - [其他场景](#其他场景)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 字符替换

将空格字符' '替换为'|'

```sh
STR="1 2 3 4";
SKYLINE=${STR// /|}
echo $SKYLINE
# 1|2|3|4
```

## 字符包含判定

### ==

```sh
STR='GNU/Linux is an operating system'
SUB='Linux'
if [[ "$STR" == *"$SUB"* ]]; then
  echo "It's there."
fi
```

### 正则=~

```sh
STR='GNU/Linux is an operating system'
SUB='Linux'
if eval '[[ "$STR" =~ .*"$SUB".* ]]'; then
  echo "It's there."
else
  echo "It's not there."
fi
eval '[[ "$STR" =~ .*"$SUB".* ]]' && echo "It's there." || echo "It's not there."
```

由于上述正则中包含了变量，需要使用 eval 来辅助，一般使用情况如下

```sh
STR='GNU/Linux is an operating system'
if [[ "$STR" =~ .*Linux.* ]]; then
  echo "It's there."
else
  echo "It's not there."
fi
[[ "$STR" =~ .*Linux.* ]] && echo "It's there." || echo "It's not there."
```

### grep

使用 grep

```sh
STR='GNU/Linux is an operating system'
SUB='Linux'

if grep -q "$SUB" <<< "$STR"; then
  echo "It's there"
fi
```

## 将字符串作为命令执行

使用 eval 命令

```sh
eval 'echo 1'
```

## 获取子串（字符串切割）

### cut

使用 cut 命令，基本使用如下

```sh
echo "STRING" | cut -cN-M
```

```sh
echo "skyline" | cut -c2-6
# kylin
```

也可以不传 M

```sh
echo "skyline" | cut -c2-
# kyline
```

上述代码实现的效果类似于 JS 中字符串 slice 的效果，但注意字符串截取的索引指代不同。
要实现字符串 split 效果，需要添加额外参数
可以通过-d 参数指定分割符号（delimiter）
分割字符后将同样得到一个数组（索引以 1 开始的数组？），需要添加 -f 参数来指定截取的索引

```sh
echo "skyline" | cut -d'i' -f1
# skyl
echo "skyline" | cut -d'i' -f2
# ne
echo "skyline" | cut -d'i' -f1-
# skyline
```

### 截取语法

基本语法

```sh
string='xxx'
echo ${string:S}
echo ${string:S:E}
```

S 与 E 分别指代开始和结束索引
使用

```sh
a=skyline
echo ${a:1}
# kyline
echo ${a:2}
# yline
echo ${a:2:4}
# ylin
```

## 字符串转数组

### read

```sh
IN="skyline/test/a"

# 将字符以 / 分割并以数组存在ADDR中
IFS='/' read -ra ADDR <<<"$IN"

# 打印数组的每一项
echo ${ADDR[@]}
# skyline test a

# 打印数组的第一项
echo ${ADDR[0]}
# skyline

# 打印数组的长度
echo ${#ADDR[@]}
# 4

# 遍历每一项
for i in ${ADDR[@]}; do
    echo "$i"
done
```

read 命令 -a 参数是指将输入以数组形式存储
read 命令 -r 参数是指将输入中的反斜杠\不具备转义，为普通字符，此处可不加

### 字符替换

将字符串替换为`xx xx xx`后的形式后用`()`包裹，即构建数组字面量形式`(xx xx xx)`
(经测试，Mac 下无效，Centos7 可行)

```sh
IN="skyline/test/a"
arrIN=(${IN//// })
echo ${arrIN[1]}
# test
echo ${arrIN[*]}
# skyline test a
```

### 其他场景

如下场景非严格意义转数组，但应对于需要数组实现的某些效果

- cut

若只需要使用分割后的字符某项，使用 cut 更加方便易懂。
如上获取子串一节所示，需要注意此处索引不是以 0 开始

```sh
echo "skyline/test/a" | cut -d'i' -f1
# skyline
```

- tr

若只需要打印分割后的每项，可以使用 tr

```sh
IN="skyline/test/a"
for i in $(echo $IN | tr "/" "\n")
do
  echo $i
done
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Shell 中字符串相关操作.html](http://www.skyline.show/Shell中字符串相关操作.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

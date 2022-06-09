# Shell 中字符串相关操作

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 中字符串相关操作](#shell-中字符串相关操作)
  - [字符包含判定](#字符包含判定)
    - [==](#)
    - [grep](#grep)
  - [将字符串作为命令执行](#将字符串作为命令执行)
  - [获取子串（字符串切割）](#获取子串字符串切割)
    - [cut](#cut)
    - [截取语法](#截取语法)
  - [字符串转数组](#字符串转数组)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 字符包含判定

### ==

```shell
STR='GNU/Linux is an operating system'
SUB='Linux'
if [[ "$STR" == *"$SUB"* ]]; then
  echo "It's there."
fi
```

### grep

使用 grep

```shell
STR='GNU/Linux is an operating system'
SUB='Linux'

if grep -q "$SUB" <<< "$STR"; then
  echo "It's there"
fi
```

## 将字符串作为命令执行

使用 eval 命令

```shell
eval 'echo 1'
```

## 获取子串（字符串切割）

### cut

使用 cut 命令，基本使用如下

```shell
echo "STRING" | cut -cN-M
```

```shell
echo "skyline" | cut -c2-6
# kylin
```

也可以不传 M

```shell
echo "skyline" | cut -c2-
# kyline
```

上述代码实现的效果类似于 JS 中字符串 slice 的效果，但注意字符串截取的索引指代不同。
要实现字符串 split 效果，需要添加额外参数
可以通过-d 参数指定分割符号（delimiter）
分割字符后将同样得到一个数组，需要添加 -f 参数来指定截取的索引

```shell
echo "skyline" | cut -d'i' -f1
# skyl
echo "skyline" | cut -d'i' -f2
# ne
echo "skyline" | cut -d'i' -f1-
# skyline
```

### 截取语法

基本语法

```shell
string='xxx'
echo ${string:S}
echo ${string:S:E}
```

S 与 E 分别指代开始和结束索引
使用

```shell
a=skyline
echo ${a:1}
# kyline
echo ${a:2}
# yline
echo ${a:2:4}
# ylin
```

## 字符串转数组
```shell

```
## BMW WARNING

### Bulletin

本文首发于 [skyline.show](http://www.skyline.show)  欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>   

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh
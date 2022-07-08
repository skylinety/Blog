# Shell 中数组相关操作

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 中数组相关操作](#shell-中数组相关操作)
  - [获取数组长度](#获取数组长度)
  - [列出数组项](#列出数组项)
  - [数组合并](#数组合并)
  - [数组遍历](#数组遍历)
  - [数组下标获取](#数组下标获取)
  - [数组转字符串](#数组转字符串)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 获取数组长度

```sh
skyline=(4 3 2 1)
echo ${#skyline[*]}
# 4
echo ${#skyline[@]}
# 4
```

## 列出数组项

- 列出所有项

```sh
skyline=(4 3 2 1)
echo ${skyline[@]}
# 4 3 2 1
echo ${skyline[*]}
# 4 3 2 1
```

列出单项

```sh
skyline=(4 3 2 1)
echo ${skyline[1]}
# 3
```

## 数组合并

```sh
skyline=(4 3 2 1)
lty=(2 3 4)
ret=($skyline $lty)
echo  $ret
# 4 3 2 1 2 3 4
```

```sh
skyline=(4 3 2 1)
ret=($skyline 2 3 4)
echo  $ret
# 4 3 2 1 2 3 4
```

当数组添加项只有一项时，即可实现 JS 数组类似于 push 的效果

```sh
skyline=(4 3 2 1)
ret=($skyline 0)
echo  $ret
# 4 3 2 1 0
```

## 数组遍历

```sh
skyline=(4 3 2 1)
for value in $skyline
# for value in "${skyline[@]}"
do
     echo $value
done
# 4
# 3
# 2
# 1
for (( i=1; i<=${#skyline}; i++ ))
do
  echo ${skyline[$i]}
done
# 4
# 3
# 2
# 1
```

## 数组下标获取

```sh
skyline=(4 3 2 1)
echo ${skyline[1]}
# 3
echo ${skyline[2]}
# 2
echo ${skyline[-1]}
# 1
echo ${skyline[-2]}
# 2
```

## 数组转字符串

直接赋值后即为以空格分隔的字符串，若需要将空格换成其他字符串，使用`${STRING//DELIMITER/SUBSTITUTION}`方案更换

```sh
ARR=(1 2 3 4);
STR=$ARR

# 将空格换成|
SKYLINE=${STR// /|}
echo $SKYLINE
# 1|2|3|4
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

文章链接：[http://www.skyline.show/Shell 中数组相关操作.html](http://www.skyline.show/Shell中数组相关操作.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

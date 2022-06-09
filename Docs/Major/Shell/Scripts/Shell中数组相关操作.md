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

<!-- /code_chunk_output -->

## 获取数组长度

```sh
skyline=(4 3 2 1)
echo ${#skyline}
# 4
echo ${#skyline[*]}
# 4
echo ${#skyline[@]}
# 4
```

## 列出数组项

```sh
skyline=(4 3 2 1)
echo $skyline
# 4 3 2 1
echo ${skyline[@]}
# 4 3 2 1
# 或使用echo ${skyline[*]}
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
# 4
echo ${skyline[-1]}
# 1
echo ${skyline[-2]}
# 2
```

## 数组转字符串
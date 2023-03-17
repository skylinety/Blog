# Shell 基础命令

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 基础命令](#shell-基础命令)
  - [echo](#echo)
  - [head](#head)

<!-- /code_chunk_output -->

## echo

echo 打印输出命令

```sh
echo "Hello World"
```

启用特殊字符转换（\特殊字符）

```sh
echo -e "Column 1\tColumn 2"
# Column 1        Column 2
```

## head

根据要求展示输入的前置部分

> output the first part of files

展示前两行

```sh
ls -lh | head -2
# total 8
# drwxr-xr-x  5 macmini  staff   170B Mar  3 17:06 Demos

# 其他方案
ls -lh | sed -n '1,2p'
# total 8
# drwxr-xr-x  5 macmini  staff   170B Mar  3 17:06 Demos
```

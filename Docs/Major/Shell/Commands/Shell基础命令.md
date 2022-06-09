# Shell 基础命令

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 基础命令](#shell-基础命令)
  - [echo](#echo)
  - [ls](#ls)

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

## ls

ls list，列出目录内容

| 参数 | 使用  | 描述                         |
| ---- | ----- | ---------------------------- |
| 1    | ls -1 | 换行列出文件                 |
| a    | ls -a | 列出所有文件，包括隐藏文件   |
| d    | ls -d | 列出目录本身，而不是其下内容 |

```sh
ls -d
```

列出的目录为当前目录，结果为.，要想列出当前目录下的所有目录使用

```sh
ls -d */
```

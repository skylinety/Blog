# Shell 常见操作汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 常见操作汇总](#shell-常见操作汇总)
  - [查看端口占用](#查看端口占用)
  - [删除目录下模糊匹配的文件](#删除目录下模糊匹配的文件)
    - [命令](#命令)
    - [解析](#解析)

<!-- /code_chunk_output -->

## 查看端口占用

    `netstat -apn | grep 8884`

    `lsof -i:8884`

## 删除目录下模糊匹配的文件

### 命令

    `find . -name "*.js" | xargs rm -rf`

### 解析

Shell 中只有部分命令支持标准输入，例如 wc、grep 等，通过管道 | 很容易将前置命令的标准输出传递给这些命令。但是部分命令不支持标准输入，例如 echo rm mkdir 等，这里需要 xargs 来提供
[xargs](https://github.com/skylinety/Blog/blob/b941cb7487a5e46cee010461e38e89fb2eb897dc/Docs/Major/Shell/Shell%E4%B8%ADxargs%E4%BD%BF%E7%94%A8.md)

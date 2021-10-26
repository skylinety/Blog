# Shell 常见操作汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 常见操作汇总](#shell-常见操作汇总)
  - [设置别名](#设置别名)
    - [临时别名](#临时别名)
    - [永久生效](#永久生效)
  - [查看端口占用](#查看端口占用)
  - [删除目录下模糊匹配的文件](#删除目录下模糊匹配的文件)
    - [命令](#命令)
    - [解析](#解析)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warranty](#warranty)

<!-- /code_chunk_output -->

## 设置别名

### 临时别名

`alias m="tldr"`
tldr 是一个以示例代替说明的命令使用说明。

### 永久生效

```bash
vim ~/.bashrc
# vim ~/.zshrc
```

在末尾行加入
`alias m="tldr"`
然后
`source ~/.bashrc`

## 查看端口占用

    `netstat -apn | grep 8884`

    `lsof -i:8884`

## 删除目录下模糊匹配的文件

### 命令

    `find . -name "*.js" | xargs rm -rf`

### 解析

Shell 中只有部分命令支持标准输入，例如 wc、grep 等，通过管道 | 很容易将前置命令的标准输出传递给这些命令。但是部分命令不支持标准输入，例如 echo rm mkdir 等，这里需要 xargs 来提供
[xargs](https://github.com/skylinety/Blog/blob/b941cb7487a5e46cee010461e38e89fb2eb897dc/Docs/Major/Shell/Shell%E4%B8%ADxargs%E4%BD%BF%E7%94%A8.md)

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warranty

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

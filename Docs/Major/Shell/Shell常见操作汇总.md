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
  - [查找目录下包含指定字符的文件](#查找目录下包含指定字符的文件)
    - [命令](#命令-1)
    - [解析](#解析-1)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 创建嵌套文件夹并进入

```shel
mkdir /home/foo/123 && cd $_
```

## 查看远程服务及端口是否开启

`telnet ip 3306`

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

## 查找目录下包含指定字符的文件

### 命令

在 Docs 目录下查找包含 find 字符的文件

```shell
ls ./ | xargs grep -rni find

find . -type f | xargs grep -rni find

grep -rni ./ -e find
```

![Shell常见操作汇总20211112174412](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C%E6%B1%87%E6%80%BB20211112174412.png)

```shell
grep -rniw ./ -e user

```

![Shell常见操作汇总20211112182828](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C%E6%B1%87%E6%80%BB20211112182828.png)

上述代码不会匹配 users

```shell
grep -rniw ./ -e user -l

```

-l --files-with-matches
只输出匹配的文件名

> Only the names of files containing selected lines are written to standard output

![Shell常见操作汇总20211112182942](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C%E6%B1%87%E6%80%BB20211112182942.png)

### 解析

grep 参数

- r 递归查找子目录文件
- n 列出行标
- i 忽略大小写
- e 搜索时启用正则匹配
- w 精确指定单词，需要为单词，英文单词前后有字母不匹配
- l 只输出匹配的文件名

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

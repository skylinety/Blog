# Shell 中查找相关命令

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 中查找相关命令](#shell-中查找相关命令)
  - [which/whereis/whatis](#whichwhereiswhatis)
    - [which](#which)
    - [whereis](#whereis)
    - [whatis](#whatis)
  - [find](#find)
  - [grep](#grep)
  - [汇总](#汇总)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## which/whereis/whatis

### which

搜索某个命令在文件系统中的的位置并展示，若命令为别名，则会展示别名对应的命令。

> shows the full path of (shell) commands.

默认使用时，搜索某个系统命令的位置，并且返回第一个搜索结果

```sh
which netstat
# /usr/sbin/netstat
which ls
# ll: aliased to ls -G
```

-a 选项，搜索某个系统命令的位置，并且返回所有搜索结果

```sh
which -a ls
# ls: aliased to ls -G
# /bin/ls
```

### whereis

命令只能用于程序名的搜索，而且只搜索二进制文件（参数-b）、man 说明文件（参数-m）和源代码文件（参数-s）

> locate the binary, source, and manual page files for a command

```sh
whereis ls
# ls: /bin/ls /usr/share/man/man1/ls.1
whereis -b ls
# ls: /bin/ls
whereis -m ls
# ls: /usr/share/man/man1/ls.1
```

### whatis

展示命令手册中对应的的简要介绍

> display manual page descriptions

```sh
whatis shutdown
# shutdown (8)         - Halt, power-off or reboot the machine

whatis whereis
# whereis (1)          - locate the binary, source, and manual page files for a command

whatis which
# which (1)            - shows the full path of (shell) commands.

whatis whatis
# whatis (1)           - display manual page descriptions
```

## find

文件搜索命令。

> search for files in a directory hierarchy

在项目根目录下执行如下命令。

- 根据文件名称搜索

```sh
find ./ -name 'Nas*'
# .//Demos/Tools/OS/Nas
# .//Docs/Tools/OS/Nas
# .//Docs/Tools/OS/Nas/Nas使用frp内网穿透.md
# .//Docs/Tools/OS/Nas/Nas系统选择.md
```

- 忽略文件名大小写

```sh
find ./ -name 'nas*'
#
find ./ -iname 'nas*'
# .//Demos/Tools/OS/Nas
# .//Docs/Tools/OS/Nas
# .//Docs/Tools/OS/Nas/Nas使用frp内网穿透.md
# .//Docs/Tools/OS/Nas/Nas系统选择.md
```

- 根据文件权限搜索

```sh
# 查找具有SUID权限的文件
find /usr/bin/ -perm /4000 | xargs ls -lh
# 查找具有SGID权限的文件
find /usr/bin/ -perm /2000 | xargs  ls -lh
# 查找具有Sticky bit权限的文件
find /usr/bin/ -perm /1000 | xargs  ls -lh

# 查找777权限文件
find /usr/bin/ -perm 777 | xargs  ls -lh

# 查找755权限文件
find /usr/bin/ -perm 755 | xargs  ls -lh

# 查找4755权限文件(具有755与SUID权限)
find /usr/bin/ -perm 4755 | xargs  ls -lh

```

- 根据修改日期搜索

```sh
# 列出七天内修改的文件
find ./ -name 'nas*' -mtime -7
```

- 根据文件类型搜索

```sh
find ./ -name 'Nas*' -type d
# .//Demos/Tools/OS/Nas
# .//Docs/Tools/OS/Nas
find ./  -name 'Git*' -type f
# .//Docs/Tools/DEVs/Git/Git常见命令.md
# .//Docs/Tools/DEVs/Git/Git常见操作.md
# .//Docs/Tools/DEVs/Git/Git常见符号.md
# .//Docs/Tools/DEVs/Git/Git常见问题.md
```

文件类型

```sh
- f: 普通文件
- d: 文件夹
- l: 链接
- c: character devices
- b: block devices
- p: named pipe (FIFO)
- s: socket
```

- 根据文件大小搜索

```sh
find ./ -name 'Git*' -type f | xargs ls -lh
# -rw-r--r--  1 macmini  staff   1.7K Jun  9 17:41 .//Docs/Tools/DEVs/Git/Git常见命令.md
# -rw-r--r--  1 macmini  staff   6.5K Jun 16 11:50 .//Docs/Tools/DEVs/Git/Git常见操作.md
# -rw-r--r--  1 macmini  staff   1.2K Mar  2 16:38 .//Docs/Tools/DEVs/Git/Git常见符号.md
# -rw-r--r--  1 macmini  staff   1.2K Jun  9 17:41 .//Docs/Tools/DEVs/Git/Git常见问题.md
find ./ -name 'Git*' -type f -size +1k -size -2k
# .//Docs/Tools/DEVs/Git/Git常见命令.md
# .//Docs/Tools/DEVs/Git/Git常见符号.md
# .//Docs/Tools/DEVs/Git/Git常见问题.md
```

- 多个条件搜索

```sh
find ./ -name 'Nas*' -type d -or -name 'Git*' -type f
.//Demos/Tools/OS/Nas
.//Docs/Tools/DEVs/Git/Git常见命令.md
.//Docs/Tools/DEVs/Git/Git常见操作.md
.//Docs/Tools/DEVs/Git/Git常见符号.md
.//Docs/Tools/DEVs/Git/Git常见问题.md
.//Docs/Tools/OS/Nas
```

- 对找到的多个文件执行命令操作
  `{}`指代文件

```sh
find ./ -name 'Git*' -type f -size +1k -size -2k -exec wc -l {} \;
#   54 .//Docs/Tools/DEVs/Git/Git常见命令.md
#   41 .//Docs/Tools/DEVs/Git/Git常见符号.md
#   56 .//Docs/Tools/DEVs/Git/Git常见问题.md

```

- 查找空文件和空目录

```sh
touch Git.txt;mkdir Git_test;
find ./ -empty -name "Git*"
# .//Git.txt
# .//Git_test
```

- 删除搜索结果

```sh
find ./ -empty -name "Git*" -delete
```

- Find files matching a given pattern, excluding specific paths:
  find root*path -name '*.py' -not -path '\_/site-packages/\*'

## grep

grep 是一个字符搜索命令，使用的基础语法为

```sh
grep [options] pattern [files]
```

具体参考
[Shell 中 grep 的使用](http://www.skyline.show/Shell中grep的使用.html)

## 汇总

| 命令    | 描述                                                                    |
| ------- | ----------------------------------------------------------------------- |
| which   | 展示命令在系统路径中的位置。                                            |
| whereis | 用于程序名的搜索                                                        |
| locate  | 通过数据库显示文件或目录                                                |
| find    | 查找硬盘中文件或目录                                                    |
| grep    | 查找某个文件中匹配项所在行并输出整行                                    |
| type    | 用来区分某个命令出处，是由 shell 自带的，或外部的独立二进制文件提供的。 |

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Shell 中查找相关命令.html](http://www.skyline.show/Shell中查找相关命令.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

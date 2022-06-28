# Shell 中 ls 的使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 中 ls 的使用](#shell-中-ls-的使用)
  - [基础使用](#基础使用)
    - [参数](#参数)
    - [常见用法](#常见用法)
  - [权限](#权限)
  - [BMW WARNING](#bmw-warning)


<!-- /code_chunk_output -->

## 基础使用

### 参数

ls 即 list，列出目录内容

| 参数 | 使用  | 描述                             |
| ---- | ----- | -------------------------------- |
| 1    | ls -1 | 换行列出文件                     |
| a    | ls -a | 列出所有文件，包括隐藏文件       |
| d    | ls -d | 列出当前目录本身，而不是其下内容 |

### 常见用法

```sh
ls -d
# .
```

列出的目录为当前目录，结果为.，要想列出当前目录下的所有目录使用

```sh
ls -d */
```

详细显示所有文件

```sh
ls -la
```

详细显示当前目录的具体信息

```sh
ls -ld
# drwxr-xr-x+  5 skyline  staff   170  4  3 12:30 .
```

## 权限

`ls 【选项】【目录/文件】`

```sh
ls -l
# total 0
# drwx------@  3 skyline  staff   102B  4  4 11:17 Applications
# drwx------+ 16 skyline  staff   544B  5 11 17:52 Desktop
# drwx------+ 11 skyline  staff   374B  4 18 09:33 Documents
# drwx------+ 78 skyline  staff   2.6K  5 26 10:43 Downloads
# drwxr-xr-x   4 skyline  staff   136B  5 11 10:17 ENV
# drwxr-xr-x   5 skyline  staff   170B  4  5 15:30 HBuilder
# drwxr-xr-x   3 skyline  staff   102B  4  5 15:30 HBuilderProjects
# drwx------@ 64 skyline  staff   2.1K  5 22 14:18 Library
# drwx------+  3 skyline  staff   102B  4  3 12:30 Movies
# drwx------+  6 skyline  staff   204B  4 25 17:31 Music
# drwx------+  3 skyline  staff   102B  5 22 14:19 Pictures
# drwxr-xr-x+  5 skyline  staff   170B  4  3 12:30 Public
# drwxr-xr-x   9 skyline  staff   306B  5 11 09:57 workSpace
```

上述倒数第二列`drwxr-xr-x+ 5 skyline staff 170B 4 3 12:30 Public`的含义如下

| 文件格式 | 所有者权限 | 群组权限 | 其他人权限 | ACL 权限 | 引用计数 | 所有者  | 所在组 | 大小 | 最后修改日期 | 文件名 |
| -------- | ---------- | -------- | ---------- | -------- | -------- | ------- | ------ | ---- | ------------ | ------ |
| d        | rwx        | r-x      | r-x        | +        | 5        | skyline | staff  | 170B | 4 3 12:30    | Public |

权限由第一列列出，一般有 11 位，即如上`drwxr-xr-x+`

- 第 1 位代表文件类型:

  - -文件
  - d 目录
  - l 软链接文件
  - b 装置文件里面的可供储存的接口设备(可随机存取装置)；
  - c 装置文件里面的串行端口设备，例如键盘、鼠标(一次性读取装置)

- 接下来中间 9 位，以 3 个为 1 组，且均为『rwx』 的 3 个参数的组合。
  - [ r ]代表可读(read)
  - [ w ]代表可写(write)
  - [ x ]代表可执行(execute)

要注意的是，这三个权限的位置不会改变，如果没有权限，就会出现减号[ - ]而已。

对目录如果没有 w 权限，即使里面的文件有写权限，也不能对文件进行移动，重命名操作。
此时，需要给目录加上 w 权限：`chmod +w`（注意此时 cwd 是此目录）

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https: //creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

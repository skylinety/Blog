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

| 参数 | 使用  | 描述                                   |
| ---- | ----- | -------------------------------------- |
| 1    | ls -1 | 换行列出文件                           |
| l    | ls -l | 换行列出文件详细信息                   |
| a    | ls -a | 列出所有文件，包括隐藏文件             |
| d    | ls -d | 列出当前目录本身，而不是其下内容       |
| h    | ls -h | 文件大小可读化输出，需要与 -l 配合使用 |

### 常见用法

列出目录信息

```sh
ls -dlh /var/log
drwxr-xr-x  47 root  wheel   1.5K Jan  6 09:22 /var/log
# .
```

列出当前目录下的所有目录使用

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
# total 8
# drwxr-xr-x  5 macmini  staff   170B Mar  3 17:06 Demos
# drwxr-xr-x+  7 macmini  staff   238B Jun 15 16:39 Docs
# -rwxr-xr-x  1 macmini  staff   143B Sep 18  2021 README.md
```

上述倒数第二列`drwxr-xr-x+ 7 macmini staff 238B Jun 15 16:39 Docs`的含义如下

| 文件格式 | 所有者权限 | 群组权限 | 其他人权限 | ACL 权限 | 引用计数 | 所有者  | 所在组 | 大小 | 最后修改日期 | 文件名 |
| -------- | ---------- | -------- | ---------- | -------- | -------- | ------- | ------ | ---- | ------------ | ------ |
| d        | rwx        | r-x      | r-x        | +        | 5        | macmini | staff  | 238B | Jun 15 16:39 | Docs   |

权限由第一列列出，一般有 11 位，即如上`drwxr-xr-x+`

- 第 1 位代表文件类型:

  - `-` 普通文件
  - `d` 目录
  - `l` 软链接文件
  - `s` socket 文件
  - `b` 装置文件里面的可供储存的接口设备(可随机存取装置)；
  - `c` 装置文件里面的串行端口设备，例如键盘、鼠标(一次性读取装置)

- 接下来中间 9 位，以 3 个为 1 组，且均为『rwx』 的 3 个参数的组合。
  - [ r ]代表可读(read)
  - [ w ]代表可写(write)
  - [ x ]代表可执行(execute)

要注意的是，这三个权限的位置不会改变，如果没有权限，就会出现减号[ - ]而已。

对目录如果没有 w 权限，即使里面的文件有写权限，也不能对文件进行移动，重命名操作。
此时，需要给目录加上 w 权限：`chmod +w`（注意命令在该目录下执行）

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https: //creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

# Shell 中 chmod 的使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 中 chmod 的使用](#shell-中-chmod-的使用)
  - [文件权限](#文件权限)
  - [使用字符赋权](#使用字符赋权)
    - [字符含义](#字符含义)
    - [添加权限](#添加权限)
    - [删除权限](#删除权限)
    - [权限赋值](#权限赋值)
  - [使用数字赋权](#使用数字赋权)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 文件权限

通过`ls -lh`命令可以查看文件权限

已拿到某个文件夹的权限`drwxr-xr-x+ 7 macmini staff 238B Jun 15 16:39 Docs`为例，其含义如下

| 文件格式 | 所有者权限(u) | 群组权限(g) | 其他人权限(o) | ACL 权限 | 引用计数 | 所有者  | 所在组 | 大小 | 最后修改日期 | 文件名 |
| -------- | ------------- | ----------- | ------------- | -------- | -------- | ------- | ------ | ---- | ------------ | ------ |
| d        | rwx           | r-x         | r-x           | +        | 5        | macmini | staff  | 238B | Jun 15 16:39 | Docs   |

其 2-10 位位权限位，以 3 个为 1 组，且均为『rwx』 的 3 个参数的组合。

要注意的是，这三个权限的位置不会改变，如果没有权限，就会出现减号[ - ]而已。
通过 chmod 命令可以更改文件权限。

## 使用字符赋权

### 字符含义

通过 `r w x`字符来指定权限。

- [ r ]代表可读(read)
- [ w ]代表可写(write)
- [ x ]代表可执行(execute)

通过 `u g o a`来指定更改的用户。

- [ u ]代表当前用户(user)
- [ g ]代表当前用户所在组(group)
- [ o ]代表非当前用户所在组的其他用户(other)
- [ a ]代表所有用户(all)

### 添加权限

当前用户添加全部权限

```sh
chmod u+rwx file
```

所有用户添加读写权限

```sh
chmod a+rx file
```

当前组写权限，其他组读权限

```sh
chmod g+r,o+w file
```

对所有用户在当前目录下所有文件（夹）递归赋全部权

```sh
chmod -R a+rwx directory
```

### 删除权限

移除当前用户所在组执行权限

```sh
chmod g-x file
```

### 权限赋值

给予当前用户全部权限，其他人员赋予读取与执行权限

```sh
chmod u=rwx,g=rx,o=rx file
```

## 使用数字赋权

使用数字赋权时，通过如下数字代表不同的权限

| 权限    | 数字 |
| ------- | ---- |
| read    | 4    |
| write   | 2    |
| execute | 1    |

则常见的权限通过数字相加组合，例如：

| 赋权 | 取值 | 计算      |
| ---- | ---- | --------- |
| r--  | 4    | 4 + 0 + 0 |
| r-x  | 5    | 4 + 0 + 1 |
| rw-  | 6    | 4 + 2 + 0 |
| rwx  | 7    | 4 + 2 + 1 |

chmod 通过指定三位数字来给一个文件向不同的用户赋权
例如，要想一个文件的权限为 `rwxr-xr-x`，每三位一组，即为 755
使用

```sh
chmod 755 file
# 或
chmod u=rwx,g=r-x,o=r-x file
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

文章链接：[http://www.skyline.show/Shell 中 chmod 的使用.html](http://www.skyline.show/Shell中chmod的使用.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

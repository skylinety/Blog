# Shell 中 chmod 的使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 中 chmod 的使用](#shell-中-chmod-的使用)
  - [文件权限](#文件权限)
    - [权限查看](#权限查看)
    - [权属调整](#权属调整)
  - [使用字符赋权](#使用字符赋权)
    - [字符含义](#字符含义)
    - [添加权限](#添加权限)
    - [删除权限](#删除权限)
    - [赋予权限](#赋予权限)
  - [使用数字赋权](#使用数字赋权)
  - [特殊权限](#特殊权限)
    - [权限进阶](#权限进阶)
    - [SUID](#suid)
    - [SGID](#sgid)
    - [Sticky bit](#sticky-bit)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 文件权限

### 权限查看

通过`ls -lh`命令可以查看文件权限

已拿到某个文件夹的权限`drwxr-xr-x+ 7 macmini staff 238B Jun 15 16:39 Docs`为例，其含义如下

| 文件格式 | 所有者权限(u) | 群组权限(g) | 其他人权限(o) | ACL 权限 | 引用计数 | 所有者  | 所在组 | 大小 | 最后修改日期 | 文件名 |
| -------- | ------------- | ----------- | ------------- | -------- | -------- | ------- | ------ | ---- | ------------ | ------ |
| d        | rwx           | r-x         | r-x           | +        | 5        | macmini | staff  | 238B | Jun 15 16:39 | Docs   |

第一位为文件格式，其字符含义对照如下

| 字符 | 含义                |
| ---- | ------------------- |
| -    | 文件                |
| d    | 文件夹（directory） |
| l    | 连接（link）        |
| c    | 字符设备（char）    |
| b    | 块设备（block）     |
| s    | 套接字（sockets）   |
| p    | 管道（pipe）        |

其余 2-10 位位权限位，以 3 个为 1 组，且均为『rwx』 的 3 个参数的组合。

要注意的是，这三个权限的位置不会改变，如果没有权限，该位置以[ - ]占位。

### 权属调整

文件所属权限调整，使用 chown 命令。

调整文件拥有者

```sh
chown user file
```

调整文件所属组，可使用 chown 命令，也可使用 chgrp 命令

```sh
chown :group file
chgrp group file
```

调整文件拥有者与所属组

```sh
chown user:group file
```

chown 调整文件权属，各用户更细分权限调整，通过 chmod 命令实现。
后续章节围绕 chmod 展开。

## 使用字符赋权

### 字符含义

通过 `u g o a`来指定被操作的用户。

- [ u ]代表文件拥有者(user)
- [ g ]代表文件所属组(group)
- [ o ]代表既非所有者也不在所属组的其他用户(other)
- [ a ]代表所有用户(all)

需要注意的是，文件拥有者不一定在文件所属组中，当文件拥有者在文件所属组中时，检查的是所有者权限，而不是其所属组权限。
Linux 在检查用户权限时，按照用户、组、其他的优先级依次检查，若命中则不会再次向后检查。
例如，当一个文件的权限位`----r-xr-x+ 7 macmini staff`时，即便 macmini 用户属于 staff 权限，其也不能读取该文件。

通过 `+ - =`字符来指定权限操作。

- [ + ]代表添加权限
- [ - ]代表缩减权限
- [ = ]代表赋予（更改）权限

通过 `r w x`字符来指定具体权限。

对于文件

- [ r ]代表可读(read)
- [ w ]代表可写(write)
- [ x ]代表可执行(execute)

对于文件夹

- [ r ]代表列举文件夹内容(ls)，可拷贝文件夹内容(cp)
- [ w ]代表可新增和删除文件内容，需要拥有可执行权限，否则进不去文件夹拥有写权限也无效
- [ x ]代表可进入文件夹

### 添加权限

当前用户添加全部权限

```sh
chmod u+rwx file
```

所有用户添加读写权限

```sh
chmod a+rx file
```

当前组写权限，其他组读权限，分别赋权用`,`隔开

```sh
chmod g+r,o+w file
```

当多个赋权一致时，也可以合并书写。
当前用户与主赋予执行权限

```sh
chmod u+x,g+x file
# 或合并写为
chmod ug+x file
```

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

### 赋予权限

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

## 特殊权限

### 权限进阶

对于各用户赋权，除了常见的`r w x`权限，还有另外的三种附加权限。分别是

- SUID(Set-user Identification)
- SGID(Set-group Identification)
- Sticky bit

上述权限在基本权限的基础上，进一步拓展了文件权限限制与开放的层级。
在 linux 中，文件权限实际用 12 位二进制来存储。

| 位置 | 11  | 10  | 9   | 8   | 7   | 6   | 5   | 4   | 3   | 2   | 1   | 0   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 权限 | S   | G   | T   | r   | w   | x   | r   | w   | x   | r   | w   | x   |

在这 12 位上，拥有该权限则对应 1，无权限对应为 0

| 权限      | 权限二进制              | 数值 |
| --------- | ----------------------- | ---- |
| rw-r-sr-- | 0 1 0 1 1 0 1 0 0 1 0 0 | 2654 |
| rwsr-xr-x | 1 0 0 1 1 1 1 0 1 1 0 1 | 4755 |
| rwsr-sr-x | 1 1 0 1 1 1 1 0 1 1 0 1 | 6755 |
| rwsr-sr-t | 1 1 1 1 1 1 1 0 1 1 0 1 | 7755 |
| rwxr-xr-x | 0 0 0 1 1 1 1 0 1 1 0 1 | 755  |

每三位一组，在附加权限位（9-11 位）上，转换为 10 进制 SUID 对应值为 4，SGID 对应 2，Sticky bit 对应 1。
同理，在前 9 位上的读写位上，每 3 位一组，读对应值为 4，写对应值为 2，执行对应值为 1。
这些值在使用数字赋权时供计算使用。
例如，将所有权限存储二进制位置为 1。

```sh
chmod 7777 file
# -rwsrwsrwt 1 root root    0 Jul  4 16:41 file
```

### SUID

SUID 设定任何执行该文件的用户其身份为文件拥有者，并以文件拥有者权限执行文件。
拥有该权限的标识为'S'。
其设定的标识位于所有者权限标识三位中的最后一位（即可执行位）上，以初始文件权限`rw-r-xr-x`为例。
当其设定了 SUID 权限时，其标识为`rwSr-xr-x`。
由于占据了可执行位，若此时文件用户所有者具有可执行(x)权限，区分的方案为采用大小写，同时具备 SUID 和 x 权限时，使用小写's'
对应的权限为`rwsr-xr-x`
该权限仅对所有者设定有效，对所属组(g)、其他用户(o)、全部用户(a)设定无效。
其权限增减方式为

```sh
# 添加
chmod u+s file
# 删除
chmod u-s file
```

使用数字方式增减权限的方式为

```sh
# 添加 chmod 4xxx file
chmod 4777 file
# 删除 chmod 0xxx file 或chmod xxx file
chmod 0777 file
```

SUID 多用于可执行文件上。
一个常见的情形为用户更改自己的密码。
在 linux 中，普通用户更改密码都涉及修改`/etc/passwd` 文件，而该文件的权限如下，普通用户无权操作。

```sh
ll /etc/passwd
# -rw-r--r-- 1 root root 1192 Nov 12  2021 /etc/passwd
```

普通用户可使用 `passwd` 命令修改自己的密码，这是由于`passwd`对应的文件`/usr/bin/passwd`拥有 SUID 权限

```sh
ls -lh /usr/bin/passwd
# -rwsr-xr-x 1 root root 28K Apr  1  2020 /usr/bin/passwd
```

### SGID

SGID 类似于 SUID，其权限调整由 SUID 的调整拥有者权限变更到调整所属组权限。
当 SGID 用于可执行文件时，任何执行该文件的用户拥有文件对应所属组权限。
拥有 SGID 权限的标识为'S'。
其设定的标识位于所属组权限标识三位中的最后一位（即可执行位）上，以初始文件权限`rw-r--r-x`为例。
当其设定了 SGID 权限时，其标识为`rw-r-Sr-x`。
由于占据了可执行位，若此时文件用户所属组具有可执行(x)权限，区分的方案为采用大小写，同时具备 SGID 和 x 权限时，使用小写's'
对应的权限为`rwxr-sr-x`
该权限仅对所属组设定有效，对文件拥有者(u)、其他用户(o)、全部用户(a)设定无效。
即其操作方式为

```sh
# 添加
chmod g+s file
# 删除
chmod g-s file
```

使用数字方式操作权限的方式为

```sh
# 添加 chmod 2xxx file
chmod 2777 file
# 删除 chmod 0xxx file 或chmod xxx file
chmod 0777 file
chmod 777 file
```

Linux 执行程序的进程中，通过 euid 和 egid 来判定进程对资源的访问权限。
假定用户 skyline 的 uid=66，所在组 sky 的 gid=666
假定用户 guest 的 uid=88，所在组 test 的 gid=888
skyline 来执行 guest 用户如下 private.sh 文件

```sh
-rwxr-xr-x+ 7 guest test 238B Jun 15 16:39 private.sh
```

private.sh 未设定 SUID 和 SGID，则执行进程时 euid=66，egid=666，即取执行该进程用户 skyline 的 uid 和 gid。
此时，该进程无法获取到执行文件所有者的资源权限。

当 skyline 来执行 guest 如下 share.sh 文件

```sh
-rwsr-sr-x+ 7 guest test 238B Jun 15 16:39 share.sh
```

share.sh 设定 SUID 和 SGID，则执行进程时 euid=88，egid=888，即取执行文件的拥有者与所属组对应 的 uid 和 gid。
此时，该进程相当于所有者自己运行，可以获取所有者相当的资源权限。

当 SGID 用于文件夹时，效果作用于文件夹内部文件。
当父文件夹未设定 SGID 时，其内部新增的文件所属组为创建该文件用户在系统中的基本组。
当父文件夹设定 SGID 时，其内部新增的文件所属组为父文件夹所属组。
SGID 常用于共享文件夹等场景。

### Sticky bit

Sticky bit 限定只有文件所有者和超级用户可删除文件。
拥有该权限的标识为'T'。
其设定的标识位于其他用户权限标识三位中的最后一位（即可执行位）上，以初始文件权限`rw-r--r--`为例。
当其设定了 Sticky bit 权限时，其标识为`rw-r--r-T`。
由于占据了可执行位，若此时文件用户所属组具有可执行(x)权限，区分的方案为采用大小写，同时具备 Sticky bit 和 x 权限时，使用小写't'
对应的权限为`rwxr--r-t`
该权限仅对其他用户设定有效，对文件拥有者(u)、所属组(o)设定无效。
由于不存在 SUID 与 SGID 都使用 s 标识的冲突，操作时，可以不添加使用者来指定权限，其操作方式为

```sh
# 添加
chmod +t file
# 删除
chmod -t file
```

实际上`a+t,o+t`在部分系统也生效，但不推荐这种写法。
使用数字方式操作权限的方式为

```sh
# 添加 chmod 1xxx file
chmod 1777 file
# 删除 chmod 0xxx file 或 chmod xxx file
chmod 0777 file
chmod 777 file
```

Sticky bit 常用于共享文件夹中限制其他人的删除权限。

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

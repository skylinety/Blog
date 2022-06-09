# SSH 使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [SSH 使用](#ssh-使用)
  - [SSH 登陆](#ssh-登陆)
  - [SSH 连接历史](#ssh-连接历史)
    - [方法集](#方法集)
    - [who & w](#who--w)
    - [last](#last)
    - [netstat & ss](#netstat--ss)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## SSH 登陆

对于默认使用了默认 SSH 配置的服务器，可以直接如下登陆

```shell
ssh root@10.2.160.12
```

根据提示输入密码即可。
上述使用了 SSH 常用的 root 用户，默认的 22 端口

```shell
ssh -i /a/b/c/d.private -p 50777 root@10.2.160.12
```

i 指定秘钥位置，p 指定端口。

## SSH 连接历史

### 方法集

常用如下命令查看 SSH 连接。

| 命令    | 描述                                                    |
| ------- | ------------------------------------------------------- |
| who     | 查看当前连接用户、连接 IP、登录时间                     |
| w       | 查看当前连接用户与连接 IP、登录时间、当前启动的进程等   |
| last    | 查看登入历史等信息                                      |
| netstat | 查看网络状态                                            |
| ss      | 查看网络连接信息，与 netstat 类似，但可查看根据状态信息 |

### who & w

相比于 who，w 可以获取登陆用户当前正在进行的进程操作(对应命令)
![SSH使用20220314155021](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/SSH%E4%BD%BF%E7%94%A820220314155021.png)

### last

last 其实质是读取/var/log/wtmp(从该文件创建开始)中的内容并整理成输出。
wtmp 日志文件主要记录系统登入、 重启等关键信息。
![SSH使用20220314162422](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/SSH%E4%BD%BF%E7%94%A820220314162422.png)
last 输出内容较多，当在普通个人电脑上执行该命令的由于经常开关机内容更加庞杂，可通过如下方式进行筛选。
last 命令参数

```shell
last shutdown
last reboot
```

grep 查找

```shell
last | grep reboot
last | grep still
```

### netstat & ss

```shell
netstat | grep ssh
ss | grep ssh
```

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](http://www.skyline.show)  欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh

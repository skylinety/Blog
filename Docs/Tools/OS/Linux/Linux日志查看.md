# Linux 日志查看

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Linux 日志查看](#linux-日志查看)
  - [日志文件](#日志文件)
  - [tail](#tail)

<!-- /code_chunk_output -->

## 日志文件

Linux 系统日志文件位于`/var/log/`目录下.
常见日志文件如下：

| 文件         | 描述                                                        |
| ------------ | ----------------------------------------------------------- |
| messages     | 记录全局系统信息，包含 mail, cron, daemon, kern, auth 等    |
| dmesg        | kernel 内核日志                                             |
| auth.log     | 系统登陆授权信息                                            |
| boot.log     | 启动日志                                                    |
| daemon.log   | 守护进程日志                                                |
| dpkg.log     | dpkg 命令安装卸载历史                                       |
| lastlog      | 记录所有用户最后一次登陆信息，可通过 lastlog 命令直接查看。 |
| mail.log     | 邮件服务日志                                                |
| user.log     | 用户信息                                                    |
| btmp         | 失败登陆尝试日志，可用 last -f /var/log/btmp 查看           |
| anaconda.log | linux 安装日志                                              |
| yum.log      | yum 包安装日志                                              |
| secure       | 安全日志，包含身份鉴权信息，如 SSH 登陆尝试相关信息         |
| wtmp 或 utmp | 二进制文件，记录登入启动等历史。可用 last 命令查看扼要信息  |
| faillog      | 登陆失败尝试日志                                            |

wtmp 为 last 默认文件，查看其它文件时，添加 -f 参数指定

```shell
last -f /var/log/btmp
```

## tail

对于不断产生新信息而写入的日志文件来说，一般通过 tail 来查看日志。

```shell
tail -fn 10 /var/log/system.log

```

![Linux日志查看20220316172232](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Linux%E6%97%A5%E5%BF%97%E6%9F%A5%E7%9C%8B20220316172232.png)

参数解析

- f
  不断打印文件最新内容直到终止前
- n
  指定打印的末尾行数

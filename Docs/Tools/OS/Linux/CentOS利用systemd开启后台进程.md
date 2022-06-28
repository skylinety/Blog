# 利用 Systemd 开启后台进程

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [利用 Systemd 开启后台进程](#利用-systemd-开启后台进程)
  - [简介](#简介)
    - [创建新服务](#创建新服务)
    - [开启服务](#开启服务)
  - [systemd服务操作汇总](#systemd服务操作汇总)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 简介

systemd 是 Linux 中系统与服务管的系列套件，其中 d 沿用传统指代 daemon。
systemd 提供多个命令行工具，最基本的为 systemctl
systemd 体系庞大，提供繁杂的功能，其中一个常用的功能就是开启后台服务。

### 创建新服务

创建服务文件并打开

```sh
vi /etc/systemd/system/foo.service
```

输入以下内容

```sh
[Unit]
Description=My custom service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/brook server --listen :992 --password xxxx
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

[Unit]

    提供服务基础信息
    Description 为描述信息
    After
    服务启动的前置条件

[Service]

    提供启动服务的相关信息

[Install]

    WantedBy
    定义服务被谁触发

> Defines which service triggers the custom service if enabled with systemctl enable. This is mostly used for starting the custom service on boot. In this example, foo.service uses multi-user.target, which starts foo.service when systemd loads multi-user.target on boot.

### 开启服务

创建该服务后，需要重载 systemd 服务文件

```sh
systemctl daemon-reload
```

开启该服务

```sh
systemctl start foo
```

查看该服务运行状态

```sh
systemctl status foo
```

## systemd服务操作汇总

开启服务

```sh
systemctl start foo
```

关闭服务

```sh
systemctl stop foo
```

重启服务

```sh
systemctl restart foo
```

服务状态

```sh
systemctl status foo
```

开机自启动服务

```sh
systemctl enable foo
```

禁止开机启动

```sh
systemctl disable foo
```

查看是否允许开机启动

```sh
systemctl is-enabled foo
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

文章链接：[http://www.skyline.show/CentOS利用systemd开启后台进程.html](http://www.skyline.show/CentOS利用systemd开启后台进程.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

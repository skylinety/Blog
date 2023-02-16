# Brook 服务搭建与访问

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Brook 服务搭建与访问](#brook-服务搭建与访问)
  - [Server 配置](#server-配置)
    - [安装](#安装)
    - [后台运行](#后台运行)
  - [client](#client)
  - [常见问题](#常见问题)
    - [连接后无法访问](#连接后无法访问)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## Server 配置

### 安装

```sh
curl -L https://github.com/txthinking/brook/releases/latest/download/brook_linux_amd64 -o /usr/bin/brook
chmod +x /usr/bin/brook
brook server --listen :9999 --password hello
```

### 后台运行

```sh
vi /etc/systemd/system/brook.service
```

输入如下内容：

```sh
[Unit]
Description=brook vpn

[Service]
ExecStart=/usr/bin/brook server --listen :2000 --password mima
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

要开启多个服务，只需要创建多个 service 文件监听不同端口即可。

重置守护进程服务

```sh
systemctl daemon-reload
```

开启服务

```sh
systemctl start brook
```

检查服务是否开启成功，查看 2000 端口是否开启服务即可。

```sh
netstat -anp | grep 2000
```

如上操作完成后，服务即后台启动成功。
要想服务开机自启动，输入：

```sh
systemctl enable brook
```

即可。

## client

在如下地址下载客户端界面：
https://txthinking.github.io/brook/#/install-gui-client
下载后连接成功如下图所示：
![Brook服务搭建与访问20220118111315](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Brook%E6%9C%8D%E5%8A%A1%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE20220118111315.png)

## 常见问题

### 连接后无法访问

进入服务器查看双方连接是否建立
同样适用端口占用查看命令

```sh
netstat -anp  | grep 2000
tcp6       0      0 :::2000                 :::*                    LISTEN      4498/brook
tcp6       0      0 服务器IP:2000     访问主机IP:51810    ESTABLISHED 4498/brook
tcp6       0      0 服务器IP:2000     访问主机IP:51633    ESTABLISHED 4498/brook
```

出现 ESTABLISHED 才是连接成功
不成功则尝试断开重连

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Brook 服务搭建与访问.html](http://www.skyline.show/Brook服务搭建与访问.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

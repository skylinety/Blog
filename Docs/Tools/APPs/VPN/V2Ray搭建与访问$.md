# V2Ray 搭建与访问

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [V2Ray 搭建与访问](#v2ray-搭建与访问)
  - [搭建](#搭建)
  - [使用](#使用)
    - [openwrt](#openwrt)
  - [常见问题](#常见问题)
    - [搭建完成无法访问](#搭建完成无法访问)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 搭建

服务端搭建推荐使用一键脚本，改脚本内置 SSR 服务，可一个脚本开启两种服务。
脚本如下

```sh
bash <(curl -s -L https://git.io/v2ray.sh)
```

具体参照这个[教程](https://github.com/233boy/v2ray/wiki/V2Ray%E6%90%AD%E5%BB%BA%E8%AF%A6%E7%BB%86%E5%9B%BE%E6%96%87%E6%95%99%E7%A8%8B)

## 使用

### openwrt

通过 passwall 使用。

获取 v2ray 链接：

```jsx
v2ray infolink
```

拿到服务端链接信息，在节点列表通过通过链接添加节点导入。

![V2Ray搭建与访问$20230212230920](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/V2Ray%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE%2420230212230920.png)

配置基本模式->主要

![V2Ray搭建与访问$20230212231026](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/V2Ray%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE%2420230212231026.png)

配置基本模式->DNS

![V2Ray搭建与访问$20230212231141](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/V2Ray%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE%2420230212231141.png)

配置基本模式->模式

![V2Ray搭建与访问$20230212231200](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/V2Ray%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE%2420230212231200.png)

配置完成。

## 常见问题

### 搭建完成无法访问

首先定位问题是客户端配置还是服务端配置问题。
可以在网上查找 免费的 v2ray 服务 临时使用测试客户端是否配置正确。
在 openwrt 下 passwall 下检查日志

![V2Ray搭建与访问$20230212232236](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/V2Ray%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE%2420230212232236.png)

发现日志中服务将数据进行了转发

![V2Ray搭建与访问$20230212232142](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/V2Ray%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE%2420230212232142.png)

而系统防火墙默认将转发关闭，尝试打开后重试。

![V2Ray搭建与访问$20230212232313](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/V2Ray%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE%2420230212232313.png)

一般来说，客户端出问题可能性较小。

定位到是服务端问题，尝试防火墙检查。

首先考虑服务端的防火墙是否屏蔽对应端口。

暴露端口段

```sh
firewall-cmd --permanent --add-port 8300-8400/tcp
```

或直接指定端口

```sh
firewall-cmd --permanent --add-port 1191/tcp
```

暴露后需要重启防火墙

```sh
firewall-cmd --reload
```

查看暴露的端口

```sh
firewall-cmd  --list-ports
# 8300-8400/tcp
```

在服务端通过 netstat 查看对应服务端口相关情况

```sh
netstat -anp | grep 1110
```

需要看到

```sh
tcp6       0      0 dist:1110     src:port      ESTABLISHED 7147/v2ray
```

双方才算建立了链接。若连接建立成功，无法访问，进一步检查错误日志。

```sh
v2ray log
```

若出现

```js
proxy/vmess/encoding: invalid user
```

考虑客户端服务端时间是否同步

查看当前服务器系统时间

```sh
date -R
```

若不一致，修改时间

```sh
date -s "2023-02-12 12:46:30"
```

可进一步通过时间同步服务 ntpdate 从时间服务器来自动更行系统时间
如果系统没有 ntpdate 命令,安装

```sh
yum -y install ntp
```

后续使用该命令同步时间即可。

若出现

```sh
environment variable v2ray.vmess.aead.forced = false
```

通过 whereis 找到 v2ray 配置文件位置

```sh
whereis v2ray
```

一般在/etc/v2ray 下。
修改目录下的 config.json 中的 alterId，改为 0

若将 v2ray 设置为了守护进程
则在`vi /etc/systemd/system/v2ray.service`
将

```jsx
ExecStart=/usr/bin/v2ray/v2ray -config /etc/v2ray/config.json
```

改为

```jsx
ExecStart=/usr/bin/env v2ray.vmess.aead.forced=false /usr/bin/v2ray/v2ray -config /etc/v2ray/config.json
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

文章链接：[http://www.skyline.show/V2Ray 搭建与访问.html](http://www.skyline.show/V2Ray搭建与访问.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

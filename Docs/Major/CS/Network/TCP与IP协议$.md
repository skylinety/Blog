# TCP 与 IP 协议

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [TCP 与 IP 协议](#tcp-与-ip-协议)
  - [TCP/IP 概述](#tcpip-概述)
  - [TCP/IP 网络模型](#tcpip-网络模型)
    - [常见网络模型](#常见网络模型)
    - [应用层](#应用层)
    - [传输层](#传输层)
    - [网络层](#网络层)
    - [物理层](#物理层)
  - [TCP](#tcp)
    - [TCP 数据分段](#tcp-数据分段)
    - [三次握手](#三次握手)
    - [四次挥手](#四次挥手)
    - [TCP 拥塞控制](#tcp-拥塞控制)
    - [TCP VS UDP](#tcp-vs-udp)
  - [IP](#ip)
    - [IP 地址](#ip-地址)
    - [子网掩码](#子网掩码)
    - [网关/路由](#网关路由)
    - [DHCP 服务器](#dhcp-服务器)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## TCP/IP 概述

TCP 和 IP 常被放在一起，即 TCP/IP 协议；
这是一套网络通信协议的集合，包含其他协议，以主要的 TCP/IP 来代表。
TCP/IP 是 Transmission Control Protocol/Internet Protocol 的简写。
TCP 用以定义数据格式、数据拆分组装、数据传输等。
IP 定义了地址格式使得数据能够在万千网络设备中传输到正确的地址。
一个简单的类比为手机通讯场景，
用 IP 来规定手机号，而通话信息传输等则归 TCP 管。

TCP/IP 采用的是 CS 模式（ client-server model ）。
TCP/IP 是无状态（stateless）的，即当前请求与上一请求无直接关联。
TCP/IP 协议使得网络通信可靠且在出现错误得以恢复。

常见基于 TCP/IP 协议的应用层协议有：

- HTTP
- HTTPS
- FTP

## TCP/IP 网络模型

### 常见网络模型

通常被提及的网络模型有 TCP/IP 模型 和 OSI(Open System Interconnect protocol suite)。
OSI 分为 7 层，仅提供理论，并未实际应用。
TCP/IP 网络模型通常分为 4 层。
![TCP与IP协议20221207144058](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/TCP%E4%B8%8EIP%E5%8D%8F%E8%AE%AE20221207144058.png)

### 应用层

应用层处于最顶层，其协议处理应用数据（Data）。
常见的应用层协议有，HTTP、SSH、SFTP、Telnet、DNS、BitTorrent 等。
通常情况下，通过 IP 地址可以定位设备，但同一设备可能有多个应用在同时接收数据。
故需要在 提供端口来定位接收数据的应用程序。
为了数据追踪能够到目标设备上正确的应用程序，不同的应用程序暴露不同的端口。
常见的应用层协议的默认端口如下：

| 协议  | 端口 |
| ----- | ---- |
| HTTP  | 80   |
| HTTPS | 443  |
| SSH   | 22   |

DNS 域名服务(Domain Name System)。
域名与 IP 地址之间是一一对应的，域名方便人使用，但机器之间只能互相认识 IP 地址。
域名与 IP 之间的对应关系不是固定的，IP 可能会变更，IP 与域名的转换工作称为域名解析。
域名解析需要由专门的域名解析服务器来完成，DNS 就是进行域名解析的服务器。
DNS 可简单类比成一个电话本，其也是应用层协议。

### 传输层

传输层将应用层的数据进行分块处理。
如 TCP 协议会将数据分割成 TCP Segments 报文段。
一个 TCP 段包含的应用层数据最大的长度为 1460 bytes，简称为 MSS(Maximum Segment Size)
这里的 MSS 不是限制 TCP 端的最大长度，限制的是包含应用层的数据长度，不包含 TCP 段头部
超过这个长度，TCP 会进行重新分段。
分块的好处是当出现数据丢失时，只需要重新传输丢失的块而不是全部重传。

### 网络层

网络层协议将传输层数据端进一步添加上地址相关信息进行装包，然后将数据包（Pockets）准确传输到对应地址。
一个数据包携带传输层数据的最大长度为 1500 bytes，简称为 MTU(Maximum Transmission Unit)
超过这个长度，IP 会进行重新分包。

### 物理层

物理层又称为链路层。
常见的物理层协议有 Ethernet（以太网）、WIFI、 ARP（Address Resolution Protocol）。

当数据来到路由时，如何确定目标 IP 是哪一台设备，这里就需要进行地址解析。
每一台物理设备都有一个独一无二的 MAC 地址，但是同一设备在接入不同网络时，IP 地址并不唯一。
FRP 地址解析协议简单来说可将 IP 与 MAC（Media Access Control，介质访问控制）地址进行映射解析。

Mac 地址共 48 位，前 24 位由 IEEE 的注册管理机构给不同厂家分配的唯一代码。
后 24 位是由厂家自己分配的，称为扩展标识符。
同一个厂家生产的网卡中 MAC 地址后 24 位是不同的。

## TCP

### TCP 数据分段

### 三次握手

### 四次挥手

### TCP 拥塞控制

### TCP VS UDP

UDP 与 TCP 同为传输层协议。
UDP 可简单理解为 TCP 的阉割版，其 只负责数据发包，不保证数据传输过程的可靠性。
TCP 是一套可靠数据传输协议。相比于 UDP，其增加了流量控制、超时重传、拥塞控制等机制，来保证数据传输可靠性。
TCP 的可靠并不是指数据一定会被对方接收到，她只提供可靠数据递送和不可传输时的可靠通知。
UDP 的优势在于其实时性好，传输效率高。

## IP

### IP 地址

常见的 IP 协议为 IPv4 和 IPv6 协议
目前 IPv4 地址接近耗尽，部分网站已提供 IPv6 支持。
IPv4 协议中，将 IP 地址分为 4 段，每段 8 位，共 32 位。

### 子网掩码

子网掩码用以确认 IP 的网络号与主机号。
子网掩码（IPv4）一共 32 位，前半部分为连续的 1，确认网络号，后半部分为连续的 0，确认主机号。
在寻址过程中，通过网络号确定是否在目标网络，再寻找对应主机。
类似场景较多，比如大学的学号，可以用前半部分规定班级；拨打电话时，加 028（成都） 的区号等。

常见的子网掩码
`255.255.255.0` 的二进制位

```js
11111111.11111111.11111111.00000000
```

`255.255.255.192` 的二进制为

```js
11111111.11111111.11111111.11000000
```

以 iphone 分享热点来说明，通过 Mac 连接热点，WIFI 相关信息如下：

![TCP与IP协议20221226161319](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/TCP%E4%B8%8EIP%E5%8D%8F%E8%AE%AE20221226161319.png)
`255.255.255.240` 的二进制为

```js
11111111.11111111.11111111.11110000
```

后 4 位为主机位。
网关 `172.20.10.1` 的二进制为

```js
10101100. 00010100. 00001010. 00000001
```

那么根据子网掩码规则

```js
10101100. 00010100. 00001010. 00000000
10101100. 00010100. 00001010. 00001111
```

在同一网段，
再转换为十进制为

```js
172.20.10.0
172.20.10.15
```

超过 15 就不在同一网段。

### 网关/路由

通过子网掩码判断两台主机是否处以同一网络。
同一网络直接通信，两个不同网络之间的通信，必须通过网关。
如果网络 A 中的主机发现数据包的目标主机不在本地网络中，就把数据包转发给它自己的网关，再由网关转发给网络 B 的网关，网络 B 的网关再转发给网络 B 的某个主机。
只有设置好网关的 IP 地址，TCP/IP 协议才能实现不同网络之间的相互通信。

### DHCP 服务器

DHCP 服务器可以在主机上线时自动为其分配子网掩码以及自动给设备分配 IP 地址，防止手动分配时冲突。

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

文章链接：[http://www.skyline.show/TCP 与 IP 协议.html](http://www.skyline.show/TCP与IP协议.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

# Shadowsocks 服务搭建与访问

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shadowsocks 服务搭建与访问](#shadowsocks-服务搭建与访问)
  - [SS server](#ss-server)
    - [安装](#安装)
    - [配置文件](#配置文件)
    - [开启服务](#开启服务)
  - [SS client](#ss-client)
  - [常见问题](#常见问题)
    - [配置完成无法访问墙外](#配置完成无法访问墙外)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## SS server

### 安装

SS server 服务端有多语言版本支持
此处采用 python 版本
首先安装 pip 包管理器

Debian / Ubuntu

```shell
apt-get install python-pip
```

CentOS

```shell
sudo yum install epel-release # 添加Enterprise Linux企业源
sudo yum install python-pip
```

查看是否安装成功

```shell
pip --version
# pip 8.1.2 from /usr/lib/python2.7/site-packages (python 2.7)
```

然后直接输入以下命令安装

```python
sudo pip install shadowsocks
```

### 配置文件

新增配置文件
`/etc/shadowsocks.json`

```json
{
  "server": "23.234.212.12",
  "port_password": {
    "8388": "123",
    "8389": "456"
  },
  "timeout": 300,
  "method": "rc4-md5",
  "fast_open": false,
  "workers": 1
}
```

| 参数          | 含义               |
| ------------- | ------------------ |
| server        | vps ip 地址        |
| port_password | 服务端口和对应密码 |
| method        | 加密方法           |
| workers       | 线程数             |

### 开启服务

调用命令开启服务。
相关命令如下

- 指定配置文件开启服务

```shell
sudo ssserver -c /etc/shadowsocks.json -d start
```

- 指定配置文件重启

```shell
sudo ssserver -c /etc/shadowsocks.json -d restart
```

- 关闭服务

```shell
sudo ssserver -d stop
```

### 开机启动

```shell
vi /etc/rc.local
```

然后将开启服务的命令添加进去即可。

```shell
ssserver -c /etc/shadowsocks.json -d start

```

## SS client

在如下位置新增服务配置
![Shadowsocks服务搭建与访问20211210170145](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shadowsocks%E6%9C%8D%E5%8A%A1%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE20211210170145.png)
与服务端配置对应
![Shadowsocks服务搭建与访问20211210170258](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shadowsocks%E6%9C%8D%E5%8A%A1%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE20211210170258.png)
选择全局或者 PAC 模式，浏览器输入科学上网网址即可

## 常见问题

### 配置完成无法访问墙外

- IP 检查

检查 vps ip 是否被封
在http://ping.pe/下输入ip

异常情况
![Shadowsocks服务搭建与访问20211210170940](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shadowsocks%E6%9C%8D%E5%8A%A1%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE20211210170940.png)
正常情况下面部分为绿色
![Shadowsocks服务搭建与访问20211210171222](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shadowsocks%E6%9C%8D%E5%8A%A1%E6%90%AD%E5%BB%BA%E4%B8%8E%E8%AE%BF%E9%97%AE20211210171222.png)

ip 异常需要向 vps 提供商发起工单。

- 防火墙检查

若 ip 正常，检查 vps 防火墙。
CentOS7 等版本默认防火墙非常严格，一般端口都屏蔽都外部访问。
关闭防火墙测试是否能访问
centos7 关闭防火墙使用如下命令

```shell
sudo systemctl stop firewalld
```

检查是否可正常访问。
若是防火墙问题，暴露对应端口即可，不要关闭防火墙。

打开防火墙的命令

```shell
sudo systemctl start firewalld
```

暴露端口段

```shell
firewall-cmd --permanent --add-port 8300-8400/tcp
```

或直接指定端口

```shell
firewall-cmd --permanent --add-port 1191/tcp
```

暴露后需要重启防火墙

```shell
firewall-cmd --reload
```

查看暴露的端口

```shell
firewall-cmd  --list-ports
# 8300-8400/tcp
```

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

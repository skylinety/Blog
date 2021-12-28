# CentOS 防火墙

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CentOS 防火墙](#centos-防火墙)
  - [firewalld](#firewalld1)
    - [firewalld 基本理念](#firewalld-基本理念)
    - [Firewalld Zones](#firewalld-zones)
    - [Firewalld services](#firewalld-services)
    - [设置生效时长](#设置生效时长)
    - [查看防火墙状态](#查看防火墙状态)
    - [关闭防火墙](#关闭防火墙)
    - [打开防火墙](#打开防火墙)
    - [暴露端口](#暴露端口)
    - [查看暴露的端口](#查看暴露的端口)
    - [允许暴露端口的服务](#允许暴露端口的服务)

<!-- /code_chunk_output -->

## firewalld[^1]

### firewalld 基本理念

firewalld 采用区域与服务的概念来控制流量的出入。
* zones
* services

firewalld 是 CentOS 7/8, Red Hat Enterprise Linux 7 (RHEL 7), Fedora 18+等 Linux 发行版本默认防火墙程序。
其命令行工具为 firewall-cmd

### Firewalld Zones
zones预设级别不同的防火墙策略，用户可以自定义zones，也可以使用预设的zones。
默认使用 public zone
根据拦截级别严格程度，预设zones如下
zone | 拦截说明
--- | ---
drop | 丢弃区，所有接入连接都会进行无消息响应拦截，只有输出连接被允许。
block | 拦截区，接入连接都会被拦截，会响应icmp-host-prohibited等拦截消息，只有输出连接被允许。
public | 公共区，用于不受信任的公共区域，仅允许自选接入连接，默认允许 ssh 和 dhcpv6-client
external | 外部区，用于外部网络，系统充当网关角色，仅允许自选接入连接，默认允许ssh
internal | 内部区，用于内部网络，系统充当网关角色，仅允许自选接入连接
dmz |  隔离区，demilitarized zone（隔离区，军事缓冲区），用于允许部分服务被外网访问，仅允许自选接入连接
work | 工作区，用于工作网络，信任网络中其他机器，仅允许自选接入连接，默认允许 ssh，ipp-client 和 dhcpv6-client
home | 家庭区，用于工作家庭网络，信任网络中其他机器，仅允许自选接入连接，默认允许ssh，ipp-client，mdns，samba-client 和 dhcpv6-client
trusted | 信任区，并接受所有网络连接

新建防火墙区域策略
```shell
sudo firewall-cmd --new-zone=memcached --permanent
```
查看系统默认区
```shell
sudo firewall-cmd --get-default-zone
# public
```
调整系统默认区
```shell
sudo firewall-cmd --set-default-zone=home
```
系统中配置的所有区
```shell
sudo firewall-cmd --get-zones
# block dmz drop external home internal public trusted work
```
```shell
sudo firewall-cmd --list-all-zones
# 上述命令会打印所有区与其详细的配置，输出内容较长
```

查看系统使用区
```shell
sudo firewall-cmd --get-active-zones
# public
#   interfaces: eth0 eth1
```

查看指定区的详细配置
```shell
sudo firewall-cmd --zone=public --list-all
# public (active)
#   target: default
#   icmp-block-inversion: no
#   interfaces: eth0 eth1
#   sources:
#   services: ssh dhcpv6-client
#   ports:
#   protocols:
#   masquerade: no
#   forward-ports:
#   source-ports:
#   icmp-blocks:
#   rich rules:
```
### Firewalld services
services 在zones中为不同的服务预设不同的配置。
例如，可以为服务提供不同的端口等配置

查看所有的服务
```shell
 sudo firewall-cmd --get-services
# RH-Satellite-6 RH-Satellite-6-capsule amanda-client amanda-k5-client amqp amqps... git... ssh ...dhcpv6-client
```
查看当前开放的服务
```shell
 sudo firewall-cmd --list-services
# dhcpv6-client ssh
```
增加开放服务
```shell
sudo firewall-cmd --zone=public --add-service=http
```
移除开放的服务
```shell
sudo firewall-cmd --zone=public --remove-service=http
# 永久配置需要添加 --permanent后缀
```

所有服务的配置都在/usr/lib/firewalld/services目录下
例如http服务的配置为
```xml
<?xml version="1.0" encoding="utf-8"?>
<service>
  <short>WWW (HTTP)</short>
  <description>HTTP is the protocol used to serve Web pages. If you plan to make your Web server publicly available, enable this option. This option is not required for viewing pages locally or developing Web pages.</description>
  <port protocol="tcp" port="80"/>
</service>
```

自定义服务
```shell
sudo cp /usr/lib/firewalld/services/ssh.xml /etc/firewalld/services/diyservice.xml
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<service version="1.0">
<short>diyservice</short>
<description>Plex is a streaming media server that brings all your video, music and photo collections together and stream them to your devices at anytime and from anywhere.</description>
<port protocol="udp" port="1900"/>
<port protocol="tcp" port="32400"/>
</service>
```
重启防火墙后就可以看到该服务。

### 配置的有效期

Firewalld 提供运行时与永久两种配置有效期限。
* runtime
* permanent
runtime 只有当次开机有效，重启会恢复到默认配置，permanent会让配置永久生效。
默认指定防火墙相关配置时使用的是runtime。
要让指定的配置永久有效，需要指定 --permanent 

```shell
sudo firewall-cmd <options>
```
上述配置生效后只在runtime有效
要使其永久有效
```shell
sudo firewall-cmd --permanent <options>
```
使当前runtime的所有配置永久有效
```shell
sudo firewall-cmd --runtime-to-permanent
```
要让配置立即生效，需要重启进程
```shell
sudo firewall-cmd --reload
```
### 查看防火墙状态

```shell
firewall-cmd --state
```

输出

```shell
running #打开状态
not running #关闭状态
```

完整信息

```shell
firewall-cmd --list-all
```

输出

```shell
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: eth0
  sources:
  services: dhcpv6-client ssh
  ports:
  protocols:
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:

```

### 关闭防火墙

- 临时关闭

```shell
sudo systemctl stop firewalld
```

只对当前运行时有效

- 永久关闭

1. 关闭防火墙

```shell
sudo systemctl stop firewalld
```

2. 防止开机重启

```shell
sudo systemctl disable firewalld
```

输出

```shell
Removed symlink /etc/systemd/system/multi-user.target.wants/firewalld.service.
Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.

```

3. 防止其他程序启动防火墙

```shell
sudo systemctl mask --now firewalld
```

输出

```shell
Created symlink from /etc/systemd/system/firewalld.service to /dev/null.
```

### 打开防火墙

```shell
sudo systemctl start firewalld
```

### 暴露端口

暴露端口段

```shell
firewall-cmd --permanent --add-port 8300-8400/tcp
```
协议可选tcp, udp, sctp, or dccp

暴露端口

```shell
firewall-cmd --permanent --add-port 1191/tcp
```

临时暴露需要去除 `--permanent`，重启后端口暴露将会失效。
执行暴露端口的命令后，需要重启防火墙

```shell
firewall-cmd --reload
```

### 查看暴露的端口

```shell
firewall-cmd  --list-ports
# 8300-8400/tcp
```

移除暴露的端口

```shell
firewall-cmd --remove-port 8300-8400/tcp --permanent
```

注意开启时添加了`--permanent`，关闭时也需要

### 允许暴露端口的服务

```shell
sudo firewall-cmd --list-services
# ssh dhcpv6-client http
```
### 指定允许访问的IP
```shell
sudo firewall-cmd --zone=public --add-source=192.168.100.30/32 --permanent
# sudo firewall-cmd --add-source=192.168.100.30 --permanent
```
### 查看允许访问的IP
```shell
sudo firewall-cmd --zone=public --list-sources
```
### 移除指定的IP
```shell
sudo firewall-cmd --zone=public --remove-source=192.168.1.10
```
### 转发
在进行转发前，需要开启转发支持
```shell
sudo firewall-cmd --zone=external --add-masquerade --permanent
```

同主机
```shell
sudo firewall-cmd --zone=external --add-forward-port=port=80:proto=tcp:toport=8080
```
上述命令会把80端口的tcp全部转发到当前服务器的8080端口

转发到其他主机
```shell
sudo firewall-cmd --zone=external --add-forward-port=port=80:proto=tcp:toaddr=10.10.10.2
```
上述命令会把80端口的tcp全部转发到服务器10.10.10.2的80端口
[^1]: 本节命令在 centos7 下验证

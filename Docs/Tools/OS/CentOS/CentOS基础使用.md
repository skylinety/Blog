# CentOS 基础使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CentOS 基础使用](#centos-基础使用)
  - [防火墙](#防火墙1)
    - [查看防火墙状态](#查看防火墙状态)
    - [关闭防火墙](#关闭防火墙)
    - [打开防火墙](#打开防火墙)
    - [暴露端口](#暴露端口)
    - [查看暴露的端口](#查看暴露的端口)

<!-- /code_chunk_output -->

## 防火墙[^1]

### firewalld 简介

firewalld 是 CentOS 7, Red Hat Enterprise Linux 7 (RHEL 7), Fedora 18+等 Linux 发行版本默认防火墙程序。
其命令行工具为 firewall-cmd

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

[^1]: 本节命令在 centos7 下验证

# 利用systemd开启后台进程
## 简介
systemd 是Linux中系统与服务管的系列套件，其中d沿用传统指代daemon。
systemd提供多个命令行工具，最基本的位systemctl
systemd体系庞大，提供繁杂的功能，其中一个常用的功能就是开启后台服务。

### 创建新服务
创建服务文件并打开
vi /etc/systemd/system/foo.service

输入以下内容

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

* Unit
提供服务基础信息
Description为描述信息
After
服务启动的前置条件

* Service
提供启动服务的相关信息
* Install
WantedBy
> Defines which service triggers the custom service if enabled with systemctl enable. This is mostly used for starting the custom service on boot. In this example, foo.service uses multi-user.target, which starts foo.service when systemd loads multi-user.target on boot.
定义服务被谁触发

### 开启服务
创建该服务后，需要重载systemd服务文件
systemctl daemon-reload
开启该服务
systemctl start foo

查看该服务运行状态
systemctl status foo

## 服务操作汇总
开启服务
systemctl start foo

关闭服务
systemctl stop foo

重启服务
systemctl restart foo

服务状态
systemctl status foo

开机自启动服务
systemctl enable foo

禁止开机启动
systemctl disable foo

查看是否允许开机启动
systemctl is-enabled foo


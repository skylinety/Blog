# frp内网穿透

## 简介
frp是一款开源的内网穿透软件，github主页为：https://github.com/fatedier/frp
其架构如下图所示：
![20220117182759](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/20220117182759.png)

## Server端
### 下载包
在Release 页面下载服务器CPU架构对应的版本 https://github.com/fatedier/frp/releases
如果不知道，可以通过lscpu命令查看，一般为arm_64位或X86_64位。
![20220117185544](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/20220117185544.png)
确定后通过 weget命令下载。如X86_64对应下载为
weget https://github.com/fatedier/frp/releases/download/v0.38.0/frp_0.38.0_freebsd_amd64.tar.gz
也可下载到本地后通过SecureCRT等工具上传.

下载成功后通过
tar -zxvf frp_0.38.0_linux_amd64.tar.gz 
解压成功后
打开目录下的frps.ini文件，修改如下
[common]
bind_port = 7000
token = mima

尝试启动服务
./frps -c frps.ini 
成功一般有success提示信息，如果遇到Segmentation fault错误，检查下载的包版本是否有错。
### 后台启动服务

touch /etc/systemd/system/frp.service

输入frp.service内容如下：
[Unit]
Description=FRP service
After=network.target syslog.target
Wants=network.target

[Service]
ExecStart=/root/apps/frp/frps -c /root/apps/frp/frps.ini
Restart=always
User=root

[Install]
WantedBy=multi-user.target

重置守护进程服务
systemctl daemon-reload 

开启服务
 systemctl start frp 

查看服务是否开启成功，查看7000端口是否开启服务即可。
netstat -anp | grep 7000

注意，此处需要在服务器提供网站对应的配置处将7000端口的防火墙限制打开，centos等系统下，注意firewalld是否开放防火墙端口。

## Client端

Client端此处采用Docker方式。
将下载的frpc.ini 放在Docker宿主机本地
![20220117194957](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/20220117194957.png)
frpc.ini 内容修改如下：

[common]
server_addr = 42.113.1.102
server_port = 7000
token = mima

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6000

[DSM]
type = tcp
local_ip = 127.0.0.1
local_port = 5000
remote_port = 5000

如上配置后，我们可以通过42.113.1.102:5000来进入群晖，通过42.113.1.102:22进入群晖后台。
添加docker镜像
![20220117195517](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/20220117195517.png)
地址如下：
https://hub.docker.com/r/chenhw2/frp
双击镜像，做如下修改
![20220117195707](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/20220117195707.png)


![20220117195946](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/20220117195946.png)

![20220117200053](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/20220117200053.png)

在进行如上三处修改后应用退出。

启动容器
![20220117200151](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/20220117200151.png)

外网环境在浏览器输入42.113.1.102:5000
来到群晖登录页即穿透成功。
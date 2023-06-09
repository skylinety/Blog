# DNS 域名解析

## DNS
DNS 即Domain Name System 。
IP地址反应特定时刻计算机设备在网络中的唯一标识，
但IP地址不便记忆且不能反应对应公司或组织的特性与名称。
DNS将浏览器便于人类阅读与记忆的域名解析成机器能够理解的 IP 地址。
简单地说就是做域名和IP的映射。
DNS协议使用53端口，属于应用层协议，数据可使用TCP和UDP(多数情况)传输。

## 本地解析

### 浏览器缓存
本地域名解析，首先去查询浏览器缓存，如果有缓存，则直接拿到缓存的IP地址。
可以在chrome浏览器地址栏输入
```sh
chrome://net-internals/#dns
```
来查询对应网站是否有浏览器缓存的域名解析地址。


### 操作系统缓存
浏览器缓存未找到对应缓存时，查找操作系统缓存。

查看操作系统DNS缓存，
通过如下命令
mac
```sh
nslookup qq.com 
```
windows
```sh
ipconfig /displaydns
```

### host文件
操作系统缓存未找到对应缓存时，查找电脑host文件
Windows 的host文件路径如下
```sh
C:\Windows\System32\drivers\etc\hosts
```
Linux 和 Mac 的host文件路径如下

```sh
/etc/hosts
```
一个Host文件内容如下
```sh
127.0.0.1       localhost
::1             localhost
# GitHub Start
151.101.184.133 assets-cdn.github.com
# GitHub End
```

在电脑本地的解析大致会经过如上三个过程，
![DNS域名解析$20230506155327](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/DNS%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90%2420230506155327.png)
另外，电脑本地的解析未找到缓存时，在本地网络，还会去问路由器缓存。
当这些情况都未找到对应的IP，进入互联网解析阶段。

## 互联网域名服务器解析


### 域名服务器解析

![DNS域名解析$20230506161306](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/DNS%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90%2420230506161306.png)

### 域名递归与迭代解析



### 
    ISP缓存
    ｜ DNS劫持
    根服务器
    ｜ www.skyline.show
        迭代查询
            匹配到.show一级域名服务器
            ｜ ▷首先，匹配到.show一级域名服务器，请求转发到.show域名服务器。
            匹配到skyline的二级域名服务器
            ｜ ▷然后，匹配到.yangoogle的二级域名服务器，请求接着转发到.yangoogle服务器。
            匹配到test这个三级域名的ip地址
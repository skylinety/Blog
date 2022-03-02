# MacOS 常见问题汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

## "You do not have permission to open the application" in Big Sur

` brew install upx`
`sudo upx -d /Applications/my_app.app/Contents/MacOS/my_app`

## 无法打开“XXXX”,因为 Apple 无法检查其是否包含恶意软件

sudo spctl --master-disable

## mac wifi 链接失败，图标出现感叹号

这是由于 ip 地址未分配或分配错误导致，一般情况下，在配置中进行手动配置 Ipv4 与 DNS 即可
IPv4
IPv4 地址可多尝试修改末尾数字。不同路由网关（Router）配置可能路由不同，家用网络可能为 192.168.1.1，192.168.0.1，其他可能以 10 等开头

![MacOS常见问题汇总79D5340FB869E40EA854EE0A467D7CE6](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/MacOS%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BB79D5340FB869E40EA854EE0A467D7CE6.jpg)

DNS
DNS 可选 8.8.8.8 或 114.114.114.114 等

![MacOS常见问题汇总AEE2809B2227E6A3775504783CD7845A](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/MacOS%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BBAEE2809B2227E6A3775504783CD7845A.jpg)

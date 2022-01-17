## 其他
### brook
* server
```shell
curl -L https://github.com/txthinking/brook/releases/latest/download/brook_linux_amd64 -o /usr/bin/brook
chmod +x /usr/bin/brook
brook server --listen :9999 --password hello
```
* client
https://txthinking.github.io/brook/#/install-gui-client


vi /etc/systemd/system/brook.service


[Unit]
Description=brook vpn

[Service]
ExecStart=/usr/bin/brook server --listen :9991 --password liuzxcvbnm...
Restart=always
User=root

[Install]
WantedBy=multi-user.target

要开启多个服务，只需要创建多个service文件监听不同端口即可。
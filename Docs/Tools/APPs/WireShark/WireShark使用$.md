# WireShark 使用

## 安装

WireShark 开源，直接官网[下载](https://www.wireshark.org/#download)
下载完成后双击，在 Mac 下直接拖动对应 app 文件到应用目录。
同时双击安装 Install ChmodBPF.pkg
![WireShark使用$20230105142430](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/WireShark%E4%BD%BF%E7%94%A8%2420230105142430.png)

## 常见错误

### 双击对应网卡后无法捕获网络请求

通常报错为
`The capture session could not be initiated on capture device "en0"`
报错弹窗如下
![WireShark使用$20230105142245](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/WireShark%E4%BD%BF%E7%94%A8%2420230105142245.png)

首先检查是否安装过程中是否安装 ChmodBPF
Read me first 文档已说明，不安装无法获取权限

> In order to be able to capture packets, install the Install ChmodBPF package

若安装后重新尝试仍旧出现上述报错弹窗，
进一步检查 bpf 权限

```sh
ls -lh /dev/bpf*
crw-rw-r--  1 root  wheel  0x17000000 Jan  5 09:07 /dev/bpf0
crw-rw-r--  1 root  wheel  0x17000001 Jan  5 09:47 /dev/bpf1
crw-rw-r--  1 root  wheel  0x17000002 Jan  5 09:47 /dev/bpf2
crw-rw-r--  1 root  wheel  0x17000003 Jan  5 09:07 /dev/bpf3
```

若不是上述权限，尝试执行如下命令

```sh
sudo chmod u+rw,g+rw,o+r /dev/bpf*
```

上述命令执行后一般本次开机就可以正常执行，但是开机后权限会重置，查阅资料初步估计为/dev/bpf 实际是挂载在内存中的文件，故重启后更改不再生效。
解决方案多种，
MacOS 下可以添加一个打开 WireShark 时自动执行该脚本的捷径 Shortcuts;
其他系统同理，可以将该脚本写入开机执行或打开 APP 时执行。

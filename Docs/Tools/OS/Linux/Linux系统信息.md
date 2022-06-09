# Linux 系统信息

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Linux 系统信息](#linux-系统信息)
  - [系统信息](#系统信息)
    - [uname](#uname)
    - [lshw](#lshw)
  - [CPU](#cpu)
  - [硬盘](#硬盘)
    - [df](#df)
    - [du](#du)
    - [diskutil](#diskutil)
    - [lsblk](#lsblk)
    - [fdisk](#fdisk)
  - [USB](#usb)
  - [PCI](#pci)
  - [内存](#内存)

<!-- /code_chunk_output -->

## 系统信息

### uname

查看系统版本信息，使用 uname 命令
uname 直接使用时，显示系统内核名。
显示完整系统信息

```sh
uname -a
```

### lshw

lshw 即 list hardware 可以查看 cpu, disks, memory, usb controllers 等相关信息，一般需要 sudo 权限

直接使用该命令查看展示内容比较繁杂
![Linux系统信息20220315224550](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Linux%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF20220315224550.png)
添加 short 参数来显示扼要信息

```sh
sudo lshw -short
```

![Linux系统信息20220315224854](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Linux%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF20220315224854.png)

## CPU

查看 CPU 信息采用 lscpu 命令
![Linux系统信息20220315230624](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Linux%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF20220315230624.png)

## 硬盘

### df

即 disk usage information，展示系统中各分区可用空间。
![Linux系统信息20220316160957](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Linux%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF20220316160957.png)

### du

即 disk usage，分析计算指定目录对应的硬盘空间使用情况。

```sh
 du -hd 0 ./*
#   du -h -d 0 ./*
```

![Linux系统信息20220316020230](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Linux%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF20220316020230.png)
参数解析
-h 可读化展示
-d 指定分析的目录层级，后接数字，部分系统下必接数字，部分系统不接默认为 0
-a 列出指定目录下所有文件与层级目录
-s 只列出指定目录的大小
--exclud 排除指定目录，如--exclude=./node_modules

![Linux系统信息20220316161537](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Linux%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF20220316161537.png)

### diskutil

在 MacOS 下使用 diskutil 管理硬盘，查看硬盘信息命令如下

```sh
diskutil list
```

### lsblk

即 list block devices，包括硬盘，闪存等。
![Linux系统信息20220315231451](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Linux%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF20220315231451.png)

### fdisk

fdisk 主要用于修改系统分区，在 linux 下加-l 参数也可用来查看硬盘分区信息。

```sh
fdisk -l
```

![Linux系统信息20220316005447](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Linux%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF20220316005447.png)
在 MacOS 下，不支持-l 参数

## USB

通过 lsusb 查看 USB 连接设备信息。

## PCI

通过 lspci 查看 PCI 连接设备信息。可能包含图形卡、网卡、USB 等设备。
![Linux系统信息20220315232209](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Linux%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF20220315232209.png)

## 内存

free 来查看内存空间使用情况，包括交换空间
![Linux系统信息20220316160521](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Linux%E7%B3%BB%E7%BB%9F%E4%BF%A1%E6%81%AF20220316160521.png)

# MacOS 基础使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [MacOS 基础使用](#macos-基础使用)
  - [Macos Beta 系统更新开启](#macos-beta-系统更新开启)
  - [网络磁盘映射](#网络磁盘映射)
  - [剪切（移动）](#剪切移动)
    - [常规](#常规)
    - [快捷键](#快捷键)
  - [直接删除文件](#直接删除文件)
  - [修改终端用户名](#修改终端用户名)
  - [启用 SSD 的 TRIM 支持](#启用-ssd-的-trim-支持)
  - [关闭 SIP](#关闭-sip)
  - [设定文件默认打开方式](#设定文件默认打开方式)
    - [单文件](#单文件)
    - [同类文件](#同类文件)
  - [打开允许未知来源 app 选项](#打开允许未知来源-app-选项)
  - [设定快捷打开程序快捷键](#设定快捷打开程序快捷键)
    - [设置 automator 任务](#设置-automator-任务)
    - [设置程序打开快捷键](#设置程序打开快捷键)
  - [关闭 spotlight 索引](#关闭-spotlight-索引)
  - [MacOS 命令行定时开关机](#macos-命令行定时开关机)
  - [禁止APP重启时打开原来文件](#禁止app重启时打开原来文件)

<!-- /code_chunk_output -->

## Macos Beta 系统更新开启

在 apple beta 地址上登录
https://beta.apple.com

在如下网站下载 [MacOS Public Beta Access Utility](https://beta.apple.com/sp/betaprogram/enroll#macos)工具
注意开启前在 Time Mechine 中进行系统备份
下载工具安装后即可开启。

## 网络磁盘映射

在 finder 下操作 ⌘ + k
在弹出框中输入网络共享服务地址
![MacOS基本操作20211227153214](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/MacOS%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C20211227153214.png)
一般有 Samba 或 AFP 等方式共享服务
常见地址如下

```sh
afp://192.168.2.20
smb://192.168.2.20
```

## 剪切（移动）

### 常规

复制需要移动的文件。
在目标位置右击鼠标，一般出现粘贴项目选项。
![Macos基本操作20211118165151](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C20211118165151.png)
此时按住 ⌥ 键，菜单会变为将项目移动到此处。
![Macos基本操作20211118165216](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C20211118165216.png)

### 快捷键

```sh
⌘ + c
⌘ + ⌥ + v
```

⌘ + c 复制文件
在目标目录 ⌘ + ⌥ + v 即可移动成功

## 直接删除文件

放进垃圾桶
【Command】+【Backspace】/【Delete】
永久删除
【Option】+【Command】+【Backspace】/【Delete】

## 修改终端用户名

修改前图示

![Macos基本操作E77BBFF51DF4A64E8C6FA24BFEF8D2AF](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9CE77BBFF51DF4A64E8C6FA24BFEF8D2AF.jpg)

输入
`sudo scutil --set HostName <name>`
改后图示
![Macos基本操作F5C2146E34383DB6E8EE91DC7AD8EC82](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9CF5C2146E34383DB6E8EE91DC7AD8EC82.jpg)

## 启用 SSD 的 TRIM 支持

mac 更换非官方固态和默认不启动 TRIM 硬盘优化，可输入
`sudo trimforce enable`
打开

## 关闭 SIP

mac 关闭系统完整性保护 System Integrity Protection
重启时，出现 apple logo 时按住
`⌘+R`
进入恢复模式
点击工具中的终端
输入
`csrutil disable`
输出
Successfully disabled System Integrity Protection. Please restart the machine for the changes to take effect.
表示关闭 SIP 成功
开启命令为
`csrutil enable`

## 设定文件默认打开方式

### 单文件

按住 option 键，鼠标右击，查看菜单栏变化
这种方式只会更改当前文件的打开方式，不会修改所有同后缀文件。

### 同类文件

第一步：右键单击该文件，然后选择「显示简介」选项。
第二步：找到「打开方式」项目，点击倒三角选择你想指定的默认应用程序。
第三步：单击「全部更改」按钮即可生效
![MacOS基本操作20211215113806](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/MacOS%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C20211215113806.png)

## 打开允许未知来源 app 选项

`sudo spctl --master-disable`

![Macos基本操作20211118165525](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C20211118165525.png)

## 设定快捷打开程序快捷键

### 设置 automator 任务

如下动态图所示

![Macos基本操作4DE1B15BC1EABA0DAE13F68FF436371B](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C4DE1B15BC1EABA0DAE13F68FF436371B.gif)

### 设置程序打开快捷键

![Macos基本操作3B838E4C4D5B3D48BED0B7FB2AE51847](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C3B838E4C4D5B3D48BED0B7FB2AE51847.jpg)

## 关闭 spotlight 索引

关闭索引

```sh
sudo mdutil -a -i off
```

关闭索引后不再索引数据卷上的新增内容，不会清除已建立索引，不会停用 Spotlight。

打开索引

```sh
sudo mdutil -a -i on
```

重建索引

```sh
sudo mdutil -a -E
```

关闭所有索引命令（待核实）

```sh
sudo mdutil -a -d
```

## MacOS 命令行定时开关机

原系统提供操作入口
![MacOS基本操作20240110180504](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/MacOS基本操作20240110180504.png)
更新macOS14后入口已被关闭
通过终端可执行如下命令

查看当前的定时开关任务

```sh
pmset -g sched
```

清除当前的任务

```sh
sudo pmset repeat cancel
```

工作日定时开机

```sh
sudo pmset repeat wakeorpoweron MTWRF 09:05:00
```

指定时间开机

```sh
sudo pmset schedule wakeorpoweron "03/01/23 07:00:00"
```

工作日定时关机

```sh
sudo pmset repeat shutdown MTWRF 19:00:00
```

指定时间关机

```sh
sudo pmset schedule shutdown "04/01/23 00:00:00​​​​​​​"
```

工作日定时重启

```sh
sudo pmset repeat restart MTWRFSU 00:00:00
```

日期规则
星期 | 字母
--|--
Monday | M
Tuesday | T
Wednesday | W
Thursday | R
Friday | F
Saturday | S
Sunday | U

日期格式MM/DD/YY, 时间格式HH:MM:SS 2024年1月10日 `1/10/24 07:00:00`

## 禁止APP重启时打开原来文件
设定全部程序，打开Close windows when quitting an application即可
![MacOS基本操作20240202102436](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/MacOS基本操作20240202102436.png)
上述方法部分程序不生效。
设定特定程序
```sh
# defaults write com."producer"."program-name" ApplePersistenceIgnoreState YES
defaults write com.apple.Preview ApplePersistenceIgnoreState YES
```

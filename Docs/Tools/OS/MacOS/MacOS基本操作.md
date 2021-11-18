# MacOS 基础使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [MacOS 基础使用](#macos-基础使用)
  - [剪切（移动）](#剪切移动)
    - [常规](#常规)
    - [快捷键](#快捷键)
  - [直接删除文件](#直接删除文件)
  - [修改终端用户名](#修改终端用户名)
  - [启用 SSD 的 TRIM 支持](#启用-ssd-的-trim-支持)
  - [关闭 SIP](#关闭-sip)
  - [设定文件默认打开方式](#设定文件默认打开方式)
    - [常规](#常规-1)
    - [其他方式](#其他方式)
  - [打开允许未知来源 app 选项](#打开允许未知来源-app-选项)
  - [设定快捷打开程序快捷键](#设定快捷打开程序快捷键)
    - [设置 automator 任务](#设置-automator-任务)
    - [设置程序打开快捷键](#设置程序打开快捷键)

<!-- /code_chunk_output -->

## 剪切（移动）

### 常规

复制需要移动的文件。
在目标位置右击鼠标，一般出现粘贴项目选项。
![Macos基本操作20211118165151](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C20211118165151.png)
此时按住 ⌥ 键，菜单会变为将项目移动到此处。
![Macos基本操作20211118165216](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C20211118165216.png)

### 快捷键

```shell
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

### 常规

按住 option 键，鼠标右击，查看菜单栏变化

### 其他方式

第一步：右键单击该文件，然后选择「显示简介」选项。
第二步：找到「打开方式」项目，点击倒三角选择你想指定的默认应用程序。
第三步：单击「全部更改」按钮即可生效

## 打开允许未知来源 app 选项

`sudo spctl --master-disable`

![Macos基本操作20211118165525](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C20211118165525.png)

## 设定快捷打开程序快捷键

### 设置 automator 任务

如下动态图所示

![Macos基本操作4DE1B15BC1EABA0DAE13F68FF436371B](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C4DE1B15BC1EABA0DAE13F68FF436371B.gif)

### 设置程序打开快捷键

![Macos基本操作3B838E4C4D5B3D48BED0B7FB2AE51847](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Macos%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C3B838E4C4D5B3D48BED0B7FB2AE51847.jpg)

# VIM 基本使用

## 模式

### 正常模式 (Normal-mode)

正常模式一般用于浏览文件，同时包括一些复制、粘贴、删除等快捷操作。
其他模式通常通过 ESC 键返回正常模式。

### 插入模式 (Insert-mode)

用于编辑文档，直接输入内容。

### 命令模式 (Command-mode)

输入:或/进入命令模式
命令模式用于执行 VIM 提供的相关指令。

### 可视模式 (Visual-mode)

在正常模式按下 v, V, <Ctrl>+v，可以进入可视模式
可视模式下执行文本选择操作。

## .vimrc

### inoremap

按键映射

```shell
inoremap zz

```

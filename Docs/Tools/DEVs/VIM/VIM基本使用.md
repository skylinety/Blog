# VIM 基本使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [VIM 基本使用](#vim-基本使用)
  - [模式](#模式)
    - [正常模式 (Normal-mode)](#正常模式-normal-mode)
    - [插入模式 (Insert-mode)](#插入模式-insert-mode)
    - [命令模式 (Command-mode)](#命令模式-command-mode)
    - [可视模式 (Visual-mode)](#可视模式-visual-mode)
  - [.vimrc](#vimrc)
    - [inoremap](#inoremap)

<!-- /code_chunk_output -->

## 模式

### 正常模式 (Normal-mode)

正常模式一般用于浏览文件，同时包括一些复制、粘贴、删除等快捷操作。
其他模式通常通过 ESC 键返回正常模式。

| 操作 | 按键 | EN   |
| ---- | ---- | ---- |
| 撤销 | u    | undo |

### 插入模式 (Insert-mode)

可理解为编辑模式，
用于编辑文档，直接输入内容。

- 删除

| 输入         | 含义                          | 示例    |
| ------------ | ----------------------------- | ------- |
| x            | 删除光标所在处字符            | -       |
| X            | 删除光标所在前字符（大写 X ） | -       |
| dw           | 删除到下一个单词开头          | -       |
| de           | 删除到本单词末尾              | -       |
| dE           | 删除到本单词末尾包括标点在内  | -       |
| db           | 删除到前一个单词              | -       |
| dB           | 删除到前一个单词包括标点在内  | -       |
| dd           | 删除一整行                    | -       |
| D d$         | 删除光标位置到本行结尾        | -       |
| d0           | 删除光标位置到本行开头        | -       |
| :[number],.d | 删除到光标所在行              | :[9],.d |

### 命令模式 (Command-mode)

输入:或/进入命令模式
命令模式用于执行 VIM 提供的相关指令。

| 命令 | 按键 | EN   |
| ---- | ---- | ---- |
| 移动 | :m   | move |
| 设定 | :set |      |

**:m**
:m 多用于换行操作，当前行的位置为 0.具体使用如下

- :m -2 移动到-2 行的位置(当前行与上一行互换)
- :m +1 移动到+1 行的位置(当前行与下一行互换)
- :m 0 移动到首行的位置
- :m $ 移动到尾行的位置

**:set**
:set number 显示行索引

### 可视模式 (Visual-mode)

在正常模式按下 v, V, ^ + v，可以进入可视模式
可视模式下执行文本选择操作。

## .vimrc

### inoremap

按键映射

```sh
inoremap zz

```

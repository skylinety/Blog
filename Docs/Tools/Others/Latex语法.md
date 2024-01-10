# Latex 语法


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Latex 语法](#latex-语法)
  - [Latex 简介](#latex-简介)
  - [基础](#基础)
  - [符号](#符号)
    - [关系符](#关系符)
    - [表达式](#表达式)
    - [其他符号](#其他符号)
    - [无符号标记](#无符号标记)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->



## Latex 简介

Latex 用于编辑数学公式，目前较为友好支持 Latex 语法的笔记相关软件有

- quiver(Mac)
- 幕布

## 基础

Latex 语法可在 markdown 文件中进行书写，其标记为$
在行内展示对应公式，标记为

```md
$ $
```

例如

```md
$ \frac{a+1}{b+1} \quad $
```

展示为$ \frac{a+1}{b+1} \quad $

换行展示对应公式，标记为

```md
$$ $$
```

例如

```md
$$ \frac{a+1}{b+1} \quad $$
```

展示为 $$ \frac{a+1}{b+1} \quad $$

## 符号

### 关系符

| 符号            | 写法            | 示例                     |
| --------------- | --------------- | ------------------------ |
| $\pm$           | `\pm`           |
| $\mp$           | `\mp`           |
| $\times$        | `\times`        |
| $\div$          | `\div`          |
| $\leq$          | `\leq`          |
| $\neq$          | `\neq`          |
| $\geq$          | `\geq`          |
| $\approx$       | `\approx`       |
| $\sum$          | `\sum`          | $\sum\limits_{i=1}$      |
| $\cdot$         | `\cdot`         | ${a}\cdot{b}$            |
| $\lvert \rvert$ | `\lvert \rvert` | $\lvert a + b \rvert ^2$ |
| $\in$ | `\in` |  |
| $\notin$ | `\notin` |  |
| $\vee$ | `\vee` |  |
| $\land$ | `\land` |  |

### 表达式

| 符号          | 写法       | 示例                      |
| ------------- | ---------- | ------------------------- |
| $x^{n}$       | `x^{n}`    |
| $x_{n}$       | `x_{n}`    |
| $\sqrt[m]{n}$ | `\sqrt{n}` | $\sqrt[5]{x^2+(y + 1)^2}$ |
| $\frac{a}{b}$ | `\frac`    |
| $\=a$ | `\=`    |
| $\overline a$ | `\=`    |
| $\.a$ | `\.`    |
| $\dot a$ | `\dot`    |
| $\"a$ | `\"`    |

### 其他符号

| 符号        | 写法        | 示例 |
| ----------- | ----------- | ---- |
| $\triangle$ | `\triangle` |
| $\square$   | `\square`   |
| $\rightarrow$   | `\rightarrow`   |
| $\leftarrow$   | `\leftarrow`   | 
| $\Rightarrow$   | `\Rightarrow`   |
| $\Leftarrow$   | `\Leftarrow`   |
| $\leftrightarrow$   | `\leftrightarrow`   |
| $\Leftrightarrow$   | `\Leftrightarrow`   |

### 无符号标记

| 含义         | 写法      | 示例                | 说明                                       |
| ------------ | --------- | ------------------- | ------------------------------------------ |
| 下标位置迁移标记 | `\limits` | $\sum\limits_{i=1}\limits^{i=1}$ | \limits 控制右侧下标到上下两侧 |
| 底部位置标记 | `\underset` | $\underset{i=1}\sum$ | |
| 顶部位置标记 | `\overset` | $\overset{i=1}\sum$ | |

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️


> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Latex语法.html](http://www.skyline.show/Latex语法.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

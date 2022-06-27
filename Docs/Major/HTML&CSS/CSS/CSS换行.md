# CSS 换行

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CSS 换行](#css-换行)
  - [段落换行](#段落换行)
    - [overflow-wrap](#overflow-wrap)
    - [word-break](#word-break)
    - [换行总结](#换行总结)
  - [处理文字空白](#处理文字空白)
    - [white-space](#white-space)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 段落换行

### overflow-wrap

```js
overflow-wrap: normal;
overflow-wrap: break-word;
```

word-wrap 原始微软私有，css3 统一规范重命名为 overflow-wrap。

overflow-wrap 常见取值为 normal 和 break-word。
normal，默认值，单词保留完整，**最后一个单词超出也不换行**，直到该单词结束，只在 CJK(汉语系文字) 和空白符换行
break-word，尽量保持英文完整，除非一个单词占一行才断开换行，否则从空白或 CJK 换行

### word-break

```js
word-break: normal
word-break: break-all
word-break: keep-all
```

normal，默认值，单词保留完整，**最后一个单词超出也不换行**，直到该单词结束，CJK 换行
break-all 超出即换行，不考虑单词完整（适用所有语言），内容**把未填充部分的空白填满**就换行。
keep-all，**只有遇到空白**才换行（CJK 也不换行），超出不管。
break-word，word-break 也可取 break-word 值，但被废弃，不再推荐使用

### 换行总结

- normal 按照默认排版
- break-word 保持英文完整
- break-all 空白填满换行
- keep-all 只在空白换行

注意对应的键值。

## 处理文字空白

### white-space

white-space 主要用于处理段落中的空白符。
其用于处理换行问题时，解决的是换不换行的问题。
段落换行章节的 overflow-wrap、word-break 两个属性处理的是什么时候换行（遇到合适的断点如空白基本所有取值都会换行）。
常见使用是 white-space: nowrap 让文字直接不换行。

| 值       | 换行符 | 空格和制表符 | 文字换行 |
| -------- | ------ | ------------ | -------- |
| normal   | 合并   | 合并         | 换行     |
| nowrap   | 合并   | 合并         | 不换行   |
| pre      | 保留   | 保留         | 不换行   |
| pre-wrap | 保留   | 保留         | 换行     |
| pre-line | 保留   | 合并         | 换行     |

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/CSS 换行.html](http://www.skyline.show/CSS换行.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

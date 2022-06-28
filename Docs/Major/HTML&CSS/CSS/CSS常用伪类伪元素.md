# CSS 常用伪类伪元素

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CSS 常用伪类伪元素](#css-常用伪类伪元素)
  - [伪类](#伪类)
    - [综述](#综述)
    - [详解](#详解)
  - [伪元素](#伪元素)
    - [综述](#综述-1)
    - [详解](#详解-1)
  - [区分](#区分)
  - [BMW WARNING](#bmw-warning)


<!-- /code_chunk_output -->

## 伪类

### 综述

伪类即伪造一个类来为选定元素来描述特殊状态下的样式。
通过伪类实现的效果可以直接在选定元素添加一个 class 来模拟实现。
伪类通过:前缀来表示

| Name         | Desc                             | EG               |
| ------------ | -------------------------------- | ---------------- |
| :nth-of-type | 指定标签在相同类型同级标签的位置 | p:nth-of-type(n) |
| :nth-child   | 指定标签在所有类型同级标签的位置 | p:nth-child(n)   |

其中 n 可以是整数（1，2，3）、关键字（even，odd）、可以是公式 2n+1(奇数），n+5(大于等于 5)，-n+5(小于等于 5),而且**n 值起始值 0**.

### 详解

- nth-of-type

以标签和伪类作为前置条件进行筛选，选后添加类等其他条件进一步筛选。

```js

p.skyline:nth-of-type(2n+1) {
  text-decoration: underline;
}
```

上述代码首先选出奇数的 p 标签集合 A，然后进一步在 A 中筛选有 skyline 类的标签。
容易错误理解成选出有 skyline 类的 p 标签，然后选出其中的奇数。
用下述代码更加不容易出错

```js
p:nth-of-type(2n+1).skyline {
    text-decoration: underline;
}
```

[:nth-of-type demo](https://jsfiddle.net/skylinety/zsx4j03g/)

- nth-child

[:nth-child demo](https://jsfiddle.net/skylinety/Lhs9pg6w/1/)

## 伪元素

### 综述

伪元素表现为向 HTML 中添加了一个新的元素，而不是向已有元素中适配一个类的样式。
通过伪元素实现的效果可以直接添加一个新的元素来模拟实现。
伪元素通过::前缀来表示（标准），但也可通过:表示。

| Name           | Desc                                    | EG         |
| -------------- | --------------------------------------- | ---------- |
| ::after        | 指定标签后插入样式元素(content 非 none) |            |
| ::before       | 指定标签前插入样式元素(content 非 none) |            |
| ::first-line   | 选中标签的第一行                        |            |
| ::first-letter | 选中标签的第一个字                      |            |
| ::marker       | 选中列表前修饰类容，一般为数字或圆点。  | li::marker |
| ::selection    | 选中选择的文档。                        |            |

### 详解

**::marker**

```css
li::marker {
  content: '✪';
}
```

## 区分

伪元素目前不多，最常见的为::after 和::before
通过字面，其最大的区别就在于伪造类和伪造元素。
以伪类:first-child 和伪元素::first-letter 来说明

```css
i:first-child {color: red}
<p>
    <i>first</i>
    <i>second</i>
</p>
p::first-letter {color: red}
<p>
    first second
</p>
```

模拟实现

```css
.first-child {color: red}
<p>
    <i class="first-child">first</i>
    <i>second</i>
</p>
span {color: red}
<p>
    <span>first</span> second
</p>
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-of-type

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

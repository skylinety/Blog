# CSS 常用伪元素

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CSS 常用伪元素](#css-常用伪元素)
  - [汇总](#汇总)
    - [表格综述](#表格综述)
    - [详解](#详解)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warranty](#warranty)

<!-- /code_chunk_output -->

## 汇总

### 表格综述

| Name         | Desc                         | EG                |
| ------------ | ---------------------------- | ----------------- |
| :nth-of-type | 指定标签在相同类型标签的位置 | p:nth-of-type(2n) |

### 详解

**:nth-of-type**
以标签和伪类作为前置条件进行筛选，选后添加类等其他条件进一步筛选。

```js
/* This will match the 3rd paragraph as it will match elements which are 2n+1 AND have a class of fancy.
The second paragraph has a class of fancy but is not matched as it is not :nth-of-type(2n+1) */
p.fancy:nth-of-type(2n+1) {
  text-decoration: underline;
}
```

上述代码首先选出奇数的 p 标签集合 A，然后进一步在 A 中筛选有 fancy 类的标签。
容易错误理解成选出有 fancy 类的 p 标签，然后选出其中的奇数。
用下述代码更加不容易出错

```js
p:nth-of-type(2n+1).fancy {
    text-decoration: underline;
}
```

[详细代码示例参考](https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-of-type)

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://developer.mozilla.org/en-US/docs/Web/CSS/:nth-of-type

### Warranty

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

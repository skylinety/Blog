# CSS 常见效果实现

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CSS 常见效果实现](#css-常见效果实现)
  - [CSS 行溢出省略号](#css-行溢出省略号)
    - [单行溢出省略号](#单行溢出省略号)
    - [多行溢出省略号](#多行溢出省略号)
  - [实现矩形对角线](#实现矩形对角线)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## CSS 行溢出省略号

### 单行溢出省略号

```css
div {
  width: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

需要设置定长以及超出隐藏。
如果要设置隐藏后鼠标悬浮显示的效果，可以为 div 设定 title 属性，也可以用 hover 来达到效果

### 多行溢出省略号

```css
div {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2; // (两行文字)
  -webkit-box-orient: vertical;
}
```

## 实现矩形对角线

```css
div {
  background: linear-gradient(
    to top right,
    transparent 49.5%,
    rgb(235, 238, 245) 49.5%,
    rgb(235, 238, 245) 50.5%,
    transparent 50.5%
  );
}
```

![CSS常见效果实现20220614181936](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/CSS%E5%B8%B8%E8%A7%81%E6%95%88%E6%9E%9C%E5%AE%9E%E7%8E%B020220614181936.png)

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>   

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)
# CSS 常见问题汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CSS 常见问题汇总](#css-常见问题汇总)
  - [display:none 与 visibility:hidden 区别](#displaynone-与-visibilityhidden-区别)
  - [媒体查询失效](#媒体查询失效)
  - [img 标签是行内还是块级元素](#img-标签是行内还是块级元素)
  - [BMW WARNING](#bmw-warning)


<!-- /code_chunk_output -->

## display:none 与 visibility:hidden 区别

两者虽简单来说都是用于隐藏元素，表现形式大有不同。

display 会被文档流给移除，影响页面布局，导致重排重绘，原本位置会被其他元素占据。

visilibity:hidden 不会被文档流给移除，不会影响布局，页面重绘出一片空白，但不会重新排版。

display 不是继承属性，而 visibility 是继承属性。
若祖先设定为 visibility:hidden，后代元素会继承该属性不可见。
此时，若重置后代元素的 visibility 为 visible，其后代元素将可见。
若祖先设定的 display 属性设为 none 时，其不可继承，后代元素无力通过改变该属性重现。
总结如下表格所示：

| 样式              | 页面重绘 | 页面重排 | 显示效果     | 对应 css 属性是否继承 |
| ----------------- | -------- | -------- | ------------ | --------------------- |
| display:none      | 是       | 是       | 无显示       | 否（display）         |
| visibility:hidden | 是       | 否       | 所处区域空白 | 是（visibility）      |

## 媒体查询失效

媒体查询的常见用法为

设置屏幕在 300px 到 900px 时的背景

```css
@media screen and (min-width: 300px) and (max-width: 900px) {
  body {
    background: #eee;
  }
}
```

当设置不生效时，检查在 `<head>` 中是否添加了如下 `<meta>` 标签

```html
<meta name="viewport" content="width=device-width,initial-scale=1.0" />
```

## img 标签是行内还是块级元素

img 标签是行内元素。
打开控制台查看：
![CSS常见问题汇总20220421165556](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/CSS%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BB20220421165556.png)
但是，作为行内元素，img 标签为什么可以设定其宽高属性？
**img 标签准确来说，是行内可替换元素。**
所谓的可替换元素，简单来说，就是除了位置和大小，其自己内部的内容不受当前页面获取的样式与内部的填入的标签或文本等内容所影响。
img 标签可能不太好理解，另一个常见的行内可替换元素是 iframe 标签，其内部有自己一套样式来决定展现的内容。
常见的行内可替换元素有：

- img
- video
- iframe
- embed

总体来看，行内可替换元素趋向于 display:inline-block 的表现

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://developer.mozilla.org/en-US/docs/Web/CSS/Replaced_element

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh

# CSS 盒模型

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CSS 盒模型](#css-盒模型)
  - [盒模型组成](#盒模型组成)
  - [margin](#margin)
    - [概述](#概述)
    - [margin 负值](#margin-负值)
    - [margin auto](#margin-auto)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 盒模型组成

盒模型由内到外依次是content、padding、border、margin。
[w3](https://www.w3.org/TR/CSS2/box.html#box-margin-area)上的盒模型示意如下：

![CSS盒模型20230306232037](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/CSS%E7%9B%92%E6%A8%A1%E5%9E%8B20230306232037.png)

## margin

### 概述

marign 用于设定元素的外边距，属于[盒模型](https://www.w3.org/TR/CSS2/box.html#box-margin-area)。
margin 常规用法比较简单，用于布局时，需要注意其设定为 auto 与负值的情况。

### margin 负值

margin 左上（左或者上）设定为负值时，相当于拖拽对应的元素。

```css
margin-left: -10px;
/* 向左拖拽元素，拖拽后右边空间会被其他元素占据 */
margin-top: -10px;
/* 向上拖拽元素，拖拽后下边空间会被其他元素占据 */
```

margin 右下（右或者下）设定为负值时，元素本身不动，右侧或下侧元素移动。

```jsx
margin-right: -10px;
/* 元素不动，拖拽右边元素 */
margin-bottom: -10px;
/* 元素不动，拖拽下边元素 */
```

magin 可简单看成拖拽元素，至于拖元素本身还是其后边的元素，
以 margin-left，和 margin-right 来[示例](https://github.com/skylinety/Blog/blob/main/Demos/Major/HTML&CSS/CSS/CSS_negative_margin.html)说明：

margin-left 由正变负的情况：
可在示例上 chrome 手动改变 margin-left 值尝试，也可想象 margin-left 由正到负

```html
<div class="cell first" style="margin-left: 30em;"></div>
```

![CSS布局$left](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/CSS%E5%B8%83%E5%B1%80%24left.gif)
不难得出结论：margin-left 由大变小是在拖拽自己

margin-right 由正变负的情况：

可在示例上 chrome 手动改变 margin-right 值尝试，也可想象 margin-right 由正到负

```html
<div class="cell first" style="margin-right: 30em;"></div>
```

![CSS布局$right](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/CSS%E5%B8%83%E5%B1%80%24right.gif)
不难得出结论：margin-right 由大变小是在拖拽兄弟

margin设定的负值绝对值大于本身宽度时，如果上一行有空间，其会回到上一行。
利用margin设定负值的特性，可以进行圣杯布局。

### margin auto

margin auto 即自动外边距，常用于居中。

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  https://www.w3.org/TR/CSS2/box.html#box-margin-area

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/CSS盒模型.html](http://www.skyline.show/CSS盒模型.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

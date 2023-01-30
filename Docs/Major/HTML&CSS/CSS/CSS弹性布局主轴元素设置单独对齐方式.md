# CSS 弹性布局主轴元素设置单独对齐方式

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CSS 弹性布局主轴元素设置单独对齐方式](#css-弹性布局主轴元素设置单独对齐方式)
  - [效果图示](#效果图示)
  - [效果实现](#效果实现)
  - [BMW WARNING](#bmw-warning)


<!-- /code_chunk_output -->

## 效果图示

灰色为 flex 盒子，其水平方向的主轴内部有 4 个子元素。
通过设置特定属性将最后红框圈出的元素置于容器最右侧。

![CSS弹性布局flex主轴元素设置单独对齐方式20220617145752](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/CSS%E5%BC%B9%E6%80%A7%E5%B8%83%E5%B1%80flex%E4%B8%BB%E8%BD%B4%E5%85%83%E7%B4%A0%E8%AE%BE%E7%BD%AE%E5%8D%95%E7%8B%AC%E5%AF%B9%E9%BD%90%E6%96%B9%E5%BC%8F20220617145752.png)
实现效果
![CSS弹性布局flex主轴元素设置单独对齐方式20220617145350](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/CSS%E5%BC%B9%E6%80%A7%E5%B8%83%E5%B1%80flex%E4%B8%BB%E8%BD%B4%E5%85%83%E7%B4%A0%E8%AE%BE%E7%BD%AE%E5%8D%95%E7%8B%AC%E5%AF%B9%E9%BD%90%E6%96%B9%E5%BC%8F20220617145350.png)

## 效果实现

- 方案 1
  为红框子元素设定如下属性

```css
.red {
  flex-grow: 1; //红框子项目将占据了所有剩余空间
  display: flex; //将自身设置为flex,作为容器之后就可以单独对内部文字项目进行右对齐
  justify-content: flex-end; // 单独对内部文字项目进行右对齐
}
```

通过浏览器检视如下
![CSS弹性布局flex主轴元素设置单独对齐方式20220617150203](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/CSS%E5%BC%B9%E6%80%A7%E5%B8%83%E5%B1%80flex%E4%B8%BB%E8%BD%B4%E5%85%83%E7%B4%A0%E8%AE%BE%E7%BD%AE%E5%8D%95%E7%8B%AC%E5%AF%B9%E9%BD%90%E6%96%B9%E5%BC%8F20220617150203.png)

- 方案 2

将前 3 个子元素进行一层包裹，然后调整容器的 justify-content
`justify-content: space-between`

- 方案 3

为红框子项目添加如下属性

```css
margin-left: auto;
```

- 方案 4

为红框子项目添加如下属性

```css
.red {
  flex-grow: 1;
  text-align: right;
}
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/CSS 弹性布局 flex 主轴元素设置单独对齐方式.html](http://www.skyline.show/CSS弹性布局flex主轴元素设置单独对齐方式.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

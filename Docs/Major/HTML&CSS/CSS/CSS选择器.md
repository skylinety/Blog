# CSS 选择器

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CSS 选择器](#css-选择器)
  - [兄弟选择器](#兄弟选择器)
  - [BMW WARNING](#bmw-warning)


<!-- /code_chunk_output -->

## 兄弟选择器

CSS 常见的兄弟选择器包括 `+` `~`
其中`+` 是相邻兄弟选择器，`~` 是通用兄弟选择器。
选择器前后的标签有有相同父标签。

相邻兄弟选择器 + 选择的是紧邻在前置标签后的第一个标签。
通用兄弟选择器命中的标签必须是(不一定是紧邻)前置标签后面的兄弟标签。

| 选择器 | 描述 | 同父 | 后置标签要求首个 | 选中标签                 |
| ------ | ---- | ---- | ---------------- | ------------------------ |
| '+'    | 相邻 | 是   | 是               | 最多一个（非紧邻不选中） |
| '~'    | 通用 | 是   | 否               | 多个                     |

```css
/* 紧邻 h5 的第一个 p 兄弟标签中招，h5 之后第一个元素不是p，就无命中 */
h5 + p {
  color: red;
}

/*  比 h5 小（在其后面）的 p 兄弟标签全部中招，h5 之后没有 p，就无命中 */
h5 ~ p {
  color: red;
}
```

[示例](https://github.com/skylinety/Blog/blob/main/Demos/Major/HTML&CSS/CSS/CSS_Selector.html)

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

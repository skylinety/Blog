# 常见 DOM 操作

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [常见 DOM 操作](#常见-dom-操作)
  - [设置元素类](#设置元素类)

<!-- /code_chunk_output -->

## 设置元素类

```js
el.setAttribute("class", "abc"); //ie6、7不支持
el.setAttribute("className", "abc"); // 存在严重兼容问题
el.className = "abc"; //推荐
```

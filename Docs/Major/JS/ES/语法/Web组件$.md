# Web组件

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Web组件](#web组件)
  - [Web components](#web-components)
  - [自定义标签](#自定义标签)
    - [包含下划线](#包含下划线)
  - [影子 DOM](#影子-dom)
  - [HTML模板](#html模板)

<!-- /code_chunk_output -->

## Web components

前端组件化开发流行多时，现阶段的主流框架基本都是组件化的。
浏览器原生组件也一直在发展，现阶段，浏览器主要提供了三组原生API:

* 自定义组件（Custom elements）
* 影子 DOM（Shadow DOM）
* HTML模板（HTML templates）


## 自定义标签
### 包含下划线

HTML规范约定，自定义的标签（Custom elements）包含中划线，以与原型标签区分。

例如：
```jsx
<skyline-diy></skyline-diy>
// 不能写成 <skylinediy></skylinediy>
```

## 影子 DOM

Shadow DOM
## HTML模板

HTML templates
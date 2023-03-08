# CSS 基础布局

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [CSS 基础布局](#css-基础布局)
  - [居中布局](#居中布局)
    - [居中布局概述](#居中布局概述)
    - [flex](#flex)
    - [position+transform](#positiontransform)
    - [position+margin](#positionmargin)
    - [table-cell](#table-cell)
  - [三栏布局](#三栏布局)
    - [三栏布局概述](#三栏布局概述)
    - [基础三栏布局](#基础三栏布局)
    - [圣杯布局](#圣杯布局)
    - [双飞翼布局](#双飞翼布局)
    - [三栏布局对比](#三栏布局对比)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 居中布局

### 居中布局概述

| 方案                | 宽高固定 |
| ------------------- | -------- |
| flex                | 否       |
| position+transition | 否       |
| position+margin     | 是       |
| display:table-cell  | 是       |

几种[实现方案](https://github.com/skylinety/Blog/blob/main/Demos/Major/HTML&CSS/CSS/CSS_center_layout.html)使用共同的类样式：

```css
.simulated_body {
  resize: both;
  overflow: scroll;
  width: 50%;
}

.example {
  background-color: #eee;
  overflow: hidden;
  height: 200px;
}

.cell {
  width: 100px;
  height: 100px;
  background: lightblue;
  text-align: center;
}
```

### flex

flex 布局实现比较简单，该方案无需宽高固定，当前用得比较多。

```html
<h3>flex</h3>
<div class="simulated_body">
  <section
    class="example"
    style="display: flex;justify-content: center;align-items: center;"
  >
    <div class="cell">
      I am a bucolic migrant worker but I never walk backwards.
    </div>
  </section>
</div>
```

### position+transform

position+transform 实现在 flex 之前比较常见，该方案无需宽高固定。

```html
<h3>position+transform</h3>
<div class="simulated_body">
  <section class="example" style="position: relative;">
    <div
      class="cell"
      style="position: absolute;top: 50%;left: 50%;transform:translate(-50%, -50%)"
    >
      I am a bucolic migrant worker but I never walk backwards.
    </div>
  </section>
</div>
```

### position+margin

position+margin 细分由两种方式，两种细分方案都需宽高固定，
主要不同点在于 magin 设定 auto 还是负值。

```html
<h3>position+margin:auto</h3>
<div class="simulated_body">
  <section class="example" style="position: relative;">
    <div
      class="cell"
      style="margin: auto;position: absolute;top: 0;left: 0;right: 0;bottom: 0;"
    >
      I am a bucolic migrant worker but I never walk backwards.
    </div>
  </section>
</div>
<h3>position+margin:负值</h3>
<div class="simulated_body">
  <section class="example" style="position: relative;">
    <div
      class="cell"
      style="margin: -50px 0 0 -50px;position: absolute;top: 50%;left:50%"
    >
      I am a bucolic migrant worker but I never walk backwards.
    </div>
  </section>
</div>
```

### table-cell

table-cell 布局来实现局限性较大，较少使用。
该方案需宽高固定，另外需要注意的是，table-cell 设定百分比宽度无效。

```html
<h3>table-cell</h3>
<div class="simulated_body">
  <section
    class="example"
    style="display: table-cell;vertical-align: middle;width: 500px;"
  >
    <div class="cell" style="margin: auto">
      I am a bucolic migrant worker but I never walk backwards.
    </div>
  </section>
</div>
```

## 三栏布局

### 三栏布局概述

三栏布局是最常见的基本布局，其有多重实现方式，
后续三种实现方式的[示例](https://github.com/skylinety/Blog/blob/main/Demos/Major/HTML&CSS/CSS/CSS_layout.html)中，使用统一的基本样式为

```css
.simulated_body {
  resize: both;0
  overflow: scroll;
  width: 50%;
}

.example {
  background-color: #eee;
  overflow: hidden;
}

.cell {
  width: 50px;
  height: 50px;
  background: lightblue;
}

.text {
  background: violet;
  height: 100px;
}
```

布局中的关键样式，通过书写内联样式来方便对比查看。

### 基础三栏布局

基础三栏布局主要运用了 float、overflow 等属性来实现,
其中，overflow 用于形成 BFC 来排斥外部浮动元素

```html
<h3>基础三栏布局</h3>
<div class="simulated_body">
  <section class="example">
    <div class="cell" style="float: left; "></div>
    <div class="cell" style="float: right; "></div>
    <div class="text" style="overflow: hidden;">
      I am a bucolic migrant worker but I never walk backwards.
    </div>
  </section>
</div>
```

### 圣杯布局

圣杯布局主要运用了 float、margin、position 等属性来实现，
使用 margin 负值来拖拽元素，使用 padding 正值来预留左右占位空间。

```html
<h3>圣杯布局</h3>
<div class="simulated_body">
  <section class="example" style="padding: 0 50px; ">
    <div class="text" style="float: left;width: 100%;">
      I am a bucolic migrant worker but I never walk backwards.
    </div>
    <div
      class="cell"
      style="float: left;margin-left: -100%;position: relative;left: -50px;"
    ></div>
    <div class="cell" style="float: left;margin-right: -50px;"></div>
  </section>
</div>
```

### 双飞翼布局

双飞翼布局主要运用了 float、margin、等属性来实现，同时为内容 DOM 添加了包裹层，
使用 margin 负值来拖拽元素，正值来预留左右占位空间。

```html
<h3>双飞翼布局</h3>
<div class="simulated_body">
  <section class="example">
    <div class="content" style="float: left; width: 100%">
      <div class="text" style="margin: 0 50px;">
        I am a bucolic migrant worker but I never walk backwards.
      </div>
    </div>
    <div class="cell" style="float: left; margin-left: -100%;"></div>
    <div class="cell" style="float: left; margin-left: -50px;"></div>
  </section>
</div>
```

### 三栏布局对比

[三栏布局](https://github.com/skylinety/Blog/blob/main/Demos/Major/HTML&CSS/CSS/CSS_layout.html)各种方式最终呈现效果基本一致。

![CSS基础布局$20230307181645](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/CSS%E5%9F%BA%E7%A1%80%E5%B8%83%E5%B1%80%2420230307181645.png)

基础三栏布局实现简单，但需要将中间栏正文内容置于文档最后；
在浏览器渲染时，中间栏内容部分最后渲染，这并不合理，需要进行优化。

圣杯布局在未增加 DOM 的情况下将中间栏 DOM 前置；
双飞翼布局将中间栏 DOM 前置，但为内容层新增了一层 DOM。

圣杯布局没有添加 DOM 就实现了优化，
但是存在一个问题，当中间栏宽度小于右边栏宽度时，圣杯布局的样式会出现混乱。
将示例中的容器拖动到一定程度，显示效果如下：

![CSS基础布局$20230307181949](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/CSS%E5%9F%BA%E7%A1%80%E5%B8%83%E5%B1%80%2420230307181949.png)

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/CSS 基础布局.html](http://www.skyline.show/CSS基础布局.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

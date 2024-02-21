# Vue 渲染机制

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Vue 渲染机制](#vue-渲染机制)
  - [VDOM](#vdom)
  - [渲染流程](#渲染流程)
  - [Template优化](#template优化)
    - [模板语法的优势](#模板语法的优势)
    - [VDOM的优化](#vdom的优化)
    - [静态节点提升](#静态节点提升)
    - [补丁标记（更新类型标记）](#补丁标记更新类型标记)
    - [Tree Flatting](#tree-flatting)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## VDOM

在 JQuery 同时代，大多数的框架首先都是直接操作 DOM 元素。
但是不管多简单的 DOM 元素，都包含了较为复杂的属性。
打开任意网页，右键审查元素，在控制台输入

```jsx
Object.keys(console.dir($0))
```

![Vue渲染机制$20230222094020](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E6%B8%B2%E6%9F%93%E6%9C%BA%E5%88%B6%2420230222094020.png)

截图仅为很小的部分，可以看到即便是最简单的叶子节点，其都有较为庞大的身躯。
直接操作 DOM，当交互复杂时，不可避免会频繁操作 DOM， 这将造成浏览器回流重绘等性能问题。
最为直接的表现就是页面卡顿。

真实 DOM 上的额外的属性与方法往往与我们的操作无关，最终实现的效果也毫无关系。
于是为 DOM 瘦身，同时将频繁操作统一一步进行等理念应运而生。

虚拟 Dom，由 React 最先提出，她不是一种标准，更像是思想理念，或者说是一种设计，一个模式。
VDom 可以被看做是 UI 在内存中的虚拟。

假定 HTML 为：

```html
<div id="skyline">
    <h3 class="title"></h3>
    <p>{{ name }}</p>
</div>
```

则用 JS 对象简单实现的 VDOM 类似如下：

```jsx
{
  type: 'div',
  props: {
    id: 'skyline'
  },
  children: [
    {
        type: 'h3',
        props: {
            class: 'title'
        },
    },
    {
        type: 'p',
        props: {},
    },
  ]
}
```

每一个节点可以称为虚拟节点 vnode 。
不同框架定义的节点属性可能不同，但大体都有上述属性。
若以上节点为根节点，子节点不断扩展，便可联结壮大这颗 VDOM 树。

Vue render 函数返回 VDOM(准确来说是 AST，即虚拟语法树)。
通过官方的工具进行如下 [Demo](https://template-explorer.vuejs.org/#eyJzcmMiOiI8ZGl2IGlkPVwic2t5bGluZVwiPlxuICAgIDxoMyBjbGFzcz1cInRpdGxlXCI+PC9IMz5cbiAgICA8cD57eyBuYW1lIH19PC9wPlxuPC9kaXY+XG4iLCJvcHRpb25zIjp7fX0=):

仍以前述 HTML 模板为例，上述模板会被解析成 Render 语法

```jsx
import {
  createElementVNode as _createElementVNode,
  toDisplayString as _toDisplayString,
  openBlock as _openBlock,
  createElementBlock as _createElementBlock,
} from 'vue'

export function render(_ctx, _cache, $props, $setup, $data, $options) {
  return (
    _openBlock(),
    _createElementBlock('div', { id: 'skyline' }, [
      _createElementVNode('h3', { class: 'title' }),
      _createElementVNode('p', null, _toDisplayString(_ctx.name), 1 /* TEXT */),
    ])
  )
}

// Check the console for the AST
```

通过打开控制台找到 AST，可以看到:

![Vue渲染机制$20230210110315](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E6%B8%B2%E6%9F%93%E6%9C%BA%E5%88%B6%2420230210110315.png)

VDOM实质是在真实DOM和JS之间做“缓存”的作用，
减轻了真实DOM更新与构建缓慢带来的影响。

## 渲染流程

Vue底层将模板语法编译成 Render（或直接写Render函数），
通过Render创建VDOM，
通过mount将VDOM挂载或更新成真实DOM。

具体用一个官方图来说明

![Vue渲染机制$20230222093857](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E6%B8%B2%E6%9F%93%E6%9C%BA%E5%88%B6%2420230222093857.png)

一个简单的记忆方式如下： TRUE

**真实**(TRUE)的DOM渲染需要经过 


```jsx
Template-Render-Unreal(Virtual)-DOM(Element) 
```
四个阶段

## Template优化

### 模板语法的优势

相比Template语法，render函数写法可以直接操作vnode，代码编写更加灵活，主要用于高动态渲染逻辑，而Template可以高效应付大部分代码场景。
Vue 推荐使用 Template 语法。
不仅仅因为模板语法跟贴近 HTML，可复用现有的HTML代码段，应用CSS样式
也因为模板语法固定，Vue底层对模板语法转换成 Render 函数进行语法分析时，做了很多优化。
这些优化都是基于将模板上的语法信息放在了VDOM上。

### VDOM的优化

React等框架在更新等动作都基于运行时，当页面对应的数据状态发生改变时，
代码无法预知新的VDOM，故而需要重新遍历生成整个新的VDOM来保证页面更新的准确性。

用过这些框架都知道，许多地方的vnode往往没有任何变化，完全没有必要遍历和新建这些vnode；
同时与数据状态绑定的节点有框架设定的特定的语法信息，可将这些语法信息进行标记。
Vue从这些切入点进行了优化工作。

### 静态节点提升

Vue将与页面数据状态无关联的节点（静态节点）放在render函数之外形成闭包，
当页面更新时，这些节点被不会在渲染函数中遍历和重新生成节点。

优化后的模板语法通过工具查看如下[示例](https://template-explorer.vuejs.org/#eyJzcmMiOiI8ZGl2IGlkPVwic2t5bGluZVwiPlxuICAgIDxoMyBjbGFzcz1cInRpdGxlXCI+PC9IMz5cbiAgICA8cD57eyBuYW1lIH19PC9wPlxuPC9kaXY+XG4iLCJvcHRpb25zIjp7fX0=)

```jsx
import { createElementVNode as _createElementVNode, toDisplayString as _toDisplayString, openBlock as _openBlock, createElementBlock as _createElementBlock } from "vue"

const _hoisted_1 = { id: "skyline" }
const _hoisted_2 = /*#__PURE__*/_createElementVNode("h3", { class: "title" }, null, -1 /* HOISTED */)

export function render(_ctx, _cache, $props, $setup, $data, $options) {
  return (_openBlock(), _createElementBlock("div", _hoisted_1, [
    _hoisted_2,
    _createElementVNode("p", null, _toDisplayString(_ctx.name), 1 /* TEXT */)
  ]))
}

// Check the console for the AST
```

Vue将不会变化的div和h3节点放在render之外，
当页面更新时直接使用这些节点从而提升效率。

同时，连续的静态节点会被看做一个大的静态“HTML节点”通过innerHTML挂载。
当组件多次复用时，这些静态节点也会直接克隆出新的DOM节点。

如下[示例](https://vue-next-template-explorer.netlify.app/#eyJzcmMiOiI8ZGl2IGlkPVwic2t5bGluZVwiPlxuICAgIDxoMyBjbGFzcz1cInRpdGxlXCI+PC9IMz5cbiAgICA8aDMgY2xhc3M9XCJ0aXRsZVwiPjwvSDM+XG4gICAgPGgzIGNsYXNzPVwidGl0bGVcIj48L0gzPlxuICAgIDxoMyBjbGFzcz1cInRpdGxlXCI+PC9IMz5cbiAgICA8aDMgY2xhc3M9XCJ0aXRsZVwiPjwvSDM+XG4gICAgPHA+e3sgbmFtZSB9fTwvcD5cbjwvZGl2PlxuIiwic3NyIjpmYWxzZSwib3B0aW9ucyI6eyJob2lzdFN0YXRpYyI6dHJ1ZX19)

```jsx
<div id="skyline">
    <h3 class="title"></H3>
    <h3 class="title"></H3>
    <h3 class="title"></H3>
    <h3 class="title"></H3>
    <h3 class="title"></H3>
    <p>{{ name }}</p>
</div>
```

编译成

```jsx
import { createElementVNode as _createElementVNode, toDisplayString as _toDisplayString, createStaticVNode as _createStaticVNode, openBlock as _openBlock, createElementBlock as _createElementBlock } from "vue"

const _hoisted_1 = { id: "skyline" }
const _hoisted_2 = /*#__PURE__*/_createStaticVNode("<h3 class=\"title\"></h3><h3 class=\"title\"></h3><h3 class=\"title\"></h3><h3 class=\"title\"></h3><h3 class=\"title\"></h3>", 5)

export function render(_ctx, _cache, $props, $setup, $data, $options) {
  return (_openBlock(), _createElementBlock("div", _hoisted_1, [
    _hoisted_2,
    _createElementVNode("p", null, _toDisplayString(_ctx.name), 1 /* TEXT */)
  ]))
}

// Check the console for the AST
```

### 补丁标记（更新类型标记）

Vue为不同的模板语法，如双大括号，类绑定等，
添加了特殊的补丁更新标记（[patch flag](https://github.com/vuejs/core/blob/main/packages/shared/src/patchFlags.ts)）来更新VNode节点内容。

```js
export const enum PatchFlags {
    TEXT = 1,
        CLASS = 1 << 1,
        STYLE = 1 << 2,
        PROPS = 1 << 3,
        ...
}
```

当对如下[模板](https://template-explorer.vuejs.org/#eyJzcmMiOiI8ZGl2IDppZD1cInNreWxpbmVcIj5cbiAgPGgzIDpjbGFzcz1cInRpdGxlXCI+PC9oMz5cbiAgPHAgOmNsYXNzPVwiY29udGVudFwiIDppZD1cImN0eFwiPnt7IG5hbWUgfX08L3A+XG48L2Rpdj4iLCJvcHRpb25zIjp7fX0=)进行解析时，

```jsx
<div :id="skyline">
  <h3 :class="title"></h3>
  <p :class="content" :id="ctx">{{ name }}</p>
</div>
```

会被解析成

```jsx
export function render(_ctx, _cache, $props, $setup, $data, $options) {
  return (_openBlock(), _createElementBlock("div", { id: _ctx.skyline }, [
    _createElementVNode("h3", {
      class: _normalizeClass(_ctx.title)
    }, null, 2 /* CLASS */),
    _createElementVNode("p", {
      class: _normalizeClass(_ctx.content),
      id: _ctx.ctx
    }, _toDisplayString(_ctx.name), 11 /* TEXT(1), CLASS(2), PROPS(8) */, ["id"])
  ], 8 /* PROPS */, ["id"]))
}

```

在_createElementVNode函数内部，不同的更新标记进行位检查运算执行不同的内容

```jsx
if (vnode.patchFlag & PatchFlags.CLASS /* 2 */) {
  // update the element's class
}
if (vnode.patchFlag & PatchFlags.PROPS /* 8 */) {
  // update the element's props
}
...
```

多种更新标记会被合成一个数，如模板中的p标签含有文本，类以及属性传递，
会相加合并成一个数例如上例的11。
在进行if判断时，通过左移形成的标记多个相加也可进行判定。

标记合并：

```jsx
000000001 +
// 1
000000010 +
// 2
000000100 =
// 8
000000111
// 11
```

if判定：

```jsx
// vnode.patchFlag & PatchFlags.TEXT
000000111 &
// 11
000000001 =
// 1
000000001 
// 1

// vnode.patchFlag & PatchFlags.CLASS
000000111 &
// 11
000000010 =
// 2
000000010 
// 2

// vnode.patchFlag & PatchFlags.PROPS
000000111 &
// 11
000000100 =
// 8
000000100 
// 8
```

当合并后，TEXT，CLASS，PROPS的更新也能被监测到。

### Tree Flatting

官方将Tree Flattening 中文命名为树结构打平，
其含义为将区块中不携带patch flag的VNode踢出后续更新的遍历和重新渲染，极大的减少需要遍历的节点数目。
例如上述的

```jsx
<div id="skyline">
    <h3 class="title"></H3>
    <h3 class="title"></H3>
    <h3 class="title"></H3>
    <h3 class="title"></H3>
    <h3 class="title"></H3>
    <p>{{ name }}</p>
</div>
```

会被扁平化为

```jsx
div 根区块
  p 带有name文本
```

来进行遍历。

这里引入区块（block）的概念，
当一个模板内部内容稳定不包含动态增减结构的指令如v-if，v-for等时，
可以将这一部分认为是一个区块。
动态内容整体部分也被看做是一个区块而包含在另一个区块中。
可以看到，上面的所有示例都会在render函数涉及到 createElementBlock。
测试如下示例

```jsx
<div id="skyline">
    <div>
      <p v-if="name">{{ name }}</p>
    </div>
</div>
```

会被编译成

```jsx
export function render(_ctx, _cache, $props, $setup, $data, $options) {
  return (_openBlock(), _createElementBlock("div", { id: "skyline" }, [
    _createElementVNode("div", null, [
      (_ctx.name)
        ? (_openBlock(), _createElementBlock("p", { key: 0 }, _toDisplayString(_ctx.name), 1 /* TEXT */))
        : _createCommentVNode("v-if", true)
    ])
  ]))
}
```

## BMW WARNING

* Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github 仓库](https://github.com/skylinety/Blog)点亮 ⭐️

> I am a bucolic migant worker but I never walk backwards.

* Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://vuejs.org//guide/extras/rendering-mechanism.html

* Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Vue 渲染机制.html](http://www.skyline.show/Vue渲染机制.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

# Vue 渲染机制

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Vue 渲染机制](#vue-渲染机制)
  - [VDOM](#vdom)
  - [虚拟节点渲染](#虚拟节点渲染)
  - [Template优化](#template优化)
    - [模板语法的优势](#模板语法的优势)
    - [VDOM的优化](#vdom的优化)
    - [静态节点提升](#静态节点提升)
    - [动态节点更新类型标记](#动态节点更新类型标记)
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

## 虚拟节点渲染

Vue底层将模板语法编译成 Render（或直接写Render函数），
通过Render创建VDOM，
通过mount将VDOM挂载或更新成真实DOM。

具体用一个官方图来说明

![Vue渲染机制$20230222093857](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E6%B8%B2%E6%9F%93%E6%9C%BA%E5%88%B6%2420230222093857.png)

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

同时，连续的静态节点会被看做一个大的静态HTML节点通过innerHTML挂载。
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
### 动态节点更新类型标记

Vue将使用其定义语法（双大括号，v-指令等）的节点进行特殊标记并生产虚拟节点，
对未使用语法，页面表现为其节点基本不更新的部分不做处理。



## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github 仓库](https://github.com/skylinety/Blog)点亮 ⭐️

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://vuejs.org//guide/extras/rendering-mechanism.html

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Vue 渲染机制.html](http://www.skyline.show/Vue渲染机制.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

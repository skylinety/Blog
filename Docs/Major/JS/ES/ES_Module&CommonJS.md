# ES Module vs CommonJS

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES Module vs CommonJS](#es-module-vs-commonjs)
  - [模块系统](#模块系统)
  - [ESM VS CJS](#esm-vs-cjs)
  - [ESM VS CJS 要点解析](#esm-vs-cjs-要点解析)
    - [模块输出](#模块输出)
    - [模块加载](#模块加载)
  - [tree shaking](#tree-shaking)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 模块系统

早期 JS 出现只是作为脚本语言来进行简单的表单验证与控制简单动画，所有操作与变量都在全局进行，设计之初，不需要考虑模块系统。
随着 JS 的发展，其应用越来越复杂，逐渐进入多 JS 脚本通过 script 标签引入的年代。
多脚本需要解决脚本引入的顺序，脚本互相引入，脚本循环引入，全局命名污染，命名冲突等诸多问题，同时后期维护特别困难。
对于复杂 JS 程序，需要解决的主要问题如下

- 模块隔离（私有代码权限访问控制）
- 模块间依赖
- 代码传递到执行环境

早期解决方案如下：

* 命名空间
* 立即执行匿名函数 + 闭包

ES5 时代，模块化的标准与方案有很多，亟需统一，ES6 的模块系统应运而生。
由于影响力较大的 NodeJS 大方向参照了 CommonJS 标准，并在其上做了取舍，故本文主要对比 ES6 与 CommonJS 两种方案。
其他规范 AMD（Asynchronous Module Definiton）如 requireJS,CMD(Common Module Definition)如 SeaJS 皆支持异步模块定义，在 ES6 模块系统后使用频率降低，如下简单对比。

AMD 典型示例

```js
//依赖前置
require(['a', 'b'], function (a, b) {
  a.someFn()
  b.someFn()
})
```

CMD 典型示例

```js
define('main', function (require, exports, module) {
  var a = require('a') //依赖就近
  a.someFn()
  var b = require('b')
  b.someFn()
})
```

上述代码可以看到，AMD 规范在于依赖前置、提前执行，CMD 在于依赖就近、延迟执行。
为了兼容各种模块系统，UMD(Universal Module Definition) 通用模块规范进行了兼容处理。
常用的开源库打包后会生成 xxx.umd.js
webpack 打包后 UMD 兼容模块代码的如下：

```js
;(function webpackUniversalModuleDefinition(root, factory) {
  if (typeof exports === 'object' && typeof module === 'object')
    //Node.js (拓展CommonJS),ES6
    module.exports = factory()
  else if (typeof define === 'function' && define.amd)
    //amd cmd
    define([], factory)
  else if (typeof exports === 'object')
    // CommonJS标准方案
    exports['skyline-ui'] = factory()
  else root['skyline-ui'] = factory() // 未引入规范模块，全局申明
})(typeof self !== 'undefined' ? self : this, function () {
  // ...some code
})
```

ES6 兼容 Node.js 模块方案

## ESM VS CJS

| 标准     | 输出           | 加载时机 | 加载方式     |
| -------- | -------------- | -------- | ------------ |
| ES6 模块 | 值引用（只读） | 编译     | import 异步  |
| CommonJS | 值浅拷贝       | 运行     | require 同步 |

## ESM VS CJS 要点解析

### 模块输出

- ES6

ES6 模块输出的是对值的引用，**即便是简单类型，模块内值的改变也会引起之后值得改变**
JS 引擎对脚本静态分析的时候，遇到模块加载命令 import，就会生成一个只读引用。
等到脚本真正执行时，再根据这个**只读引用**，到被加载的那个模块里面去取值（对象存在于导出模块的文件）。
ES6 模块是动态引用，并且不会缓存值，模块里面的变量绑定其所在的模块。

例 1

```jsx
// lib.js
export let counter = 3
export function incCounter() {
  counter++
}

// main.js
import { counter, incCounter } from './lib'
console.log(counter) // 3
incCounter()
console.log(counter) // 4
```

例 2

```jsx
// mod.js
function C() {
  this.sum = 0
  this.add = function () {
    this.sum += 1
  }
  this.show = function () {
    console.log(this.sum)
  }
}

export let c = new C()

// x.js
import { c } from './mod'
c.add()

// y.js
import { c } from './mod'
c.show()

// main.js
import './x'
import './y'

//输出1
```

引用只读

```jsx
// lib.js
export let obj = {}

// main.js
import { obj } from './lib'

obj.prop = 123 // OK
obj = {} // TypeError
```

main.js 从 lib.js 输入变量 obj，可以对 obj 添加属性，但是重新赋值就会报错。
因为变量 obj 指向的地址是只读的，不能重新赋值，这就好比 main.js 创造了一个名为 obj 的 const 变量

- CommonJS

对应 CommonJS 规范中，导出的是一个对象，引入时采用的是对象的浅拷贝（在导出和导入时各有一个对象生成）。
该对象的属性如果是简单类型，模块内部值得改变则不会对之后引用产生影响

```jsx
// lib.js
var counter = 3
function incCounter() {
  counter++
}
module.exports = {
  counter: counter,
  incCounter: incCounter,
}

// main.js
var mod = require('./lib')
console.log(mod.counter) // 3
mod.incCounter() // 引起lib.js中counter 值改变为4
console.log(mod.counter) // 3
```

### 模块加载

- 加载时机

CommonJS 导出的是一个对象（即 module.exports 属性），该对象只有在脚本运行完才会生成。
而 ES6 模块不是对象，它的对外接口只是一种静态定义，在代码静态解析阶段就会生成

- 加载方式

commonJS 规范用同步的方式加载模块.
例如实现该规范的 nodeJS，因为在服务端，模块文件都存在本地磁盘，可以进行快速度读取，等待模块加载不会耗费过多的时间，所以这样做不会有问题。
但是在浏览器端，限于网络等各种原因，需要使用异步加载获取更好的体验。

## tree shaking

由于 ES6 的模块暴露的是引用而不是生成一个对象.
从加载时机来看，ES6 的 import 命令会被 JavaScript 引擎静态分析编译时就分析是否被引用，而不是在代码运行时加载。
编译时加载使得对 ES6 静态分析并进行无用代码删除成为可能。
这就是为什么 ES6 出来之后，tree shaking 才成为可能，这也是为什么要使用 tree shaking，必须使用 ES6 模块。

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](http://www.skyline.show)  欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://es6.ruanyifeng.com/#docs/module-loader

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

# ES Module vs CommonJS

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES Module vs CommonJS](#es-module-vs-commonjs)
  - [概要对比](#概要对比)
  - [要点解析](#要点解析)
    - [模块输出](#模块输出)
    - [模块加载](#模块加载)
  - [tree shaking](#tree-shaking)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 概要对比

| 标准     | 输出           | 加载时机 | 加载方式     |
| -------- | -------------- | -------- | ------------ |
| ES6 模块 | 值引用（只读） | 编译     | import 异步  |
| CommonJS | 值浅拷贝       | 运行     | require 同步 |

## 要点解析

### 模块输出

- ES6

ES6 模块输出的是对值的引用，即便是简单类型，模块内值的改变也会引起之后值得改变
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
mod.incCounter() // 引起lib.js中counter 值改变
console.log(mod.counter) // 3
```

### 模块加载

- 加载时机

CommonJS 导出的是一个对象（即 module.exports 属性），该对象只有在脚本运行完才会生成。
而 ES6 模块不是对象，它的对外接口只是一种静态定义，在代码静态解析阶段就会生成

- 加载方式

commonJS 规范用同步的方式加载模块.
例如实现该规范的 nodeJS，因为在服务端，模块文件都存在本地磁盘，可以进行快速度读取，所以这样做不会有问题。
但是在浏览器端，限于网络等各种原因，需要使用异步加载获取更好的体验。

## tree shaking

由于 ES6 的模块暴露的是引用而不是生成一个对象.
从加载时机来看，ES6 的 import 命令会被 JavaScript 引擎静态分析编译时就分析是否被引用，而不是在代码运行时加载。
编译时加载使得对 ES6 静态分析并进行无用代码删除成为可能。
这就是为什么 ES6 出来之后，tree shaking 才成为可能，这也是为什么要使用 tree shaking，必须使用 ES6 模块。

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://es6.ruanyifeng.com/#docs/module-loader

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

# ES 闭包

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 闭包](#es-闭包)
  - [闭包定义](#闭包定义)
  - [闭包应用](#闭包应用)
    - [函数柯里化](#函数柯里化)
    - [偏函数](#偏函数)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 闭包定义

- MDN

> 闭包是指那些能够访问自由变量的函数。

- JavaScript 权威指南

> 从技术的角度讲，所有的 JavaScript 函数都是闭包。
> 在开发实践角度讲，即使创建该函数的上下文已经销毁（父函数执行完毕），该函数仍然存在（比如，内部函数从父函数中返回），该函数中引用了自由变量

自由变量是指在函数中使用的，但既不是函数参数也不是函数的局部变量的变量。

闭包可以理解为包含如下要素

- 函数
- 自由变量

## 闭包应用

### 函数柯里化

函数柯里化是将一个多元（多个参数）函数拆分成多个一元函数，通过依次传入参数来执行该函数。

```jsx
function line(a, b, c, d) {
  return a + b + c + d
}
```

line 函数柯里化后 lineCurry，函数可像如下调用

```jsx
lineCurry('1', '2', '3', '4')
lineCurry('1', '2')('3')('4')
lineCurry('1')('2')('3')('4')
...
```

curry 封装如下

基础版本

```jsx
function curry(fn) {
  let params = []
  return function step(...args) {
    params = params.concat(args)
    if (params.length < fn.length) {
      return step
    } else {
      const ret = fn(...params)
      // 重置闭包数据
      params = []

      return ret
    }
  }
}

var lineCurry = curry(line)
```

占位符优化版本

```jsx
function curry(fn) {
  let params = []
  return function step(...args) {
    params = params
      .map((v) => (v == '_' ? args.shift() || '_' : v))
      .concat(args)
    if (params.includes('_') || params.length < fn.length) {
      return step
    } else {
      const ret = fn(...params)
      // 重置闭包数据
      params = []

      return ret
    }
  }
}
var lineCurry = curry(line)
lineCurry('1', '2', '3', '4')
lineCurry('_', '2', '3', '4')('1')
lineCurry('1', '_', '3', '4')('2')
lineCurry('1', '_', '3')('_', '4')('2')
lineCurry('1', '_', '_', '4')('_', '3')('2')
lineCurry('_', '2')('_', '_', '4')('1')('3')
```

上述 lineCurry 都返回'1234'

考虑到'\_'在代码中出现频率较高，多数资料使用如下方式创建一个占位符对象来防止冲突。
本文简化便于理解

```jsx
var _ = {}
```

优雅写法版本
（引自 segmentfault@大笑平 ）

```jsx
const curry = (fn) =>
  (judge = (...args) =>
    args.length === fn.length ? fn(...args) : (arg) => judge(...args, arg))
```

### 偏函数

偏函数指固定函数的部分参数，产生更小元（函数参数更少）的函数，以减少实际函数调用时传参数。

偏函数和柯里化的区别在于：
偏函数将多元函数固定部分参数值，减少部分元。
柯里化是将多元函数拆分成多个一元函数。

偏函数可以有以下几种方式简单实现

```jsx
function add(a, b) {
  return a + b
}
function add5(y) {
  return add(5, y)
}
function add6(y) {
  return add(6, y)
}
```

```jsx
function add(a) {
  return function (b) {
    return a + b
  }
}

let add5 = add(5)
let add6 = add(6)
```

```jsx
function add(a, b) {
  return a + b
}

let add5 = add.bind(null, 5)
let add6 = add.bind(null, 6)
```

上述方式作临时使用，存在 this 指向变更，传参顺序固定等问题，
当需要多次使用偏函数时，可封装成一个函数函数，
根据偏函数的功能，实现如下基础版本。

初始版本

```jsx
function partial(fn, ...args) {
  return (...params) => fn(...args, ...params)
}
```

保留 this 指向（注意不要使用箭头函数）

```jsx
function partialWithThis(fn, ...args) {
  return function (...params) {
    return fn.call(this, ...args, ...params)
  }
}
```

this 指向验证

```jsx
var c = 2
function add(a, b) {
  return a + b + this.c
}

const skyline = {
  c: 1,
  add1: partial(add, 1),
  addOne: partialWithThis(add, 1),
}

skyline.add1(1) // 4
skyline.addOne(1) // 3
```

添加占位符优化

```jsx
function partialWithHolder(fn, ...args) {
  return function (...params) {
    const _args = args.map((v) => (v == '_' ? params.shift() : v))
    return fn.call(this, ..._args, ...params)
  }
}
```

占位符验证

```jsx
// a为被除数。b为除数
var dividedBy = function (a, b) {
  return a / b
}
dividedBy5 = partialWithHolder(dividedBy, '_', 5)
dividedBy5(20)
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github 仓库](https://github.com/skylinety/Blog)点亮 ⭐️

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> [JavaScript 专题之函数柯里化](https://github.com/mqyqingfeng/Blog/issues/42)

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES 闭包.html](http://www.skyline.show/ES闭包.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

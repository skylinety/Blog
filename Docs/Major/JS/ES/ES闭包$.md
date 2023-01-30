# ES 闭包

## 闭包理解

- MDN
  闭包是指那些能够访问自由变量的函数。闭包 = 函数 + 函数能够访问的自由变量
  自由变量是指在函数中使用的，但既不是函数参数也不是函数的局部变量的变量。

- JavaScript 权威指南
  技术角度
  从技术的角度讲，所有的 JavaScript 函数都是闭包。
  实践角度
  上下文已经销毁
  ｜ ▷ 即使创建它的上下文已经销毁（父函数执行完毕），它仍然存在（比如，内部函数从父函数中返回）
  引用自由变量
  ｜ ▷ 在代码中引用了自由变量

## 闭包应用

### 函数柯里化

函数柯里化是将一个多元（多个参数）函数拆分成多个一元函数，通过依次传入参数来执行该函数。

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

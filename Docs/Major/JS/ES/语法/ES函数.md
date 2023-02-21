# ES 函数

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 函数](#es-函数)
  - [函数的长度](#函数的长度)
  - [函数参数](#函数参数)
  - [参数传递](#参数传递)
    - [按值传递](#按值传递)
    - [引用传递](#引用传递)
  - [ES6 默认参数](#es6-默认参数)
    - [默认参数的影响](#默认参数的影响)
    - [作用域前后变化](#作用域前后变化)
    - [懒执行](#懒执行)
    - [TDZ(Temporal Dead Zone)](#tdztemporal-dead-zone)
  - [函数创建](#函数创建)
  - [作用域链](#作用域链)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 函数的长度

函数的长度等于形参的个数。

```jsx
function skyline(a, b, c){
    console.log(`输入${arguments.length}个参数`)
}

console.log(`函数的长度为：${skyline.length}`)

skyline(1)

// 函数的长度为：3
// 输入1个参数
```
## 函数参数

函数的参数被放在一个arguments的类数组中。

它的值永远与对应命名参数的值保持同步。  
设函数第 n 个参数为 a， 当在函数内部修改了 a，那么 arguments[n-1]保持同步也为更改后的值

arguments 的长度是由运行时传入参数个数决定的，而不是定义时

```js
function test(a, b, c) {
  arguments[0] = { name: 'skyline' }
  arguments[1] = 2
  c = 5
  console.log(
    `a=${a}, b=${b}, 第三个参数的值是：${arguments[2]}, 参数的长度：${
      arguments.length
    }, 第一个参数与a是否相等：${arguments[0] === a}`
  )
}

test(1, { firstName: 'liu' }, '3', 3)
// a=[object Object], b=2, 第三个参数的值是：5, 参数的长度：4, 第一个参数与a是否相等：true
```

对于 ES6 中通过扩展运算符获取参数，示例如下

```js
function createArray6(...args) {
  console.log(args)
  console.log(args instanceof Array)
  return args
}

createArray6(11, 2, 3)
//  (3) [11, 2, 3]
//  true
```

不同于 ES5 的 arguments 是一种类数组，ES6 拓展运算符获取 args 是一个数组。

arguments 与实参的绑定的绑定情况如下：
非严格，传入值共享，没传不共享

```jsx
function skyline(a, b, c){
    console.log(`输入的a:${a}`)
    console.log(`输入的第一个参数：${arguments[0]}`)
    b = 2
    console.log(`b值为${b}`)
    console.log(`第而个参数：${arguments[1]}`)
}

console.log(`函数的长度为：${skyline.length}`)

skyline(1)

// 函数的长度为：3
// 2 输入的a:1
// 3 输入的第一个参数：1
// 5 b值为2
// 6 第而个参数：undefined
```

在严格模式下，实参和 arguments 是不会共享的，也就是都会为上述b的情况。
## 参数传递

### 按值传递

**函数的参数都是按值传递的，当传递引用类型的值时，会把这个值在内存中的地址复制给局部变量**。
其实质就是把实参在内存中的数据传递给形参，基本类型拷贝了本身，引用类型拷贝的是引用的地址。

- 示例一

```js
var str1 = 'aaa'
var num2 = 2
var obj1 = {
  value: 1,
}

function skyline(obj2) {
  obj2.value = 2
  console.log(obj2.value) //2
}
skyline(obj1)
console.log(obj1.value) // 2
```

上述进入函数时，通过值传递，形参 obj2 拷贝了实参 obj1 的内存数据，即拷贝一个引用地址。

在函数执行`obj2.value = 2;`前后的内存状态
![ES函数20220613193938](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E5%87%BD%E6%95%B020220613193938.png)
（图解与说明仅为了解释参数传递，计算机内存远比此复杂）

- 示例二

```js
var str1 = 'aaa'
var num2 = 2
var obj1 = {
  value: 1,
}

function skyline(obj2) {
  obj2 = 2
  console.log(obj2) //2
}
skyline(obj1)
console.log(obj1.value) // 2
```

在函数执行`obj2 = 2;`前后的内存状态
![ES函数20220613194012](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E5%87%BD%E6%95%B020220613194012.png)

### 引用传递

ES 函数的参数时按值传递的，部分语言支持参数按引用传递。
以上述示例二为例，若函数 skyline 参数按引用传递，则传入是形参 obj2 直接记录实参 obj1 的内存地址。
故而后续不管两者谁变化，都将影响另一方。
即上述代码执行到最后，obj1 的值将会被变更为数字 2。
在 C#中，区分值传递和引用传递是方法参数前加 ref，加 ref 就是引用传递, 不加就是值传递。

## ES6 默认参数

### 默认参数的影响

ES6 可为函数设定默认值。设定默认值后，函数的 length 和作用域将会发生变化。
函数的 length 只计算没有设定默认值得参数个数（默认值应该是尾参数）。
对于作用域的变化，函数设定默认参数后，函数参数将会形成一个全新的作用域，这个作用域居于函数内部和外部作用域之间。

### 作用域前后变化

* 不带默认参数

```jsx
var x = 1
function fun(x, z) {
  debugger
  var x = 2
  var y = 3
  console.log(x, y)
}
fun(4, 5)
```
打开Chrome控制台，
![ES函数20230210172132](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E5%87%BD%E6%95%B020230210172132.png)

* 带默认参数

```jsx
var x = 1
function fun(x = 6, z = 7) {
  debugger
  var x = 2
  var y = 3
  console.log(x, y)
}
fun(4, 5)
```

![ES函数20230210172219](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E5%87%BD%E6%95%B020230210172219.png)

由此可见，在 chrome 中，ES5 函数参数只用 LocalScope 作用域；而 ES6 中函数默认值参数会形成单独的作用域，这个作用域占用了之前的 Local Scope  而函数体内声明的变量形成了一个块级作用域 Block Scope，通常情况下，此时的 local 作用域被称为居间作用域（intermediate scope）

* Babel 转换 默认参数代码

转换后如下

```jsx
'use strict'

var x = 1

function fun() {
  var x = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : 6
  var z = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 7
  return (function (x) {
    debugger
    var x = 2
    var y = 3
    console.log(x, y)
  })(x)
}

fun(4, 5)
```

是否携带默认参数，作用域前后变化如下：

![ES函数20230210173242](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E5%87%BD%E6%95%B020230210173242.png)

### 懒执行

**默认参数只有在函数每次执行的时候才会调用，而不是在函数定义时**。这与其他部分语言是表现是不相同的。
如下代码由于默认参数的懒执行(惰性求值)，只要不运行 skyline 函数，控制台执行并不会报错。

```jsx
var x = 1

function skyline(x = z) {}
```

### TDZ(Temporal Dead Zone)

TDZ 即暂时性死区，简单来说就是 let/const 声明之前（包括声明时）就访问对应的变量与常量，会抛出 ReferenceError 错误。

```
// 不报错
var x = x;

// 报错
let x = x;
```

函数默认值传参也会造成暂时性死区。

```jsx
var x = 1

function haha(x = x) {}
haha() //Uncaught ReferenceError: Cannot access 'x' before initialization

function skyline(x = y, y) {}
skyline(1, 2)
skyline(undefined, 2) //Uncaught ReferenceError: Cannot access 'y' before initialization
```

## 函数创建

函数创建一般有函数声明与函数表达式两种方式。
函数表达式: `let fn1 = function() {}`
函数声明: `function fn2() {}`
Javascript 解析器会率先读取函数声明，在函数代码执行之前，已经将函数声明提升到执行环境，故可以在声明前执行。
但是，函数表达式提前执行会导致错误。

## 作用域链
作用域链的作用是保证最执行环境有权访问的所有变量和函数的有序访问。
作用域链最前端始终都是当前代码所在环境的变量对象，而后一步一步向外成延伸，直到全局执行环境。
标志符解析是沿着作用域链一级一级搜索的过程，直到找到为止，故而位于作用域链最前端的变量作为当前环境的变量。
## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github 仓库](https://github.com/skylinety/Blog)点亮 ⭐️。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> 《JavaScript 高级程序设计》

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

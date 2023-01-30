# ES 函数

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 函数](#es-函数)
  - [arguments](#arguments)
  - [参数传递](#参数传递)
    - [按值传递](#按值传递)
    - [引用传递](#引用传递)
  - [BMW WARNING](#bmw-warning)


<!-- /code_chunk_output -->

## arguments

- arguments 是一个类数组
- 它的值永远与对应命名参数的值保持同步。
  设函数第 n 个参数为 a， 当在函数内部修改了 a，那么 arguments[n-1]保持同步也为更改后的值
- arguments 的长度是由运行时传入参数个数决定的，而不是定义时

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

function foo(obj2) {
  obj2.value = 2
  console.log(obj2.value) //2
}
foo(obj1)
console.log(obj1.value) // 2
```

上述进入函数时，通过值传递，形参 obj2 拷贝了实参 obj1 的内存数据，即拷贝一个引用地址。

在函数执行`obj2.value = 2;`前后的内存状态
![ES函数20220613193938](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E5%87%BD%E6%95%B020220613193938.png)
（说明：图解与说明仅为了解释参数传递，计算机内存远比此复杂）

- 示例二

```js
var str1 = 'aaa'
var num2 = 2
var obj1 = {
  value: 1,
}

function foo(obj2) {
  obj2 = 2
  console.log(obj2) //2
}
foo(obj1)
console.log(obj1.value) // 2
```

在函数执行`obj2 = 2;`前后的内存状态
![ES函数20220613194012](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E5%87%BD%E6%95%B020220613194012.png)

### 引用传递

ES 函数的参数时按值传递的，部分语言支持参数按引用传递。
以上述示例二为例，若函数 foo 参数按引用传递，则传入是形参 obj2 直接记录实参 obj1 的内存地址。
故而后续不管两者谁变化，都将影响另一方。
即上述代码执行到最后，obj1 的值将会被变更为数字 2。
在 C#中，区分值传递和引用传递是方法参数前加 ref，加 ref 就是引用传递, 不加就是值传递。

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

# ES 中 Generator 函数

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 中 Generator 函数](#es-中-generator-函数)
  - [\*函数语法](#函数语法)
    - [基本语法](#基本语法)
    - [使用示例](#使用示例)
  - [执行过程重点值](#执行过程重点值)
    - [围绕 yield 产生的值](#围绕-yield-产生的值)
    - [yield 语句整体值](#yield-语句整体值)
    - [next 函数返回对象](#next-函数返回对象)
  - [自动执行](#自动执行)
  - [实战分析](#实战分析)
    - [fibonacci 函数](#fibonacci-函数)
    - [计数器](#计数器)
    - [自定义可迭代对象](#自定义可迭代对象)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## \*函数语法

### 基本语法

\*函数不同于普通函数执行它不会直接返回函数内部的结果（return），返回的是一个 Generator 指针对象。
Generator 对象不能通过构造函数直接生产，需要配合\*函数。
同时 Generator 对象 遵循[Iteration 迭代规范](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterable_protocol)。
这个规范规定了函数返回的迭代器对象(或其原型链)包含了 next、return 等函数。

Generator 对象通过调用自身的 next 方法，保证游标后移，并且 next 方法返回一个包含了 value 和 done（迭代器是否完成标识）的对象。

### 使用示例

```jsx
function* generator() {
  yield 1
  yield 2
  yield 3
}

const gen = generator() // "Generator { }"

console.log(gen.next().value) // 1
console.log(gen.next().value) // 2
console.log(gen.next().value) // 3
```

![ES中Generator函数20230217163224](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E4%B8%ADGenerator%E5%87%BD%E6%95%B020230217163224.png)

## 执行过程重点值

### 围绕 yield 产生的值

对于执行过程中涉及的值，围绕 yield，需要重点区分 yield 和其之后表达式整体的值， yield 之后表达式值。

```jsx
const a = yield b + c;
```

即这段代码中 a 的值，以及 b+c 的值。

### yield 语句整体值

yield 语句整体值，上述代码示例中 a 的值。
第 n 个 yield 语句整体值$a_n$，为第 n+1 次调用 next 时 传入的第一个参数的值，不传参即为 undefined。

```jsx
function* gen(x) {
  const y = yield x + 1
  console.log(y)
}

const g = gen(1)
g.next()
g.next(100)
// 100
```

上述代码打印的值 y 为 100。
这样设计的目的是让函数外部（主要是异步）获取的结果进行回传。

### next 函数返回对象

next 方法返回一个包含了 value 和 done（迭代器是否完成标识）的对象。
这里的 value 值与 yield 后的表达式有关，即上述代码示例 b + c 的值。

第 n 次执行 next 函数获取到的对象其 value 值等于第 n 个 yield 后的表达式的值$(a+b)_n$
若只有 n 个 yield 语句，第 n+1 次执行 next 函数获取到的对象 value 的值是 Generator 函数的返回值，超过 n+1 次执行得到 value 值是 undefined。

```jsx
function* gen(x) {
  const y = yield x + 1
  return 100
}

const g = gen(1)
console.log(g.next())
//{value: 2, done: false}
console.log(g.next())
//{value: 100, done: true}
console.log(g.next())
//{value: undefined, done: true}
```

yield 即生产的意思，yield 后的值不难理解成造出成果（value）。

## 自动执行

可以通过 while 来简单实现 generator 的自动执行。

```jsx
function* generator() {
  yield 1
  yield 2
  yield 3
}

const gen = generator()
while (!gen.next().done) {}
console.log(gen)
// generator {<closed>}
```

使用递归实现自动执行。

```jsx
function autoExec(gen) {
  if (!gen.next().done) {
    autoExec(gen)
  }
}
```

但是在实际开发过程中，往往有结合异步事件传值，获取最终结果等需求。
具体推荐这篇文章
[ES6 系列之 Generator 的自动执行](https://github.com/mqyqingfeng/Blog/issues/99)

但是在实际开发过程中，往往有结合异步事件传值，获取最终结果等需求。

## 实战分析

### fibonacci 函数

```jsx
function* fibonacci() {
  let current = 0
  let next = 1
  while (true) {
    const reset = yield (current[(current, next)] = [next, next + current])
    if (reset) {
      current = 0
      next = 1
    }
  }
}

const sequence = fibonacci()
console.log(sequence.next().value) // 0
console.log(sequence.next().value) // 1
console.log(sequence.next().value) // 1
console.log(sequence.next().value) // 2
console.log(sequence.next().value) // 3
console.log(sequence.next().value) // 5
console.log(sequence.next(true).value) // 0
console.log(sequence.next().value) // 1
console.log(sequence.next().value) // 1
console.log(sequence.next().value) // 2
```

### 计数器

```jsx
function* infinite() {
  let index = 0

  while (true) {
    yield index++
  }
}

const generator = infinite() // "Generator { }"

console.log(generator.next().value) // 0
console.log(generator.next().value) // 1
console.log(generator.next().value) // 2
```

### 自定义可迭代对象

内置的可迭代类有：
String，Array，TypedArray，Map 以及 Set

这些类的原型链上都包含

如下为自定义对象实现可迭代

```jsx
const myIterable = {
  *[Symbol.iterator]() {
    yield 1
    yield 2
    yield 3
  },
}
for (const value of myIterable) {
  console.log(value)
}
// 1
// 2
// 3

;[...myIterable] // [1, 2, 3]
```

该对象可使用 for...of 遍历，可使用展开运算法展开。

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github 仓库](https://github.com/skylinety/Blog)点亮 ⭐️

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator
> 
> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES 中 Generator 函数.html](http://www.skyline.show/ES中Generator函数.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

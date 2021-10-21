# Interface VS Abstract Class

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Interface VS Abstract Class](#interface-vs-abstract-class)
  - [Interface](#interface)
  - [Abstract Class](#abstract-class)
  - [综述](#综述)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warranty](#warranty)

<!-- /code_chunk_output -->

## Interface

在 JS 中，在没有技术文档或找到对应函数(对象)定义在代码中位置的情况下，我们很难确认：

- 函数参数方式
- 函数参数的类型
- 使用参数的方式
- 对象提供的方法与属性

同时，在对象中，多层嵌套时，需要写如下代码：
`a && a.b ** a.b.c()`
在 TS 中，与大多数面向对象编程语言一样，引入了 Interface。
Interface 用以描述对象结构
Interface 的职责在于签订契约，即使用该接口则必须实现该接口中的属性和方法。
使用时只需要知道接口，就可知道使用该接口对象的一些基础的构造。

## Abstract Class

虚拟类不能直接实例化。

```js
abstract class Base {
  abstract getName(): string;

  printName() {
    console.log("Hello, " + this.getName());
  }
}
var a = new Base() // Cannot create an instance of an abstract class.(

```

虚拟方法与虚拟属性只能存在与虚拟类中，均使用 abstract 关键字。
虽然 TS 未做错误校验，但虚拟类至少有一个虚拟方法，否则应该定义为实体类。
虚拟方法的主要职责是为其派生的实体类提供蓝图，后续实体类需要实现的方法与属性提供参考（需要实现其中定义的虚拟方法属性等）。

## 综述

| type           | 继承数                       | 使用时机 | 可否拥有实体方法 | 主要职责 |
| -------------- | ---------------------------- | -------- | ---------------- | -------- |
| Interface      | implements 多个接口          | 编译时   | true             | 签订契约 |
| Abstract Class | extends 一个基类（不管虚实） | 运行时   | false            | 绘制蓝图 |

虚拟类可在运行时使用，而接口只在编译时使用。例如对于接口，你不能使用 instanceof

```js
abstract class Base {
  abstract getName(): string;

  printName() {
    console.log("Hello, " + this.getName());
  }
}
interface IBase {
  getName(): string;

  printName():void
}
let x: any;

if (x instanceof IBase) { // Error: 'IBase' only refers to a type, but is being used as a value here.

}

if (x instanceof Base) { // OK

}

```

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warranty

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

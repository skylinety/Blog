# JS 对象的属性

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [JS 对象的属性](#js-对象的属性)
  - [属性描述符](#属性描述符)
    - [属性分类](#属性分类)
    - [Enumerable](#enumerable)
    - [Configurable](#configurable)
  - [属性创建](#属性创建)
    - [直接创建](#直接创建)
    - [Object.defineProperty() & Object.defineProperties()](#objectdefineproperty-objectdefineproperties)
    - [Object.create](#objectcreate)
  - [扩展、封印与冻结](#扩展-封印与冻结)
    - [preventExtensions](#preventextensions)
    - [seal](#seal)
    - [freeze](#freeze)
  - [屏蔽、检测与遍历](#屏蔽-检测与遍历)
    - [属性屏蔽](#属性屏蔽)
    - [属性检测](#属性检测)
    - [属性遍历](#属性遍历)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#Warrant)

<!-- /code_chunk_output -->

## 属性描述符

### 属性分类

- 数据属性
  - Configurable
  - Enumerable
  - Writable
  - Value
- 访问器属性
  - Configurable
  - Enumerable
  - Get
  - Set

### Enumerable

Enumerable 表示能否枚举，常见

### Configurable

Configurable 表示能否删除属性，能否修改某些属性描述符，能否将属性改为访问器(数据)属性。

configurable 一旦指定为 false，则 configurable、enumerable、value、get、set 将无法通过 Object.defineProperty()重新配置，删除对应的属性将不产生效果（严格模式导致错误），属性将不能转换（数据与访问器之间）

configurable 一旦指定为 false,此时的 Writable 如果是 true 则可以修改为 false，但是不能从 false 改为 true（只关不开）

configurable true，writable false 时，可以通过 Object.defineProperty()修改 value 的值，直接赋值无效；configurable false，writable true 时可以通过赋值直接修改 value 的值，通过 Object.defineProperty()指定 value 值将会报错

数据属性能否重新直接赋值取决于 writable
属性能否重新通过 defineProperty 定义属性描述与值以及被删除取决于 configurable

忽略 enumerable 为 false 属性的操作

![JS对象属性20210928105422](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%AF%B9%E8%B1%A1%E5%B1%9E%E6%80%A720210928105422.png)

## 属性创建

### 直接创建

直接建立的布尔型属性描述默认都是 true

```js
var a = { c: 1 };
Object.getOwnPropertyDescriptor(a, "c");
// {value: 1, writable: true, enumerable: true, configurable: true}
a.d = 2;
Object.getOwnPropertyDescriptor(a, "d");
//{value: 2, writable: true, enumerable: true, configurable: true}
```

### Object.defineProperty() & Object.defineProperties()

通过 Object.defineProperty()来定义或者修改属性

Object.defineProperty()接受三个参数，分别是对象名，属性名，描述符对象。

数据属性描述符对象只接受 configurable、enumerable、writable、value 四种属性中的一个或多个;访问器属性描述符对象只接受 configurable、enumerable、get、set 四种属性中的一个或多个。

描述符对象不指定 configurable、enumerable、writable 时，他们的默认值是 false；不指定 value、get、set 时，默认值是 undefined
在使用 defineProperty 时通常需要代码直接指定布尔型描述全为 true

```js
var a = {};
Object.defineProperty(a, "name", { value: "skyline" });
a; // {name: "skyline"}
a.name = "lala";
a; // {name: "skyline"} 修改不生效
Object.defineProperty(a, "name", { value: "skyline", writable: true }); // Uncaught TypeError: Cannot redefine property: name writeable是false，无法再改为true
Object.defineProperty(a, "age", { value: "18", configurable: true });
a.age = 19; // 19 修改不生效
a; // {name: "skyline", age: "18"}
Object.defineProperty(a, "age", { value: "18", writable: true });
a.age = 19;
a; // {name: "skyline", age: 19} 修改生效
```

### Object.create

Object.create 方法的第二个参数添加的对象属性，同样的，只指定 value 不指定其他将会导致 configurable、enumerable、writable 都是 false

```js
const obj = Object.create({}, { p: { value: 1 } });
Object.values(obj); // []
Object.getOwnPropertyDescriptor(obj, "p");
//{value: 1, writable: false, enumerable: false, configurable: false}
```

Object.getOwnPropertyDescriptor(s) 查看属性描述符

## 扩展、封印与冻结

### preventExtensions

Object.preventExtensions()禁止扩展，即防止对象添加新的属性，Object.isExtensible()检查是否可扩展

```js
const object1 = {};

Object.preventExtensions(object1);

try {
  Object.defineProperty(object1, "property1", {
    value: 42,
  });
} catch (e) {
  console.log(e);
  // expected output: TypeError: Cannot define property property1, object is not extensible
}
```

### seal

Object.seal()封印对象，防止对象添加新的属性，且将所有属性的 Configurable 置为 false Object.isSealed()检查是否被封印

### freeze

Object.freeze()冻结对象，防止对象添加新的属性，且将所有属性的 Configurable 置为 false ，数据属性的所有 writable 设置为 false，防止对象属性直接重新赋值， Object.isFrozen()检查是否被冻结

被冻结的对象一定被封印了；被封印的对象一定不能扩展。

当一个被封印的对象所有自有（实例）属性的描述符 writable 改为 false 时，那么此时它也是被冻结的，通过 isFrozen 返回 true

被冻结对象的访问器属性如果有 set 描述符，则它仍旧是可写的

## 屏蔽、检测与遍历

### 属性屏蔽

原型属性指存在于原型链上的属性。实例中创建与原型中同名的属性，会屏蔽原型中的属性值。delete 可以删除实例中的属性，来重新暴露原型中的属性

### 属性检测

hasOwnProperty()来获取自有（实例）属性

**in 操作符来确定属性是否存在于实例属性与原型链中**

属性检测不受枚举与否影响

[Detection](https://www.notion.so/f21a953fb05546148c673bb69ff7b17a)

```js
const obj = Object.create({}, { p: { value: 1 } });
Object.values(obj); // []
Object.getOwnPropertyDescriptor(obj, "p");
// {value: 1, writable: false, enumerable: false, configurable: false}
"p" in obj; // true
"valueOf" in obj; // true
obj.hasOwnProperty("p"); // true
obj.hasOwnProperty("valueOf"); // false
```

### 属性遍历

for-in 语句遍历所有可枚举的自有（实例）和原型属性

Object.keys()只会收录自有可枚举属性名在数组中

[Iteration](https://www.notion.so/91b7ac8e68c7480dbc50a20db50e1cc6)

```js
const obj = Object.create({}, { p: { value: 1 } });
Object.values(obj); // []
Object.getOwnPropertyDescriptor(obj, "p");
// {value: 1, writable: false, enumerable: false, configurable: false}
Object.getOwnPropertyNames(obj); //["p"]
Object.keys(obj); // []
```

![JS对象属性20210928105558](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%AF%B9%E8%B1%A1%E5%B1%9E%E6%80%A720210928105558.png)

常见方法需要可枚举，非常见不限制枚举

## BMW WARNING

### Bulletin

I am a bucolic migrant worker but I never walk backwards.

### Material

> 《JavaScript 高级程序设计》

### Warrant

> 本文作者： Skyline(lty)
> 版权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

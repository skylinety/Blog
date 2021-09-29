# JS 对象的创建

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [JS 对象的创建](#js-对象的创建)
  - [工厂模式](#工厂模式)
  - [构造函数模式](#构造函数模式)
    - [实现](#实现)
    - [优化](#优化)
  - [原型模式](#原型模式)
    - [实现](#实现-1)
    - [原型判定](#原型判定)
    - [原型重写](#原型重写)
    - [原型模式问题](#原型模式问题)
  - [组合构造与原型](#组合构造与原型)
  - [动态原型](#动态原型)
    - [实现](#实现-2)
    - [重写原型](#重写原型)
  - [寄生构造函数](#寄生构造函数)
  - [稳妥构造函数](#稳妥构造函数)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warranty](#warranty)

<!-- /code_chunk_output -->

## 工厂模式

工厂模式解决了创建多个对象的问题，但是没有解决对象识别问题（创建对象后其父对象？）

```js
function person(name) {
  var p = new Object();
  p.name = name;
  return p;
}

var me = person("skyline");
me.name; // 'skyline'
```

## 构造函数模式

### 实现

解决了对象识别问题

构造函数首字母都要大写，非构造函数小写字母开头

构造函数主要问题是方法会在实例中各自创建，me.say === you.say 说明了这个问题

```js
function Person(name) {
  this.name = name;
  this.say = function () {
    console.log(`My name is ${this.name}`);
  };
}

var me = new Person("skyline");
var you = new Person("hahaha");
me.say(); // My name is skyline
you.say(); // My name is hahaha
me.say === you.say; // false
```

### 优化

优化方案解决了方法不能复用的问题，但破坏了封装

```js
function sayName() {
  console.log(`My name is ${this.name}`);
}

function Person(name) {
  this.name = name;
  this.say = sayName;
}

var me = new Person("skyline");
var you = new Person("hahaha");
me.say(); // My name is skyline
you.say(); // My name is hahaha
me.say === you.say; // false
```

## 原型模式

### 实现

ES 中，无论何时创建的新函数，都会根据一组特定的规则来为函数添加一个指向原型对象名为 prototype 的指针属性，该原型对象自动获得一个 constructor 属性，属性指向该函数，而后基于原型对象添置实例共享的属性和方法

```js
function Person() {}

Person.prototype.name = "skyline";
Person.prototype.age = 27;
Person.prototype.sayName = function () {
  alert(this.name);
};
var skyline = new Person();
skyline.sayName(); // My name is skyline
skyline instanceof Person; // true
```

### 原型判定

调用构造函数创建一个新的实例之后，该实例内部包含一个指向构造函数原型对象的指针[[Prototype]]（内部属性）。多数浏览器实现了`__proto__`来获取[[Prototype]]内部属性

![JS对象创建20210928110402](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%AF%B9%E8%B1%A1%E5%88%9B%E5%BB%BA20210928110402.png)

可以通过 isPrototypeOf()与 getPrototypeOf()来确定与获取关系

```js
skyline.__proto__ == Person.prototype; // true
Object.getPrototypeOf(skyline) == Person.prototype; // true
Person.prototype.isPrototypeOf(skyline); // true
```

### 原型重写

为了更好的封装性，有时会进行原型重写。

重写原型对象会切断新原型对象与之前已存在的实例对象之间的联系，故重写需谨慎，最好在新建函数的时候重写

通过直接重写 prototype 时，注意将构造函数属性加上 constructor 属性来指定构造函数，此时重新设定的 constructor 属性是可枚举的，es 原生的是不可枚举的，可通过 Object.defineProperty()来定义 constructor

```js
Person.prototype = {
  //  constructor: Person, // 不指定构造函数
  say: function () {
    console.log(`My name is ${this.name}`);
  },
};
skyline.constructor === Person; // false
```

### 原型模式问题

- 属性和方法都共享，多个实例之间会相互影响
- 无法动态传递参数
- 组合构造与原型

## 组合构造与原型

组合使用两者，构造函数模式用于实例属性，原型模式用于定义方法和共享属性

应用最广泛的模式，没有在一个地方使用构造函数与原型，对于封装性而言，不算最佳

## 动态原型

### 实现

动态原型模式是将原型与自有的信息都封装在构造函数中，通过在必要情况下初始化原型，实现组合使用构造函数与原型的优点。

实质就是通过检查某个应该存在的方法是否有效来决定是否初始化原型方法，if 语句检查初始化后应该存在的任何属性或方法，检查其中一个即可

```js
function Person() {
  this.name = "skyline";
  if (typeof this.say != "function") {
    Person.prototype.say = function () {
      console.log(`My name is ${this.name}`);
    };
    Person.prototype.sayHi = function () {
      console.log(`Hi!${this.name}`);
    };
  }
}

var skyline = new Person();

skyline.say(); // My name is skyline
```

### 重写原型

在构造函数中通过对象字面量重写原型

```js
function Person() {
  this.name = "skyline";
  if (typeof this.say != "function") {
    // 不能再构造函数中直接用对象字面量重写原型，重写原型对象会切断新原型对象与之前已存在的实例对象之间的联系
    Person.prototype = {
      constructor: Person, // 指定构造函数
      say: function () {
        console.log(`My name is ${this.name}`);
      },
    };
  }
}

var skyline = new Person();
// 首次使用时，skyline的__proto__是指向
// 默认产生的原型对象，而不是由字面量创建的新原型对象，调用say将会找不到
skyline.say(); // VM846:1 Uncaught TypeError: skyline.say is not a function
```

![JS对象创建20210928110309](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%AF%B9%E8%B1%A1%E5%88%9B%E5%BB%BA20210928110309.png)

可以通过如下方式解决上述问题

```js
function Person() {
  this.name = "skyline";
  if (typeof this.say != "function") {
    // 不能再构造函数中直接用对象字面量重写原型，重写原型对象会切断新原型对象与之前已存在的实例对象之间的联系
    Person.prototype = {
      constructor: Person, // 指定构造函数
      say: function () {
        console.log(`My name is ${this.name}`);
      },
    };
    return new Person();
  }
}
```

## 寄生构造函数

new 操作符并把使用的包装函数叫做构造函数之外，此模式与工厂模式并没有区别

创建的对象与构造函数之间毫无关系

```js
function Person(name) {
  var p = new Object();
  p.name = name;
  return p;
}

var me = new Person("skyline");
me.name; // 'skyline'
me instanceof Person; // false
```

## 稳妥构造函数

- 稳妥对象是指没有公共属性，其方法不使用 this 的对象稳妥构造函数模式与寄生构造函数类似，有两点不同一是实例方法不引用 this，二是构造函数不使用 new。
- 如下代码中创建了一个稳妥对象，除了 say 没有其他方式可以访问传入构造函数的原始数据。保证了数据的安全性。
- 稳妥构造函数模式也跟工厂模式一样，无法识别对象所属类型

```js
function Person(name) {
  var p = new Object();
  var age = 27;
  p.say = function () {
    console.log(`My name is ${name} and I am ${age}`);
  };
  return p;
}

var me = Person("skyline");
```

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> 《JavaScript 高级程序设计》

### Warranty

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

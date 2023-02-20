# ES 类的使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 类的使用](#es-类的使用)
  - [静态（类）、实例、原型属性与方法](#静态类实例原型属性与方法)
    - [ES5](#es5)
    - [ES6](#es6)
    - [属性访问结论](#属性访问结论)
  - [Class](#class)
    - [原型方法语法糖](#原型方法语法糖)
    - [Class 中属性与方法的枚举性质](#class-中属性与方法的枚举性质)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 静态（类）、实例、原型属性与方法

### ES5

Baby 类

```js
//对象构造函数
function Baby(name) {
  var className = "Baby";
  //实例属性，每个实例私有，在对象实例化后调用，实例属性在对象实力化后创建
  this.name = name;
  this.weight = "3kg";

  this.hello = function () {
    console.log(this.name);
    console.log(this.msg()); //使用原型方法扩充的方法可以在类内部使用
    console.log(this.sex); //使用原型方法扩充的属性可以在类内部使用
    console.log(Baby.age, this.age); //静态属性调用时格式为[对象.静态属性]
  }; //对象方法
}

//类方法 (实际是静态方法直接调用)，只有类才能访问类方法，实例不能访问 ，在类方法中通过this只能访问类属性不能访问其他属性，即在本例中，Run方法只能访问到this.age
Baby.Run = function () {
  console.log("跑起来！！！");
};

//原型方法，如果原型方法当作静态方法直接调用时，this.name无法被调用
Baby.prototype.msg = function () {
  console.log("我叫：" + this.name);
};

//类属性 在类的外部。公有静态属性不能使用 【this.属性】，只能使用 【对象.属性】 调用，只有类才能访问类属性，实例不能访问
Baby.age = 20;

//原型属性，所有实例共有，【this.属性】这种写法访问时，先会访问实例对象属性，没有实例对象属性就会访问原型属性 ，也可以当成公有静态属性使用【对象.prototype.原型属性。
Baby.prototype.sex = "男娃娃";
```

使用

```js
//实例方法和原型方法需要实例化对象后才可以使
var bob = new Baby("bob");
Baby.name;
//"Baby" :每一个类都有一个基本的name属性

bob.name;
//"bob"

Baby.weight;
//undefined

bob.weight;
//"3kg"

Baby.hello();
//Uncaught TypeError: Baby.hello is not a function

bob.hello();
// bob
// 我叫：bob
// undefined :this.msg没有返回所以undefined
// 男娃娃
// 20 undefined

Baby.Run(); //跑起来！！！
//类方法也是静态方法，可以直接使用 【对象.静态方法()】

bob.run(); // TypeError: bob.run is not a function

Baby.msg();
// Uncaught TypeError: Baby.msg is not a function

Baby.prototype.msg();
// 我叫：undefined
//原型方法当成静态方法使用时【对象.prototype.方法()】

bob.msg();
// 我叫：bob
//原型方法必须实例化对象

bob.age;
// undefined
//错误，公有静态属性只能使用 【对象.属性】调用

Baby.age;
// 20

Baby.prototype.sex;
// 男娃娃
//原型属性当作静态属性使用时【对象.prototype.方法()】

Baby.sex;
// undefined

bob.sex;
// 男娃娃
```

### ES6

Baby 类

```js
class Baby {
  //实例属性、方法
  eat = "meat";
  constructor(x, y) {
    //实例属性、方法
    this.firstName = x;
    this.lastName = y;
    this.say = function () {
      return "skyline";
    };
  }

  //原型属性，使用存取器
  get prop() {
    return "skyline getter";
  }
  set prop(value) {
    console.log("skyline setter: " + value);
  }

  //原型方法

  toString() {
    return "(" + this.firstName + ", " + this.lastName + ")";
  }

  //类方法
  static hello() {
    return "hello skyline";
  }

  static hi() {
    return this.hello; //如果静态方法包含this关键字，这个this指的是类，而不是实例
  }
}
//类属性，ES6 在当前阶段，Class 内部只有静态方法，没有静态属性，可以直接指定类（静态）属性
Baby.age = 1;
```

### 属性访问结论

不论是哪种方式创建对象，基本遵循以下结论：

- 静态属性方法，可以直接通过类进行访问
- 实例属性方法是需要创建实例对象进行访问
- 静态与实例之间的属性与方法不能互访

## Class

### 原型方法语法糖

对于 ES6 的 Baby 类的 toString

```js
  toString() {
    return '(' + this.firstName + ', ' + this.lastName + ')';
  }
```

ES5 中可以看做是如下代码的语法糖

```js
Point.prototype.toString = function () {
  return "(" + this.firstName + ", " + this.lastName + ")";
};
```

### Class 中属性与方法的枚举性质

Reflect.ownKeys 可列出所有自有属性，不管枚举与否。
Object.keys 可列出可枚举的自有属性。

实例属性可枚举

```js
const skyline = new Baby(1, 1);
Reflect.ownKeys(skyline);
// (4) ['eat', 'firstName', 'lastName', 'say']
Object.keys(skyline);
// (4) ['eat', 'firstName', 'lastName', 'say']
```

原型属性与方法不可枚举，这与 ES5 中原型属性方法不同，其是可枚举的。

```js
Reflect.ownKeys(skyline.__proto__);
// (3) ['constructor', 'prop', 'toString']
Object.keys(skyline.__proto__);
//[]
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show)  欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

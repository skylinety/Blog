# Factory 工厂模式

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Factory 工厂模式](#factory-工厂模式)
  - [概述](#概述)
    - [变种](#变种)
    - [解耦](#解耦)
  - [简单工厂（静态工厂）](#简单工厂静态工厂)
    - [实现](#实现)
    - [图示](#图示)
    - [对象创建](#对象创建)
  - [工厂方法](#工厂方法)
    - [实现](#实现-1)
    - [使用](#使用)
    - [图示](#图示-1)
  - [抽象工厂](#抽象工厂)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#Warrant)

<!-- /code_chunk_output -->

## 概述

### 变种

虽然 ES 可以通过 new 关键字直接构造对象，但有时候，只有在具体业务场景中才能知道在多个候选对象中具体实例哪一个，我们可以把实例化的任务委托给工厂。

工厂的关键在于可扩展性，用于生成与管理包含部分相同特性的不同对象
『工厂模式』有三个变种，分别是『简单工厂模式』、『工厂方法模式』以及『抽象工厂模式』

### 解耦

工厂模式最大的好处就是解耦。
假设当前有多个页面都有造车的需求。
根据用户选择来造具体的车辆。
A 页面为华北工厂使用，B 页面为华南工厂使用。则存在如下代码。
`bmw.js`

```js
export function Bmw(model, price, maxSpeed) {
  this.model = model;
  this.price = price;
  this.maxSpeed = maxSpeed;
}
```

`a.js`

```js
import { Bmw } from "./bmw.js";
var type = $("#input").val();
if (type === "X5") new Bmw(type, 108000, 300);
if (type === "X6") new Bmw(type, 111000, 320);
```

`b.js`

```js
import { Bmw } from "./bmw.js";
var type = $("#input").val();
if (type === "X5") new Bmw(type, 108000, 300);
if (type === "X6") new Bmw(type, 111000, 320);
```

如果此时需求进行调整，需要新生产 X100 型号轿车？
如果工厂合作方调整，开始生产 Benz 轿车？
那么我们除了替换 Bmw 类，还要在各个使用 Bmw 的页面经行替换或修改对应代码。
如果很多地方都用到，那么替换就是一场灾难。
上述代码使用简单工厂很容易就规避这些问题。

## 简单工厂（静态工厂）

### 实现

**ES5**

```jsx
function bmwFactory(type) {
  if (type === "X5") return new Bmw(type, 108000, 300);
  if (type === "X6") return new Bmw(type, 111000, 320);
}

function Bmw(model, price, maxSpeed) {
  this.model = model;
  this.price = price;
  this.maxSpeed = maxSpeed;
}

module.exports = bmwFactory;
```

**ES6**

```jsx
class BmwFactory {
  static create(type) {
    if (type === "X5") return new Bmw(type, 108000, 300);
    if (type === "X6") return new Bmw(type, 111000, 320);
  }
}

class Bmw {
  constructor(model, price, maxSpeed) {
    this.model = model;
    this.price = price;
    this.maxSpeed = maxSpeed;
  }
}

export default BmwFactory;
```

直接使用 new 的方式来创建对象，客户(调用方)与 new 出来的这个对象和当前耦合，也就是，当前客户端(调用方)依赖着这个 new 出来的对象，不利于对象或相关逻辑调整！
采用简单工厂，如果我们修改了具体的实现类或添加相关类型，当需求有调整时，对客户(调用方)而言是完全不用修改。
简单工厂的缺点很明显，就是当有新需求时，需要不断地修改工厂代码。
优点也很明确，一个工厂来创建对象，代码量少且逻辑不复杂。
简单工厂将所有产品杂糅在一起，直接生产产品，对于只生产某种产品或结构类似的产品，使用此模式特别方便。

### 图示

### 对象创建

在[ES 对象的创建](https://github.com/skylinety/Blog/blob/03a9341704f535ad4d59a2ac513281bde5e7d22c/Docs/Major/JS/ES/%E5%A4%8D%E6%9D%82%E7%B1%BB%E5%9E%8B/ES%E5%AF%B9%E8%B1%A1%E5%88%9B%E5%BB%BA.md)的文章中，创建对象使用的工厂模式也是简单工厂。

```js
function person(name) {
  var p = new Object();
  p.name = name;
  return p;
}

var me = person("skyline");
me.name; // 'skyline'
```

## 工厂方法

### 实现

现在 Bmw 获得资本青睐，急速扩张，不仅要生产汽车，还要生产自行车。
如果继续使用简单工厂，所有不同类型产品放在一起，逻辑会随着产品的增加而越来越复杂和混乱。
将工厂进行拆分，不同类型产品由不同工厂生产。
工厂方法定义一个创建对象的工厂接口，让适配接口的子类工厂决定生产哪一类产品，而不是直接通过 new 调用产品类方法。
工厂方法使得类实例化延迟到其子类。

```js
abstract class Product {
	abstract getWheels(): void;
}

class Car extends Product {
  model: string;
  price: number;
  maxSpeed: number;
  constructor(model:string, price:number, maxSpeed: number) {
    super()
    this.model = model;
    this.price = price;
    this.maxSpeed = maxSpeed;
  }
	getWheels() {
    console.log('4 wheels');
  };
}
class Bike extends Product {
  model: string;
  price: number;
  maxSpeed: number;
  constructor(model:string, price:number, maxSpeed: number) {
    super()
    this.model = model;
    this.price = price;
    this.maxSpeed = maxSpeed;
  }
	getWheels():void  {
    console.log('2 wheels');
  };
}

interface ProductFactory {
	 createProduct(model: string):Product;
}

class CarFactory implements ProductFactory {
     createProduct(model: string): Product {
    if (model === "X5") return new Car(model, 108000, 300);
    if (model === "X6") return new Car(model, 111000, 320);
    return new Car("X5", 111000, 320);
    }
}
class BikeFactory implements ProductFactory {
     createProduct(model: string): Product {
    if (model === "X500") return new Bike(model, 18000, 30);
    if (model === "X600") return new Bike(model, 11000, 32);
    return new Bike("X500", 111000, 320);
    }
}


```

### 使用

```js
const bf: ProductFactory = new BikeFactory();
const b: Product = bf.createProduct("X500");
b.getWheels(); // 2 wheels
```

**优势**
采用工厂方法，使用方不需要负责产品的创建，只需明确工厂类的职责。
如果有新的产品增加,只需要增加一个具体的类和具体的工厂类即可
不会影响已有的代码,后期维护容易,增强系统的扩展性，避免了大量的 if-else 判断
**缺点**
额外代码较多

### 图示

在上诉例子中，对应的类图为
![Factory工厂模式20211027172323](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Factory%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F20211027172323.png)
工厂方法的类图如下
![Factory工厂模式20211027172311](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Factory%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F20211027172311.png)

[示例图源](https://github.com/skylinety/Blog/blob/main/Demos/Major/CS/DesignPatterns/Creational/factory.drawio)

## 抽象工厂

在工厂模式中，随着需求的增加，工厂会越来越多而难以管理和维护。
抽象工厂将提取产品共性，通过共性将工厂进行分类，以共性来划分工厂。
在上述例子中，可以通过轮胎数量来划分工厂。
抽象工厂应用较少，待续。

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> [fbeline/design-patterns-JS/blob](https://github.com/fbeline/design-patterns-JS/blob/master/docs.md#factory) > https://www.zhihu.com/question/27125796

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

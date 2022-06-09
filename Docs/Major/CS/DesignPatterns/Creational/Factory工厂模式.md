# Factory 工厂模式

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Factory 工厂模式](#factory-工厂模式)
  - [概述](#概述)
    - [工厂](#工厂)
    - [设计模式中的工厂](#设计模式中的工厂)
    - [解耦](#解耦)
  - [简单工厂（静态工厂）](#简单工厂静态工厂)
    - [实现](#实现)
  - [工厂方法](#工厂方法)
    - [实现](#实现-1)
    - [使用](#使用)
    - [类图图示](#类图图示)
  - [抽象工厂](#抽象工厂)
    - [实现](#实现-2)
    - [类图图示](#类图图示-1)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 概述

### 工厂

工厂这个词往往让人感到困惑，特别是与设计模式中的工厂模式杂糅在一起的时候。
一般来说，工厂可以指用于生产产品的一个函数、方法或者类。
对于工厂具体所指，一般可以从所读文章的上下文来得到。
如在对象创建的文章中，也采用的是工厂。

> 在[ES 对象的创建](https://github.com/skylinety/Blog/blob/03a9341704f535ad4d59a2ac513281bde5e7d22c/Docs/Major/JS/ES/%E5%A4%8D%E6%9D%82%E7%B1%BB%E5%9E%8B/ES%E5%AF%B9%E8%B1%A1%E5%88%9B%E5%BB%BA.md)的文章中，创建对象使用的也是工厂。

```js
function person(name) {
  var p = new Object()
  p.name = name
  return p
}

var me = person('skyline')
me.name // 'skyline'
```

另，如下常见的代码中，

```ts
class Person {
  create() {
    return new Object()
  }
  static createA() {
    return new Array()
  }
}
```

其 create 方法往往被叫做工厂方法。
于是在这类方法前加入 static 关键字也就被叫做静态工厂方法。
上述方法叫做工厂的思想很简单，调用他们都创建了新的产品，故就是工厂。
这与设计模式中的工厂模式往往容易混淆。
为了区分，我们可以把这种用包裹构造函数创建对象的方法叫做构建方法（Creation method）

### 设计模式中的工厂

虽然 ES 可以通过 new 关键字直接构造对象，但有时候，只有在具体业务场景中才能知道在多个候选对象中具体实例哪一个，我们可以把实例化的任务委托给工厂。

工厂的关键在于可扩展性，用于生成与管理包含部分相同特性的不同对象。
注意本文后续的工厂模式（工厂方法）指的是设计模式中的工厂。
『工厂模式』有三个变种，分别是『简单工厂模式』、『工厂方法模式』以及『抽象工厂模式』

### 解耦

工厂模式最大的好处就是解耦。
假设当前有多个页面都有造车的需求。
根据用户选择来造具体的车辆。
A 页面为华北工厂使用，B 页面为华南工厂使用。则存在如下代码。
`bmw.js`

```js
export function Bmw(model, price, maxSpeed) {
  this.model = model
  this.price = price
  this.maxSpeed = maxSpeed
}
```

`a.js`

```js
import { Bmw } from './bmw.js'
var type = $('#input').val()
if (type === 'X5') new Bmw(type, 108000, 300)
if (type === 'X6') new Bmw(type, 111000, 320)
```

`b.js`

```js
import { Bmw } from './bmw.js'
var type = $('#input').val()
if (type === 'X5') new Bmw(type, 108000, 300)
if (type === 'X6') new Bmw(type, 111000, 320)
```

如果此时需求进行调整，需要新生产 X100 型号轿车？
如果工厂合作方调整，开始生产 Benz 轿车？
那么我们除了替换 Bmw 类，还要在各个使用 Bmw 的页面进行替换或修改对应代码。
如果很多地方都用到，那么替换就是一场灾难。
上述代码使用简单工厂很容易就规避这些问题。

## 简单工厂（静态工厂）

### 实现

**ES5**

```jsx
function bmwFactory(type) {
  if (type === 'X5') return new Bmw(type, 108000, 300)
  if (type === 'X6') return new Bmw(type, 111000, 320)
}

function Bmw(model, price, maxSpeed) {
  this.model = model
  this.price = price
  this.maxSpeed = maxSpeed
}

module.exports = bmwFactory
```

**ES6**

```jsx
class BmwFactory {
  static create(type) {
    if (type === 'X5') return new Bmw(type, 108000, 300)
    if (type === 'X6') return new Bmw(type, 111000, 320)
  }
}

class Bmw {
  constructor(model, price, maxSpeed) {
    this.model = model
    this.price = price
    this.maxSpeed = maxSpeed
  }
}

export default BmwFactory
```

直接使用 new 的方式来创建对象，客户(调用方)与 new 出来的这个对象和当前耦合，也就是，当前客户端(调用方)依赖着这个 new 出来的对象，不利于对象或相关逻辑调整！
采用简单工厂，如果我们修改了具体的实现类或添加相关类型，当需求有调整时，对客户(调用方)而言是完全不用修改。
简单工厂的缺点很明显，就是当有新需求时，需要不断地修改工厂代码。
优点也很明确，一个工厂来创建对象，代码量少且逻辑不复杂。
简单工厂将所有产品杂糅在一起，直接生产产品，对于只生产某种产品或结构类似的产品，使用此模式特别方便。

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

工厂方法要求不同的工厂要生产具有相同超类或实现同一接口的产品。
如上例中的产品都实现了 Product 接口。

### 使用

```js
const bf: ProductFactory = new BikeFactory()
const b: Product = bf.createProduct('X500')
b.getWheels() // 2 wheels
```

**优势**
采用工厂方法

- 使用方不需要负责产品的创建，只需明确工厂类的职责
- 使用方不关注产品如何创建，创建产品不需要知道其实体类（创建 bike x500 并不需要知道其实体类 Bike）

如果有新的产品增加,只需要增加一个具体的类和具体的工厂类即可
不会影响已有的代码,后期维护容易,增强系统的扩展性，避免了大量的 if-else 判断

**缺点**
额外代码较多

### 类图图示

在上诉例子中，对应的类图为
![Factory工厂模式20211123154744](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Factory%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F20211123154744.png)
工厂方法的类图如下
![Factory工厂模式20211123154758](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Factory%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F20211123154758.png)

[示例图源](https://github.com/skylinety/Blog/blob/main/Demos/Major/CS/DesignPatterns/Creational/factory.drawio)

## 抽象工厂

### 实现

抽象工厂将提取产品共性。
通过共性将工厂进行分类，以共性来划分工厂。
例如在上述例子中，客户只有山地的需求，只会购买山地能力的交通工具。
这时，可以将山地越野自行车与汽车化为一类，将城市车划为另一类。
**抽象工厂让客户能够生产同一系列的产品而不需要知道其中每个产品对应的实体类。**

```ts
interface AbstractVehicleFactory {
  createCar(): AbstractCar

  createBike(): AbstractBike
}

/**
 * 越野车辆（off-road vehicle）
 */
class ORVFactory implements AbstractVehicleFactory {
  public createCar(): AbstractCar {
    return new ORVCar()
  }

  public createBike(): AbstractBike {
    return new ORVBike()
  }
}
/**
 * 城市车辆
 */
class UrbanVehicleFactory implements AbstractVehicleFactory {
  public createCar(): AbstractCar {
    return new UrbanCar()
  }

  public createBike(): AbstractBike {
    return new UrbanBike()
  }
}

interface AbstractCar {
  desc(): string
}

class ORVCar implements AbstractCar {
  public desc(): string {
    return '越野汽车'
  }
}

class UrbanCar implements AbstractCar {
  public desc(): string {
    return '城市汽车'
  }
}

interface AbstractBike {
  desc(): string

  withCar(car: AbstractCar): string
}

class ORVBike implements AbstractBike {
  public desc(): string {
    return '越野自行车'
  }

  public withCar(car: AbstractCar): string {
    const result = car.desc()
    return `${this.desc()}与${result}都用于越野`
  }
}

class UrbanBike implements AbstractBike {
  public desc(): string {
    return '城市自行车'
  }

  public withCar(car: AbstractCar): string {
    const result = car.desc()
    return `${this.desc()}与${result}都用于城市`
  }
}

function clientCode(factory: AbstractVehicleFactory) {
  const Car = factory.createCar()
  const Bike = factory.createBike()

  console.log(Bike.desc())
  console.log(Bike.withCar(Car))
}

clientCode(new ORVFactory())
// "越野自行车"
// "越野自行车与越野汽车都用于越野"
clientCode(new UrbanVehicleFactory())
// "城市自行车"
// "城市自行车与城市汽车都用于城市"
```

使用工厂模式还是抽象工厂取决于需要是某种产品还是产品系列的需求。
工厂模式对应的需求是买车还是买自行车
抽象工厂对应的是山村客户还是城市客户买系列交通工具的需求

### 类图图示

![Factory工厂模式20211123162628](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Factory%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F20211123162628.png)

[类图图源](https://github.com/skylinety/Blog/blob/54a10cfbabd061ae15c5afb1914fb749238c0bed/Demos/Major/CS/DesignPatterns/Creational/abstractFactory.drawio)

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](http://www.skyline.show)  欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> [fbeline/design-patterns-JS/blob](https://github.com/fbeline/design-patterns-JS/blob/master/docs.md#factory) > https://www.zhihu.com/question/27125796

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

# Builder 建筑工模式

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Builder 建筑工模式](#builder-建筑工模式)
  - [概述](#概述)
  - [实例](#实例)
    - [修房子](#修房子)
    - [找工人](#找工人)
    - [监工](#监工)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#Warrant)

<!-- /code_chunk_output -->

## 概述

Builder 模式一般翻译为建造者模式。
在重构代码的过程中，我们常看到几百上千行的复杂类。
这些类往往由于最初设定不合理以及需求不断增加而壮大。
建筑工模式主要思想是我们将类的实例（产品）构建相关的代码单独交给一个类来实现。
建筑工模式通常支持链式调用。

```js
House.setDoors(1).setRooms(2).getHouse();
```

## 实例

### 修房子

现在有一个基础房屋类如下所示

```ts
class House {
  public windows: string[] = [];
  public doors: string[] = [];
  public rooms: string[] = [];
  public area: number = 0;
  public parts: string[] = [];
  constructor() {
    this.setWindows("window");
    this.setDoors("door");
    this.setBedRooms("room");
  }
  public listWindows(): House {
    console.log(`House windows: ${this.windows.join(", ")}\n`);
    return this;
  }
  public listDoors(): House {
    console.log(`House doors: ${this.doors.join(", ")}\n`);
    return this;
  }
  public listRooms(): House {
    console.log(`House rooms: ${this.rooms.join(", ")}\n`);
    return this;
  }

  public setWindows(w: string): House {
    this.windows.push(w);
    return this;
  }
  public setDoors(d: string): House {
    this.doors.push(d);
    return this;
  }
  public setBedRooms(r: string): House {
    this.rooms.push(r);
    this.area += 30;
    return this;
  }
  public setKitchens(r: string): House {
    this.rooms.push(r);
    this.area += 20;
    return this;
  }
  public capacity(): number {
    return this.area / 15;
  }
}
```

现在生活水平不断提高，我们开始有不同的要求，有车的人需要有车库的房子，有人需要有花园的，有泳池，有庭院等的房子。
一种常用的方法是，基于 House 类派生出 HouseWithGarage、HouseWithPool、HouseWithYard...

```ts
class HouseWithGarage extends House {
  constructor() {
    super();
    this.setGarges("garage");
  }
  public listGarges(): House {
    console.log(`House parts: ${this.parts.join(", ")}\n`);
    return this;
  }
  public setGarges(g: string): House {
    this.parts.push(g);
    return this;
  }
}
```

```js
const hg = new HouseWithGarage();
console.log("builderProblem.ts第63行:::hg", hg);
```

使用后得到如下的建筑

```json
{
  "windows": ["window"],
  "doors": ["door"],
  "rooms": ["room"],
  "area": 30,
  "parts": ["garage"]
}
```

[详细代码](https://github.com/skylinety/Blog/blob/main/Demos/Major/CS/DesignPatterns/Creational/builder/builderProblem.ts)
当又有智能家居、新风系统等新需求来的时候，相关的派生类变得非常多。
![Builder建筑工模式20211104113645](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Builder%E5%BB%BA%E7%AD%91%E5%B7%A5%E6%A8%A1%E5%BC%8F20211104113645.png)

另一种基本不会用的方法是直接在构造函数中进行相关配置并初始化。

```ts
class House {
    ...,
    constructor(hasGarage: boolean, hasYard: boolean, hasPool: boolean, ...) {
        this.setWindows('east-window');
        this.setDoors('east-door');
        this.setBedRooms('east-room');
        if(hasGarage) {
            this.setGarges("garage");
        }
    }
    ...
}
```

调用的时候会出现如下情况

```js
new House(true, null, true, ...);
new House(null, null, true, ...);
```

![Builder建筑工模式20211104113734](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Builder%E5%BB%BA%E7%AD%91%E5%B7%A5%E6%A8%A1%E5%BC%8F20211104113734.png)
上述方案虽然可以解决一定的问题，但是在易用性与维护性方面大打折扣。
这些场景中的建筑工可以很好地解决问题。

### 找工人

在 House 类中，有最终生产与配置房屋实例相关的方法（set...)。
这些方法都为构建产品而立，我们可以把这些工作都交给建筑工。

```ts
class House {
  public windows: string[] = [];
  public doors: string[] = [];
  public rooms: string[] = [];
  public area: number = 0;
  public parts: string[] = [];
  [s: string]: any;
  public listWindows(): House {
    console.log(`House windows: ${this.windows.join(", ")}\n`);
    return this;
  }
  public listDoors(): House {
    console.log(`House doors: ${this.doors.join(", ")}\n`);
    return this;
  }
  public listRooms(): House {
    console.log(`House rooms: ${this.rooms.join(", ")}\n`);
    return this;
  }

  public capacity(): number {
    return this.area / 15;
  }
}
/**
 * 建筑者接口，提供创建产品的基本方法与步骤
 */
interface Builder {
  setBase(): Builder;
  setKitchens(r: string): Builder;
  setGarges(g: string): Builder;
  setPools(g: string): Builder;
  setYards(g: string): Builder;
}

/**
 * 建筑者实体类。不同的建筑者实体类可以对方法进行不同实现
 */
class HouseABuilder implements Builder {
  private house!: House;

  constructor() {
    this.reset();
  }

  public reset(): House {
    this.house = new House();
    return this.house;
  }
  /**
   *
   * @returns 提供this 链式调用
   */
  public setBase(): Builder {
    this.setWindows("window");
    this.setDoors("door");
    this.setBedRooms("room");
    return this;
  }

  public setWindows(w: string): Builder {
    this.house.windows.push(w);
    return this;
  }
  public setDoors(d: string): Builder {
    this.house.doors.push(d);
    return this;
  }
  public setBedRooms(r: string): Builder {
    this.house.rooms.push(r);
    this.house.area += 30;
    return this;
  }

  public setKitchens(r: string): Builder {
    this.house.rooms.push(r);
    this.house.area += 20;
    return this;
  }
  public setGarges(g: string): Builder {
    this.house.parts.push(g);
    return this;
  }
  public setPools(g: string): Builder {
    this.house.parts.push(g);
    return this;
  }
  public setYards(g: string): Builder {
    this.house.parts.push(g);
    return this;
  }

  /**
   *
   * 暴露产品的方法。
   * 在将现有产品交付后，建筑工通常需要初始化一个新的产品，供后续调用。
   * 此处通过reset，这不是必须的，可以在客户使用时显示调用reset
   */
  public getHouse(): House {
    const result = this.house;
    this.reset();
    return result;
  }
}
```

现在我们可以请建筑工来帮我们建筑不同的房子。

```js
const builder = new HouseABuilder();
builder.setBase().setGarges("garage").setYards("yard");
const gy = builder.getHouse();
console.log("builder.ts第85行:::gy", gy);
builder.setBase().setGarges("garage");
const g = builder.getHouse();
console.log("builder.ts第88行:::g", g);
builder.setBase().setPools("pool");
const p = builder.getHouse();
console.log("builder.ts第91行:::p", p);
```

得到如下的结果

```json
[LOG]: "builder.ts第85行:::gy",  House: {
  "windows": [
    "window"
  ],
  "doors": [
    "door"
  ],
  "rooms": [
    "room"
  ],
  "area": 30,
  "parts": [
    "garage",
    "yard"
  ]
}
[LOG]: "builder.ts第88行:::g",  House: {
  "windows": [
    "window"
  ],
  "doors": [
    "door"
  ],
  "rooms": [
    "room"
  ],
  "area": 30,
  "parts": [
    "garage"
  ]
}
[LOG]: "builder.ts第91行:::p",  House: {
  "windows": [
    "window"
  ],
  "doors": [
    "door"
  ],
  "rooms": [
    "room"
  ],
  "area": 30,
  "parts": [
    "pool"
  ]
}
```

[详细代码](https://github.com/skylinety/Blog/blob/main/Demos/Major/CS/DesignPatterns/Creational/builder/builder.ts)

通过找建筑工帮忙，我们的产品交付给客户时只剩下客户关心的配置。
当客户有不同客制化需求时，我们只需让建筑工工程师帮忙发挥他的技能即可。
建筑工模式让我们再构建一个产品时让建筑工来执行一系列步骤，通过执行不同步骤来定制不同的产品。
虽然当前的建筑工技能已经比较全面，但是某项特定的需求也可能差异化。
例如，建筑普通房子的窗可能只需要挖个洞，而富豪的窗是需要镶钻的。
普通的院子大小只能让小孩打滚，富豪的院子则需要能打高尔夫。
这时候，我们需要差异化建筑工，用不同的建筑工，构建不同的房子。
![Builder建筑工模式20211104140334](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Builder%E5%BB%BA%E7%AD%91%E5%B7%A5%E6%A8%A1%E5%BC%8F20211104140334.png)
当不同的建筑工越来越多时，什么时候用什么样的工人，需要统一管理，我们引入监工。

### 监工

```ts
/**
 * 引入监工是为指定的需求做定制，
 * 如此处定制基础房屋、小房子、大房子等
 * 另一个用处是调配工人
 * 这不必须的。客户也可去掉这个中间商，直接去找工人
 */
class Director {
  private builder: Builder;

  /**
   * 调配工人
   */
  public setBuilder(builder: Builder): void {
    this.builder = builder;
  }

  /**
   * 建筑基础房子
   */
  public buildMini(): void {
    this.builder.setBase();
  }

  public buildMedium(): void {
    this.builder.setBase().setGarges("garage").setYards("yard");
  }
  public buildLarge(): void {
    this.builder
      .setBase()
      .setGarges("garage")
      .setYards("yard")
      .setPools("pool");
  }
}
```

监工的使用

```ts
const director = new Director();
const builderA = new HouseABuilder();
director.setBuilder(builderA);
director.buildLarge();
const f = builderA.getHouse();
console.log("director.ts第214行:::large base house", f);

const builderB = new HouseBBuilder();
director.setBuilder(builderB);
director.buildMedium();
const m = builderB.getHouse();
console.log("director.ts第214行:::medium diamond house", m);
```

得到如下的结果

```js
[LOG]: "director.ts第214行:::large base house",  House: {
  "windows": [
    "window"
  ],
  "doors": [
    "door"
  ],
  "rooms": [
    "room"
  ],
  "area": 30,
  "parts": [
    "garage",
    "yard",
    "pool"
  ]
}
[LOG]: "director.ts第214行:::medium diamond house",  House: {
  "windows": [
    "Diamond window"
  ],
  "doors": [
    "Diamond door"
  ],
  "rooms": [
    "Diamond room"
  ],
  "area": 300,
  "parts": [
    "Diamond garage",
    "Diamond yard"
  ]
}

```

监工的引入不是必须的，根据实际的需求，选用简单的建筑工还是引入监工。

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show)  欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://refactoring.guru/design-patterns/builder > https://refactoring.guru/design-patterns/builder/typescript/example

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

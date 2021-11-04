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
 * 该建筑工只能建普通房子
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
   * @returns this 提供链式调用
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
/**
 * 建筑者实体类。不同的建筑者实体类可以对方法进行不同实现
 * 该建筑工能建镶钻的房子
 * 在具体项目中，不同方法的实现差异化更多
 * 此处简单添加Diamond前缀
 */
class HouseBBuilder implements Builder {
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
    this.house.windows.push("Diamond " + w);
    return this;
  }
  public setDoors(d: string): Builder {
    this.house.doors.push("Diamond " + d);
    return this;
  }
  public setBedRooms(r: string): Builder {
    this.house.rooms.push("Diamond " + r);
    this.house.area += 300;
    return this;
  }

  public setKitchens(r: string): Builder {
    this.house.rooms.push("Diamond " + r);
    this.house.area += 200;
    return this;
  }
  public setGarges(g: string): Builder {
    this.house.parts.push("Diamond " + g);
    return this;
  }
  public setPools(g: string): Builder {
    this.house.parts.push("Diamond " + g);
    return this;
  }
  public setYards(g: string): Builder {
    this.house.parts.push("Diamond " + g);
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
/**
 * 引入监工是为指定的需求做定制，
 * 如此处定制基础房屋、一般房屋、全套宫殿等
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

# Factory 工厂模式

## 概述

虽然 ES 可以通过 new 关键字直接构造对象，但有时候，只有在具体业务场景中才能知道在多个候选对象中具体实例哪一个，我们可以把实例化的任务委托给工厂函数。

工厂函数的关键在于可扩展性，用于生成与管理包含部分相同特性的不同对象

## 实现

### ES5

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

### ES6

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

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> [fbeline/design-patterns-JS/blob](https://github.com/fbeline/design-patterns-JS/blob/master/docs.md#factory)

### Warranty

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

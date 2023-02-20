# ES 继承的实现

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 继承的实现](#es-继承的实现)
  - [原型链](#原型链)
    - [概述](#概述)
    - [代码示例](#代码示例)
    - [优劣分析](#优劣分析)
  - [构造函数](#构造函数)
    - [概述](#概述-1)
    - [代码示例](#代码示例-1)
    - [优劣分析](#优劣分析-1)
  - [组合继承](#组合继承)
    - [概述](#概述-2)
    - [代码示例](#代码示例-2)
    - [优劣分析](#优劣分析-2)
  - [原型式继承(Object.create)](#原型式继承objectcreate)
    - [概述](#概述-3)
    - [代码示例](#代码示例-3)
    - [优劣分析](#优劣分析-3)
  - [寄生式继承](#寄生式继承)
    - [概述](#概述-4)
    - [代码示例](#代码示例-4)
    - [优劣分析](#优劣分析-4)
  - [寄生组合式继承](#寄生组合式继承)
    - [概述](#概述-5)
    - [代码示例](#代码示例-5)
    - [优劣分析](#优劣分析-5)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 原型链

### 概述

由于函数没有签名，ES无法实现接口继承

原型链继承的本质是重写原型对象，代之以一个新类型的实例

通过instanceof isPrototypeOf 来判定原型与实例的关系

给原型添加方法需要在替换原型之后

通过原型链继承，不能通过字面量重写原型

### 代码示例

```jsx
function Person(name) {
    // 两只眼睛两条腿
    this.eyes = 'two'
    this.feet = 'two'
    this.families = ['papa', 'mama']
}

function Man() {
    this.sex = 'male'
}
function Woman() {
    this.sex = 'female'
}
Man.prototype = new Person()
var skyline = new Man()
skyline.families.push('sister', 'grandma')
var haha = new Man()

console.log(haha.families) // ["papa", "mama", "sister", "grandma"]
skyline.__proto__ == Man.prototype // true
Man.prototype.__proto__ == Person.prototype // true

haha.eyes = 2
skyline.eyes // 'two'
```

### 优劣分析

采用原型链继承无法避免原型中共享值所带来的问题。
同时无法向超类型构造函数传递参数，实际很少使用（在创建 Man 的实例时，不能向Person传参）

上述示例中haha.eyes = 2 后skyline值不变并不是eyes没有通过原型共享，而是因为haha在其自身添加了实例属性eyes。

进一步尝试如下代码

```jsx
haha.__proto__.eyes = 2
skyline.eyes // 2
```

## 构造函数

### 概述

为解决原型链继承引用问题而引入，同时解决了无法向超类型传递参数的问题。又称为伪造对象或经典继承

基本思想是子类型构造函数内部调用超类型构造函数

为保证调用超类构造函数不会重写子类属性，需要先调用超类构造函数

### 代码示例

```jsx
function Person(name) {
    // 两只眼睛两条腿
    this.eyes = 'two'
    this.feet = 'two'
    this.families = ['papa', 'mama']
}

function Man() {
    Person.call(this)
    this.sex = 'male'
}
var skyline = new Man()
console.log(skyline.feet) // two
```

### 优劣分析

此方式最大的问题是将产生可以公共使用的方法多次创建，无法复用共有方法。


## 组合继承

### 概述

又称为伪经典继承，就是组合使用原型链和构造函数模式

组合继承是最为常见的继承方式

### 代码示例

```jsx
function Person(name) {
    // 两只眼睛两条腿
    this.name = name
    this.eyes = 'two'
    this.feet = 'two'
    this.families = ['papa', 'mama']
}

Person.prototype.say = function() {
    console.log(`My name is ${this.name}`)
} // 共享的原型属性在这

function Man(name) {
    Person.call(this, name) // 私有的实例属性在这
    this.sex = 'male'
}
Man.prototype = new Person() 
var skyline = new Man('skyline')
skyline.say() // My name is skyline
skyline.families.push('sister', 'grandma')
var haha = new Man('haha')
console.log(skyline.families) // ["papa", "mama", "sister", "grandma"]
console.log(haha.families) // ["papa", "mama"]
console.log(skyline.feet) // two
```

### 优劣分析

Man.prototype通过调用构造函数获取了Person内部的那些实例属性。
这导致超类型Person实例属性同时存在于子（孙）类型原型（链）与实例属性中，造成浪费。
注意，在重复的属性中，实例属性会覆盖原型属性。

![ES继承的实现![Untitled](Untitled.png)](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E7%BB%A7%E6%89%BF%E7%9A%84%E5%AE%9E%E7%8E%B0!%5BUntitled%5D(Untitled.png).png)



## 原型式继承(Object.create)

### 概述

借助原型可以基于已有的对象创建新对象，不必因此创建自定义类型，大致思路如下代码所示

### 代码示例

```jsx
function create(o) {
    var F = function() {}
    F.prototype = o
    return new F()
}

a = {}
b = create(a)
b.__proto__ == a // true
```

**该函数为了实现`b.__proto__ == a`的效果**

### 优劣分析

采用此方法与原型链方式相似，类型a中包含引用类型的属性始终会被共享。

ES6新增了Object.create方法规范了原型式继承。

## 寄生式继承

### 概述

创建一个仅用于封装继承过程的函数，函数内部以某种方式来增强对象

### 代码示例

```jsx
function createA(o) {
    var clone = Object.create(o) // 调用任意一个可以返回对象的函数
    clone.say = function() { // 增强对象
        console.log('hahaha')
    }
    return clone // 返回对象
}
```

### 优劣分析

与构造函数类似，方法不能复用


## 寄生组合式继承

### 概述

组合式继承会导致超类型构造函数的两次调用，超类型的实例属性将分别在原型中和实例中被复制而产生两组，实例属性屏蔽了原型中的属性

问题的原因是Man.prototype = new Person() 时让原型产生冗余属性，这一步的目的是使得 `Man.prototype__proto__ == Person.prototype` 。
优化时仅需考虑而是间接的让上述等式成立即可。

最为理想的继承方式

💡 寄生组合式继承，就是通过借用构造函数来继承属性，通过原型链混成形式来继承方法

### 代码示例

```jsx
function copyPrototype(subType, superType) {
    var p = Object.create(superType.prototype) // p.__proto__ == superType.prototype
    p.constructor = subType
    subType.prototype = p
}

function Person(name) {
    // 两只眼睛两条腿
    this.name = name
    this.eyes = 'two'
    this.feet = 'two'
    this.families = ['papa', 'mama']
}

Person.prototype.say = function() {
    console.log(`My name is ${this.name}`)
}
        
function Man(name) {
    Person.call(this, name)
    this.sex = 'male'
}

copyPrototype(Man, Person)
// Man.prototype.__proto__ == Person.prototype

var skyline = new Man('skyline')
skyline.say() // My name is skyline
skyline.families.push('sister', 'grandma')
var haha = new Man('haha')

console.log(skyline.families) // ["papa", "mama", "sister", "grandma"]
console.log(haha.families) // ["papa", "mama"]
console.log(skyline.feet) // two
skyline.__proto__.__proto__ == Person.prototype //true
skyline.__proto__ == Man.prototype //true

Man.prototype.__proto__ == Person.prototype //true
Man.__proto__ == Person.prototype //false
Man.__proto__ == Function.prototype //true
```

### 优劣分析

子类想要在原型上添加方法，由于subType.prototype = p 进行了赋值，必须在继承之后(copyPrototype后)添加，否则赋值将覆盖掉原有原型上的方法。

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️


> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  《JavaScript 高级程序设计》

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES继承的实现.html](http://www.skyline.show/ES继承的实现.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

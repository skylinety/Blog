# UML 类图画图图解

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [UML 类图画图图解](#uml-类图画图图解)
  - [简介](#简介)
  - [Object](#object)
    - [Classes](#classes)
    - [Interface](#interface)
    - [Abstract Classes](#abstract-classes)
  - [Relations](#relations)
    - [Dependency](#dependency)
    - [Association](#association)
    - [Aggregation](#aggregation)
    - [Composition](#composition)
    - [Inheritance](#inheritance)
  - [BMW WARNING](#bmw-warning)


<!-- /code_chunk_output -->

## 简介

统一建模语言（Unified Modeling Language）简写 UML

## Object

### Classes

在面向对象编程语言中，常使用 UML 画对象关系图。
Class 图包含三个部分(三行)

- 类名
- 属性与属性类型
- 方法名、方法参数与返回值类型

![UML画图图解20211027144207](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/UML%E7%94%BB%E5%9B%BE%E5%9B%BE%E8%A7%A320211027144207.png)
属性方法访问符标记

- Public (+)
- Private (-)
- Protected (#)
- Package (~)
- Derived (/)
- Static (underlined)

### Interface

Interface 与 Class 类似，只需在第一层类名头部加上 `<<interface>>`即可，接口第二层一般为空。
![UML类图画图图解20211101113439](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/UML%E7%B1%BB%E5%9B%BE%E7%94%BB%E5%9B%BE%E5%9B%BE%E8%A7%A320211101113439.png)

### Abstract Classes

Abstract Classes 与 Interface 类似，只需在第一层类名头部加上 `<<abstract>>`即可

## Relations

### Dependency

依赖关系
是一种弱关联关系。
依赖（Dependency）体现的是对象间的使用关系，即 'use a' 的关系。
类在其方法中使用了另一个类（类实例）
![UML画图图解20211027161917](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/UML%E7%94%BB%E5%9B%BE%E5%9B%BE%E8%A7%A320211027161917.png)
图示 Person 的 hasRead 方法使用了 Book 实例，存在依赖关系。

### Association

关联关系
即是强关联，存在两种。
**Unidirectional Association**

单边关系
类某个属性引用了另一个类（类实例）

![UML画图图解20211027162204](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/UML%E7%94%BB%E5%9B%BE%E5%9B%BE%E8%A7%A320211027162204.png)
图示 Person 的 owns 属性引用了一组 Book 实例

**Bidirectional Association**

双边关系
类互相引用了对应的类（实例）
![UML画图图解20211027162339](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/UML%E7%94%BB%E5%9B%BE%E5%9B%BE%E8%A7%A320211027162339.png)
图示 Person 的 owns 属性引用了一组 Book 实例，Book 的 owners 储存了一组 Person 实例
在 UML 中，通过放置多重性（multipicity）表达式在关联线的末端来表示。多重性表达式可以是一个数字、一段范围或者是它们的组合。多重性允许的表达式示例如下

- 数字：精确的数量
- \*或者 0..\*：表示 0 到多个
- 0..1：表示 0 或者 1 个，在 Java 中经常用一个空引用来实现
- 1..\*：表示 1 到多个

### Aggregation

聚合关系，是一种弱依赖关系。整体不存在，部分可依旧存在。
聚合（Aggregation）体现的是整体与部分的拥有关系，即 'has a' 的关系。此时整体与部分之间是可分离的，它们可以具有各自的生命周期，部分可以属于多个整体对象，也可以为多个整体对象共享，所以聚合关系也常称为共享关系。
用空心菱形和实线表示。
![UML类图画图图解20211101140847](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/UML%E7%B1%BB%E5%9B%BE%E7%94%BB%E5%9B%BE%E5%9B%BE%E8%A7%A320211101140847.png)

### Composition

组合关系（如螺丝钉，整体的一部分），是一种强依赖关系。整体不存在，则部分一定消失。
组合（Composition）体现整体与部分间的包含关系，即 'contains a' 的关系。但此时整体与部分是不可分的，部分也不能给其它整体共享，作为整体的对象负责部分的对象的生命周期。这种关系比聚合更强，也称为强聚合。
用实心菱形和实线表示。
![UML类图画图图解20211101140910](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/UML%E7%B1%BB%E5%9B%BE%E7%94%BB%E5%9B%BE%E5%9B%BE%E8%A7%A320211101140910.png)

### Inheritance

**Generalization**
泛化关系，一般用于类继承。
泛化（Generalization）体现的是对象与派生对象之间的关系，即 'is a' 的关系。
类继承采用实线加三角箭头
![UML类图画图图解20211101113806](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/UML%E7%B1%BB%E5%9B%BE%E7%94%BB%E5%9B%BE%E5%9B%BE%E8%A7%A320211101113806.png)
**Realization**
实现关系，一般用于接口继承。
实现（Realization）体现的是对象与接口之间的关系，即 'realizes a' 的关系。
接口继承采用虚线加三角箭头
![UML类图画图图解20211101113917](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/UML%E7%B1%BB%E5%9B%BE%E7%94%BB%E5%9B%BE%E5%9B%BE%E8%A7%A320211101113917.png)

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show)  欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> http://www.cs.utsa.edu/~cs3443/uml/uml.html

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

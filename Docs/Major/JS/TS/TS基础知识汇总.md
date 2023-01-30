# TS 基础知识汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [TS 基础知识汇总](#ts-基础知识汇总)
  - [TS 简介](#ts-简介)
    - [简述](#简述)
    - [优势](#优势)
    - [劣势](#劣势)
  - [TS 常见类型](#ts-常见类型)
  - [class 实例属性可见性](#class-实例属性可见性)

<!-- /code_chunk_output -->

## TS 简介

### 简述

TS 被看做是 JavaScript 的超集
浏览器不能直接编译解析 TS，开发完成的 TS 代码需要先转义成 JS

### 优势

TS 具有如下优势

- 减少错误

TS 的类型系统能够提前发现部分类型关联的隐藏问题

- 代码干净整洁，可读性高

TS 代码提高了代码可读性，减少代码注释工作量

- 双端支持

支持客户端与服务端。

### 劣势

TS 具有如下劣势

- 需要编译

JS 代码可以直接运行，而 TS 需要编译后方可发布生产运行，这通常被视为一个弊端。
但是，在现代 JS 中，工程通常需要 Webpack、Gulp、Vite、Babel 等工具先行编译，不管怎么说，编译工作已必不可少。

## TS 常见类型

- Boolean type
- Number type
- String type
- Object type
- Array type
- Tuple Type
- Enum Type
- Any Type
- Union Type
- Literal Type
- Function Type
- Unknown Type
- Never Type
- Custom Type

## class 实例属性可见性

class 实例通过 public、protected、private 来控制属性与方法的可用范围，类本生不可直接访问.
若要设置类自身属性，采用 static。
public 为默认值，任何位置，类和子类、类的实例都可访问。
protected 在类和子类中可用，实例化后不可用。
private 在类中可用，实例化和子类不可用。

```js
class Greeter {
  public greet() {
    console.log("Hello, " + this.getName() + this.getAge());
  }
  protected getName() {
    return "skyline";
  }
  private getAge() {
    return "18";
  }
}

class GreeterCN extends Greeter {
  public nihao() {
    console.log("你好, " + this.getName());
  }
}
const g = new GreeterCN();
g.greet();  //"Hello, skyline18"
g.nihao() // "你好, skyline"

```

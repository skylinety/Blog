# JS 垃圾回收机制

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [JS 垃圾回收机制](#js-垃圾回收机制)
  - [垃圾回收(GC:Garbage Collecation)](#垃圾回收gcgarbage-collecation)
    - [简介](#简介)
    - [引用计数（Reference Counting）](#引用计数reference-counting)
    - [标记清除（Mark & Sweep）](#标记清除mark-sweep)

<!-- /code_chunk_output -->

## 垃圾回收(GC:Garbage Collecation)

### 简介

JS 自动进行垃圾回收，不需要如 C 语言等一般需要代码中指定回收。
垃圾收集器会定期（周期性）找出那些不再继续使用的变量，然后释放其内存。
垃圾回收开销较大，垃圾回收时会停止其他操作，所以垃圾回收并不是实时的，而是周期性地进行。
垃圾标记器会跟踪内存，有用内存打上标记，回收垃圾时，需要将那些未被标记的供垃圾回收器清理。
标记的策略一般有两种，引用计数与标记清除。

### 引用计数（Reference Counting）

传统的引用计数方式简单来说就是记录内存引用的总数，当总数为 0 时，该内存将被回收。
该方式最大的弊端是循环引用对应的内存将不能被回收。
循环引用代码示例：

```js
function test() {
  var a = new Object()
  var b = new Object()
  a.child = b
  b.child = a
}
```

### 标记清除（Mark & Sweep）

根对象长驻内存，故其关联引用的后代可认为也该常驻内存。
故标记清除基本策略可认为就是扫描根对象与关联对象，有关联保留，无关联销毁。

- 标记阶段

JavaScript 由根对象开始，例如浏览器中的 window，定期遍历找出其所有关联引用的对象。
即找所有从这个全局对象开始引用的对象，再找这些对象引用的对象...
对这些存在引用关系的对象进行标记，这是标记阶段。

- 清除阶段

清除阶段就是垃圾收集器清除那些没有被标记的对象，释放其内存。

现代浏览器一般采用此方式来 GC。
内存泄漏可认为是开发者不再使用的对象但标记阶段仍可以由根节点关联到。

# JS 垃圾回收机制

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [JS 垃圾回收机制](#js-垃圾回收机制)
  - [垃圾回收(GC:Garbage Collecation)](#垃圾回收gcgarbage-collecation)
  - [内存标记策略](#内存标记策略)
    - [引用计数（Reference Counting）](#引用计数reference-counting)
    - [标记清除（Mark & Sweep）](#标记清除mark--sweep)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 垃圾回收(GC:Garbage Collecation)

在各编程语言中，内存的生命周期大概经历如下三个阶段：

- 内存分配（allocate）
- 内存使用（read | write）
- 内存释放（free）

不管是在高级还是低级语言中，第二阶段的读写都很明确，而内存的分配与释放阶段，
JS 等高级语言会自动分配内存，通过算法自动进行垃圾回收，释放内存。
局部变量会在离开环境时自动解除引用，后续算法自动计数或标记来确定是否释放。
对于全局对象与属性，可通过将值设置成 null 来**解除引用**以释放内存。
而 C 语言等低级语言在代码中显式分配与释放内存。

JS 的自动回收垃圾机制大致如下：
垃圾收集器会定期（周期性）找出那些不再继续使用的变量，然后释放其内存。
垃圾回收开销较大，垃圾回收时会停止其他操作，所以垃圾回收并不是实时的，而是周期性地进行。
垃圾标记器会跟踪内存，有用内存打上标记，回收垃圾时，需要将那些未被标记的供垃圾回收器清理。
标记的策略一般有两种，引用计数与标记清除。

## 内存标记策略

### 引用计数（Reference Counting）

传统的引用计数方式简单来说就是记录内存引用的总数，当总数为 0 时，该内存将被回收。
该方式最大的弊端是循环引用时对应的内存将不能被回收。
引用计数的主要标记策略为获取不再使用的对象（计数为 0 即不再使用）
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
标记清除的主要标记策略为对象可否获取。

- 标记阶段

JavaScript 由根对象开始，例如浏览器中的 window，定期遍历找出其所有关联引用的对象。
即找所有从这个全局对象开始引用的对象，再找这些对象引用的对象...
对这些存在引用关系的对象进行标记，这是标记阶段。

- 清除阶段

清除阶段就是垃圾收集器清除那些没有被标记的对象，释放其内存。

现代浏览器一般采用此方式来 GC。
内存泄漏可认为是开发者不再使用的对象但标记阶段仍可以由根节点关联到。

对于标记清除策略，循环引用将不再是问题，在上述循环引用实例中，
test 执行完毕上下文被销毁后，其内部变量 a 或 b 都不可以通过 window 对象获取，故而被销毁。

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management#reference-counting_garbage_collection

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

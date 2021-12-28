# JS 内存泄漏与处理

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [JS 内存泄漏与处理](#js-内存泄漏与处理)
  - [垃圾回收(GC:Garbage Collecation)](#垃圾回收gcgarbage-collecation)
    - [简介](#简介)
    - [引用计数（Reference Counting）](#引用计数reference-counting)
    - [标记清除（Mark & Sweep）](#标记清除mark-sweep)
  - [内存泄漏（Memory Leaks）](#内存泄漏memory-leaks)
    - [简介](#简介-1)
    - [常见内存泄漏情况](#常见内存泄漏情况)
    - [常见情况示例](#常见情况示例)
  - [内存泄漏处理](#内存泄漏处理)
    - [Chrome Memory 调试](#chrome-memory-调试)
    - [内存泄漏监测](#内存泄漏监测)
    - [泄漏内存对比](#泄漏内存对比)
    - [泄漏内存对象详情](#泄漏内存对象详情)
    - [对象引用链](#对象引用链)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 垃圾回收(GC:Garbage Collecation)

### 简介

JS 自动进行垃圾回收，不需要如 C 语言等一般需要代码中指定回收。
垃圾收集器会定期（周期性）找出那些不再继续使用的变量，然后释放其内存。
垃圾回收开销较大，垃圾回收时会停止其他操作，所以垃圾回收并不是实时的，而是周期性地进行。
回收垃圾时，需要将那些被标记的清除掉，垃圾标记器会跟踪无用内存并打上标记，以供垃圾回收器清理。
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

- 标记阶段

JavaScript 由根对象开始，例如浏览器中的 window，定期遍历找出其所有关联引用的对象。
即找所有从这个全局对象开始引用的对象，再找这些对象引用的对象...
对这些存在引用关系的对象进行标记，这是标记阶段。

- 清除阶段

清除阶段就是垃圾收集器清除那些没有被标记的对象，释放其内存。

## 内存泄漏（Memory Leaks）

### 简介

JS 为复杂对象分配堆内存，对象被引用，该堆内存存在。
一旦对象不再被引用，此时 JS 垃圾回收机制将回收该堆内存。
内存泄漏（Memory Leak）一般指当代码中不再使用该对象而未及时解除引用关系时（对象指针没有被置为 null），该内存分配将一直存在。
造成 JS 内存泄漏的主要原因就是非正常引用。
现代浏览器一般采用标记清除方式清理内存，故内存泄漏也可认为是：
**开发者不再使用的对象但标记阶段仍可以由根节点关联到。**

### 常见内存泄漏情况

- 意外全局对象

- DOM 多方引用

- 绑定的事件未销毁

- 定时器未清除

- 闭包未销毁

- EventBus 事件没解绑

- Vuex $store watch 后没 unwatch

- 三方库函数对象未调用销毁函数

### 常见情况示例

- 意外全局对象

```js
function foo(arg) {
  skyline = 'skyline 是全局变量'
  this.haha = 'haha 也是全局变量'
}
```

函数执行完成后 skyline 与 haha 并不会被销毁

- DOM 多方引用

在 JS 代码中引用了 DOM 对象，DOM 对象被移除，引用未解除，造成该 DOM 对象一直存在内存中。

```js
window.test = {
  node: document.getElementById('home'),
}

document.body.removeChild(document.getElementById('home'))
```

上述例子中，移除 home 节点前，对于 home 节点对象，存在两个引用。
一个是 DOM Tree 中的引用，另一个是全局变量 test 的引用。
移除 home 节点，只是将 DOM Tree 中的引用解除掉。
在全局变量 test 中仍旧存在对 home 的引用，造成 home 节点在 removeChild（人为废弃）后仍旧游离于内存之中。
需要特别注意的是，如果上述情况发生在 li、tr 等节点上，那么其关联的 ul 以及 table 等节点也将一致保存在内存中。
一个更加常见的例子是在使用 echarts 的单页面项目中，图表容器与某个 DOM 节点绑定。
如果图表在路由切换后不再使用，
需要在 unmount，destroy 等生命周期中调用 echarts 实例的 dispose 方法。

- 绑定的事件未销毁

```js
var element = document.getElementById('button')

function onClick(event) {
  element.innerHtml = 'text'
}

element.addEventListener('click', onClick)
// element.removeEventListener('click', onClick); // 加入此行代码解除事件监听
element.parentNode.removeChild(element)
```

上述代码中 element 被引用两次且被点击事件的回调函数使用。
将 DOM Tree 中的引用解除掉后，节点引用并未完全解除。
需要调用`element.removeEventListener('click', onClick)`将事件监听销毁来解除 element 对节点的引用。
这种内存泄漏常见于老一代（IE6 等）浏览器中。
现代浏览器或一些三方库（JQuery 等），能够在移除节点前，自动将所有节点上的监听事件移除掉，避免内存泄漏。

- 定时器未清除

另一个回调内引用节点的常见例子是 timeout 与 interval 中

```js
var someResource = 'I am skyline'
var node = document.getElementById('Node')
setInterval(function () {
  if (node) {
    node.innerHTML = someResource
  }
}, 1000)
element.parentNode.removeChild(node)
```

上诉代码不调用 clearInterval，node 变量将常驻内存中。

- 闭包未销毁

一个内存泄漏更加严重的例子如下

```js
var theThing = null
var replaceThing = function () {
  var originalThing = theThing
  var unused = function () {
    if (originalThing) console.log('hi')
  }
  theThing = {
    longStr: new Array(1000000).join('*'),
    someMethod: function () {
      console.log(someMessage)
    },
  }
}
setInterval(replaceThing, 1000)
```

由于 unused 与 someMethod 的作用域链都引用了 replaceThing 的活动对象 AO。
unused 的作用域链为

```
[unusedContext.AO, replaceThingContext.AO, globalContext.VO]
```

someMethod 的作用域链为

```
[someMethodContext.AO, replaceThingContext.AO, globalContext.VO]
```

unused 与 someMethod 作用域链引用同一个 replaceThingContext.AO
由于 unused 引用 originalThing 导致 replaceThingContext 即便执行完成，
其 replaceThingContext.AO 仍旧会被保留。
由于 someMethod 保留在全局变量 theThing 中故而其作用域链也并不会被销毁
上述代码造成内存泄漏的效果与如下代码一致，下述代码更易于理解。

```js
var theThing = null
var replaceThing = function () {
  var originalThing = theThing
  theThing = {
    longStr: new Array(1000000).join('*'),
    someMethod: function () {
      if (originalThing) console.log('hi')
    },
  }
}
setInterval(replaceThing, 1000)
```

![JS内存泄漏与处理20211227190852](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211227190852.png)
从 Chrome 内存分析工具可以看到，由于 originalThing 的闭包使用，导致 originalThing 引用上一轮的 theThing 而造成内存泄漏链条。
详细分析参考 [An interesting kind of JavaScript memory leak](https://blog.meteor.com/an-interesting-kind-of-javascript-memory-leak-8b47d2e7f156)

## 内存泄漏处理

### Chrome Memory 调试

Chrome 控制台的 Memory 板块提供 3 个功能选项。
![JS内存泄漏与处理20211217112531](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211217112531.png)

- Heap snapshot

堆快照。
堆快照提供 JS 对象与关联 DOM 节点的内存分配情况。

- Allocation instrumentation on timeline

内存分配时间轴。
通过内存分配时间轴可以监测内存在时间轴上随着时间变化的分配情况。
![JS内存泄漏与处理20211217114604](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211217114604.png)
如上图
A 可以选部分时间段。
B 处悬浮 2S 查看内存中的对象。
C 处查看内存分配调用栈。

- Allocation sampling

内存分配抽样
抽样获取最耗损内存的操作（函数等），性能开销最小，通过采样方法记录内存分配，提供 JS 执行堆栈的近似分配值。
默认以 Heavy 排序，即耗损排序。
![JS内存泄漏与处理20211217140701](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211217140701.png)

### 内存泄漏监测

当页面卡顿或者直接卡死报错页面无响应时，一般都是内存泄漏造成的。
定位内存泄漏，首先定位造成内存泄漏的页面或者操作。
在浏览器控制台，打开 Performance Monitor 查看内存状态，定位内存激增的操作。
![JS内存泄漏与处理20211217104829](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211217104829.png)
建议用此方式排查，也可以通过 Allocation instrumentation on timeline 来找到内存泄漏的地方。

### 泄漏内存对比

在内存泄漏的操作前拍下快照，执行操作，拍下快照，对比两次快照。
在搜索框输入 detached 过滤泄漏的对象，选择 Comparison。
可以看到泄漏的 DIV DOM 对象新增了 88 个（截图是将代码置于项目中测试，有干扰，忽略）。
![JS内存泄漏与处理20211216202518](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211216202518.png)

### 泄漏内存对象详情

查看泄漏内存对应对象详情，只需将 鼠标移动到对应的节点上等待两秒。
![JS内存泄漏与处理20211216195654](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211216195654.png)

### 对象引用链

在 Object 板块，可以查看该对象引用链，可以看到泄漏的对象位于一个 test 对象的 node 属性上，test 对象位于 window 当中
![JS内存泄漏与处理20211216195848](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211216195848.png)

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> [An interesting kind of JavaScript memory leak](https://blog.meteor.com/an-interesting-kind-of-javascript-memory-leak-8b47d2e7f156)

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

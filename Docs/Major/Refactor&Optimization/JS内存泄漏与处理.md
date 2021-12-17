# JS 内存泄漏与处理

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [JS 内存泄漏与处理](#js-内存泄漏与处理)
  - [垃圾回收](#垃圾回收)
    - [简介](#简介)
    - [引用计数（Reference Counting）](#引用计数reference-counting)
    - [标记清除（Mark & Sweep）](#标记清除mark-sweep)
  - [内存泄漏](#内存泄漏)
    - [简介](#简介-1)
    - [常见内存泄漏情况](#常见内存泄漏情况)
    - [Chrome Memory](#chrome-memory)
    - [常见情况](#常见情况)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 垃圾回收

### 简介

JS 自动进行垃圾回收(GC:Garbage Collecation)，不需要如 C 语言等一般需要代码中指定回收。
垃圾收集器会定期（周期性）找出那些不在继续使用的变量，然后释放其内存。
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

## 内存泄漏

### 简介

JS 为复杂对象分配堆内存，对象被引用，该堆内存存在。一旦对象不再被引用，此时 JS 垃圾回收机制将回收该堆内存。
一般情况下，JS 都能自动将不再使用（引用）的内存及时释放。
内存泄漏（Memory Leak）一般指当代码中不再使用该对象而未及时解除引用关系时（对象指针没有被置为 null），该内存分配将一直存在，这就是内存泄漏。

### 常见内存泄漏情况

- 监听在 DOM 上的事件没有解绑

- EventBus 的事件没有解绑

- Vuex 的$store watch 了之后没有 unwatch

- 模块形成的闭包内部变量使用完后没有置成 null

- 使用第三方库创建的对象，没有调用正确的销毁函数

### Chrome Memory

Chrome 控制台的 Memory 板块提供 3 个功能选项。
![JS内存泄漏与处理20211217112531](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211217112531.png)

- Heap snapshot

堆快照。
堆快照提供 JS 对象与关联 DOM 节点的内存分配情况。

- Allocation instrumentation on timeline

内存分配时间轴。
通过内存分配时间轴可以监测内存在时间轴上分配情况。
![JS内存泄漏与处理20211217114604](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211217114604.png)
如上图
A 可以选部分时间段。
B 处悬浮 2S 查看内存中的对象。
C 处查看内存分配调用栈。

- Allocation sampling

内存分配抽样
抽样获取最耗损内存的操作（函数等），性能开销最小。
默认以 Heavy 排序，即耗损排序。
![JS内存泄漏与处理20211217140701](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211217140701.png)

### 常见情况

- Detached Dom elements

DOM 对象泄漏。
在 JS 代码中引用了 DOM 对象，DOM 对象被移除，引用未解除，造成该 DOM 对象一直存在内存中。

```js
window.test = {
  node: document.getElementById('home'),
}

document.body.removeChild(document.getElementById('home'))
```

上述例子，在全局变量 test 中仍旧存在对 home 的引用，造成移除节点后游离与内存之中
一个更加常见的例子是在使用 echarts 的单页面项目中，图表容器与某个 DOM 节点绑定。
如果图表在路由切换后不再使用，
需要在 unmount，destroy 等生命周期中调用 echarts 实例的 dispose 方法。

- 内存泄漏监测

当页面卡顿或者直接卡死报错页面无响应时，一般都是内存泄漏造成的。
定位内存泄漏，首先定位造成内存泄漏的页面或者操作。
在浏览器控制台，打开 Performance Monitor 查看内存状态，定位内存激增的操作。
![JS内存泄漏与处理20211217104829](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211217104829.png)
建议用此方式排查，也可以通过 Allocation instrumentation on timeline 来找到内存泄漏的地方。

- 泄漏内存对比

在内存泄漏的操作前拍下快照，执行操作，拍下快照，对比两次快照。
在搜索框输入 detached 过滤泄漏的对象，选择 Comparison。
可以看到泄漏的 DIV DOM 对象新增了 88 个（截图是将代码置于项目中测试，有干扰，忽略）。
![JS内存泄漏与处理20211216202518](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211216202518.png)

- 泄漏内存对象详情

查看泄漏内存对应对象详情，只需将 鼠标移动到对应的节点上等待两秒。
![JS内存泄漏与处理20211216195654](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211216195654.png)

- 对象引用链

在 Object 板块，可以查看该对象引用链，可以看到泄漏的对象位于一个 test 对象的 node 属性上，test 对象位于 window 当中
![JS内存泄漏与处理20211216195848](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F%E4%B8%8E%E5%A4%84%E7%90%8620211216195848.png)

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

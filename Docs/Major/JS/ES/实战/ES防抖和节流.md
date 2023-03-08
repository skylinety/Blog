# ES防抖和节流

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES防抖和节流](#es防抖和节流)
  - [防抖](#防抖)
    - [防抖的理解](#防抖的理解)
    - [防抖基础版本](#防抖基础版本)
    - [立即执行首次](#立即执行首次)
    - [this绑定与event](#this绑定与event)
  - [节流](#节流)
    - [节流的理解](#节流的理解)
    - [节流基础版本](#节流基础版本)
    - [this绑定与event](#this绑定与event-1)
    - [头尾执行定制](#头尾执行定制)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 防抖

### 防抖的理解

防抖debounce ，即防止抖动。
当事件不停地触发时，浏览器为了应对同一时间段的大量任务，交互区域表现出来就像是在抖动。
防抖将事件触发规定在单位时间内，单位时间内新事件触发会丢弃上次事件并重新计算下个时间段，
以此往复，直到最新的单位时间段内无新事件触发，对应函数执行完成。

防抖一般只执行最后一次函数，
或根据需求，立即执行首次函数，然后只执行后续连续触发的最后一次。

其主要实现原理：

* setTimeout
* 闭包

### 防抖基础版本

```jsx
function debounce(fn, time) {
    let t = null

    return () => {
        if(t){
            clearTimeout(t)
        }
        t = setTimeout(fn, time)
    }
}
```

### 立即执行首次

只在第一次触发时执行，后续重新执行时的第一次不再执行

```jsx
function debounce(fn, time) {
    let t = null
    let count = 0

    return () => {
        if(t){
            clearTimeout(t)
        }
        if(count){
            t = setTimeout(fn, time)
        }else{
            fn()
        }
        count++
    }
}
```

第一次触发时执行，后续重新执行时的第一次都会执行

```jsx
function debounce(fn, time) {
    let t = null
    let count = 0

    return () => {
        if (t) {
            clearTimeout(t)
        }
        if (count) {
            t = setTimeout(() => { count = 0; fn() }, time)
        } else {
            fn()
        }
        count++
    }
}
```

由于使用了setTimeout对实际回调进行包裹，fn的this指向改变，
同时，这里event对象回调参数丢失，可通过apply绑定this并获取arguments进行传参。

### this绑定与event

```jsx
function debounce(fn, time) {
    let t = null
    let count = 0

    return function() {
        const me = this
        const args = arguments
        if (t) {
            clearTimeout(t)
        }
        if (count) {
            t = setTimeout(() => { count = 0; fn.apply(this, args) }, time)
        } else {
            fn.apply(this, args)
        }
        count++
    }
}
```

这里需要注意，由于箭头函数this在定义时已定不再是执行时，故而需要改为普通函数。

## 节流

### 节流的理解

节流 throttle ，顾名思义，就是控制流量。
例如，当持续触发事件，单元时间内，只执行一次事件。
节流会执行多次函数，只是减少了函数执行的次数。
节流的实现在闭包的基础上，可以通过时间戳求差或者setTimeout来实现。

其主要实现原理：

* 闭包
* 时间戳差/setTimeout

### 节流基础版本

```js
function throttle(fn, time) {
    let t = null

    return () => {
        if (!t) {
            t = setTimeout(() => {
                t = null;
                fn()
            }, time)
        }
    }
}
```

### this绑定与event

```jsx
function throttle(fn, time) {
    let t = null

    return function () {
        const args = arguments
        if (!t) {
            t = setTimeout(() => {
                t = null;
                fn.apply(this, args)
            }, time)
        }
    }
}
```

### 头尾执行定制

节流的需求不同，往往有事件触发时（头）立即执行，事件停止触发（尾）后不再执行的需求。
可能需要执行有头有尾，有头无尾，无头有尾。
这一部分内容实现需要引入时间戳来实现，具体参照underscore等三方库的完整轮子。
文章对应[示例](https://github.com/skylinety/Blog/blob/main/Demos/Major/HTML&CSS/CSS/Debounce_Throttle.html)文件可在浏览器直接执行。
## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️


> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES防抖和节流.html](http://www.skyline.show/ES防抖和节流.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！


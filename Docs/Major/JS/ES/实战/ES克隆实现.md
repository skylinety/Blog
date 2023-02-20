# ES克隆实现

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES克隆实现](#es克隆实现)
  - [浅克隆](#浅克隆)
    - [常见浅克隆](#常见浅克隆)
    - [浅克隆的问题](#浅克隆的问题)
  - [深克隆](#深克隆)
    - [深克隆的方案](#深克隆的方案)
    - [JSON.stringify](#jsonstringify)
    - [cloneDeep的简单实现](#clonedeep的简单实现)
  - [三方库深克隆源码分析](#三方库深克隆源码分析)
    - [Jquery.extend](#jqueryextend)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 浅克隆

### 常见浅克隆

在日常代码中，常用的对象克隆方式较多，多数直接使用的API是浅克隆。

* Object.assign

```js
const circle = (radius) => {
  const proto = {
    type: "Circle",
    //code
  };
  return Object.assign(Object.create(proto), { radius });
};
const square = (length) => {
  const proto = {
    type: "Square",
    //code
  };
  return Object.assign(Object.create(proto), { length });
};
```

* ...

```jsx
const square = {
    type: "Square",
    borders: [2, 2, 2, 2],
    perimeter: function() {
      return this.borders.reduce((p, n) => {
        return p + n
      }, 0);
    },
};

const rectangel = {...square}

rectangel.type = 'Rectangel'
rectangel.borders[1] = 4
rectangel.borders[3] = 4

```

### 浅克隆的问题

由于复杂类型存储方式的不同，如果只是进行简单的赋值，就会造成新对象修改将影响初始对象的相关值。
以扩展运算符为例，后续代码的调整导致了正方形的边长被改变。
```jsx
square.borders
// [2, 4, 2, 4]
```

## 深克隆

### 深克隆的方案
现在已有第三方库的成熟实现，
例如，可用lodash underscore 等插件提供的类似于cloneDeep的方法。
另常见的用法为使用JSON序列化API,
当然，也可尝试自写深克隆函数。

### JSON.stringify

```jsx
let newObj = JSON.parse(JSON.stringify(obj))
```
JSON.stringify存在主要如下问题：

* 无法复制函数（JSON.stringify()无法序列化函数）
* 原型链，所属的类等信息丢失
* 对象循环引用的问题无法解决

```jsx
var a = function(){}
var b = JSON.stringify(a)
a //function (){}
b //undefined

var c = []
c //[]
var d = JSON.stringify(c)
d //"[]"
```

### cloneDeep的简单实现

```jsx
var cloneDeep= function(source) {
    let target = {};
        // isArray = false;

    if(typeof source === 'object'){
        // source[key] instanceof Array && (isArray = true)
        target = source[key] instanceof Array ? [] : {}
    }else{
        return source;
    }

    for (var key in source) {
        target[key] = typeof source[key] === 'object' ? cloneDeep(source[key]) : source[key];
    } 
    return target; 
}
```

## 三方库深克隆源码分析

### Jquery.extend

[Jquery extend 源码地址](https://github.com/jquery/jquery/blob/1472290917f17af05e98007136096784f9051fab/src/core.js#L121)
Jquery.extend代码使用示例

```js
var x = {
    a: 1,
    b: { f: { g: 1 } },
    c: [ 1, 2, 3 ]
};

var y = $.extend({}, x),          //shallow copy
    z = $.extend(true, {}, x);    //deep copy

y.b.f === x.b.f       // true
z.b.f === x.b.f       // false
```
源码分析
```js
jQuery.extend = jQuery.fn.extend = function() {
    var src, //缓存目标对象属性
        copyIsArray, //标记被复制对象属性是否是数组
        copy, //缓存被复制对象属性
        name, options, clone,
        target = arguments[0] || {}, //目标对象，如果没有传入参数，则默认为空对象
        i = 1, //标记参数的位置
        length = arguments.length,
        deep = false; //深浅克隆标志

    // 处理深克隆
    if (typeof target === "boolean") {
        deep = target;

        // 如果第一个参数为布尔值，则目标对象顺移值第二个参数
        target = arguments[i] || {};
        i++;
    }

    //处理目标参数是非对象情况（注意第二个判断条件是由于typeof用于function返回的是'Function')
    // Handle case when target is a string or something (possible in deep copy)
    if (typeof target !== "object" && !jQuery.isFunction(target)) {
        target = {};
    }

    // 如果传入参数只有一个（任意）则直接赋值Jquery对象
    if (i === length) {
        target = this;
        i--;
    }

    for (; i < length; i++) {
        //undefined == null true
        // 处理非null与undefined值
        if ((options = arguments[i]) != null) {

            for (name in options) {
                src = target[name];
                copy = options[name];

                // 如果目标属性与被复制对象属性相等
                if (target === copy) {
                    continue;
                }

                // 如果是纯粹对象或数组，则递归调用。（通过 "{}" 或者 "new Object" 创建的是纯粹对象）
                if (deep && copy && (jQuery.isPlainObject(copy) || (copyIsArray = jQuery.isArray(copy)))) {
                    if (copyIsArray) {
                        copyIsArray = false;
                        clone = src && jQuery.isArray(src) ? src : [];

                    } else {
                        clone = src && jQuery.isPlainObject(src) ? src : {};
                    }

                    target[name] = jQuery.extend(deep, clone, copy);

                } else if (copy !== undefined) {
                    target[name] = copy;
                }
            }
        }
    }

    return target;
};
```


## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️


> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  [深入剖析 JavaScript 的深复制](http://jerryzou.com/posts/dive-into-deep-clone-in-javascript/)

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES克隆实现.html](http://www.skyline.show/ES克隆实现.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

# ES 严格模式

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 严格模式](#es-严格模式)
  - [严格模式启用](#严格模式启用)
  - [强化安全](#强化安全)
    - [未声明变量禁止使用](#未声明变量禁止使用)
    - [this 不再自动全局对象](#this-不再自动全局对象)
    - [禁止使用 with 语句](#禁止使用-with-语句)
  - [拥抱未来](#拥抱未来)
  - [ES6 中的严格模式](#es6-中的严格模式)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 严格模式启用

ES5 通过

```jsx
'use strict'
```

启用严格模式。

严格模式会强化安全并对未来的一些特性做考虑,
如下梳理一些经常遇到的严格模式。

## 强化安全

### 未声明变量禁止使用

```jsx
'use strict'
skyline = { a: 1 }
//  skyline is not defined
```

### this 不再自动全局对象

非严格模式

```jsx
var name = 'window'
function Skyline() {
  this.name = 'skyline'
  this.say = function () {
    console.log(`${this.name} said hahaha`)
  }
}
var me = new Skyline()
me.say()
// skyline said hahaha

var say = me.say
say()
// window said hahaha
```

严格模式

```jsx
'use strict'
var name = 'window'
function Skyline() {
  this.name = 'skyline'
  this.say = function () {
    console.log(`${this.name} said hahaha`)
  }
}
var me = new Skyline()
me.say()
// skyline said hahaha

var say = me.say
say()
// Cannot read properties of undefined (reading 'name')
```

### 禁止使用 with 语句

with 语句用于修改作用域链。
with 用于拓展代码块中的作用域链

```jsx
const skyline = { a: 1 }
with (skyline) {
  console.log(a + 1)
  // 2
}
```

可简单理解为在 with 内，skyline 就是语句块内原 window 的作用。

启用严格模式报错：

```jsx
'use strict'
const skyline = { a: 1 }
with (skyline) {
  console.log(a + 1)
}
// Strict mode code may not include a with statement
```

## 拥抱未来

严格模式将未来可能用到的关键字启用保护限制。
这些关键字有：

- implements
- interface
- let
- package
- private
- protected
- public
- static
- yield

这些关键字在 ES6 版本中多数如约而来。
严格模式有更多其他特性的限制出现较少，后续进一步更新。

## ES6 中的严格模式

在 ES5 中，大多数开发不会显示启用严格模式，导致开发风格与规范良（nan）好(kan)。
而 ES6 类与模块的导入导出会导致启用严格模式而不用再显式书写'use strict'

对于严格模式下一些常用的规则，会造成一些代码输出超出预期。
例如，在严格模式下，函数无调用对象时，this 不会自动指向 Window。

```jsx
class Skyline {
  constructor(x, y) {
    //实例属性、方法
    this.name = 'skyline'
  }

  say() {
    console.log(`${this.name} said hahaha`)
  }
}

const me = new Skyline()
me.say()
const say = Skyline.prototype.say
say()
```

执行结果为

```jsx
'skyline said hahaha'

"TypeError: Cannot read properties of undefined (reading 'name')"
```

通过 [Babel](https://www.babeljs.cn/repl#?browsers=%3E%200.25%25%2C%20not%20dead&build=&builtIns=false&corejs=3.21&spec=false&loose=false&code_lz=MYGwhgzhAEDKDWBPEBLAdgU2gbwFDWmAHs0IAXAJwFdgyiKAKADwBppEBKHfA6Aej6A87UDR8oD0dQOQGgQAZAnaaBVmx4EyACxQQAdGjABbLAF5oAcghJUmAzwC-uHhDCIGXPL0IkIREBjUgiAcwYADABJsZVUNbQwLaFsUABNoJTBExP8OS1wrXGJSMmgdaH1MAHc4E3QMB1wdNVt7NOzyaLsC0uRytQAHCiI6MkQOz1rcWocgA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=false&presets=env%2Creact&prettier=false&targets=&version=7.21.2&externalPlugins=&assumptions=%7B%7D) 转义，
代码如下

```jsx
'use strict'

// ...

var Skyline = /*#__PURE__*/ (function () {
  function Skyline(x, y) {
    _classCallCheck(this, Skyline)
    //实例属性、方法
    this.name = 'skyline'
  }
  _createClass(Skyline, [
    {
      key: 'say',
      value: function say() {
        console.log(''.concat(this.name, ' said hahaha'))
      },
    },
  ])
  return Skyline
})()
var me = new Skyline()
me.say()
var say = Skyline.prototype.say
say()
//# sourceURL=traceured.js
```

可以看到转义添加了'use strict'
删除'use strict'，浏览器控制台重新执行上述代码，不会存在问题。
在使用 babel 在线转换工具时，需要配置左边栏 TARGETS 预设，预设配置参考这个[仓库](https://github.com/browserslist/browserslist)。

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Strict_mode

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES 严格模式.html](http://www.skyline.show/ES严格模式.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

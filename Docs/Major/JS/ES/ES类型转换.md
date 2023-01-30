# ES 类型转换

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 类型转换](#es-类型转换)
  - [类型转换](#类型转换)
    - [类型转换概述](#类型转换概述)
    - [to boolean](#to-boolean)
    - [to number](#to-number)
    - [to string](#to-string)
    - [to object](#to-object)
  - [ToPrimitive](#toprimitive)
  - [隐式转换场景](#隐式转换场景)
    - [隐式转换场景概述](#隐式转换场景概述)
    - [一元操作符](#一元操作符)
    - [二元加](#二元加)
    - [乘、除、取余、二元减](#乘除取余二元减)
    - [比较运算符](#比较运算符)
  - [Expression or Statement](#expression-or-statement)
    - [几个有意思的输出](#几个有意思的输出)
    - [AST](#ast)
    - [{}语法解析分析](#语法解析分析)
  - [JSON.stringify](#jsonstringify)
    - [处理规则](#处理规则)
    - [参数](#参数)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 类型转换

### 类型转换概述

- 隐式转换
  JS 是弱类型语言，在使用运算符时，多个参与其中的数据类型可以是任意的，最终得到的结果却只是一种类型。
  结果的类型可能是参与运算操作类型中的一种，也可能并非其中任何一种。
  这就涉及到运算过程中，进行过的隐式类型转换。
- 强制转换
  JS 中每一种类型都有自己的构造函数，直接调用该构造函数可以强制获得该类型的值，同时 JS 还提供了其他显示调用函数转换类型的方法。

### to boolean

其他类型转换为布尔值。

- 隐式转换

隐式转换为布尔值

| 数据类型  | 转化成 true  | 转化成 false |
| --------- | ------------ | ------------ |
| String    | 非空字符     | ""(空字符）  |
| Number    | 非零         | 0 与 NaN     |
| Object    | 非 Null 对象 | null         |
| undefined | 无           | undefined    |

- 强制转换

强制转换为布尔值
调用 Boolean()与隐式转换规则转换一致，当不传参数时为 false

```jsx
console.log(Boolean()) // false
```

### to number

其他类型转换成数字

- 隐式转换

隐式转换成数字

| 数据类型  | 转化成数字                                                                             | 示例                                                      |
| --------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| undefined | NaN                                                                                    |                                                           |
| null      | 0                                                                                      |                                                           |
| Number    | 等值                                                                                   |                                                           |
| Boolean   | true: 1,false:0                                                                        |                                                           |
| String    | 忽略前导 0，转换成的 10 进制数，有一个字符不是数字（进制标识除外），则为 NaN，空串为 0 | ` "0x11" - 1 // 16;`;`"100a" - 1 // NaN `; `- '' // -0`   |
| Object    | 调用 ToPrimitive                                                                       | `var a = {valueOf: function() {return 1}} `; `a + 1 // 2` |

```jsx
'0x11' - 1 // 16

var a = {
  valueOf: function () {
    return 1
  },
}
a + 1 // 2
```

- 强制转换

  - **Number()**
    其他类型转换为数字时调用的是 Number()，故参考上述隐式转换。
    要返回数字，只接收**纯数字**字符串作为参数，允许前后有空格，中间不能有，否则返回 NaN

  ```jsx
  var a = {
    valueOf: function () {
      return 1
    },
  }
  Number(a) // 1
  Number('0x11') // 17
  Number('100a') // NaN
  ```

  - **parseInt()**
    只要非空格的第一个字符是**数字**，它就会尽可能长地进行转换，直到遇到空格会或非字母
    如果第一个非空格字符是其他，则返回 NaN
    可接受两个参数，第二个参数指定进制
  - **parseFloat()**
    只要非空格的第一个字符是**数字或小数点**，它就会尽可能长地进行转换，直到遇到空格会或非字母
    如果第一个非空格字符是其他，则返回 NaN
    接受一个参数，**只解析十进制**
    只解析一个小数点，第二个小数点号以后字符忽略

### to string

其他类型转换成字符

- 隐式转换

隐式转换成字符

| 数据类型  | 转化成字符                 | 示例 |
| --------- | -------------------------- | ---- |
| undefined | "undefined"                |      |
| null      | "null"                     |      |
| Number    | 数值字符串形式             |      |
| Boolean   | true: 'true',false:'false' |      |
| Object    | 调用 ToPrimitive           |      |

- 强制转换
  - toString()
  - String()
    规则同隐式转换,，null 和 underfined 没有.toString 方法

### to object

隐式转换
Boolean、Number、String 三种简单类型在设置和访问其属性时会隐式转换成基本包装类型，在使用完后会马上销毁

```jsx
var s = 'skyline'
s.age = 23
console.log(s.age)
```

上述代码的 JS 执行可以简单看成
![JS 类型转换 e5ac0e3f765948ac86725eaa7decec19Untitled](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%20%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A2%20e5ac0e3f765948ac86725eaa7decec19Untitled.png)

- 强制转换

直接**new**关键字调用各类型构造函数，得到对应类型的基本包装类型，调用 Object 得到类似的基本包装对象
![JS 类型转换 e5ac0e3f765948ac86725eaa7decec1920220613161239](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%20%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A2%20e5ac0e3f765948ac86725eaa7decec1920220613161239.png)

## ToPrimitive

- ToPrimitive 综述

  在 JS 中，使用 ToPrimitive 将对象转为原始值
  ToPrimitive 大致的处理逻辑如下图所示
  ![JS 类型转换 e5ac0e3f765948ac86725eaa7decec1920220613161404](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/JS%20%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A2%20e5ac0e3f765948ac86725eaa7decec1920220613161404.png)

- toString()

| 数据类型               | 调用 toString()                   |
| ---------------------- | --------------------------------- |
| 普通对象               | "[object Object]"                 |
| 数组 arr               | arr.join(',')                     |
| 函数类                 | 定义函数的代码                    |
| 日期类                 | 可读日期                          |
| 正则对象               | 正则对象字面量的字符              |
| 基本包装类型的引用类型 | 用其字面量形式的值调用 toString() |

**如果数组的某一项的值是 null 或者 undefined，join()方法返回的结果以空字符串连接**

- valueOf()
  大多数对象，包括普通对象、数组、函数、正则简单返回对象本身
  日期对象返回 19700101 以来的毫秒数值
  基本包装类型的引用类型返回其字面量形式的值，该值存在于内部属性 PrimitiveValue 中
  ![ES类型转换20220613192434](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A220220613192434.png)

## 隐式转换场景

### 隐式转换场景概述

JS 隐式转换规则大致为简单类型调用目标类型的构造函数，复杂类型由内部方法 ToPrimitive 处理，见上述章节。触发隐式转换，通常是以下场景

### 一元操作符

一元+运算符将其操作数转换为 Number 类型。一元减号同理但是反转正负

```jsx
;+'3' - // 数字3
  '-3' + // 数字3
  [] + //0
  [1] + //1
  [1, 2] //NaN
```

### 二元加

规范地址：[http://es5.github.io/#x11.6.1](http://es5.github.io/#x11.6.1)
当计算 value1 + value2 时：

1. lprim = ToPrimitive(value1)
2. rprim = ToPrimitive(value2)
3. 如果 lprim 是字符串或者 rprim 是字符串，那么返回 ToString(lprim) 和 ToString(rprim)的拼接结果
4. 返回 ToNumber(lprim) 和 ToNumber(rprim)的运算结果

将加号两边值转换成原始值，原始值中有字符串则转换成字符串拼接，无则转换成数字相加；简单口诀记下：
先转原始，有字符转字符，没有字符转数字

多个加号时，按照从左到右的顺序，两两进行计算

```jsx
2 + '3' // "23"
1 + 2 + '3' // "33"
true + 2 + '3' // "33"
1 + '2' + 3 // "123"

1 + [] //"1"
1 + [1] //"11"
1 + { a: 'a' } //"1[object Object]"
null + null //0
true + { a: 'a' } //"true[object Object]"

null + undefined //NaN
1 + undefined //NaN
```

### 乘、除、取余、二元减

隐式转换为数字

```jsx
1 - '5' //-4
1 - [2, 2] //NaN
1 - { a: 1 } //NaN
1 - undefined //NaN
1 - [] //1
1 - [2, 2] //NaN
1 - null //1
```

### 比较运算符

包括> < >= <= ==，这里主要以==来说明

- 规范
  关于使用"=="进行比较的时候，具体步骤可以查看[规范 11.9.5](http://es5.github.io/#x11.9.3)：
  当执行 x == y 时：

```shell
1. 如果 x 与 y 是同一类型：
   1. x 是 Undefined，返回 true
   2. x 是 Null，返回 true
   3. x 是数字：
      1. x 是 NaN，返回 false
      2. y 是 NaN，返回 false
      3. x 与 y 相等，返回 true
      4. x 是+0，y 是-0，返回 true
      5. x 是-0，y 是+0，返回 true
      6. 返回 false
   4. x 是字符串，完全相等返回 true,否则返回 false
   5. x 是布尔值，x 和 y 都是 true 或者 false，返回 true，否则返回 false
   6. x 和 y 指向同一个对象，返回 true，否则返回 false
2. x 是 null 并且 y 是 undefined，返回 true
3. x 是 undefined 并且 y 是 null，返回 true
4. x 是数字，y 是字符串，判断 x == ToNumber(y)
5. x 是字符串，y 是数字，判断 ToNumber(x) == y
6. x 是布尔值，判断 ToNumber(x) == y
7. y 是布尔值，判断 x ==ToNumber(y)
8. x 不是字符串或者数字，y 是对象，判断 x == ToPrimitive(y)
9. x 是对象，y 不是字符串或者数字，判断 ToPrimitive(x) == y
10. 返回 false
```

- 总结

  - 数字 vs 其他（其他 vs 数字，忽略顺序，下同），其他转化为数字
  - 布尔值 vs 其他，布尔值转数字，数字 vs 其他
  - 字符串 vs 字符串，按 unicode 依次比较(大写字母总是在小写字母之后)
  - 对象 vs 数字，对象 vs 字符串，将对象转化为转换成原始值，再进行比较。
  - 操作数含 NaN，直接返回 false(NaN 和 NaN 是不相等的)
  - null 与 undefined 是好基友（互相相等）

  **总结起来一句话，先转原始，有数字转数字，布尔值也转数字**

  ```jsx

  NaN === NaN; // false

  undefined == "undefined" // false
  null == "null" // false
  null == 0 // false
  null == false // false
  undefined == 0 // false
  undefined == false // false
  true == '2' // false
  false == [] // true
  [] == ![] // true
  // ![]会先执行为false 即比较 ([] == false) => ([] == 0) => ('' == 0) => (0 == 0)
  ```

* 其他情况
  除了上述情景，if 语句，三元运算符，逻辑与或都会触发隐式转换，这些情况一般简单分析即可

## Expression or Statement

### 几个有意思的输出

chrome/firefox

```js
[] + {} //"[object Object]"

{} + [] // 0

[] + {} === {} + [] // true

{} + [] === [] + {} // true

{a: 1} // {a: 1}

{a: 1}; // 1

{'a': 1} // {a: 1}

{'a': 1}; // SyntaxError

{} + 0 + {}; // "0[object Object]"

{} + 0 + {} // "[object Object]0[object Object]"
```

firefox

```js
[] + {} //"[object Object]"

{} + [] // 0

[] + {} === {} + [] // true

{} + [] === [] + {} // false

{a: 1} // 1

{a: 1}; // 1

{'a': 1} // SyntaxError

{'a': 1}; // SyntaxError

{} + 0 + {}; // "0[object Object]"

{} + 0 + {} // "0[object Object]"
```

### AST

**[wikipedia: Abstract_syntax_tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree)**

> In computer science, an abstract syntax tree (AST), or just syntax tree, is a tree representation of the abstract syntactic structure of source code written in a programming language. Each node of the tree denotes a construct occurring in the source code. The syntax is "abstract" in not representing every detail appearing in the real syntax. For instance, grouping parentheses are implicit in the tree structure, and a syntactic construct like an if-condition-then expression may be denoted by means of a single node with three branches.
> 其实就是将源代码分析成所对应的树状结构，便于之后的语法分析，代码检查等。现在的很多热门工具如 webpack、vue、UglifyJS、Lint 等都会用到这个技术，各个浏览器引擎也会使用自家定义的一套语法书生成树规范，生成相应的语法树。

### {}语法解析分析

其实由于浏览器厂商众多，每个与解析情况不一致，平常代码中基本不会遇到{}+这种问题，我们也没有精力研究各厂商预解析源码，从 Chrome 和 Firefox 来看，总结出来有下面几点：

- {...}的前面有运算符号的时候，{...}都会被解析成对象字面量。
- {...}前面没有运算符时候但有;结尾的时候，{...}都会被解析成代码块。
- {...}前面什么运算符都没有，{...}后面也没有分号(;)结尾
  - Firefox 会始终如一的解析为代码块
  - chrome 在这种情况下需要被扒一下历史
    大概在 chrome 版本 49 之前，Chrome 控制台上面的输出结果基本和 Firefox 一致，之后在 chrome 上有人提出 bug，**[Issue 499864](https://bugs.chromium.org/p/chromium/issues/detail?id=499864)**，大概意思就是说我在控制台输入`{a: 4, b: 5}`你给我报个错干嘛，我就是想要一个对象而已。Chrome 确实该近几年大火，没过多久就修复了，修复的方式也特别 666，就是凡是语句以{开头，以}结尾，我解析的时候就包裹一层括号在外面。**[git 记录](https://chromium.googlesource.com/chromium/src.git/+/4fd348fdb9c0b3842829acdfb2b82c86dacd8e0a%5E!/#F2)**，里面的关键代码如下:

```
+    if (/^\s*\{/.test(text) && /\}\s*$/.test(text))

+        text = '(' + text + ')';
```

也就是说{} + 0 + {}其实是({} + 0 + {}), {a: 1}其实是({a: 1})

- 语法树图示
  以{} + 0 + {}为例来看
  - Chrome
    ![ES类型转换20220613192801](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A220220613192801.png)
    此时，Chrome 将第一个{}解析成对象
  - firefox
    ![ES类型转换20220613192825](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A220220613192825.png)
    此时，firefox 将第一个{}解析成代码块
    **[看 AST 的网站](http://resources.jointjs.com/demos/javascript-ast)**
    分析之后不难得出如上的结果

## JSON.stringify

### 处理规则

- 简单类型
  处理基本类型时，与使用 toString 基本相同，结果都是字符串，除了 undefined
- undefined
  只有 undefined 时返回 undefined，其他地方被忽略

```jsx
String(undefined) // 'undefined'
JSON.stringify(undefined) // undefined
JSON.stringify({ a: undefined }) // '{}'
```

- 简单类型包装对象
  布尔值、数字、字符串的包装对象在序列化过程中会自动转换成对应的原始值
- 部分复杂类型
  任意的函数以及 symbol 值，在序列化过程中会被忽略（出现在非数组对象的属性值中时）或者被转换成 null（出现在数组中时）

```jsx
JSON.stringify({ x: undefined, y: Object, z: Symbol('') })
// "{}"

JSON.stringify([undefined, Object, Symbol('')])
// "[null,null,null]"
```

### 参数

该函数接收三个参数，第二、三参数可选

- 第一参数（待处理对象）

  如果第一个参数的某个对象拥有 toJSON 方法，那么结果为该函数返回值的序列化

  ```jsx
  const skyline = {
    name: {
      toJSON: () => 'skyline',
    },
    age: 18,
  }
  JSON.stringify(skyline) // '{"name":"skyline","age":18}'
  ```

- 第二参数（替换者）

  MDN

  > The JSON.stringify() method converts a JavaScript object or value to a JSON string, optionally replacing values if a replacer function is specified or optionally including only the specified properties if a replacer array is specified
  > 第二参数可以是数组或函数

  - 数组
    数组列出要序列化输出的键值
    ```jsx
    JSON.stringify(foo, ['week', 'month'])
    // '{"week":45,"month":7}', only keep "week" and "month" properties
    ```
  - 函数
    指定序列化的方式，根据返回值输出
    函数返回 Number, String, Boolean, null 直接输出返回值得序列化
    undefined Symbol 函数 则忽略输出
    其他对象则递归对对象调用该函数并输出其返回

    ```jsx
    function replacer(key, value) {
      // Filtering out properties
      if (typeof value === 'string') {
        return undefined
      }
      if (value === undefined) {
        return '---'
      }
      return value
    }

    var foo = {
      foundation: 'Mozilla',
      model: 'box',
      week: 45,
      transport: 'car',
      month: 7,
      child: {
        foundation: undefined,
        model: 'box',
        week: 45,
        transport: 'car',
        month: 7,
      },
    }
    JSON.stringify(foo, replacer) // '{"week":45,"month":7,"child":{"foundation":"---","week":45,"month":7}}'
    ```

- 第三参数（缩进字符与长度）

  - 数字
    若参数为数字，则指定缩进长度，最多为 10
  - 字符
    若参数为字母，则指定缩进字符，最多为 10

  ```jsx
  JSON.stringify({ uno: 1, dos: 2 }, null, 100)
  // '{\n          "uno": 1,\n          "dos": 2\n}'
  JSON.stringify({ uno: 1, dos: 2 }, null, 10)
  // '{\n          "uno": 1,\n          "dos": 2\n}'
  JSON.stringify({ uno: 1, dos: 2 }, null, 'abcdefghijklmn')
  // '{\nabcdefghij"uno": 1,\nabcdefghij"dos": 2\n}'
  ```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> [https://github.com/mqyqingfeng/Blog/issues/164](https://github.com/mqyqingfeng/Blog/issues/164)

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

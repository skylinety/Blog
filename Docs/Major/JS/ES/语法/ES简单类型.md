# ES 简单类型

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 简单类型](#es-简单类型)
  - [ES 类型](#es-类型)
  - [Number](#number)
    - [Number进制表示](#number进制表示)
    - [NaN](#nan)
  - [Null & undefined](#null--undefined)
    - [null vs undefined](#null-vs-undefined)
  - [String](#string)
    - [字符串替换](#字符串替换)
    - [字符串截取](#字符串截取)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## ES 类型

ES 将会类型分为简单类型（原始类型）和复杂类型（结构类型）
其中常见的类型可用 typeof 进行简单判定。

```js
// Primitives:
Boolean : typeof instance === "boolean"
Number : typeof instance === "number"
String : typeof instance === "string"
BigInt : typeof instance === "bigint"
Symbol : typeof instance === "symbol"
undefined : typeof instance === "undefined"

// Structural Types:
Object : typeof instance === "object"
Function : typeof instance === "function"

// Structural Root Primitive:
null : typeof instance === "object"
```

对于复杂类型中 Array、RegExp 等对象的判定，要得到其明确类型而非'object'
需要使用
`Object.prototype.toString.call`
例如

```js
Array: Object.prototype.toString.call(instance) //'[object Array]'
RegExp: Object.prototype.toString.call(instance) //'[object RegExp]'
```

## Number

### Number进制表示

数字进制表示

| 进制 | EN          | 表示  | Input | Output |
| ---- | ----------- | ----- | ----- | ------ |
| 2    | binary      | 0b    | 0b11  | 3      |
| 8    | octal       | 0  0o | 011   | 9      |
| 16   | hexadecimal | 0x    | 0x11  | 17     |

### NaN

- NaN 的特征
  涉及 NaN 的操作返回 NaN
  NaN 不等于任何值，包括本身
- isNaN()
  isNaN 在接收到一个值以后会尝试将这个值转换成数字
  任何不能转换成数字的值都会导致该函数返回 true。

## Null & undefined

### null vs undefined

null 仿Java，表示存在但是为空（空对象指针），沿用c语言传统，隐式转换为0。
如果定义的变量将来用于保存对象，建议初始化为 null 而不是其他值
undefined 表示不存在，转为数值时为NaN 
    
    
| Name      | 表示             | 示例                  | 用法                   |
| --------- | ---------------- | --------------------- | ---------------------- |
| null      | 表示存在但是为空 | `5 + null // 5`       | 对象原型链的终点       |
| undefined | 表示不存在       | `5 + undefined// NaN` | 变量未赋值，函数未返回 |

## String

### 字符串替换

```jsx
// String.prototype.replace()
str.replace(regexp|substr, newSubstr|function)
```

字符串 replace 函数，接收两个参数，返回一个新的字符串。

第一个参数为匹配模式，第二参数为替换方案。
如果第一参数为字符串，则字符串中只有符合匹配的第一个位置会被替换。

如果第一个参数是全局匹配模式的正则表达式，同时指定一个函数作为第二个参数；
当匹配执行后，第二参数对应的函数就会执行，该函数的返回值作为替换字符串。
第二参数对应的函数，其参数如下：

```jsx
function(match,p1,p2, ... ,offset, string, groups){return newStr}
```

该函数的参数解析如下：

| key        | value                                                                           |
| ---------- | ------------------------------------------------------------------------------- |
| match      | 匹配的子串                                                                      |
| p1,p2, ... | 假如 replace()方法的第一个参数是一个 RegExp 对象，则代表第 n 个括号匹配的字符串 |
| offset     | 匹配到的子字符串在原字符串中的偏移量）                                          |
| string     | 被匹配的原字符串                                                                |
| groups     | 具名组构成的一个对象                                                            |


### 字符串截取

字符串截取常用方法为substr、substring、slice。
```jsx
var a = "skylinety"

a.slice(2,5)//"yli"

a.substr(2,5)//"yline"

a.substring(2,5)//"yli"
```

| 方法      | 参数               | 使用                                                                                                              |
| --------- | ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| slice     | 开始位置，结束位置 | slice的start如果为正数,end如果为负数，end从尾部算起，如果其位置超过开始位置，返回空字符串；slice中的start如果为负数，会从尾部算起，-1表示倒数第一个，-2表示倒数第2个。                     |
| substring | 开始位置，结束位置 | substring会取start和end中较小的值为start,二者相等返回空字符串，任何一个参数为负数被替换为0(即该值会成为start参数) |
| substr    | 开始位置，截取长度 | substr第一个参数可正负，第二个参数表示，要截取的长度,若该参数为负数或0，都将返回空字符串                          |
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

文章链接：[http://www.skyline.show/ES简单类型.html](http://www.skyline.show/ES简单类型.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

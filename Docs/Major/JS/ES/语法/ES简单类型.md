# ES 简单类型

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 简单类型](#es-简单类型)
  - [ES 类型](#es-类型)
  - [Number](#number)
    - [NaN](#nan)
  - [Null](#null)
  - [String](#string)
    - [Replace](#replace)

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

### NaN

- NaN 的特征
  涉及 NaN 的操作返回 NaN
  NaN 不等于任何值，包括本身
- isNaN()
  isNaN 在接收到一个值以后会尝试将这个值转换成数字
  任何不能转换成数字的值都会导致该函数返回 true。

## Null

null 表示存在但是为空
undefined 表示不存在

- null 表示空对象指针
- 如果定义的变量将来用于保存对象，建议初始化为 null 而不是其他值

## String

### Replace

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

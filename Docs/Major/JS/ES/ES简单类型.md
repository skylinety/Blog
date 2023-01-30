# ES 简单类型

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 简单类型](#es-简单类型)
  - [ES 类型](#es-类型)
  - [Number](#number)
    - [NaN](#nan)
  - [Null](#null)

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

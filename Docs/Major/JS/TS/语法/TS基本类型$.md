# TS 常见类型

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [TS 常见类型](#ts-常见类型)
  - [类型列表](#类型列表)
  - [Any/Unknown](#anyunknown)
  - [Object](#object)
    - [普通对象](#普通对象)
    - [函数](#函数)
    - [Array](#array)
    - [Turple](#turple)
  - [Custom Type](#custom-type)
  - [内置类型](#内置类型)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 类型列表

- Boolean type
- Number type
- String type
- Object type
- Array type
- Tuple Type
- Enum Type
- Any Type
- Union Type
- Literal Type
- Function Type
- Unknown Type
- Never Type
- Custom Type

如下列举不同类型的常见语法。

## Any/Unknown

any 表示任意类型，相当与 TS 类型系统的附加规则对于当前变量不生效。
unknown 指的是任意类型，类型未知。

使用 unknow 时需要注意，unknown 类型的变量不能赋值给明确类型的变量，除非进行类型断言,
any 则没有这个要求，二者的区别在于 any 使用基本不会存在限制，故而一般不推荐使用 any。

```jsx
let skyline: string = 'self'
let me: any
me = 1
skyline = me
```

改为使用 unknow 会报错

```jsx
let skyline: string = 'self'
let me: unknown
me = 1
skyline = me
// Type 'unknown' is not assignable to type 'string'.
```

可进行类型断言来解决

```jsx
let skyline: string = 'self';
let me: unknown;
me = 1;
// skyline = me as string;
skyline = <string>me;
```

## Object

### 普通对象

```jsx
let skyline: {
  name: string,
  age?: number,
  [prop: string]: string | number | undefined,
}
// let skyline: { name: string; age?: number; [prop: string]: string | number | void };
skyline = {
  name: 'skyline',
  gender: 'male',
}
```

`?`为非必填属性，当引入非必填属性时，动态添加的属性需要对类型延伸 void 或 undefined

### 函数

```jsx
let getMyself: (name: string, gender: string) => string
getMyself = (n: string, g: string) => `My name is ${n},I am ${g}`
```

### Array

```ts
// 纯字符串数组
const skyline: string[] = ['1', '1', '1']
const apples: Array<number> = [1, 1, 1, 1]
```

### Turple

Tuple 元组类型是固定长度的数组。

```ts
let skyline: [string, number]
skyline = ['1', 1]
```

## Custom Type

自定义类型（设定别名），通过 Type 关键字进行

```jsx
type Skyline = {
  name: string,
  age?: number,
  [prop: string]: string | number | undefined,
}
let me: Skyline
me = {
  name: 'skyline',
}
```

上述代码也可通过 interface 来实现。

```jsx
interface Skyline {
  name: string;
  age?: number;
  [prop: string]: string | number | undefined;
}
let me: Skyline
me = {
  name: 'skyline',
}
```

自定义类型与 interface 用法有诸多相似之处，
除了语法不同外，对于原始类型，联合类型，元组等，只能用 type 自定义类型来取别名。
interface可以重复声明，重复时自动合并，type只能声明一次。

```jsx
// primitive
type Name = string

// object
type SkylineX = { x: number }
type SkylineY = { y: number }

// union
type Skyline = SkylineX | SkylineY

// tuple
type Apples = [number, string]
```

## 内置类型

TODO

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://stackoverflow.com/questions/37233735/interfaces-vs-types-in-typescript

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/TS 基本类型.html](http://www.skyline.show/TS基本类型.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

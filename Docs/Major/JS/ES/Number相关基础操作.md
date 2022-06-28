# Number 相关基础操作

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Number 相关基础操作](#number-相关基础操作)
  - [保留小数](#保留小数)
    - [四舍五入](#四舍五入)
    - [不取舍](#不取舍)
  - [添加千位分隔符](#添加千位分隔符)
    - [toLocaleString](#tolocalestring)
    - [正则](#正则)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 保留小数

### 四舍五入

**toFixed**

```js
(2.123123123).toFixed(3); // 输出结果为 2.123
(2.123923123).toFixed(3); // 输出结果为 2.124
```

**toLocaleString**
toLocaleString 默认保留 3 位小数，且会产生千位分隔符

```js
(12332.123923123).toLocaleString(undefined, {
  minimumFractionDigits: 5,
  maximumFractionDigits: 6,
});
// 输出结果为 '12,332.123923'
```

可通过 minimumFractionDigits，maximumFractionDigits 来指定保留参数的长度

```js
(2.123923123).toLocaleString(undefined, {
  minimumFractionDigits: 5,
  maximumFractionDigits: 6,
});
// 输出结果为 '2.123923'
```

### 不取舍

**Math.floor**

```js
Math.floor(15.7784514 * 1000) / 1000; // 输出结果为 15.778
```

## 添加千位分隔符

### toLocaleString

通过 toLocaleString 很容易直接添加千位。

```js
(1231234234234).toLocaleString("en-US");
// '1,231,234,234,234'
```

```js
(1231234234234).toLocaleString();
// '1,231,234,234,234'
```

toLocaleString 将字符本地串化，第一个参数为串化标准，默认为'en-US'。
对于小数而言，其会四舍五入保留 3 位

### 正则

```js
(1231234234234 + "").replace(/(\d)(?=(\d{3})+$)/g, "$1,");
//'1,231,234,234,234'
```

**设计正则解析**

- `+`
  匹配前面一个表达式 1 次或者多次。等价于{1,}。
- `x(?=y)`
  匹配 x 仅仅当 x 后面跟着 y。这种叫做先行断言。

整个正则的意思为后面跟有三个或三的倍数个连续数字的数后面加上逗号

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Number相关基础操作.html](http://www.skyline.show/Number相关基础操作.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

# ES 常见符号

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 常见符号](#es-常见符号)
  - [算数操作符](#算数操作符)
    - [一元操作符](#一元操作符)
    - [二元操作符](#二元操作符)
  - [逻辑操作符](#逻辑操作符)
  - [位运算符](#位运算符)
    - [位运算概述](#位运算概述)
    - [按位与（ AND）](#按位与-and)
    - [按位或（OR）](#按位或or)
    - [按位异或（XOR）](#按位异或xor)
    - [按位非/按位取反（NOT）](#按位非按位取反not)
    - [位移](#位移)
    - [按位操作应用](#按位操作应用)
  - [其他操作符](#其他操作符)
    - [...](#)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 算数操作符
### 一元操作符

一元+运算符将其操作数转换为 Number 类型。一元减号同理但是反转正负

```js
+ '3'      // 数字3
- '-3'      // 数字3
+ [] //0
+ [1] //1
+ [1,2] //NaN
```

### 二元操作符

常见的加减乘除运算，
这里需要注意的是不同类型之间运算时会进行隐式类型转换。

## 逻辑操作符

ES 的逻辑操作符常见为逻辑与（&&）与逻辑或（||），需要掌握的要点如下：

- 都是短路操作符，即是第一个操作数可以决定结果，就不会对第二个操作数求值
  - 与操作符，第一个求值是 false，直接返回第一个操作数
  - 或操作符，第一个求值是 true，直接返回第一个操作数
- null、NaN、undefined 等求布尔值结果是 false(本点适用于第一点，单独提出只是需要注意而已）
  - 故如果它们出现在与操作符第一个操作数，则直接返回它们
  - 如果它们出现在或操作符第一个操作数，则返回第二个操作数

## 位运算符

### 位运算概述

按位运算符（bitwise operations ）有较快的运算速度，
合理应用能简化应用并提升效率。
所有的按位操作符的操作数都会被转成32位补码（two's complement）形式的**整数**进行运算。

### 按位与（ AND）

```jsx
a & b 
```

两个数对应比特位有0结果为0

### 按位或（OR）

```jsx
a | b  
```

两个数对应比特位有1结果为1

### 按位异或（XOR）

```jsx
a ^ b
```
两个数对应比特位相同为零，不同为1

### 按位非/按位取反（NOT）   
 
```jsx
~ a
```

反转操作数的比特位，即0变成1，1变成0。
在计算机中数值是通过补码的形式存在的，按位非即把补码的各位进行反转。

以数值3为例，对于正数按位非
3的补码为00000011，按位取反后得到11111100
3 按位取反
计算机正数按位取反过程
3 => 00000011 => 11111100  => -4
人为计算过程（需要得到补码后进一步推算出原码）
3 => 00000011 => 11111100 => 11111011 => 10000100 => -4
对于负数按位非
-3按位取反
-3的补码为11111101
对于计算机来说，过程如下
-3  =>  11111101 （补码） => 00000010 (按位非) => 2
人为计算需要先算出-3的补码
-3  =>  10000011（原码）  =>  11111100（反码）  =>  11111101 （补码） => 00000010 (按位非) => 2

### 位移

* 左移（Left shift）	
```jsx
a << b
```
将 a 的二进制形式向左移 b (< 32) 比特位，右边用0填充。
* 右移
有符号右移	
```jsx
a >> b
```
将 a 的二进制表示向右移 b (< 32) 位，丢弃被移出的位。
无符号右移	
```jsx
a >>> b
```
将 a 的二进制表示向右移 b (< 32) 位，丢弃被移出的位，并使用 0 在左侧填充
左侧填充0，结果非负

### 按位操作应用

* 奇偶判定
```jsx
N&1 
// 0偶数1奇数
```

* -1判定
```jsx
~N 
// 若~N == 0则N == -1
```
常用于indexOf等场景。

* 取整数部分
```jsx
~~N
// ~~(Math.random() * 10)
// 可随机获取0-9的整数
```
上文已提到，位运算会转换成二进制整数来进行运算。
同样双非运算会丢弃掉小数部分，故经过两次0-1翻转可以得到原来的整数部分。

* 框架更新补丁

在Vue对模板进行语法分析并编译成render时，
使用了左移和按位与来进行更新标记，
具体参考[官方文档](https://vuejs.org//guide/extras/rendering-mechanism.html#patch-flags)。


## 其他操作符

### ...

- 展开运算符

用作展开运算符，将数组或其他可迭代对象进行展开，也可用于对象属性展开。

数组或其他可迭代对象进行展开

```jsx
let skyline = [1, 2, 3]
myFunction(...skyline)

const clonedArray = [...skyline]
const concatArray = [...clonedArray, ...skyline]
```

对象属性展开

```jsx
const obj1 = { foo: 'bar', x: 42 }

const clonedObj = { ...obj1 }
// { foo: "bar", x: 42 }
```

这里的拷贝都是浅拷贝。

- 剩余参数

主要用在函数，将不定参数数量的函数进行参数收集。

```jsx
function f(a, b, ...theArgs) {
  // …
}
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github 仓库](https://github.com/skylinety/Blog)点亮 ⭐️

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters 
>
> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax
>
> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES 常见符号.html](http://www.skyline.show/ES常见符号.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

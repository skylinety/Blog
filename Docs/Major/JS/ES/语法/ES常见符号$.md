# ES 常见符号

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 常见符号](#es-常见符号)
  - [算数操作符](#算数操作符)
  - [逻辑操作符](#逻辑操作符)
  - [其他操作符](#其他操作符)
    - [...](#)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 算数操作符

## 逻辑操作符

ES 的逻辑操作符常见为逻辑与与逻辑或，需要掌握的要点如下：

- 都是短路操作符，即是第一个操作数可以决定结果，就不会对第二个操作数求值
  - 与操作符，第一个求值是 false，直接返回第一个操作数
  - 或操作符，第一个求值是 true，直接返回第一个操作数
- null、NaN、undefined 等求布尔值结果是 false(本点适用于第一点，单独提出只是需要注意而已）
  - 故如果它们出现在与操作符第一个操作数，则直接返回它们
  - 如果它们出现在或操作符第一个操作数，则返回第二个操作数

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

> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters > https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES 常见符号$.html](http://www.skyline.show/ES常见符号$.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

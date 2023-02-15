# String 相关基础操作

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [String 相关基础操作](#string-相关基础操作)
  - [字符串存为数组](#字符串存为数组)
  - [重复字符串](#重复字符串)
  - [变量命名](#变量命名)
    - [中划线转驼峰](#中划线转驼峰)
    - [驼峰转中划线](#驼峰转中划线)
  - [交换单词位置](#交换单词位置)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 字符串存为数组

```jsx
var a = 'skyline'

var b = Array.prototype.slice.call(a, 0)
// ['s', 'k', 'y', 'l', 'i', 'n', 'e']
var c = a.split('')
// ['s', 'k', 'y', 'l', 'i', 'n', 'e']
```

## 重复字符串

主要为使用字符串的 repeat 方法或数组来实现

```jsx
Array(7).fill('1').join('')
// '1111111'
new Array(8).join(1)
// '1111111'
'1'.repeat(7)
// '1111111'
String.prototype.repeat.call(1, 7)
// '1111111'
```

---

## 变量命名

### 中划线转驼峰

```jsx
'my-name-is-skyline'.replace(/-(\w)/g, (...args) => args[1].toUpperCase())
// 'myNameIsSkyline'
```

这里涉及字符串 replace 的用法。

```jsx
str.replace(regexp|substr, newSubstr|function)
```

如果第一个参数是正则表达式， 并且其为全局匹配模式，同时指定一个函数作为第二个参数。
当匹配执行后，第二参数对应的函数就会执行，该函数的返回值作为替换字符串。
第二参数对应的函数，其参数如下：

```jsx
function(match,p1,p2, ... ,offset, string, groups){return newStr}
```

参数解析如下：

| key        | value                                                                           |
| ---------- | ------------------------------------------------------------------------------- |
| match      | 匹配的子串                                                                      |
| p1,p2, ... | 假如 replace()方法的第一个参数是一个 RegExp 对象，则代表第 n 个括号匹配的字符串 |
| offset     | 匹配到的子字符串在原字符串中的偏移量）                                          |
| string     | 被匹配的原字符串                                                                |
| groups     | 具名组构成的一个对象                                                            |

查看上例过程输出：

```jsx
'my-name-is-skyline'.replace(/-(\w)/g, (...args) => {
  console.log(...args)
  return args[1].toUpperCase()
})

// -n n 2 my-name-is-skyline
// -i i 7 my-name-is-skyline
// -s s 10 my-name-is-skyline
```

### 驼峰转中划线

```jsx
'myNameIsSkyline'.replace(/([A-Z])/g, '-$1').toLowerCase()
// 'my-name-is-skyline'
```

若 replace 的第二个参数不是函数而是替换字符 newSubstr，
可以在第二个参数中插入特殊变量来表示源字符相关字符。
$n 表示插入第 n 个**捕获括号**匹配的字符串。

## 交换单词位置

```jsx
'Skyline Liu'.replace(/(\w+)\s(\w+)/g, '$2, $1')
// 'Liu, Skyline'
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github 仓库](https://github.com/skylinety/Blog)点亮 ⭐️

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/String 相关基础操作.html](http://www.skyline.show/String相关基础操作.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

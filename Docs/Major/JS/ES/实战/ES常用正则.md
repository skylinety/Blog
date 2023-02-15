# ES 常用正则

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 常用正则](#es-常用正则)
  - [正则对象](#正则对象)
    - [正则创建](#正则创建)
    - [双重转义](#双重转义)
    - [RegExp.prototype.exec()](#regexpprototypeexec)
    - [正则标志](#正则标志)
  - [基本规则](#基本规则)
  - [正则使用](#正则使用)
    - [汇总表](#汇总表)
    - [匹配定长字符](#匹配定长字符)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 正则对象

### 正则创建

正则创建有两种方式，对象字面量与构造函数。
使用构造函数 RegExp 创建时接受两个参数。
第一个是要匹配的字符串模式，第二个是可选的标识字符串。
当创建的字符中包含元字符(正则中有特殊含义或功能的字符)时，
要表示原有字符的含义，两种方式创建时都要需要在元字符前使用`\`进行转义，使其表示为普通含义。
常见的特殊字符有：

```jsx
[ \ ^ $ . | ? * + ( )
```

### 双重转义

`\`除了在正则中表示转义字符，在字符串中也是转义字符。
常见的就是表示换行和 Unicode 字符，其他还有制表符，回退等。

- `\n` 即换行
- `\u` 即表示 Unicode 字符。`\u{61}` 表示字符'a'

`\`接无效字符时，转义会被自动移除。

```jsx
var skyline = 's.s'
console.log(skyline) // "s.s"
var test = '.at skyline'
console.log(test) // ".at skyline"
```

当使用构造函数创建正则时，第一参数为字符串，需要匹配的字符包含元字符时，
由于字符串要消耗`\`转义，此时的元字符需要进行双重转义。

例如，当需要匹配字符串'.at skyline'时：

字面量定义： `/\.at\sskyline/gi`
构造函数定义： `new RegExp('\\.at\\sskyline', 'gi')`

```jsx
var reg = /\.at\sskyline/gi
var reg1 = new RegExp('\\.at\\sskyline', 'gi')
console.log(reg.test('.at skyline'))
// true
console.log(reg1.test('.at skyline'))
// true
```

### RegExp.prototype.exec()

exec 用于搜索指定字符串的匹配，当匹配成功时，返回数组，失败返回 null。

```jsx
RegExpObject.exec(string)
```

返回的数组跟**正则是否有子串（正则的圆括号内，圆括号被称为捕获括号），是否全局，开始匹配的位置（lastIndex 指定）有关**。

- 非全局有子串

```jsx
var str = 'Skyline should be hardworking(Skyline up up up)'
var reg = /Sky(line)/
console.log(reg.exec(str))
// ["Skyline", "line", index: 0, input: "Skyline should be hardworking(Skyline up up up)"]

console.log(reg.exec(str))
// ["Skyline", "line", index: 0, input: "Skyline should be hardworking(Skyline up up up)"]
console.log(str.match(reg))
// ["Skyline", "line", index: 0, input: "Skyline should be hardworking(Skyline up up up)"]
```

未开启全局，多次执行返回结果一致。
此时函数的用法与 String.prototype.match 类似。
只能够在字符串中匹配一次，用于获取匹配的字符串。
如果没有找到匹配的字符串，那么返回 null。

```jsx
string.match(RegExpObject)
```

- 全局有子串

```jsx
var str1 = 'Skyline should be hardworking(Skyline up up up Skyline)'
var reg1 = /Skylin(e)/g
reg1.lastIndex = 8
console.log(reg1.exec(str1))
console.log(reg1.lastIndex)
// VM1002:4 (2) ["Skyline", "e", index: 30, input: "Skyline should be hardworking(Skyline up up up Skyline)"]
// 37

console.log(reg1.exec(str1))
// VM1016:1 (2) ["Skyline", "e", index: 47, input: "Skyline should be hardworking(Skyline up up up Skyline)"]

console.log(reg1.exec(str1))
// VM1021:1 null

console.log(reg1.exec(str1))
// VM3222:1 (2) ["Skyline", "e", index: 0, input: "Skyline should be hardworking(Skyline up up up Skyline)"]

console.log(str1.match(reg1))
// ['Skyline', 'Skyline', 'Skyline']
```

exec 常用于迭代匹配字符串中的某个字符。

开启全局，此 exec 返回值同样是一个数组，并且每次迭代在字符串中匹配一次。
不过此时，exec 一般会和 该正则的 lastIndex 属性匹配使用，
检索位置由 lastIndex 属性指定的字符处开始，
未检索到返回为 null ，同时将 lastIndex 重置为 0。
注意开启全局迭代使用时与 match 表现完全不一致。

exec 作为一个原始的方法，很多延伸方法内部都在调用 exec，包括 String 对象的部分方法。

- RegExp.prototype.test()
  用于判定是否匹配
- String.prototype.match()
  获取匹配信息（不包括捕获组）
- String.prototype.search()
  字符串搜索
- String.prototype.replace()
  字符串替换

### 正则标志

- g
  全局标志，是否全局匹配，通常配合 exec 和 replace 使用。
  通过 RegExp.prototype.global 来获取是否设定。
- y
  粘滞标志，仅从正则表达式的 lastIndex 属性表示的索引处搜索。
  通过 RegExp.prototype.sticky 来获取是否设定。
- i
  忽略大小写标志。
  通过 RegExp.prototype.ignore 来获取是否设定。

全局标志通常配合 exec 和 replace 使用，前文已述。
粘滞标志通常和 test 配合使用，当粘滞设定，test 会从 lastIndex 处检索，每次检索更新 lastIndex 位置。

## 基本规则

## 正则使用

### 汇总表

| 简述     | 正则         | 描述                   |
| -------- | ------------ | ---------------------- |
| 定长字符 | /^.{1,200}$/ | 匹配 m 到 n 长度的字符 |

### 匹配定长字符

/^.{2, 5}$/匹配指定长度的字符

```sh
 /^.{2,5}$/.test('aaaaaaa') // false
 /^.{2,5}$/.test('aa') // true
 /^.{2,5}$/.test('aaaaa') // true
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github 仓库](https://github.com/skylinety/Blog)点亮 ⭐️

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/exec

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES 常用正则.html](http://www.skyline.show/ES常用正则.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

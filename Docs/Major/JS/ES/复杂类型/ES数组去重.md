# ES 数组去重

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 数组去重](#es-数组去重)
  - [举个栗子](#举个栗子)
  - [正常人](#正常人)
  - [我有想法](#我有想法)
  - [我会 es6](#我会-es6)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 举个栗子

```js
var he = { name: 'he', sex: 'male' },
  she = { name: 'she', sex: 'female' },
  age = [18, 28],
  family = [
    1,
    1,
    '1',
    'skyline',
    'skyline',
    he,
    he,
    she,
    { name: 'she', sex: 'female' },
    age,
    [18, 28],
  ]

family.length //11
```

## 正常人

使用循环

```js
function removeRepetition1(arr) {
  let ret = []

  for (let i = 0, j = arr.length; i < j; i++) {
    if (ret.indexOf(arr[i]) === -1) {
      ret.push(arr[i])
    }
  }

  return ret
}

function removeRepetition2(arr) {
  let ret = []

  arr.forEach(function (e, i, arr) {
    if (arr.indexOf(e) === i) {
      ret.push(e)
    }
  })

  return ret
}
removeRepetition1(family)
removeRepetition2(family)
```

indexOf 比较参数与数组每一项时候，使用的是严格等于。

![ES数组去重20220615145414](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E6%95%B0%E7%BB%84%E5%8E%BB%E9%87%8D20220615145414.png)

## 我有想法

```js
//使用对象
function removeRepetition3(arr) {
  let tmp = {},
    ret = []

  for (let i = 0, j = arr.length; i < j; i++) {
    if (!tmp[arr[i]]) {
      tmp[arr[i]] = 1
      ret.push(arr[i])
    }
  }

  return ret
}

//先排序
function removeRepetition4(arr) {
  let ret = [],
    end

  arr.sort()
  end = arr[0]
  ret.push(arr[0])

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] !== end) {
      ret.push(arr[i])
      end = arr[i]
    }
  }

  return ret
}
```

removeRepetition3 仅适用于简单类型，对象产生的属性相同，是`{[object Object]: 1}`,所以只会保留第一个出现的对象.
数组产生的是[xx,xx,xx].toString()作为属性，[1,2]产生的是`{1,2: 1}`，同时数字型字符串会被干掉，仅适用于纯数字去重.
该方法不推荐，只需将 tmp 对象换成 es6 的 map 结构即可。参看 removeRepetition6。

removeRepetition4 采用的是 sort 方法，该方法在不带参数的情况下，默认使用的是 unicode 字符表顺序，该排序容易导致其他问题，不推荐

## 我会 es6

```js
function removeRepetition5(arr) {
  return [...new Set(arr)]
  // return Array.from(new Set(array));
}

function removeRepetition6(arr) {
  let tmp = new Map(),
    ret = []

  for (let i = 0, j = arr.length; i < j; i++) {
    if (!tmp.has(arr[i])) {
      tmp.set(arr[i], 1)
      ret.push(arr[i])
    }
  }

  return ret
}

removeRepetition5(family)
//(10) [1, "1", "skyline", {…}, {…}, {…}, {…}, Array(2), Array(2), Array(0)]
removeRepetition6(family)
//(10) [1, "1", "skyline", {…}, {…}, {…}, {…}, Array(2), Array(2), Array(0)]
```

ES6 提供了新的数据结构 Set。它类似于数组，但是成员的值都是唯一的，没有重复的值。
ES6 提供了新的数据结构 Map。它类似于对象，也是键值对的集合，但是“键”的范围不限于字符串，各种类型的值（包括对象）都可以当作键。
Map 的键实际上是跟内存地址绑定的，只要内存地址不一样，就视为两个键。
可进一步参考[Set 和 Map 数据结构](http://es6.ruanyifeng.com/#docs/set-map)

![ES数组去重20220615150043](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E6%95%B0%E7%BB%84%E5%8E%BB%E9%87%8D20220615150043.png)

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](http: //www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warrant

本文作者： Skyline(lty)

授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https: //creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

# ES 数组

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 数组](#es-数组)
  - [常见坑点](#常见坑点)
  - [实例方法](#实例方法)
    - [表格概述](#表格概述)
    - [方法进阶](#方法进阶)
  - [部分实战](#部分实战)
    - [构造数组](#构造数组)
    - [slice 截取](#slice-截取)
    - [数据结构模拟](#数据结构模拟)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 常见坑点

- 数组的 length 不是只读的，可以通过修改来设置长度
- 一般通过 isArray 来判断是否是数组，而不用 instanceof

## 实例方法

### 表格概述

（-)表示可选参数

| 方法名      | 描述                     | 参数                                               | 返回                               | 是否修改原数组 |
| ----------- | ------------------------ | -------------------------------------------------- | ---------------------------------- | -------------- |
| push        | 逐个添加至数组屁股       | 任意（-）                                          | 数组新长度                         | 是             |
| pop         | 砍掉屁股一项             | 无                                                 | 被砍掉的屁股                       | 是             |
| shift       | 砍掉第一项               | 无                                                 | 被砍掉的第一                       | 是             |
| unshift     | 逐个添加至数组头部       | 任意（-）                                          | 数组新长度                         | 是             |
| reverse     | 反向重排                 | 无                                                 | 数组                               | 是             |
| sort        | 排序                     | fn（-）                                            | 数组                               | 是             |
| concat      | 联结                     | 任意（-）                                          | 新数组                             | 否             |
| slice       | 截取                     | 开始位置（-），结束位置（-）                       | 新数组                             | 否             |
| splice      | 删除、插入、替换         | 开始位置（-），结束位置（-），插入项（-）          | 包含被删除的项的数组，没有则空数组 | 是             |
| indexOf     | 查找位置                 | 查找项（-），开始位置（-）                         | 找到返回位置，否则-1               | 否             |
| lastIndexOf | 反向查找                 | 查找项（-），开始位置（-）                         | 找到返回位置，否则-1               | 否             |
| every       | 与迭代                   | 迭代函数，this 指向作用域（-）                     | 布尔值                             | 否             |
| some        | 或迭代                   | 迭代函数，this 指向作用域（-）                     | 布尔值                             | 否             |
| filter      | 迭代筛选                 | 迭代函数，this 指向作用域（-）                     | 函数返回值为 true 的项组成的数组   | 否             |
| map         | 迭代调整                 | 迭代函数，this 指向作用域（-）                     | 函数返回值组成的数组               | 否             |
| forEach     | 迭代循环                 | 迭代函数，this 指向作用域（-）                     | 无                                 | 否             |
| reduce      | 归并                     | 归并函数，初始值（-）                              | 归并终值                           | 否             |
| reduceRight | 反向归并                 | 归并函数，初始值（-）                              | 归并终值                           | 否             |
| copyWithin  | 复制替换                 | 替换开始位置，读取开始位置（-），读取结束位置（-） | 数组                               | 是             |
| find        | 符合条件的第一个成员     | 条件函数                                           | 符合条件的成员否则 undefined       | 否             |
| findIndex   | 符合条件的第一个成员位置 | 条件函数                                           | 符合条件的成员位置否则-1           | 否             |
| fill        | 给定值填充数组           | 填充值，开始位置（-），结束位置（-）               | 数组                               | 是             |
| entries     | 返回键值的遍历对象       | 无                                                 | 键值的遍历对象                     | 否             |
| keys        | 返回键的遍历对象         | 无                                                 | 键值的遍历对象                     | 否             |
| values      | 返回值的遍历对象         | 无                                                 | 键值的遍历对象                     | 否             |
| includes    | 包含值得判定             | 给定值                                             | 布尔值                             | 否             |

- 增删排改（push、pop、shift、unshift、reverse、sort、splice、copyWithin、fill）会修改原数组
- 涉及遍历的方法（every、some、filter、map、forEach）第二个参数可以指定 this

### 方法进阶

| 方法名  | 描述                                                                                                                                             |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| sort    | 无参数时为每一项调用 toString()方法，按返回的字符串首字母升序，有参数 fn 时 fn 接受两个参数，即数组的两项，根据 fn 返回值正负零来确定先后        |
| concat  | 无参数时返回原数组副本，**多个参数中如果有数组，数组每一项添加到新数组（相当于 ES6 中的...）**，其他类型直接添加                                 |
| slice   | 无参数时返回原数组副本，两个参数表示截取开始结束位置，一个参数时表示开始位置截取到最末。参数为负数时，加上数组长度后截取，结束大于开始返回空数组 |
| splice  | 前两项整数，第一项指定删除与插入的开始位置，第二项指定删除个数，之后项是依次插入的数据                                                           |
| indexOf | 参数一到两个，第一项指定查找项，与数组中项对比时要求使用**严格相等**判定，第二个指定开始位置（可选）                                             |
| every   | 通过对数组每一项执行函数后全返回 true 则返回 true，否则 false                                                                                    |
| some    | 通过对每一项执行函数后至少一项返回 true 则返回 true，否则 false                                                                                  |
| filter  | 返回通过对每一项执行函数后返回 true 的项组成的新数组                                                                                             |
| map     | 返回通过对每一项执行函数取返回值组成的新数组                                                                                                     |
| reduce  | 归并函数接受 4 个参数：前一个值，当前值，项索引，数组对象。归并函数当前返回值作为第一个参数传给下一项                                            |

## 部分实战

### 构造数组

构造一个一个长度为 n 的数组

```jsx
Array(7).fill()
//(7) [undefined, undefined, undefined, undefined, undefined, undefined, undefined]
Array(7)
//(7) [undefined × 7]

Array.apply(null, { length: 7 })
//(7) [undefined, undefined, undefined, undefined, undefined, undefined, undefined]
```

需要注意的是，直接调用构造函数使用 map 填充数据存在问题

```jsx
Array(7)
  .fill()
  .map(() => 1)
// (7) [1, 1, 1, 1, 1, 1, 1]
Array(7).map(() => 1)
// (7) [undefined × 7]
Array.apply(null, { length: 7 }).map(() => 1)
// (7) [1, 1, 1, 1, 1, 1, 1]
```

### slice 截取

```jsx
'skyline'.slice(1, 5)
 // "kyli"
 
['s', 'k', 'y', 'l', 'i', 'n', 'e'].slice(1, 5)
 // ["k", "y", "l", "i"]
```

![ES数组20230210161709](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E6%95%B0%E7%BB%8420230210161709.png)

### 数据结构模拟

- 模拟栈，push + pop
- 模拟队列，shift + push
- 模拟反向队列，unshift + pop

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github 仓库](https://github.com/skylinety/Blog)点亮 ⭐️

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES 数组.html](http://www.skyline.show/ES数组.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

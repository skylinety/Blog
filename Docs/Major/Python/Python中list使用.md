# Python 中 list 使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Python 中 list 使用](#python-中-list-使用)
  - [list 常见方法](#list-常见方法)
  - [list 常见使用](#list-常见使用)
    - [用法表](#用法表)
    - [用法解析](#用法解析)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## list 常见方法

| Name    | Desc                                                               | Eg                                           |
| ------- | ------------------------------------------------------------------ | -------------------------------------------- |
| append  | 列表新增元素                                                       | list.append(obj)                             |
| count   | 统计某个元素在列表中出现的次数                                     | list.count(obj)                              |
| index   | 从列表中找出某个值第一个匹配项的索引位置                           |                                              |
| remove  | 移除列表中某个值的第一个匹配项                                     | list.remove(obj)                             |
| pop     | 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值       | list.pop([index=-1])                         |
| insert  | 将对象插入列表                                                     | list.insert(index, obj)                      |
| reverse | 反向列表中元素                                                     | list.reverse()                               |
| sort    | 对原列表进行排序                                                   | list.sort(cmp=None, key=None, reverse=False) |
| extend  | 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） | list.extend(seq)                             |

## list 常见使用

### 用法表

| Name                   | Eg                                                      | Out                                                                                   |
| ---------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| map                    | list(map(lambda str: str + 'skyline', ['a', 'b', 'c'])) | ['askyline', 'bskyline', 'cskyline']                                                  |
| 重复 list              | `[5] * 5`                                               | [5, 5, 5, 5, 5]                                                                       |
| 二维 list              | `[[0] * 5 for _ in range(5)] `                          | [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] |
| list 截取              | `['a', 'b', 'c'][1:2]` `['a', 'b', 'c'][1:]`              | `['b']` `['b', 'c'] `                                                                   |
| list 长度              | len([1, 2, 3])                                          | 3                                                                                     |
| list 组合              | [1, 2, 3] + [4, 5, 6]                                   | [1, 2, 3, 4, 5, 6]                                                                    |
| 存在判定               | 3 in [1, 2, 3]                                          | True                                                                                  |
| 取最大值               | max([1,2,3])                                            | 3                                                                                     |
| 取最小值               | min([1,2,3])                                            | 1                                                                                     |
| 删除元素               | del list[2]                                             |                                                                                       |
| 遍历并获取 index/value | `for index, value in enumerate(nums): ` `for index in range(len(nums)):`                  |                                                                                       |

### 用法解析

- map

lambda 指匿名函数

```python
list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
#[1, 4, 9, 16, 25]
```

- 二维 list

不能以`[[0] * 5] * 5` 来创建二维数组，里面的每一个子数组是指向同一地址

- 遍历获取 index/value

```py
skyline = [1,2]

for i, v in enumerate(skyline):
	print (i, ",",v)
# 0 , 1
# 1 , 2

for i in range(len(skyline)):
    print (i, ",",skyline[i])
# 0 , 1
# 1 , 2
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Python中list使用.html](http://www.skyline.show/Python中list使用.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

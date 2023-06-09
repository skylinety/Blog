# Python 常见问题汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Python 常见问题汇总](#python-常见问题汇总)
  - [is 与 == 的区别](#is-与--的区别)
  - [函数内部修改外部变量](#函数内部修改外部变量)

<!-- /code_chunk_output -->

## is 与 == 的区别

is 设计用于身份确认， 判定前后两者是否为自身，即 is, is not 对比的是两个变量的内存地址
== 设计用于判等，即==，!= 对比的是两个变量的值。

在 python3.8 以前，
数值型和字符串型的情况下，a is b 才为 True，当 a 和 b 是 tuple，list，dict 或 set 型时，a is b 为 False。

== 是 python 标准操作符中的比较操作符，用来比较判断两个对象的 value(值)是否相等，不管什么类型

![Python常见问题汇总$20220713175442](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Python%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BB%2420220713175442.png)

在 python3.8+后，即便是数字与字符串判等，也不再推荐使用 is， 会有如下警告

```jsx
SyntaxWarning: "is" with a literal. Did you mean "=="?
```

## 函数内部修改外部变量

跟JS等其他语言闭包不一样的是，Python函数内部直接修改外部变量会报错。

```py
UnboundLocalError: local variable 'a' referenced before assignment
```

如在力扣题目
[404. 左叶子之和](https://leetcode.cn/problems/sum-of-left-leaves/description/)中，
其题解为

```py
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def traverse(root, isLeft):
            if not root:
                return
            if isLeft and not (root.left or root.right):
                nonlocal ret
                ret += root.val
            traverse(root.left, True)
            traverse(root.right, False)
            
        traverse(root, False)
        return ret
```
使用ret作为闭包，修改ret时，需要先行表明变量非函数内部变量

```py
nonlocal ret
```
若ret未全局变量，应为
```py
global ret
```


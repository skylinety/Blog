# Python 常见问题汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Python 常见问题汇总](#python-常见问题汇总)
  - [is 与 == 的区别](#is-与--的区别)

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

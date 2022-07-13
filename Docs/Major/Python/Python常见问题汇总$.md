# Python常见问题汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Python常见问题汇总](#python常见问题汇总)
  - [is 与 == 的区别](#is-与--的区别)

<!-- /code_chunk_output -->

## is 与 == 的区别

数值型和字符串型的情况下，a is b才为True，当a和b是tuple，list，dict或set型时，a is b为False。

==是python标准操作符中的比较操作符，用来比较判断两个对象的value(值)是否相等，不管什么类型

- is, is not 对比的是两个变量的内存地址
- ==,!= 对比的是两个变量的值
  
![Python常见问题汇总$20220713175442](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Python%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BB%2420220713175442.png)
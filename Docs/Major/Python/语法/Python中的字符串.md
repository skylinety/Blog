## Python中的字符串


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Python中的字符串](#python中的字符串)
- [内置函数](#内置函数)
- [字符串实例函数](#字符串实例函数)
- [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 内置函数

| Name | Explanation | Usage | Out | ES Counterpart |
| --- | --- | --- | --- | --- |
| max | python取列表中最长的字符串 | max(['ale', 'apple', 'plea'], key=len, default='') | apple |  |
| ord | 获取字符的utf8编码 | ord('A') | 65 | 'A'.charCodeAt() |
| chr | 把编码转换为对应的字符 | chr(65) | 'A' | String.fromCharCode(65) |
| str | 转换成字符串 | str(12) | '12' |  |

## 字符串实例函数
| Name | Explanation | Usage | Out | ES Counterpart |
| --- | --- | --- | --- | --- |
| count | 获取字符串中某个字符的数量 | 'skyline liu'.count('l') | 2 |  |
| isupper | 是否大写 | 'A'.isupper() | True |  |
| islower | 是否小写 | 'a'.islower() | True |  |
| split | 字符串分割 | 'a b c'.split(' ') | ['a', 'b', 'c'] |  |
| upper | 转换成大写 |  |  |  |
| lower | 转换成小写 |  |  |  |

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️


> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Python中的字符串.html](http://www.skyline.show/Python中的字符串.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

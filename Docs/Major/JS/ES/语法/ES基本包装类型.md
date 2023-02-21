# ES基本包装类型

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES基本包装类型](#es基本包装类型)
  - [常见的基本包装类型](#常见的基本包装类型)
  - [基本包装类型的对象生存期](#基本包装类型的对象生存期)
  - [构造函数与转型函数](#构造函数与转型函数)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->


## 常见的基本包装类型

常见的基本包装类型，包括Boolean、Number、String三种。
其创建方式包括转型函数和字面量，不包含构造函数。
引用类型与基本包装类型的主要区别就是对象的生存期。

## 基本包装类型的对象生存期

```jsx
var s = 'skyline'
s.age = 23
console.log(s.age)
```
以上代码可以想象成如下代码周期，通过使用构造函数来模拟包装：

![ES基本包装类型20230221163543](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E5%9F%BA%E6%9C%AC%E5%8C%85%E8%A3%85%E7%B1%BB%E5%9E%8B20230221163543.png)

当最后访问s.age时相当于又包装了一个新的对象，故其age不存在。

## 构造函数与转型函数

```jsx
var str = String('skyline')//转型函数，产生基本包装类型，相当于字面量创建，设置属性无效
console.log(typeof str)//string
var obj = new String('skyline')//构造函数，产生引用类型，可设置属性
console.log(typeof obj)//object
```

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

文章链接：[http://www.skyline.show/ES基本包装类型.html](http://www.skyline.show/ES基本包装类型.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

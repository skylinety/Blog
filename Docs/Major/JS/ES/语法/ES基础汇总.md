# ES 基础汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 基础汇总](#es-基础汇总)
  - [switch 语句](#switch-语句)
  - [JS 与 ES](#js-与-es)
  - [闭包](#闭包)

<!-- /code_chunk_output -->

## switch 语句

**switch 使用的是全等判定**
通过为每个 case 语句后添加 break 来避免执行多个 case 的情况，合并多种情况时最好加入注释

## JS 与 ES

![ES基础汇总20220613142541](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E5%9F%BA%E7%A1%80%E6%B1%87%E6%80%BB20220613142541.png)

## 闭包

| 源                          | 定义                                             |
| --------------------------- | ------------------------------------------------ |
| 《JavaScript 高级程序设计》 | 闭包是指有权访问另一个'函数'作用域中的变量的函数 |
| 《JavaScript 权威指南》     | 从技术的角度讲，所有的 JavaScript 函数都是闭包   |
| MDN                         | 闭包是指那些能够访问自由变量的函数               |

自由变量是指在函数中使用的，但既不是函数参数也不是函数的局部变量的变量，可以简单理解为函数外部的变量。
从理论角度出发，如《JavaScript 权威指南》所说，所有的函数都是闭包。
因为即便是最外层定义的函数，它们也可以访问全局上下文中的自由变量。
在实际编程过程中，一般认为以下函数才算是闭包：

- 即使创建它的上下文已经销毁，它仍然存在（比如，内部函数从父函数中返回）
- 在函数体中引用了自由变量

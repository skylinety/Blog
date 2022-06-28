# HTML 标签

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [HTML 标签](#html-标签)
  - [script](#script)
    - [type 属性](#type-属性)
  - [BMW WARNING](#bmw-warning)


<!-- /code_chunk_output -->

## script

### type 属性

defer 要等到整个页面在内存中 DOM 渲染结束与其他脚本执行之后，才会执行；
async 一旦下载完，渲染引擎就会中断渲染，执行改脚本，再继续渲染。**defer 是“渲染完再执行”，async 是“下载完就执行”**。

| type 值      | async                                                    | defer                          |
| ------------ | -------------------------------------------------------- | ------------------------------ |
| 描述         | 立即下载脚本，不妨碍其他操作，不依赖其他脚本，不阻塞文档 | 延迟脚本到文档被解析与显示之后 |
| 要点         | 下载完就执行                                             | 渲染完再执行                   |
| 适用范围     | 外部引入脚本                                             | 外部引入脚本                   |
| 多个执行顺序 | 不保证加载顺序                                           | 先后顺序                       |

多个执行顺序指同时出现多个 type 设置为 async 或 defer 的 script 标签。
type="module"是表明引入的是一个 ES6 模块脚本，其脚本内的模块需要遵循 ES6 模块规范，其他表现类似于 type 指定为 defer

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/HTML标签.html](http://www.skyline.show/HTML标签.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

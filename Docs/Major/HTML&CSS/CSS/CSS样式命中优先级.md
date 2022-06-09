# CSS 样式命中优先级

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

## 样式命中优先级

样式命中优先级递增表大致如下：
| 选择器 | 权重值 |
| ----------- | ------ |
| \* | 0 |
| 元素/伪元素 | 1 |
|属性选择器 | |
| 类/伪类 | 10 |
| ID | 100 |
| 内联样式 | 1000 |
| !important |

## 其他优先级

如果权重一致，最后一个指定的样式命中。

```css
<!DOCTYPE html>
<html>
  <head>
    <style>
      div.skyline {
        background-color: blue;
      }
      div.liu {
        background-color: red;
      }
    </style>
  </head>
  <body>
    <div class="skyline liu">Skyline is red</div>
  </body>
</html>
```

属性选择器权重介于元素与类选择器之间

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      div[id='skyline'] {
        background-color: blue;
      }
      body div {
        background-color: yellow;
      }
    </style>
  </head>
  <body>
    <div id="skyline">Skyline is blue</div>
  </body>
</html>
```

## 优先级示例

| 选择器                     | 权重总值    | 计算          |
| -------------------------- | ----------- | ------------- |
| p                          | 1           | 1             |
| p.skyline                  | 11          | 1 + 10        |
| p#demo                     | 101         | 1 + 100       |
| `<p style="color: pink;">` | 1000        | 1000          |
| \#demo                     | 100         | 100           |
| .skyline                   | 10          | 10            |
| p.skyline1.skyline2        | 21          | 1 + 10 + 10   |
| \#navbar                   | p\#demo 201 | 100 + 1 + 100 |
| \*                         | 0           | 0             |

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](http://www.skyline.show)  欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://www.w3schools.com/css/css_specificity.asp

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

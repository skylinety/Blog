# CSS布局相关属性

## flex

### flex-basis

flex-basis用于设定子项目**初始状态**时在主轴占据的空间，
子项目最终在主轴占据的空间，由flex决定，flex是一个复合属性，
也即由flex-grow、flex-shrink、flex-basis共同决定。

flex-basis默认值为auto，就是子项目本来占据的空间大小。
这里的子项目本来占据的空间大小，
首先取决于设定的宽高值，未设定宽高取决于盒模型内容空间，并最终受到宽高极值的设定。
如下[示例](https://github.com/skylinety/Blog/blob/main/Demos/Major/HTML&CSS/CSS/CSS_layout_properties.html)：

![CSS布局相关属性$20230320162250](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/CSS%E5%B8%83%E5%B1%80%E7%9B%B8%E5%85%B3%E5%B1%9E%E6%80%A7%2420230320162250.png)
单独设定width的子项目占据的空间不超过width设定的空间，
单独设定flex-basis的子项目会增加空间使得内容被包含在内；


flex-basis不推荐和width一起使用，一起使用时width无效，
flex-basis会根据flex-direction的变更来确认是控制宽度空间还是高度空间。

## grid

todo

## position

### absolute

todo

### relative

todo

## float

todo

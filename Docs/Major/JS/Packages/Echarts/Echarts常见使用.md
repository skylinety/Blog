# Echarts 常见使用

## Echarts 图表背景图

给图表设定背景图，一般有两种方式，第一种设定 option 中的 graphic

```js
const option = {
  graphic: [
    {
      type: 'image', // 图形元素类型
      id: 'logo', // 更新或删除图形元素时指定更新哪个图形元素，如果不需要用可以忽略。
      right: 'center', // 根据父元素进行定位 （居中）
      bottom: '0%', // 根据父元素进行定位   （0%）, 如果bottom的值是 0，也可以删除该bottom属性值。
      z: 0, // 层叠
      bounding: 'all', // 决定此图形元素在定位时，对自身的包围盒计算方式
      style: {
        // image: "https://www.boxuegu.com/assets/user/background1.png",
        width: 945,
        height: 800,
      },
    },
  ],
}
```

另一种方式为直接给图表容器设定背景图。

## Legend 使用

## Legend 超出滚动

```js
legend{
    type: scoll
}
```

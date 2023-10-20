# Echarts 常见使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Echarts 常见使用](#echarts-常见使用)
  - [Echarts 图表背景图](#echarts-图表背景图)
  - [Echarts 动态柱状图](#echarts-动态柱状图)
  - [Legend 使用](#legend-使用)
    - [Legend 超出滚动](#legend-超出滚动)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## Echarts 图表背景图

给图表设定背景图，一般有两种方式，第一种设定 option 中的 graphic

```js
const option = {
    graphic: [{
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
    }, ],
}
```

另一种方式为直接给图表容器设定背景图。

## Echarts 动态柱状图

要让柱状图平滑地向左移动，效果如下：

![Echarts常见使用QQ20230317-144305-HD](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Echarts%E5%B8%B8%E8%A7%81%E4%BD%BF%E7%94%A8QQ20230317-144305-HD.gif)

目前有三个方案。
一是修改x轴和data数据，将数组头部数据放大最末位置然后用setOption刷新图表。
另外两种方案都是使用datazoom来实现。
可以修改datazoom的startValue和endValue然后setOption来刷新图表实现，
目前，echarts已经在API中支持对应的Action，推荐的实现方案如下：

```jsx
export default {
  name: 'DynamicBar',
  data() {
    return {
      startValue: 0,
      endValue: 0,
    }
  },
  methods: {
    init() {
      const dom = document.getElementById('dynamicBar')
      this.chart = echarts.init(dom)
    },
    refresh(option) {
      this.chart.setOption(option)
    },
  },
  mounted() {
    this.init()
    this.refresh(option)
    setInterval(() => {
      this.startValue++
      this.endValue++
      this.chart.dispatchAction({
        type: 'dataZoom',
        startValue: this.startValue % 20, // X轴数据长度为29，坐标轴只显示10条数据，则需要以20为模进行计算
        endValue: (this.endValue % 20) + 9,
      })
    }, 1000)
  },
}
```

`option.js`

```js
option: {
  dataZoom: [
    {
      show: false,
      xAxisIndex: [0],
      bottom: 0,
      start: 0,
      end: 9
    },
  ],
}
```
## Legend 使用

### Legend 超出滚动

```js
legend {
    type: scoll
}
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

文章链接：[http://www.skyline.show/Echarts常见使用.html](http://www.skyline.show/Echarts常见使用.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

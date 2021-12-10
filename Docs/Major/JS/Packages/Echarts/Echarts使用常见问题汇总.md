# Echarts 使用常见问题汇总

## vue3 中在折线图、柱状图使用 datazoom 报错

在使用 datazoom 时报错如下

```js
barPolar.js:63 Uncaught TypeError: Cannot read property 'type' of undefined
    at barPolar.js:63
    at GlobalModel2.<anonymous> (Global.js:661)
    at Array.forEach (<anonymous>)
    at each (util.js:206)
    at GlobalModel2.eachSeriesByType (Global.js:657)
    at Object.barLayoutPolar (barPolar.js:61)
    at Object.overallReset (util.js:311)
    at Task2.overallTaskReset [as _reset] (Scheduler.js:460)
    at Task2._doReset (task.js:202)
    at Task2.perform (task.js:117)
```

图表简要注册代码如下

```js
const dom = document.getElementById(c.id)
if (echarts.getInstanceByDom(dom)) {
  return
}
this.chart[c.id] = echarts.init(dom)
```

这是可能是由于 vue3 深度监听可能会影响 echarts 内部一些 model 属性的正常访问
采用 shallowRef 进行浅监听。

```js
this.chart[c.id] = shallowRef(echarts.init(dom))
```

## ehcarts5 引入后找不到 echarts 对象

检查引入方式，echarts5 应该没有暴露 default echarts 对象，引入方式需要变更下

```js
// import echarts from 'echarts'; 由此改成下面
import * as echarts from 'echarts'
```

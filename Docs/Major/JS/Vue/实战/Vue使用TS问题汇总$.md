#Vue 中使用 TS

## 让 props 传递的枚举类型被正确识别

在 Vue 2.7 版本以上 SFC 写法中，使用枚举类型示例代码如下

```js
<script lang="ts">
    enum Direction {
    Horizontal = 'horizontal',
    Vertical = 'vertical',
    }
    export default {
        name: 'DirectionLayout',
        props: {
        direction: {
            type: String as () => Direction ,
            // type: Direction,
            // type: String,
            default: Direction.Horizontal,
        },
    },
    }
</script>
```
直接将type设置为Direction将报错
![Vue中使用TS$20221020170137](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E4%B8%AD%E4%BD%BF%E7%94%A8TS%2420221020170137.png)
设置为String时，使用时ts无法识别真正的direction类型
![Vue中使用TS$20221020170343](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E4%B8%AD%E4%BD%BF%E7%94%A8TS%2420221020170343.png)
正确设置方法为
```js
String as () => Direction
```
![Vue中使用TS$20221020170428](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E4%B8%AD%E4%BD%BF%E7%94%A8TS%2420221020170428.png)
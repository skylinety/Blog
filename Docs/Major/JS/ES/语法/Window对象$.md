# Window 对象

## location

### search

通过 window.location.search 来获取url中的查询参数
例如
地址栏为`https://www.baidu.com/s?wd=123`

```js
location.search
// '?wd=123'
```

当通过上述方式获取得到空串时，检查路由是否为 hash 模式
在 hash 模式下，#后面的所有内容都看做 hash 内容，从而获取到的 search 为空，可将 search 内容前置。

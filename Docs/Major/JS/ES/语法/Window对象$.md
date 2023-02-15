# Window 对象

## location

### search

通过 window.location.search 来获取 url 中的查询参数
例如
地址栏为`https://www.baidu.com/s?wd=123`

```js
location.search
// '?wd=123'
```

当通过上述方式获取得到空串时，检查路由是否为 hash 模式
在 hash 模式下，#后面的所有内容都看做 hash 内容，从而获取到的 search 为空，可将 search 内容前置。

## opener

### 刷新父页面

当前页的打开方式为前页调用 window.open()或是 a 标签的 target 跳转而来时，
当前页的 window.opener 为打开页面的 window 对象。
刷新打开页面的方法为：
`window.opener.location.reload(); `

# Window 对象

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Window 对象](#window-对象)
  - [event](#event)
    - [CustomEvent](#customevent)
    - [hashchange](#hashchange)
    - [popstate](#popstate)
  - [location](#location)
    - [search](#search)
  - [opener](#opener)
    - [刷新父页面](#刷新父页面)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## event

### CustomEvent
自定义事件监听

```jsx
window.addEventListener("whoami", (e) => console.log(e));

window.dispatchEvent(new CustomEvent("whoami", {
  me: {
    name: "skyline",
  },
}));
```

### hashchange

url 上hash（#后面）变更事件监听

```jsx
window.addEventListener('hashchange', (event) => {console.log(event) });
```

### popstate

url 变更事件监听

```jsx
window.addEventListener('popstate',  (event) => {console.log(event) });
```

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

文章链接：[http://www.skyline.show/Window对象.html](http://www.skyline.show/Window对象.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

# CSS 常见问题汇总

## 媒体查询失效

媒体查询的常见用法为

设置屏幕在 300px 到 900px 时的背景

```css
@media screen and (min-width: 300px) and (max-width: 900px) {
  body {
    background: #eee;
  }
}
```

当设置不生效时，检查在 `<head>` 中是否添加了如下 `<meta>` 标签

```html
<meta name="viewport" content="width=device-width,initial-scale=1.0" />
```

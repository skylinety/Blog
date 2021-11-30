# Nginx 常见问题汇总

## proxy_pass 代理接口不能访问

### 需求

客户端访问接口，发起请求
http://aaa.com/file/123.png

真实接口地址为
http://bbb.com/123.png

### 配置

检查配置，正确的配置如下

```shell
location ^~ /file/ {
    proxy_pass http://bbb.com/;
}
```

正确访问http://bbb.com/123.png

```shell
location ^~ /file {
    proxy_pass http://bbb.com;
}
```

http://bbb.com/file/123.png
结果为 404

```shell
location ^~ /file {
    proxy_pass http://bbb.com/;
}
```

http://aaa.com/file/123.png
304 =>123.png
http://aaa.com/123.png
404

```shell
location ^~ /file/ {
    proxy_pass http://bbb.com;
}
```

http://aaa.com/file/123.png 400 bad request

[proxy_pass 官方文档](http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass)

### 解析

## 页面刷新不能进入

检查页面的路由模式。
特别是在 Vue 项目中，具体查看 [HTML5 History Mode](https://router.vuejs.org/guide/essentials/history-mode.html#example-server-configurations)
vue 默认的是 hash 路由模式，使用此种模式，页面路由变化时，并不会重载页面

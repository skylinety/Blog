# Nginx 常见问题汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Nginx 常见问题汇总](#nginx-常见问题汇总)
  - [proxy_pass 代理接口不能访问](#proxy_pass-代理接口不能访问)
    - [问题描述](#问题描述)
    - [配置](#配置)
  - [页面刷新不能进入](#页面刷新不能进入)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## proxy_pass 代理接口不能访问

### 问题描述

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

检查地址，注意后缀'/'都不能去掉。
一般把 server:port 后的部分叫做 URI，proxy_pass 在其后加不加 URI 表现完全不同。
location 非正则匹配时，proxy_pass 有 URI 直接用 URI 把 location 对应的字符替换，无 URI 则直接替换 server:port
详细解析查看[Nginx 基础](https://github.com/skylinety/Blog/blob/bf27769f7e637edbb12e2bac320d4dd8b73692e5/Docs/Tools/DEVs/Nginx/Nginx%E5%9F%BA%E7%A1%80.md)

## 页面刷新不能进入

检查页面的路由模式。
特别是在 Vue 项目中，具体查看 [HTML5 History Mode](https://router.vuejs.org/guide/essentials/history-mode.html#example-server-configurations)
vue 默认的是 hash 路由模式，使用此种模式，页面路由变化时，并不会重载页面
在配置网站根文件的位置加入
`try_files $uri $uri/ /index.html;`
一般如下配置

```shell
location ^~ /skyline{
    alias /data/wwwroot/skyline/dist;
    index  index.html index.htm;
    try_files $uri $uri/ /index.html;
}
```

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

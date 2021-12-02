# Nginx 基础

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Nginx 基础](#nginx-基础)
  - [location](#location)
    - [基础使用](#基础使用)
    - [URL-match](#url-match)
    - [modifier](#modifier)
  - [proxy_pass](#proxy_pass)
    - [简述](#简述)
    - [URI](#uri)
    - [/ 问题](#问题)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## location

### 基础使用

location 位于 server 下或位于另一个 location 中，基本使用如下

```js
location [modifier] [URL-match] {
  ...
}
```

### URL-match

匹配所有路径
location / {
}
优先级最低，所有都不匹配时，才会命中

### modifier

URI 这里指 URL 除了 server:port 的部分。

**命中优先级**

| modifier | desc                                              | example            |
| -------- | ------------------------------------------------- | ------------------ |
| =        | exact (精确匹配)                                  | location = /site   |
| ^~       | priority prefix (优先字符)                        | location ^~ /site  |
| ~        | case sensitive regex (大小写敏感正则)             | location ~ /site   |
| ~\*      | case insensitive regex(忽略大小写)                | location ~\* /site |
| (none)   | prefix(字符匹配，无修饰符，由 URI 头字符开始匹配) | location /site     |

在如下网址可进行匹配测试 https://nginx.viraptor.info/

^~ 与(none)都 进行字符匹配（非正则），^~ 相对于(none) ，提高了命中优先级。

**典型示例**

示例 1

```shell
location ^~ /file/* {
    proxy_pass http://bbb.com/;
}
```

^~ 进行字符匹配
http://domain2.com/file/* 可以命中
http://domain2.com/file/1 不能命中

示例 2

```shell
location ~ /file/* {
    proxy_pass http://bbb.com/;
}
location ^~ /file/ {
    proxy_pass http://bbb.com/;
}
```

http://domain2.com/file/1 根据优先级命中`^~ /file/`

## proxy_pass

### 简述

proxy_pass 通常位于 location 下，用于接口转发。

### URI

一般把 server:port 后的部分叫做 URI，proxy_pass 在其后加不加 URI 表现完全不同。
location 非正则匹配时，对于 proxy_pass 有如下规则：
proxy_pass 有 URI
替换请求中匹配的 URI 并替换成 proxy_pass 中的 URI 并向上游服务转发。

```shell
location /file {
    proxy_pass http://bbb.com/src;
}
```

http://aaa.com/file/search 真实访问地址为http://bbb.com/src/search

```shell
location /file {
    proxy_pass http://bbb.com/;
}
```

http://aaa.com/file/search 真实访问地址为http://bbb.com//search

proxy_pass 无 URI
保留请求 URI 并将其转发到上游服务

```shell
location /file {
    proxy_pass http://bbb.com;
}
```

http://aaa.com/file/search 真实访问地址为http://bbb.com/file/search

location 为正则匹配时，由于 nginx 不知道替换哪些字符，
proxy_pass 的 URI 不起作用，保留原 URI，转发到上上游服务

```shell
location ~ /file {
    proxy_pass http://bbb.com/src;
}
```

http://aaa.com/file/search 真实访问地址为http://bbb.com/file/search

### / 问题

location 非正则匹配时，当 proxy_pass 有 URI 时，需要注意 URI 的尾斜杠，具体表现为如下
location 正则匹配时，不需要考虑 proxy_pass 的 URI

| location | proxy_pass          | Request               | Received by upstream  |
| -------- | ------------------- | --------------------- | --------------------- |
| /file/   | http://bbb.com/src/ | /file/search?name=baz | /src/search?name=baz  |
| /file/   | http://bbb.com/src  | /file/search?name=baz | /srcsearch?name=baz   |
| /file    | http://bbb.com/src/ | /file/search?name=baz | /src//search?name=baz |
| /file    | http://bbb.com/src  | /file/search?name=baz | /src/search?name=baz  |
| /file    | http://bbb.com/src  | /filesearch?name=baz  | /srcsearch?name=baz   |
| ~ /file/ | http://bbb.com/src/ | /file/search?name=baz | /file/search?name=baz |
| ~ /file/ | http://bbb.com      | /file/search?name=baz | /file/search?name=baz |

总之一句话

**location 非正则匹配时，proxy_pass 有 URI 直接用 URI 把 location 对应的字符替换，无 URI 则直接替换 server:port**

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://nginx.viraptor.info/ https://www.digitalocean.com/community/tutorials/understanding-nginx-http-proxying-load-balancing-buffering-and-caching

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

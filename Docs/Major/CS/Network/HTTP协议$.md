# HTTP 协议

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [HTTP 协议](#http-协议)
  - [HTTP 简介](#http-简介)
  - [HTTP 常见术语](#http-常见术语)
    - [持久连接](#持久连接)
    - [幂等](#幂等)
    - [安全](#安全)
  - [HTTP 状态码](#http-状态码)
    - [1xx 通知信息](#1xx-通知信息)
    - [2xx 成功](#2xx-成功)
    - [3xx 重定向](#3xx-重定向)
    - [4xx 客户端出错](#4xx-客户端出错)
    - [5xx 服务器出错](#5xx-服务器出错)
  - [HTTP 方法](#http-方法)
    - [常见请求方法](#常见请求方法)
    - [OPTIONS 预检请求](#options-预检请求)
    - [GET&POST](#getpost)
    - [其他请求](#其他请求)
  - [HTTP 报文](#http-报文)
    - [查看报文](#查看报文)
    - [请求报文](#请求报文)
    - [响应报文](#响应报文)
  - [HTTP 演变](#http-演变)
  - [HTTPS](#https)

<!-- /code_chunk_output -->

## HTTP 简介

HTTP 即超⽂本传输协议（HyperText Transfer Protocol）
超文本从字面意思可以简单理解为文本的超集；
其除了包含文本，还包含图片、音视频和超链接等，HTML 就是一个常见的超文本。
传输指数据在两端之间传输，两端传输中间可以存在其他中转点。

协议即约定数据传输过程中的的规范。

HTTP 的底层是 TCP/IP 协议，HTTP 也是无状态协议。

## HTTP 常见术语

### 持久连接

HTTP1.1 默认是持久的，即请求头默认携带

```sh
Connection: Keep-Alive
```

持久连接使得 HTTP 得以复用同一个 TCP
可以指定[Keep-Alive](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Keep-Alive)请求头指定空闲连接保持时间和连接关闭前可以复用 TCP 的最大 http 数量。
空闲连接指连接中不再有任何数据传输

```js
Keep-Alive: timeout=5, max=1000
```

当连接空闲超过 5 秒时关闭，且允许复用 TCP 的最大 HTTP 数量为 1000。

当连接不是持久时，单一请求完成即关闭，多个连接需要多次建立 TCP 连接，从而多次进行握手挥手，
这极大增加了网络负载，可能造成网络拥堵，多次进行握手也会增加网络延迟，
同时也增加了双端的内存 CPU 负载。

### 幂等

一般情况下，POST 方法是非幂等的，其他方法 GET ， HEAD ， PUT ，OPTIONS 和 DELETE 多为幂等。
冥等指多次发送该请求得到的响应效果是一致的。
不能简单地将幂等理解为响应结果一致。
例如多次调用 Delete 删除某条记录，第一次 200 成功，后续调用将会 404 找不到该记录，但 DELETE 方法仍旧是幂等的。

### 安全

HTTP 方法安全是指该方法的请求不修改服务器数据
常见安全的方法有 GET ， HEAD ，OPTIONS
不同于幂等，PUT 和 DELETE 是不安全的

## HTTP 状态码

### 1xx 通知信息

    100 Continue
    ｜ 目前为止的所有内容都是正常的，并且客户端应该继续请求或者如果它已经完成则忽略它
    101 Switching Protocols
    ｜ 服务器将遵从客户的请求转换到另外一种协议
    102 Processing

### 2xx 成功

    200 OK
    204 No Content
    ｜ 未内容，没有响应任何内容。请求被受理但没有资源可以返回，没有新文档，浏览器应该继续显示原来的文档
    206 Partial Content
    ｜ 客户发送了一个带有Range头的GET请求，服务器完成了它。服务器已经成功处理了部分 GET 请求。迅雷这类的HTTP下载工具都是使用此类响应实现断点续传或者将一个大文档分解为多个下载段同时下载

### 3xx 重定向

    301 Moved Permanently
    ｜ 永久性重定向，请求的URL已移走，浏览器应该自动地访问新的URL
    302 Move temporarily
    ｜ 临时重定向，维护，新的URL应该被视为临时性的替代，而不是永久性的
    304 Not Modified
    ｜ 未修改，客户端缓存已经是最新

### 4xx 客户端出错

    400 Bad Request
    ｜ 语义有误或参数有误
    401 Unauthorized
    ｜ 客户试图未经授权访问受密码保护的页面
    403 Forbidden
    ｜ 资源不可用。服务器理解客户的请求，认证成功，但拒绝处理它。通常由于服务器上文件或目录的权限设置导致，需要向管理员申请文件权限
    404 Not Found
    ｜ 未找到，无法找到指定位置的资源
    405 Method Not Allowed
    ｜ 请求方法（GET、POST、HEAD、DELETE、PUT、TRACE等）对指定的资源不适用
    406 Not Acceptable
    ｜ 指定的资源已经找到，但它的MIME类型和客户在Accpet头中所指定的不兼容
    408 Request Timeout
    ｜ 请求超时

### 5xx 服务器出错

    500 Internal Server Error
    ｜ 服务器未知错误
    502 Bad Gateway
    ｜ 网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应
    503 Service Unavailable
    ｜ 服务器由于维护或者负载过重未能应答
    504Gateway Timeout
    ｜ 由作为代理或网关的服务器使用，表示不能及时地从远程服务器获得应答

## HTTP 方法

### 常见请求方法

| 请求    | 用途                            |
| ------- | ------------------------------- |
| GET     | 查                              |
| POST    | 增                              |
| PUT     | 改                              |
| DELETE  | 删                              |
| OPTIONS | 预检请求                        |
| HEAD    | 获取 GET 请求资源响应的头部信息 |

### OPTIONS 预检请求

OPTIONS 被称为预检请求（Preflight request）
浏览器有同源安全限制，防止不同源之间资源访问与脚本执行。
同源是指浏览器要求当前网站发送的请求，其协议、主机、端口需要一致。
若不同源发起请求而服务器不支持对应请求跨域访问时，会有如下错误
![HTTP协议$20230103145518](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/HTTP%E5%8D%8F%E8%AE%AE%2420230103145518.png)
当需要解除同源限制实现跨域，在不同源之间访问资源，
常用的方案为，开发环境常配置 devServer proxy（Vue 项目）代理，
其他环境通常使用 nginx 反向代理。

也可以使用 CORS（跨域资源共享）来解决跨域问题。
请求可以根据是否对服务器数据产生副作用来分为简单请求和复杂请求。
[简单请求](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS#%E7%AE%80%E5%8D%95%E8%AF%B7%E6%B1%82)仅限 GET、HEAD、POST 方法
且限定请求头只有 Accept Content-Type 等特定字段，超出这些字段为复杂请求；
一般来说添加了自定义请求头都为复杂请求。
同时简单请求要求 Content-Type 对应字段只能为

- text/plain
- multipart/form-data
- application/x-www-form-urlencoded

其中之一。

对于简单请求，浏览器不会发起预检请求。
复杂请求发送前，浏览器会自动发起一个 OPTIONS 预检请求，检查服务端支持的请求方法，控制台会看到两次请求，第二次为实际请求。
预检请求发送后，若服务器不支持该请求，响应错误同时控制台报错 CORS 预检响应未成功。
预检请求可以避免跨域请求对服务器的用户数据产生超出预期的影响，开发者对于允许跨域的请求在预期内。
复杂请求在缓存有效期内，也不会再次发送预检请求。

OPTIONS 请求头

```js
Origin: https://skyline.show
Access-Control-Request-Method: POST
Access-Control-Request-Headers: AccessToken, Content-Type
```

先服务器表明实际请求为https://skyline.show站点的 POST，且该请求会携带额外的 AccessToken, Content-Type 请求头字段

OPTIONS 响应头

```js
Access-Control-Allow-Origin: https://skyline.show
Access-Control-Allow-Methods: POST, GET, OPTIONS
Access-Control-Allow-Headers: AccessToken, Content-Type
Access-Control-Max-Age: 86400
```

表明允许来自的https://skyline.show的POST, GET, OPTIONS 实际跨域请求。
实际请求允许携带额外的 AccessToken, Content-Type 请求头字段
该预检请求缓存有效时间为 86400 秒（一天），一天内再次发送请求时不再有预检请求。

Chrome 79+ 不在单独在控制台展示 OPTIONS 请求，其与对应后续实际请求合并展示，查看 Method 栏可以看到有预检请求的请求。
![HTTP协议$20230104144425](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/HTTP%E5%8D%8F%E8%AE%AE%2420230104144425.png)
如上图 POST+Preflight 即包含了预检请求。
要先明确看到并调试 OPTIONS 预检请求，可以使用[HTTP Tookit](https://httptoolkit.com/)或其他软件
![HTTP协议$20230104153908](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/HTTP%E5%8D%8F%E8%AE%AE%2420230104153908.png)

### GET&POST

- 不同功能

首先 GET 和 POST 用以不同的功能。
GET 用于获取服务端数据
POST 用于增加或修改服务端数据

- 不同传参

GET 将传参放在 URL 中，通信类容不安全，且传送参数有长度限制
POST 将传参放在 Body 中，更加安全，且传送参数无长度限制

- 不同安全和幂等

GET 是安全且幂等的
POST 既不安全也不幂等

### 其他请求

- HEAD 请求

## HTTP 报文

### 查看报文

可以通过 WireShark 追踪 HTTP 来查看 HTTP 报文。
在 WireShark 找到一个 HTTP 协议的请求，右键追踪 TCP 流，在弹窗中可以看到标准的 HTTP 报文。
![HTTP协议$20230105162201](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/HTTP%E5%8D%8F%E8%AE%AE%2420230105162201.png)
其中红色部分为请求报文，蓝色部分为响应报文。

### 请求报文

请求报文包含请求行，请求头，请求体（POST）
红色部分第一行为请求行

```sh
GET /addrApi/static/jquery.min.js HTTP/1.1
```

包含请求方法，路径，请求协议和版本
红色剩余部分为请求头，Get 请求不包含请求体
常见请求头如下

| 请求头          | 说明                                             | 示例                           |
| --------------- | ------------------------------------------------ | ------------------------------ |
| Host            | 服务器地址                                       |
| Connection      | 连接状态，指定为 Keep-Alive 可以持久连接复用 TCP | Connection: keep-alive         |
| Accept          | 客户端接受的响应格式                             | Accept: \*/\*                  |
| Accept-Encoding | 客户端接受的编码（压缩）方式                     | Accept-Encoding: gzip, deflate |

### 响应报文

响应报文包含状态行，响应头，响应体
蓝色部分第一行为状态行

```sh
HTTP/1.1 200 OK
```

包含响应协议和版本，响应状态码和状态文本
蓝色第一段剩余部分为响应头，蓝色第二段为响应体
常见响应头如下

| 响应头           | 说明                       | 示例                                   |
| ---------------- | -------------------------- | -------------------------------------- |
| Content-Type     | 响应数据类型               | Content-Type: text/html; charset=utf-8 |
| Content-Length   | 响应数据长度               |
| Content-Encoding | 响应数据的编码（压缩）方式 | Content-Encoding: gzip                 |

## HTTP 演变

## HTTPS

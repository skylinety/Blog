# Cookie、Session 与 Token

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Cookie、Session 与 Token](#cookiesession-与-token)
  - [请求信息保存](#请求信息保存)
  - [Cookie](#cookie)
    - [概述](#概述)
    - [属性分析](#属性分析)
    - [第三方 Cookie](#第三方-cookie)
    - [Cookie 前缀](#cookie-前缀)
  - [Session](#session)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 请求信息保存

Http 是无状态（stateless）协议，服务端接收到的每一个请求都是全新请求，之前请求的信息不会被存储。
这就导致，服务端无法判定请求是否为同一发送者，需要鉴权的请求，就无法获知用户是否进行过鉴权。
Cookie Session 等技术诞生就是为了解决请求信息无法保存的问题。

## Cookie

### 概述

当服务端请求响应头包含 Set-Cookie 属性时，Set-Cookie 对应的信息会自动保存在浏览器中。
在下次会话请求中，符合条件的请求会自动在请求头中设置 Cookie 属性，并携带之前保存的信息。
服务端请求响应携带 Cookie

```js
Set-Cookie: skyline=hello
```

客户端发送请求携带 Cookie

```js
Cookie: skyline = hello
```

**Cookie 存在于客户端中，不可跨域携带**。

Cookie 相关属性

| 属性       | 解析                                                                                |
| ---------- | ----------------------------------------------------------------------------------- |
| name=value | Cookie 键值对                                                                       |
| domain     | 携带 Cookie 的域名，默认当前域名                                                    |
| path       | 指定携带 Cookie 的路径，默认'/'，所有路径皆携带                                     |
| maxAge     | 有效期时长，单位 ms                                                                 |
| expires    | 有效期截止时间                                                                      |
| secure     | 安全传输，开启后 Cookie 只在 Https 中被自动携带                                     |
| httpOnly   | 仅用户请求携带，禁止 JS 脚本通过 Document.cookie 获取 Cookie，一定程度防止 XSS 攻击 |
| SameSite   | 同站请求设置，防止 CSRF 攻击                                                        |

Cookie 常用于临时性的细微信息存储，主要用于如下地方：

- 保存会话信息，如用户登录信息，游客购物车，游戏分数等
- 保存用户个性化配置，如网站皮肤设置等
- 追踪用户习惯，追踪分析用户浏览记录等

Cookie 在 localStorage、sessionStorage 等现代浏览器存储 API 诞生前曾一度用于存储浏览器端的信息并供脚本使用（即充当现今 localStorage 等角色 1）。
但其有一个很严重的弊端就是所有的 Cookie 都会跟随请求携带，影响接口速度与网站性能。
在现代浏览器存储 API 诞生后，Cookie 基本不再用于一般的浏览器存储。

### 属性分析

- domain
  指定接收该 Cookie 的主机，默认限制为当前域名（www.example.com），不包含example.com下的其他子域名。
  若进行指定 example.com，则包含其他子域名如 blog.example.com
- SameSite
  Strict: 严格模式，不允许其他网站发送的请求携带 Cookie
  Lax: 宽松模式，遵照在严格模式，但是允许其他网站跳转到本站时携带 Cookie，默认值
  None: 不做限制，但需要安全传输。故设定为此值时，通常要求设定 secure

SameSite 是一个较新的属性，目前多数浏览器已支持，用于限制第三方 Cookie。
该属性用于告知浏览器源于第三方网站发出的本站请求是否被允许携带 Cookie，可设定 3 种值。
SameSite 一般直接使用默认值 Lax，防止第三方网站直接发送本站请求，浏览器自动携带本站 Cookie
若使用严格模式，跳转到本站时用户信息会遗失，体验较差。
举个例子，假定 github 对用户登录信息校验的 Cookie 使用 Strict，用户在已经登录过 github，当从掘金跳转过来 github 时，仍要重新登录。

### 第三方 Cookie

当携带 Cookie 的请求其协议与域名与当前网站协议域名保持一致时被称为第一方 Cookie
当协议或域名不一致时，被称为第三方 Cookie。
第三方 Cookie 主要用于用户行为与习惯跟踪，通过分析来给用户更好的体验。
当用户在浏览购物网站 A（不一定登陆）时，其搜索，点击等操作请求被网站服务器记录并在响应头中携带有唯一标识的 Cookie 储存在浏览器中。
而后用户用同一浏览器访问该购物网站 A 投放广告的其他网站 B 时，其它网站 B 中网页内嵌入的购物网站 A 的请求（链接、图片等）会自动携带浏览器存储的 A 站相关 Cookie。
购物网站 A 通过分析 Cookie 来响应定制化的个性广告信息，实现精准广告投放到网站 B 上。
![Cookie、Session与Token20220328140802](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Cookie%E3%80%81Session%E4%B8%8EToken20220328140802.png)
由于隐私与安全等缘故，部分浏览器默认禁止了三方 Cookie

### Cookie 前缀

由于 Cookie 设计机制问题，服务器并不能确定携带 Cookie
除了 secure、httpOnly、SameSite 三个属性来增强 Cookie 的安全机制，也可也对的 Cookie 属性添加如下两个前缀来增强安全。

- \_\_Host-
- \_\_Secure-

\_\_Secure-前缀仅用于设定 Secure 的 Cookie，否则被拦截。

```js
Set-Cookie: __Secure-skyline=hello; Secure
Set-Cookie: __Secure-test=hello; // 被拦截
```

\_\_Host-前缀进行了进一步强化，需要设定 Secure; Path=/，同时不能设定 Domin 属性

```js
Set-Cookie: __Host-skyline=hello; Secure; Path=/
Set-Cookie: __Host-skyline=hello; Secure;  // 被拦截
Set-Cookie: __Host-skyline=hello; Path=/ // 被拦截
Set-Cookie: __Host-skyline=hello; Secure; Path=/; Domain=example.com // 被拦截
```

## Session

Session 是一种记录浏览器与客户端会话状态的机制，服务器通过该技术来判断浏览器发送的请求是否为同一次会话，并保留会话间产生的信息。
在该技术方案中，首次接收到请求时，服务端会存储客户端此次会话期间的基本信息。
会话基本信息并不一定包括用户登录信息，也可能保留游客用户操作相关信息。
一个典型的例子为京东游客用户也可以加购保留选择的商品。

保存相关信息后，服务端会发出响应信息并在响应头中添加 Set-Cookie：SESSIONID=XXXXXXX
浏览器接收到请求，会自动设定一个 SESSIONID=XXXXXXX 的 Cookie，并为后续的请求自动携带该 Cookie。
服务通过比对 SESSIONID 来判定后续请求的会话归属。
Cookie 中 SESSIONID 的过期时间即为此次会话的有效时间。

Session 本质上利用了 Cookie 技术。
Session 利用服务端保存会话信息，同时利用 Cookie 保存 SESSIONID。

第一次请求响应头中包含 Set-Cookie
![Cookie、Session与Token20220309160801](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Cookie%E3%80%81Session%E4%B8%8EToken20220309160801.png)
后续请求中携带 Session 关联 Cookie 信息
![Cookie、Session与Token20220309160722](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Cookie%E3%80%81Session%E4%B8%8EToken20220309160722.png)

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies > https://www.cookielawinfo.com/tracking-cookies/

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh

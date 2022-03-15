# Cookie、Session 与 Token

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Cookie、Session 与 Token](#cookiesession-与-token)
  - [请求信息保存](#请求信息保存)
  - [Cookie](#cookie)
  - [Session](#session)

<!-- /code_chunk_output -->

## 请求信息保存

Http 是无状态协议，服务端接收到的每一个请求都是全新请求，之前请求的信息不会被存储。
这就导致，服务端无法判定请求是否为同一发送者，需要鉴权的请求，就无法获知用户是否进行过鉴权。

## Cookie

当服务端请求响应头包含 Set-Cookie 属性时，Set-Cookie 对应的信息会自动保存在浏览器中。
在下次会话请求中，符合条件的请求会自动在请求头中设置 Cookie 属性，并携带之前保存的信息。
**Cookie 存在于客户端中，不可跨域携带**。

Cookie 属性解析
| 属性 | 解析 |
| ---------- | ----------------------------------------------- |
| name=value | Cookie 键值对 |
| domain | 携带 Cookie 的域名，默认当前域名 |
| path | 指定携带 Cookie 的路径，默认'/'，所有路径皆携带 |
| maxAge | 有效期时长，单位 ms |
| expires | 有效期截止时间 |
| secure | 安全传输，开启后 Cookie 只在 Https 中被自动携带 |
| httpOnly | 仅用户请求携带，禁止 JS 脚本获取 Cookie，一定程度防止 XSS 攻击 |
| SameSite | 同站请求设置，防止 CSRF 攻击 |

- domain
  指定接收该 Cookie 的主机，默认限制为当前域名（www.example.com），不包含example.com下的其他子域名。
  若进行指定 example.com，则包含其他子域名如 blog.example.com
- SameSite
  SameSite 是一个较新的属性，目前多数浏览器已支持。
  该属性用于告知浏览器源于第三方网站发出的本站请求是否被允许携带 Cookie，可设定 3 种值。
  Strict: 严格模式，不允许其他网站发送的请求携带 Cookie
  Lax: 宽松模式，遵照在严格模式，但是允许其他网站跳转到本站时携带 Cookie，默认值
  None: 不做限制，但需要安全传输。故设定为此值时，通常要求设定 secure
  SameSite 一般直接使用默认值 Lax，防止第三方网站直接发送本站请求，浏览器自动携带本站 Cookie
  若使用严格模式，跳转到本站时用户信息会遗失，体验较差。
  举个例子，假定 github 对用户登录信息校验的 Cookie 使用 Strict，用户在已经登录过 github，当从掘金跳转过来 github 时，仍要重新登录。

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

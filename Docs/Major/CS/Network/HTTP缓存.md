# HTTP缓存

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [HTTP缓存](#http缓存)
  - [缓存的优势](#缓存的优势)
  - [缓存位置](#缓存位置)
    - [memory cache](#memory-cache)
    - [disk cache](#disk-cache)
  - [缓存过程](#缓存过程)
    - [缓存流程](#缓存流程)
  - [缓存相关头部](#缓存相关头部)
    - [Expires](#expires)
    - [Cache-Control（优先级高）](#cache-control优先级高)
  - [协商缓存头部](#协商缓存头部)
    - [Last-Modified / If-Modified-Since](#last-modified--if-modified-since)
    - [Etag / If-None-Match（优先级高）](#etag--if-none-match优先级高)
  - [常见场景](#常见场景)
    - [频繁变动资源](#频繁变动资源)
    - [会变化的资源](#会变化的资源)
    - [不常变化资源](#不常变化资源)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 缓存的优势

* 减少网络带宽消耗

通过减少网络请求数量来减少网络流量消耗

* 降低服务器压力

并发的大量的请求会使得服务器负载过重，减少网络请求能是服务器与更多地客户端建立连接，
减少过载死机的次数。

* 加快页面打开速度

直接使用本地的缓存，能明显地加快页面响应速度

## 缓存位置

### memory cache

内存中的缓存，优先读取，其特点是快速读取。
内存缓存会将编译解析后的文件，直接存入该进程的内存中，占据该进程一定的内存资源，以方便下次运行使用时的快速读取。
一旦该进程关闭（一般为页面关闭），则该进程的内存则会清空。
通常Base64格式的图片会存在内存缓存中。

###  disk cache

硬盘中的缓存其特点为读取复杂，涉及I/O操作。
当从硬盘中读取到缓存后，会重新解析该缓存内容，速度比内存缓存慢。
大多数需要缓存的文件都存在硬盘中。
![HTTP缓存$20230328120139](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/HTTP%E7%BC%93%E5%AD%98%2420230328120139.png)


## 缓存过程

### 缓存流程
浏览器首次发起请求通过Cache-Control（no-store）判断是否缓存资源。
若缓存资源，后续根据Cache-Control（max-age）来判断资源是否有效来决定使用缓存（强缓存）还是重新和服务器协商要资源（协商缓存）。
若资源失效，浏览器与服务器协商，则通过E-tag/If-None-Match来判断服务器原缓存资源与其最新资源是否一致。

这里描述时用优先级更高的Cache-control代替Expires，
用E-tag/If-None-Match代替了Last-modified/If-modified-Since，他们的主要功能分别对应一致。

![HTTP缓存$20230328144813](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/HTTP%E7%BC%93%E5%AD%98%2420230328144813.png)


## 缓存相关头部

### Expires

服务器返回该请求结果缓存的到期时间。
当再次发起该请求时，如果客户端的时间小于Expires的值，则直接使用缓存结果，即强缓存生效。
Expires 是HTTP/1.0的字段，在http1.1之后使用Cache-Control代替
Expires 取值是GMT等绝对时间值。

```js
expires: Wed Jul 01 2020 11: 42: 30 GMT + 0800
```

GMT(Greenwich Mean Time，格林威治标准时间)

Expires控制缓存的原理是使用客户端的时间与服务端返回的时间做对比，
当客户端和服务端时间因为各种原因不同步时（比如不同时区），强制缓存则会不准确而失去意义

### Cache-Control（优先级高）

Cache-Control在http1.1引入以解决Expires存在的问题，
故而与Expires同时出现时，Cache-Control优先级较高。

| 取值                                       | 含义                                                                                 |
| ------------------------------------------ | ------------------------------------------------------------------------------------ |
| public                                     | 所有内容都将被缓存（客户端和代理服务器都可缓存）                                     |
| private                                    | 所有内容只有客户端可以缓存，代理服务器不能缓存，Cache-Control的默认取值              |
| no-cache                                   | 客户端会缓存内容，但是是否使用缓存则需要经过协商缓存来验证决定（即直接使用协商缓存） |
| no-store                                   | 所有内容都不会被缓存，即不使用强制缓存，也不使用协商缓存                             |
| max-age=xxx (xxx is numeric), s-maxage=xxx | 缓存内容将在xxx**秒**后失效                                                          |

Cache-Control: max-age=xxx与Expires指定具体时间值不同的是，max-age与s-maxage是一个相对值, s-maxage对应代理服务器，max-age对应客户端。

对Cache-Control/Expires进行识别后一般存在如下三种情况：
当浏览器中不存在缓存结果与标识，无缓存资源时，直接向服务器请求，一般为第一次请求或禁用缓存。
存在缓存结果与标识，但缓存结果失效，则与服务器进行协商缓存，协商缓存生效。
存在缓存结果与标识，且缓存结果有效，则直接取缓存，强缓存生效。

Cache-Control/Expires主要用于判定内容直接从浏览器获取还是需要向服务器获取或协商。

## 协商缓存头部

### Last-Modified / If-Modified-Since

```jsx
Last-Modified
```
响应头，资源最后被修改时间（时间戳）

```js
If-Modified-Since
```
请求头，浏览器向服务器再次请求该资源时，
发送之前请求资源获取的Last-Modified值，服务器将请求传递的值与文件最新值做对比。

Last-Modified单位是秒级的，1秒内的修改Last-Modified无法记录，同时负载均衡或其他原因后各服务器的Last-Modified可能不一致。
故而不推荐使用。

### Etag / If-None-Match（优先级高）

```js
Etag
```
响应头，服务器生成的资源唯一标识，Etag是服务器唯一资源Hash，资源变更都会生成新的表示，精确度高。

```js
If-None-Match
```
请求头，浏览器向服务器再次请求该资源时，
发送之前请求资源获取的Etag值，服务器将请求传递的值与文件最新值做对比。

## 常见场景

### 频繁变动资源

```js
Cache-Control: no-cache
```

使用协商缓存，使得每次请求都需要与浏览器协商，以便及时获取到最新的资源。

### 会变化的资源

```js
Cache-control: max-age = 2592000
```

设置一个较短的时间周期，来合理延迟下次需要与服务器协商去资源的时间

### 不常变化资源

```jsx
Cache-Control:max-age=31536000
```

设定一个较长日期如31536000（一年）使得未过期前直接命中缓存（强缓存）

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

文章链接：[http://www.skyline.show/HTTP缓存$.html](http://www.skyline.show/HTTP缓存$.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！


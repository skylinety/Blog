# ES 文件下载实现

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ES 文件下载实现](#es-文件下载实现)
  - [文件处理](#文件处理)
  - [代码实现](#代码实现)
  - [常见问题](#常见问题)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 文件处理

文件下载一般有两种，一种为后端接口返回连接浏览器打开即可。
本文主要为另一种，接口返回文档字节流，前端使用浏览器内置对象 Blob，用隐藏的 link 来触发下载操作。
响应内容如下：
![ES文件下载实现20220628151413](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E5%AE%9E%E7%8E%B020220628151413.png)

## 代码实现

```js
export function transFile(res, name = '导出.xlsx') {
  let fileName = res.headers['content-disposition']
    ? res.headers['content-disposition']
        .split(';')[1]
        .split('filename=')[1]
        .replace(/^\"|\"$/g, '')
    : name

  fileName = decodeURI(fileName)
  const fileNameUnicode =
    res.headers &&
    res.headers.hasOwnProperty('content-disposition') &&
    res.headers['content-disposition'].split(';')[1].split('filename=')[1]
  if (fileNameUnicode) {
    //解决中文乱码问题
    fileName = decodeURIComponent(fileNameUnicode)
  }
  let blob = new Blob([res.data], {
    // type: 'application/zip;charset=UTF-8',
    // type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel',
    // type: res.headers['content-type'],
  })
  if (window.navigator.msSaveOrOpenBlob) {
    navigator.msSaveBlob(blob, fileName)
  } else {
    let link = document.createElement('a')
    let evt = document.createEvent('HTMLEvents')
    evt.initEvent('click', false, false)
    link.href = URL.createObjectURL(blob)
    link.download = fileName
    link.style.display = 'none'
    document.body.appendChild(link)
    link.click()
    window.URL.revokeObjectURL(link.href)
    document.body.removeChild(link)
  }
}
```

## 常见问题

下载文件后打开提示文件已损坏。
如果是 axios，需要在请求的 options（非请求头）加上 **responseType: "blob"** ，表明返回服务器返回的数据类型
responseType 表示服务器响应的数据类型，默认取 'json'，可以是 'arraybuffer' , 'blob' , 'document' , 'json', 'text', 'stream'。
其他库同理，需要请求时指定响应类型，浏览器方可正常转流。
若还是损坏，考虑转换为 Blob 时，指定的文件 type 类型，可以尝试下载某类文件并指定对应格式。
常见格式有：

| Surfix     | MIME Type                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------- |
| .doc       | application/msword                                                                          |
| .docx      | application/vnd.openxmlformats-officedocument.wordprocessingml.document                     |
| .xls       | application/vnd.ms-excel                                                                    |
| .xlsx      | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet                           |
| .xlsx .xls | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel |
| .ppt       | application/vnd.ms-powerpoint                                                               |
| .pptx      | application/vnd.openxmlformats-officedocument.presentationml.presentation                   |
| .zip       | application/zip                                                                             |
| common     | application/octet-stream                                                                    |

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES文件下载实现.html](http://www.skyline.show/ES文件下载实现.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

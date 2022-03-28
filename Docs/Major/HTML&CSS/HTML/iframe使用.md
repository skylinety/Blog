# iframe 使用

## iframe 调用录音视频设备

默认情况下，iframe 无法直接获取浏览器的音视频设备权限，需要通过 allow 属性赋权。
指定`allow='microphone;camera;midi;encrypted-media;'`

```html
<iframe
  frameborder="0"
  allow="microphone;camera;midi;encrypted-media;"
  style="    width: 100%;height: 100%;"
  class="grid-content bg-purple-light"
  src=""
></iframe>
```

Chrome 下父页面需要采用 https 协议，否则也不可获取相关权限。

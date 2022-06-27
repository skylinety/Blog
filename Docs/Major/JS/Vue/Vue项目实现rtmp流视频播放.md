# Vue 项目实现 rtmp 流视频播放

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Vue 项目实现 rtmp 流视频播放](#vue-项目实现-rtmp-流视频播放)
  - [前言](#前言)
  - [代码实现](#代码实现)
  - [常见问题](#常见问题)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 前言

rtmp 流需要使用 flash 播放。
在 chrome 88 版本及以后的版本，已经移除了 flash 组件。
在 2021 年 1 月 12 日，adobe 已宣布不再支持 flash。
故本方案在次之后可能不再实用。
成功引入 rtmp 流，效果如下
![Vue项目实现rtmp流视频播放20220627173249](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E9%A1%B9%E7%9B%AE%E5%AE%9E%E7%8E%B0rtmp%E6%B5%81%E8%A7%86%E9%A2%91%E6%92%AD%E6%94%BE20220627173249.png)

## 代码实现

实现需求需要运用的包为 videojs-flash、videojs

`main.js`

```js
import videojs from 'video.js'
import 'video.js/dist/video-js.css'
Vue.prototype.$video = videojs
```

`player.vue`

```js

<template>
  <div class="demo1-video">
    <video
      ref="videoPlayer"
      id="myVideo"
      class="video-js"
      controls
      preload="auto"
      style="width: 100%"
      height="220"
      data-setup="{}"
    >
      <p class="vjs-no-js">
        To view this video please enable JavaScript, and consider upgrading to a
        web browser that
        <a
          href="https://videojs.com/html5-video-support/"
          target="_blank"
        >supports HTML5 video</a>
      </p>
    </video>
  </div>
</template>

<script>
import "videojs-flash";
export default {
  name: "VideoPlayer",
  props: ["type", "detail"],
  inject: ["gisMap"],
  data() {
    return {
      player: null,
      videoOptions: {
        autoplay: true, // 是否自动播放
        muted: false, // 是否静音
        controls: false,

        // fluid: true, // 宽高自适应
        // techOrder: ["flash"],
        sources: [
          {
            src: "//vjs.zencdn.net/v/oceans.mp4",
            type: "video/mp4"
            // type: "rtmp/flv"
          }
        ]
      }
    };
  },
  computed: {
    map() {
      return this.gisMap.map.map || {};
    },
    endType() {
      if (this.type) {
        let end = this.type.split("_")[1];
        return end;
      }
      return "";
    }
  },
  mounted() {
    // if (this.gisMap.map && this.gisMap.map.map) {
    this.map.on("popupclose", this.clearVideo);
    this.map.on("popupopen", this.playVideo);
    // }
    this.playVideo();
  },
  destroyed() {
    this.map.off("popupclose", this.clearVideo);
    this.map.off("popupopen", this.playVideo);

  },
  methods: {
    clearVideo() {
      if (this.player) {
        this.player.dispose();
        this.player = null;
      }
    },
    playVideo() {
      this.player = this.$video(
        this.$refs.videoPlayer,
        {
          autoplay: true,
          techOrder: ["flash", "html5"]
        },
        function onPlayerReady() {
          this.src({
            src: "rtmp://58.200.131.2:1935/livetv/hunantv",
            type: "rtmp/flv"
          });
          this.play();

          this.on("ended", function() {});
        }
      );
    }
  }
};
```

## 常见问题

- `No compatible source was found for this media.`

解决方式：
检查浏览器是否允许运行 flash
若果 videojs 是版本 6 以上，flash 支持已独立成 videojs-flash，检查是否引入该库
检查 option 中 techOrder 的配置是否是 ["flash", "html5"]，其默认配置是["html5"]，不配置将不会用 flash

- ` The "flash" tech is undefined. Skipped browser support check for that tech`

网络解决方案一般是删除库包重新安装或者什么 cnpm 的问题，其实不然，有关讨论[#221](https://github.com/surmon-china/vue-video-player/issues/221)

方案 1：

> [配置包优先级](https://github.com/surmon-china/vue-video-player/issues/221#issuecomment-519495293)

不管是删除 node_module 还是 cnpm 都不是根本的解决方案，
根本原因是 videojs 和 videojs-flash 里的各有一个 video.js，如果两个版本不一样可能就会报错了，终极解决方案就是配置第三方模块的查找顺序，优先查找本身安装的 videojs 就可以了

```js
// webpack.config.js
resolve: {
modules: [path.resolve('node_modules'), 'node_modules'],
    ...
}

// vue.config.js

configureWebpack: function (config) {
return {
    resolve: {
    modules: [path.resolve('node_modules'), 'node_modules']
    }
}
}
```

按照如上配置仍旧不行的话，根据问题出现原因，尝试

方案 2

在 yarn.lock 或 package-lock.json 查看 videojs-flash 对应的 videojs 版本。
也可在 node_modules 中查看。
另也可删除 videojs-flash，重新安装，查看其对应的 videojs 版本。
![Vue项目实现rtmp流视频播放20220627173957](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E9%A1%B9%E7%9B%AE%E5%AE%9E%E7%8E%B0rtmp%E6%B5%81%E8%A7%86%E9%A2%91%E6%92%AD%E6%94%BE20220627173957.png)

```sh
yarn add video.js@7.8.0
```

重新安装 videojs 指定版本

- `TypeError: this.el_.vjs_getProperty is not a function`

出现此问题多数是由于播放器在 DOM 中进行显示隐藏切换，需要在隐藏时将播放器完全销毁。调用 this.player.dispose()

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Vue项目实现rtmp流视频播放.html](http://www.skyline.show/Vue项目实现rtmp流视频播放.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

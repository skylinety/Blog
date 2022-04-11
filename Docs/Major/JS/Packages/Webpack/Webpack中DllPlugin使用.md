# Webpack 中 DllPlugin 使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Webpack 中 DllPlugin 使用](#webpack-中-dllplugin-使用)
  - [DllPlugin 概述](#dllplugin-概述)
    - [实质](#实质)
    - [DllPlugin 配置](#dllplugin-配置)
  - [引入 dll 库](#引入-dll-库)
    - [手动引入 dll 文件（不推荐）](#手动引入-dll-文件不推荐)
    - [手动引入注意](#手动引入注意)
    - [自动引入(推荐)](#自动引入推荐)
    - [自动引入常见问题](#自动引入常见问题)
  - [成果分析](#成果分析)
    - [优化前](#优化前)
    - [优化后：](#优化后)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## DllPlugin 概述

### 实质

其实质是把项目中引入的较大模块先行分离出来，之后相关模块不会再被打包。从而优化打包速度。同时兼具分离模块的作用。

> webpack v2 时已存在，在 v4+已不推荐使用该配置，新其版本迭代带来的性能提升足以忽略 DllPlugin 所带来的打包优化效益

### DllPlugin 配置

webpack.dll.config.js 配置

新建单独的配置文件

webpack.dll.config.js

```js
var path = require('path')
var webpack = require('webpack')

module.exports = {
  // 你想要打包的模块的数组
  entry: {
    vendor: [
      'vue/dist/vue.esm.js',
      'vuex',
      'axios',
      'vue-router',
      'element-ui',
    ],
  },
  output: {
    path: path.join(__dirname, '../static/js'), // 打包后文件输出的位置
    filename: '[name].dll.js',
    library: '[name]_library',
    // vendor.dll.js中暴露出的全局变量名。
    // 主要是给DllPlugin中的name使用，
    // 故这里需要和webpack.DllPlugin中的`name: '[name]_library',`保持一致。
  },
  plugins: [
    new webpack.DllPlugin({
      path: path.join(__dirname, '../', '[name]-manifest.json'),
      name: '[name]_library',
      context: __dirname,
    }),
    // 压缩打包的文件
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false,
      },
    }),
  ],
}
```

配置说明

path：manifest.json 生成的文件夹及名字，该项目让它生成在了根目录下。
name：和 output. library 保持一致即可。
context：选填，manifest 文件中请求的上下文，默认为该 webpack 文件上下文。

在 package.json 中添加执行脚本

```js
"dll": "webpack --config build/webpack.dll.conf.js",
```

执行 yarn dll
生成 dll 文件和 manifest.json 文件
![Webpack中DllPlugin使用20220411144435](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Webpack%E4%B8%ADDllPlugin%E4%BD%BF%E7%94%A820220411144435.png)
manifest.json 文件包含了引用模块的 id 映射，为 DllReferencePlugin 引用做准备

## 引入 dll 库

### 手动引入 dll 文件（不推荐）

在根目录的 index.html 里引入所生成的 dll 库

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <title>xx市城市综合管理基础</title>
  </head>
  <body>
    <div id="app"></div>
    <script src="/static/js/vendor.dll.js"></script>
    <!-- built files will be auto injected -->
  </body>
</html>
```

### 手动引入注意

如果前后端约定了项目访问 url 前缀，如'skyline',则前端可以在 output.publicPath 指定值为'/skyline/'
同时手动引入是需为如下配置。

同时在测试环境 webpack.dev.conf.js 中，需要设定代理

```js
proxyTable: {
      '/skyline': {
        target: 'http://localhost:8080/', // 本地地址，开发环境一旦端口变更就要更改，非常麻烦
        pathRewrite: {
          '^/skyline/static': '/static'
        },
}
```

### 自动引入(推荐)

html-webpack-tags-plugin 插件

html-webpack-tags-plugin 插件默认会把 publicPath 加入文件地址前缀，当 output.publicPath = 'skyline' 时，插入代码为<script src="/skyline/static/js/vendor.dll.js"></script>

html-webpack-tags-plugin 配置代码

```js
new HtmlWebpackTagsPlugin({
    tags: ['static/js/vendor.dll.js'],
    append: false // 默认true
}),
```

### 自动引入常见问题

append 使用默认 true 将会有以下错误
![Webpack中DllPlugin使用20220411144509](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Webpack%E4%B8%ADDllPlugin%E4%BD%BF%E7%94%A820220411144509.png)
这里是由于插入的代码位置不对
![Webpack中DllPlugin使用20220411144526](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Webpack%E4%B8%ADDllPlugin%E4%BD%BF%E7%94%A820220411144526.png)
设定为 false 之后，插入位置如下
![Webpack中DllPlugin使用20220411144558](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Webpack%E4%B8%ADDllPlugin%E4%BD%BF%E7%94%A820220411144558.png)

```js
Uncaught ReferenceError: \_dll_vendor is not defined
```

造成这个错误主要有 4 个可能的原因：

context 上下文不一致(DllPlugin context 与 DllReferencePlugin context 一致)
library 和 name 不一致（output.library 需要和 DllPlugin option.name 一致）
生成的 dll 文件没加入到 html 文件中
生成的 dll 文件没加入到 html 文件中位置不对，如本文所示

DllReferencePlugin 配置

```js
plugins: [
  new webpack.DllReferencePlugin({
    context: __dirname, //这个上下文对应DllPlugin
    manifest: require('./vendor-manifest.json'),
  }),
]
```

## 成果分析

### 优化前

![Webpack中DllPlugin使用20220411144752](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Webpack%E4%B8%ADDllPlugin%E4%BD%BF%E7%94%A820220411144752.png)

### 优化后：

![Webpack中DllPlugin使用20220411144800](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Webpack%E4%B8%ADDllPlugin%E4%BD%BF%E7%94%A820220411144800.png)

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> [DllPlugin](https://webpack.js.org/plugins/dll-plugin) > [webpack 进阶——DllPlugin 优化打包性能（基于 vue-cli）](https://juejin.im/entry/598bcbc76fb9a03c5754d211)

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh

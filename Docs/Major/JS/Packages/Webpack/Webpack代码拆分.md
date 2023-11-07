# Webpack代码拆分

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Webpack代码拆分](#webpack代码拆分)
  - [基础代码](#基础代码)
  - [默认开箱配置](#默认开箱配置)

<!-- /code_chunk_output -->


## 基础代码
```jsx
//pageA.js

var vue = require('vue');
var utility1 = require('./utility1');
var utility2 = require('./utility2');
new Vue()

import(/* webpackChunkName: "common-async.js" */"./common-async").then(common => {
  console.log(common);
})

module.exports = "pageA";

//pageB.js
var react = require('react');
var reactDom = require('react-dom');
var utility2 = require('./utility2');
var utility3 = require('./utility3');
import(/* webpackChunkName: "common-async.js" */"./common-async").then(common => {
  console.log(common);
})
module.exports = "pageB";

//pageC.js
var utility2 = require('./utility2');
var utility3 = require('./utility3');

module.exports = "pageC";

//pageD.js
import "./common-async"
module.exports = "pageD";

//common-async.js
import(/* webpackChunkName: "f.js" */"./f").then(f => {
  console.log(f);
})

module.exports = "common-async";

//f.js utility1.js utility1.js utility1.js
module.exports = "utility1"
module.exports = "utility2"
module.exports = "utility3"
module.exports = "f"
```




## 默认开箱配置
Webpack默认会将入口文件和按需加载的文件来生成对应的代码块
webpack.config.js
```jsx
var path = require("path");
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin // BundleAnalyzer插件，图形化分析打包文件结构

module.exports = {
  // mode: "development" || "production",
  entry: {
    pageA: "./pageA", // 引用utility1.js  utility2.js vue.js 动态引入common-async
    pageB: "./pageB", // 引用utility2.js  utility3.js react reactDom 动态引入common-async
    pageC: "./pageC", // 引用utility2.js  utility3.js,
  },
  optimization: {
  },
  output: {
    path: path.join(__dirname, "dist"),
    filename: "[name].js"
  },
  plugins: [new BundleAnalyzerPlugin()]
};
```

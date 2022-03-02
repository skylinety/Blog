# Vue 基础使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Vue 基础使用](#vue-基础使用)
  - [Vue transition](#vue-transition)
    - [基本使用](#基本使用)
    - [使用限制](#使用限制)
  - [Vue Router model](#vue-router-model)
  - [img 图片错误默认处理](#img-图片错误默认处理)
  - [extend](#extend)
    - [获取.vue 组件的构造函数](#获取vue-组件的构造函数)
    - [使用示例](#使用示例)
    - [无法挂载错误](#无法挂载错误)
  - [mixin](#mixin)
    - [混入规则](#混入规则)
  - [组件挂载顺序](#组件挂载顺序)
    - [简述](#简述)
    - [总结](#总结)
  - [computed](#computed)
    - [简单说明](#简单说明)
    - [setter](#setter)
  - [$watch](#watch)
    - [用法](#用法)
    - [注意](#注意)
    - [返回值](#返回值)
    - [深度监听](#深度监听)
  - [资源引用](#资源引用)
  - [refs 使用](#refs-使用)
  - [动态组件](#动态组件)
  - [\$attrs 与\$listeners](#attrs-与listeners)
  - [生命周期函数](#生命周期函数)
    - [监听](#监听)
  - [Vue.observable](#vueobservable)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## Vue transition

### 基本使用

将 transition name 命名后书写对应的类来自动生成的对应的类

```html
<transition name="fade">
  <p v-if="show">hello</p>
</transition>

<style>
  .fade-enter-active,
  .fade-leave-active {
    transition: width 3s, opacity 1s;
    width: 100%;
  }
  .fade-enter,
  .fade-leave-to {
    width: 0;
    display: none;
    opacity: 0;
  }
</style>
```

### 使用限制

transition 仅限用于如下组件上

- 条件渲染 (使用 v-if)
- 条件展示 (使用 v-show)
- 动态组件
- 组件根节点

对于 v-for 使用不会有任何效果， 需要改为使用 `<transition-group>`
`<transition-group>` 元素作为多个元素/组件的过渡效果

```html
<transition-group name="fade" tag="div">
  <div v-for="(item, index) in sources" :key="index">
    <p>{{item.skyline}}</p>
  </div>
</transition-group>
```

当使用 v-for 并对 key 值进行 index 绑定，会出现如下警告

> Do not use v-for index as key on `<transition-group>` children, this is the same as not using keys.

处理方式如下：

```js
:key="index + 0"
```

## Vue Router model

Vue 有两种路由模式:

- Hash
- History

默认情况下使用 Hash 模式。
哈希模式利用 URL Hash 保证单页系统不进行页面重载。
但是，传统 URL 的 Hash 中即常见的`site#thing`是来定位页面内容的，
使用`site/thing`来跳转页面
Hash 模式虽然保证了页面不跳转，但是'#'的出现破坏了传统规则。
在一些项目中，会使用 History 模式。

```js
const router = new VueRouter({
  mode: 'history',
  routes: [...]
})
```

History 模式通过 history.pushState 防止路由重载。
由于单页问题，History 在对应路由在服务器中位置并没有 HTML 入口文件，
这需要我们进行额外的服务配置。
若不进行配置，刷新页面会报错。
Nginx 配置如下

```shell
location / {
  try_files $uri $uri/ /index.html;
}

```

其余服务端配置参考
https://router.vuejs.org/guide/essentials/history-mode.html#example-server-configurations

## img 图片错误默认处理

```jsx
<img
    width="98"
    height="112"
    :src="m.imgAddr || '~@img/suspect.png'"
    @error="slotimg"
    alt
/>

let defaultImg = require("@img/suspect.png");

methods: {
    slotimg(event) {
      console.log("HotFocus.vue第211行:::err img");
      let img = event.srcElement;
      img.src = defaultImg;
      img.onerror = null; //防止闪图
    },
}
```

html 原生是 οnerrοr 来监听图片渲染错误事件

## extend

### 获取.vue 组件的构造函数

### 使用示例

Vue.extend

```jsx
var button = Vue.extend(FullScreenButton)
var b = new button()
b.$mount()
```

### 无法挂载错误

![Vue基础使用20211202165231](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A820211202165231.png)

出现这种错误是由于首字母大写导致，具体缘由待查，如下图中注释所示

![Vue基础使用20211202165302](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A820211202165302.png)

## mixin

### 混入规则

- data 在混入时会进行递归合并，如果两个属性发生冲突，则以组件自身为主
- 生命周期钩子函数 混入时会将同名钩子函数加入到一个**数组**中，会先按照数组顺序依次执行执行混入对象的同名钩子函数，再执行本组件的。

## 组件挂载顺序

### 简述

- vue 子组件与父组件之间，父组件首先加载完成（beforeCreate->beforeMount 率先执行）之后是子组件加载，最后由子向父组件挂载
- 要在所有组件生命周期完成后执行某个函数，只需要在父组件加入 nextTick 即可

vue 代码结构如下

```tsx
<template>
    <div class='papa'>
        <c1></c1>
        <c2></c2>
    </div>
</template>
<script>
export default {
    name: 'PaPa',

    components: {
        c1,
        c2
    },

    beforeCreate() {
      console.log('papa beforeCreate')
    },

    created() {
      console.log('papa created')
    },

    beforeMount() {
      console.log('papa beforeMount')
    },

    mounted(){
        console.log('papa mounted')
        this.$nextTick(() => {
            console.log('papa nextTick')
        })

        setTimeout(() => {
            console.log('papa setTimeout')
        })
    }
}
</script>
```

打印结果如下： 其中 nextTick 与 setTimeout 在生命周期的位置无关

![Vue基础使用20211202165355](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A820211202165355.png)

### 总结

加载渲染过程

```js
父 beforeCreate=>父 created=>父 beforeMount
=>子 beforeCreate=>子 created=>子 beforeMount
=>子 mounted=>父 mounted
```

子组件更新过程

```js
父 beforeUpdate=>子 beforeUpdate=>子 updated=>父 updated
```

父组件更新过程

```js
父 beforeUpdate=>父 updated
```

销毁过程

```js
父 beforeDestroy=>子 beforeDestroy=>子 destoryed=>父 destoryed
```

## computed

### 简单说明

计算属性是基于它们的依赖进行缓存的。计算属性只有在它的相关依赖发生改变时才会重新求值。这就意味着只要依赖还没有发生改变，多次访问计算属性会立即返回之前的计算结果，这一定程度上节约了开销。

### setter

setter 需要注意的是，如果需要书写 set 函数，一般需要**变更计算属性相关依赖**

```jsx
computed: {
  fullName: {
    // getter
    get: function () {
      return this.firstName + ' ' + this.lastName
    },
    // setter
    set: function (newValue) {
      var names = newValue.split(' ')
      this.firstName = names[0]
      this.lastName = names[names.length - 1]
    }
  }
}
```

## $watch

### 用法

观察 Vue 实例变化的一个表达式或计算属性函数。回调函数得到的参数为新值和旧值。表达式只接受监督的键路径。对于更复杂的表达式，用一个函数取代，或写在 computed 中，监听 computed

### 注意

第一参数

$watch 函数接受的第一个参数是属性名的字符串，一定要用引号，不能用变量来获取

```jsx
data() {
        return {
            itemList: []
        }
    },
    mounted() {
        this.$nextTick(() => {

            this.$watch('itemList', function(n, v) {//不能写成this.itemList或直接写itemList

                this.mainPostList = _.takeWhile(n,function(o) {
                    return o.id == 18
                })
            })

        })
    }
```

### 返回值

$watch 返回一个取消观察函数，用来停止触发回调

```jsx
var unwatch = vm.$watch('a', cb) // 之后取消观察
unwatch()
```

### 深度监听

为了发现对象内部值的变化，可以在选项参数中指定 deep: true 。注意监听数组的变动不需要这么做。

```
vm.$watch('someObject', callback, {  deep: true})
```

在变异 (不是替换) 对象或数组时，旧值将与新值相同，因为它们的引用指向同一个对象/数组。Vue 不会保留变异之前值的副本。

## 资源引用

vue-html-loader 和 css-loader 认为没带根的路径为相对路径。官方为了让其看起来像模块路径, 加上了~前缀标志，表示让其从 webpack 配置中 alias 的相应项目取值，不加将找不到相应模块。

```jsx
//webpack
resolve: {
    extensions: ['.js', '.vue', '.json'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
      '@': resolve('src'),
      '@assets': resolve('src/assets'),
      'static': resolve('static'),
    }
}

//less使用
<style lang="less">
       @import '~vux/src/styles/reset.less';
</style>
//dom使用
<img class="logo" src="~assets/logo.png">
```

## refs 使用

> $refs 只会在组件渲染完成之后生效，并且它们不是响应式的。这仅作为一个用于直接操作子组件的“逃生舱”——你应该避免在模板或计算属性中访问 $refs。

各生命周期中，只有 updated 阶段则是完成了数据更新到 DOM 的阶段,但当页面 DOM 频繁更新，需考虑放在此处的合法性

## 动态组件

当 v-if/v-else-if 存在较多情况且其内部渲染的组件较大时，考虑使用动态组件，例如 tab 标签下的内容

示例 1

```jsx
<component v-bind:is='currentTabComponent'></component>
```

示例 2

```jsx
export const menus = [
    {
        name: "业务管理",
        icon: "el-icon-document-copy",
        id: "form",
        children: [{
                name: "业务注册",
                icon: "el-icon-document",
                id: "formList",
                to: "formList"
            }
        ]
    },
    {
        name: "数据源注册",
        icon: "el-icon-finance",
        id: "dataSource",
        to: "dataSource"
    },
]

<el-menu
  ref="elMenu"
  class="el-menu-vertical"
  :default-active="active"
  :collapse="isCollapse"
  :router="true"
>
  <component
    v-bind:is="m.children ? 'ElSubmenu' : 'ElMenuItem'"
    v-for="(m, i) in menus"
    :index="m.to"
    :key="i"
  >
    <template slot="title">
      <i :class="m.icon"></i>
      <span>{{m.name}}</span>
    </template>
    <el-menu-item-group v-if="m.children">
      <el-menu-item v-for="(c, i) in (m.children || [])" :index="c.to" :key="i">
        <template slot="title">
          <i :class="c.icon"></i>
          <span>{{c.name}}</span>
        </template>
      </el-menu-item>
    </el-menu-item-group>
  </component>
</el-menu>
```

## \$attrs 与\$listeners

> \$attrs 包含了父作用域中不作为 prop 被识别 (且获取) 的 attribute 绑定 (class 和 style 除外)。当一个组件没有声明任何 prop 时，这里会包含所有父作用域的绑定 (class 和 style 除外) $listeners 包含了父作用域中的 (不含 .native 修饰器的) v-on 事件监听器。

即接收除了 props 声明外的所有绑定属性（class、style 除外），$listeners包含了父作用域中的事件监听器 在创建高级别的组件时，通过 v-on="$listeners“，与 v-bind=”$attrs" 将值传入内部组件。

示例 `skylline-dialog.vue`

```html
<el-dialog :visible.sync="show" v-bind="$attrs" v-on="$listeners">
  <slot></slot>
  <template #footer>
    <slot name="footer">
      <span>
        <el-button>取 消</el-button>
        <el-button>确 定</el-button>
      </span>
    </slot>
  </template>
</el-dialog>
```

在一个业务系统中所有弹窗都需要两个按钮，为了减少每次使用弹窗都写按钮，我们将弹窗组件进行二次封装。 通过*attrs 与*listeners，我们避免了 props 及$emit 对属性与事件逐个添加。

```html
<skyline-dialog :visible.sync="show" title="测试" @opened="doSth">
  这是一段内容</skyline-dialog
>
```

## 生命周期函数

### 监听

可以通过$on 监听

`this.on('hook:updated', () => {})`

`父组件监听`

<skyline-select @hook:updated=“doSth” />`

## Vue.observable

Vue.observable 会让一个对象成为响应式的。

```jsx
const state = Vue.observable({ count: 0 })

const Demo = {
  render(h) {
    return h(
      'button',
      {
        on: {
          click: () => {
            state.count++
          },
        },
      },
      `count is: ${state.count}`
    )
  },
}
```

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

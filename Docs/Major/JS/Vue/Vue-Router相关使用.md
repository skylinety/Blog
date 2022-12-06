# Vue-Router 相关使用

## Vue 路由权限拦截

### 问题描述

路由跳转时，部分页面需要进行权限验证，其中最常见的就是登陆验证，如果没有权限，则会跳转到登陆页面。
本文进行在 vue-router 的基础上进行权限探讨。

### 权限验证代码

如下示例将函数加入全局混合的方法中，通常情况下只需在组件中使用。
除了登陆验证，也可创建新函数进行其他校验，如角色验证等

```js
// 为自定义的选项 'myOption' 注入一个处理器。
Vue.mixin({
  methods: {
    /* 获取多页面的view与route */
    $viewUrl() {
      const href = window.location.href
      const url = encodeURIComponent(href) //编码转换
      return url
    },
    /* 多页面跳转 */
    $href(to, query) {
      const location = window.location
      const env = process.env.NODE_ENV
      let url = ''
      if (env === 'development') {
        url = location.protocol + '//' + location.host + '/views/' + to
      } else {
        url = location.protocol + '//' + location.host + '/dist/views/' + to
      }
      url = query ? url + '?' + query : url
      location.href = url
    },
    /**
     * 权限验证
     * @param  {Array}  rules  eg: [{name: 'isAdmin', redirect: 'index/home'}, {name: 'isLogin', redirect: 'index/login'}] || ['isAdmin', 'islogin']
     * @param  {Object} status eg: {isActive: false, isLogin: true}
     * @return {[type]}        [description]
     */
    $verifyRules(rules = [], status = {}) {
      typeof rules[0] == 'string'
        ? rules.forEach((val) => {
            !status[val] && this.$href('index/index.html#/home')
          })
        : rules.forEach((val) => {
            !status[val.name] &&
              this.$href(val.redirect || 'index/index.html#/home')
          })
    },

    /* 登录验证跳转 */
    $loginVerify() {
      const viewUrl = 'lastPath=' + this.$viewUrl
      this.$href('index/index.html#/login', viewUrl) // 将跳转的路由path作为参数，登录成功后跳转到该路由
    },
    /* 用户身份验证跳转 */
    $roleVerify() {
      const viewUrl = 'lastPath=' + this.$viewUrl
      this.$href('index/index.html#/join', viewUrl) // 将跳转的路由path作为参数，登录成功后跳转到该路由
    },
  },
})
```

---

### 路由设置

```js
const routes = [
    //顶层路由
    {
        path: '/userInfo',
        component: UserInfo,
        meta: {
            accessRules: ['isLogin'] //登录验证
        },
        children: [
            {
            name:'adminSys',
            path: '/adminSys',
            component: AdminSys,
            meta:{
               accessRules: [{name: 'isAdmin', redirect: 'index/toBeAdmin'}, {name: 'isLogin', redirect: 'index/login'}]//跳转到路由是否需要权限
            }
        ]
    }
}]

```

---

### 路由钩子

```js
/**
 * store.getters.userInfo.accessStatus = {isAdmin: false, isActive: false, isLogin: true}
 */
router.beforeEach((to, from, next) => {
  if (store.getters.userInfo.accessStatus.isAdmin) {
    const status = store.getters.userInfo.accessStatus,
      accessRules = Object.assign(
        {},
        ...to.matched.map((m) => m.meta)
      ).accessRules //父路由accessRules应用于全部路由，当子路由设定有accessRules时，子规则覆盖父路由规则

    accessRules && vue.$verifyRules(accessRules, status)

    next()
  } else {
    vue.$roleVerify()
  }
})
```

## 路由格式

### 子路由前'/'

```js
{
    path: '/index',
    component: Index,
    children: [{
            path: '/home',
            name: 'home',
            component: Home
        }
    ]
}
```

访问 Home 页面
http://10.10.7.181:8060/#/home

### 子路由

```js
{
    path: '/index',
    component: Index,
    children: [{
            path: 'home',
            name: 'home',
            component: Home
        }
    ]
}
```

访问 Home 页面
http://10.10.7.181:8060/#/index/home
子路由中不建议在 path 前加'/'绝对路径，容易造成误解（本意可能想要第二种结果）。

### 路由隐藏 index

如果需要在路由中隐藏'index'，改成如下写法

```js
{
    path: '/',
    component: Index,
    children: [{
            path: 'home',
            name: 'home',
            component: Home
        }
    ]
}
```

访问 Home 页面
http://10.10.7.181:8060/#/home

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Vue-Router 相关使用.html](http://www.skyline.show/Vue-Router相关使用.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

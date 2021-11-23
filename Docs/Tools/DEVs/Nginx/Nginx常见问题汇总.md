# Nginx 常见问题汇总

## 页面刷新不能进入

检查页面的路由模式。
特别是在 Vue 项目中，具体查看 [HTML5 History Mode](https://router.vuejs.org/guide/essentials/history-mode.html#example-server-configurations)
vue 默认的是 hash 路由模式，使用此种模式，页面路由变化时，并不会重载页面

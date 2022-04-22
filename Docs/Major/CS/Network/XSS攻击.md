## 情景复现

在输入表单中，如果对输入的字符未进行校验
![XSS攻击20220405180423](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/XSS%E6%94%BB%E5%87%BB20220405180423.png)
在 vue 使用时，直接用 render 渲染字符串时，会有如下结果
![XSS攻击20220405180301](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/XSS%E6%94%BB%E5%87%BB20220405180301.png)

## 解决

axios 中进行请求拦截，但是前端的替换只能是校验表单的内容，当攻击者捕获请求链接直接发起对应请求时，仍旧可以进行攻击。
故需要后端也对请求经行校验，防止脚本字符直接入库。

```js
// 创建axios实例
const service = axios.create({
  baseURL: '',
  timeout: 60 * 1000, // 请求超时时间
})
// 请求拦截器
service.interceptors.request.use(
  (config) => {
    // // 设置全局设置token头
    // const accessToken = store.getters.token
    // if (accessToken && !config.headers.hasOwnProperty('accessToken')) {
    //   config.headers['accessToken'] = accessToken // 让每个请求携带自定义token 请根据实际情况自行修改
    // }
    Object.entries(config.data || {}).forEach(([k, v]) => {
      if (typeof v === 'string') {
        config.data[k] = v.replace(/([^><]*<)([^><]+>)([^><]*)/g, '$1%$2$3')
      }
    })
    // if (
    //   config.headers['Content-Type'] === 'application/x-www-form-urlencoded' &&
    //   config.data &&
    //   Object.prototype.toString.call(config.data) === '[object Object]'
    // ) {
    //   config.data = qs.stringify(config.data)
    // }
    return config
  },
  (err) => {
    return Promise.reject(err)
  }
)
```

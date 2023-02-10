# ES 事件轮询

## 执行机制

### 单线程

JS 设计为单线程脚本语言，主线程只能同时处理一个任务。
为了防止主线程阻塞，事件轮询机制应运而生（event loop）
先看如下一个常见示例

```jsx
console.log(1)

setTimeout(() => {
  console.log(5)
}, 0)

setTimeout(() => {
  console.log(6)
}, 10)

Promise.resolve()
  .then(() => {
    console.log(3)
  })
  .then(() => {
    console.log(4)
  })

console.log(2)

// 1 2 3 4 5 6
```

### 同异步

### 执行栈

## 宏微任务

JS 主程序（整体代码）就是一个宏任务，主程序开始执行时，将其内部执行函数不断入栈出栈。
微任务在代码执行过程中产生并进入微任务队列。
宏任务执行过程中若遇到调用 WebAPI（UI 事件注册，定时器注册）等代码，会交于对应触发线程，主程序往后执行。
当前宏任务执行完成后，将微任务依次放入执行栈执行，直到当前微任务队列被会清空。
宏任务队列中下一个宏任务放入执行栈执行。
新的宏任务进入队列时机取决于触发线程什么时候返回结果，拿到结果时，宏任务回调进入宏任务队列中等待执行。

常见的任务
宏任务： script( 整体代码)、setTimeout、setInterval、I/O、UI 交互事件
微任务： Promise、MutaionObserver、process.nextTick(Node.js)

## 事件轮询

JS 执行机制为：
执行一个宏任务，执行完毕后，清空该宏任务产生的微任务。执行下一个宏任务，继续清空其产生的微任务。
通过不断地轮询，不断地在上述过程循环，就像是在宏任务与微任务之前转圈圈。
![ES事件轮询$20230202094126](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E4%BA%8B%E4%BB%B6%E8%BD%AE%E8%AF%A2%2420230202094126.png)
进一步简化图示，可以看成一个队列中的代码依次进入执行栈执行。
![ES事件轮询$20230202094201](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E4%BA%8B%E4%BB%B6%E8%BD%AE%E8%AF%A2%2420230202094201.png)

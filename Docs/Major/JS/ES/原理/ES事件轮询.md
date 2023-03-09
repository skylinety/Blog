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

todo

### 执行栈

函数的执行时会被放入栈中，多个函数嵌套时，遵循栈的原则，即先进后出。

## 宏微任务

JS 主程序（整体代码）就是一个宏任务，主程序开始执行时，将其内部执行函数不断入栈出栈。
微任务在代码执行过程中产生并进入微任务队列。
宏任务执行过程中若遇到调用 WebAPI（UI 事件注册，定时器注册）等代码，会交于对应触发线程，主程序往后执行。
当前宏任务执行完成后，将微任务依次放入执行栈执行，直到当前微任务队列被会清空。
宏任务队列中下一个宏任务放入执行栈执行。
新的宏任务进入队列时机取决于触发线程什么时候返回结果，拿到结果时，宏任务回调进入宏任务队列中等待执行。
任务的执行遵循队列的原则，即先进先出。

常见的任务
宏任务： script( 整体代码)、setTimeout、setInterval、I/O、UI 交互事件
微任务： Promise、async/await、MutaionObserver、process.nextTick(Node.js)

## 事件轮询

JS 执行机制为：
主程序作为一个宏任务，首先执行。
执行一个宏任务，执行完毕后，清空执行该宏任务产生的微任务。执行下一个宏任务，继续清执行空其产生的微任务，由此循环往复。
通过不断地轮询，不断地在上述过程循环，就像是在宏任务与微任务之前转圈圈。

![ES事件轮询$20230202094126](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E4%BA%8B%E4%BB%B6%E8%BD%AE%E8%AF%A2%2420230202094126.png)

进一步简化图示，可以看成一个队列中的代码依次进入执行栈执行。

![ES事件轮询$20230202094201](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/ES%E4%BA%8B%E4%BB%B6%E8%BD%AE%E8%AF%A2%2420230202094201.png)

## 轮询与页面渲染

主入口程序为宏任务，将每次轮询的宏任务和其产生的微任务看做一对，
宏任务先执行，微任务后执行（很多文章观点为微任务先执行，这是抛开主程序为宏任务的观点），
每次轮询中队列内执行会先于DOM渲染，只有微任务队列最后一个任务被执行，DOM才会被渲染。

由于alert会阻塞DOM渲染，故示例代码中间定时器的时间延长，方便观察DOM渲染的时机。

```jsx
alert('首次轮询宏任务（主入口程序）')
function createEL(tag = 'h3', content) {
    const e = document.createElement(tag)
    e.innerHTML = content
    return e
}
document.body.appendChild(createEL('h3', 'number 1'))

setTimeout(() => {
    alert('第二轮轮询只有宏任务')
    document.body.appendChild(createEL('h3', 'number 5'))
}, 3000)

setTimeout(() => {
    document.body.appendChild(createEL('h3', 'number 6'))
    alert('第三轮轮询宏任务')
    Promise.resolve()
    .then(() => {
        document.body.appendChild(createEL('h3', 'number 7'))
        alert('第三轮轮询微任务')
    })
}, 10000)

Promise.resolve()
    .then(() => {
        document.body.appendChild(createEL('h3', 'number 3'))
        alert('首次轮询微任务')
    })
    .then(() => {
        document.body.appendChild(createEL('h3', 'number 4'))
    })

document.body.appendChild(createEL('h3', 'number 2'))

```

可以观察到，只有每一轮的轮询最后的微任务执行完成，与该次轮询关联的DOM渲染才会执行。

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️


> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ES事件轮询$.html](http://www.skyline.show/ES事件轮询.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！


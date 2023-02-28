# Vue 数据驱动原理

## 通过 this 访问 data/props 中的数据

在组件的生命周期或者方法中，可以通过 this 直接拿到 props、data 等中的数据，这是由于 Vue 做了一层代理，
调用了 proxy 方法

```jsx
proxy(vm, '_data', key)
```

```jsx
var sharedPropertyDefinition = {
  enumerable: true,
  configurable: true,
  get: noop,
  set: noop
};

function proxy(target, sourceKey, key) {
  sharedPropertyDefinition.get = function proxyGetter() {
    return this[sourceKey][key]
  }
  sharedPropertyDefinition.set = function proxySetter(val) {
    this[sourceKey][key] = val
  }
  Object.defineProperty(target, key, sharedPropertyDefinition)
}
```

通过为组件定义新的访问器属性，并重写访问器的读写来达到代理的目的。

## mount

Vue.prototype.$mount 主要做了两件事：

- 编译模版语法
- 调用 mountComponent 挂在组件到页面

不管是 template 语法还是写 render 函数，Vue 最终都通过 render 来获取对应的 VDOM。

```jsx
var ref = compileToFunctions(
  template,
  {
    shouldDecodeNewlines: shouldDecodeNewlines,
    shouldDecodeNewlinesForHref: shouldDecodeNewlinesForHref,
    delimiters: options.delimiters,
    comments: options.comments,
  },
  this
)
var render = ref.render
var staticRenderFns = ref.staticRenderFns
options.render = render
options.staticRenderFns = staticRenderFns
```

如上，模版语法将通过 compileToFunctions 被编译成 render 函数。

调用 mountComponent 挂在组件到页面

```jsx
function mountComponent() {
  callHook(vm, 'beforeMount')
  // 组件首次挂载和后续更新都要调用此方法
  updateComponent = function () {
    vm._update(vm._render(), hydrating)
  }
  new Watcher(
    vm,
    updateComponent,
    noop,
    {
      before: function before() {
        if (vm._isMounted) {
          callHook(vm, 'beforeUpdate')
        }
      },
    },
    true /* isRenderWatcher */
  )
  if (vm.$vnode == null) {
    vm._isMounted = true
    callHook(vm, 'mounted')
  }
  return vm
}
```

在实例化 Watcher 时，会执行 updateComponent 方法，此时会先执行 vm.\_render()得到 VDOM，然后传参给 vm.\_update 渲染到页面。
后续页面更新时，也是调用updateComponent来更新VDOM和页面的。
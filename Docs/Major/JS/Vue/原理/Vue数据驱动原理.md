# Vue 数据驱动原理

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Vue 数据驱动原理](#vue-数据驱动原理)
  - [数据驱动流程](#数据驱动流程)
  - [init](#init)
    - [初始化数据与功能函数](#初始化数据与功能函数)
    - [进行数据代理](#进行数据代理)
  - [mount](#mount)
    - [Vue.prototype.$mount](#vueprototypemount)
    - [模版编译](#模版编译)
    - [创建 watcher 实例](#创建-watcher-实例)
  - [render](#render)
    - [Vue.prototype.\_render](#vueprototype_render)
    - [createElement 创建 Vnode](#createelement-创建-vnode)
    - [树形结构扁平化](#树形结构扁平化)
  - [update](#update)
    - [Vue.prototype.\_update](#vueprototype_update)
    - [页面渲染](#页面渲染)
    - [偏函数技巧](#偏函数技巧)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 数据驱动流程

> 本文对应的 Vue 版本为 2.5.17

数据驱动是指视图由数据来调配生成，视图的更新不直接操作 DOM，而是直接修改数据。

Vue 时数据驱动的，其数据驱动流程大致如下：
![Vue数据驱动原理$20230304194743](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Vue%E6%95%B0%E6%8D%AE%E9%A9%B1%E5%8A%A8%E5%8E%9F%E7%90%86%2420230304194743.png)

## init

### 初始化数据与功能函数

在实例化 Vue（new Vue）时，主要调用了\_init 方法。

函数内部初始化一系列数据与功能函数
主要包括：

- 合并配置
- 初始化生命周期
- 初始化事件中心
- 初始化渲染
- 初始化数据
- 执行生命周期函数钩子

```jsx
Vue.prototype._init = function (options?: Object) {
  const vm: Component = this
  ...
  initLifecycle(vm)
  initEvents(vm)
  initRender(vm)
  callHook(vm, 'beforeCreate')
  initInjections(vm) // resolve injections before data/props   initState(vm)   initProvide(vm)
  callHook(vm, 'beforeCreate')
  initInjections(vm) // resolve injections before data/props
  initState(vm)
  initProvide(vm) // resolve provide after data/props
  callHook(vm, 'created')
  ...

  if (vm.$options.el) {
    vm.$mount(vm.$options.el)
  }
```

### 进行数据代理

在初始化数据 initState 函数中，内部调用了 proxy 方法进行数据代理，
使得可以通过 this 访问 data/props 中的数据。

```jsx
initState(vm)
```

在组件的生命周期或者方法中，可以通过 this 直接拿到 props、data 等中的数据，
就是由于 Vue 做了一层代理，

```jsx
proxy(vm, '_data', key)
```

```jsx
var sharedPropertyDefinition = {
  enumerable: true,
  configurable: true,
  get: noop,
  set: noop,
}

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

### Vue.prototype.$mount

在 init 函数最后，调用了 mount。

```jsx
vm.$mount(vm.$options.el)
```

这对应组件挂载函数 Vue.prototype.$mount ，
mount 有一个公共的函数，

```jsx
// public mount method
Vue.prototype.$mount = function (
  el?: string | Element,
  hydrating?: boolean
): Component {
  el = el && inBrowser ? query(el) : undefined
  return mountComponent(this, el, hydrating)
}
```

根据不同的平台，调用公共 mount 的同时，进行平台或环境定制。

```jsx
const mount = Vue.prototype.$mount
Vue.prototype.$mount = function (
  el?: string | Element,
  hydrating?: boolean
): Component {
  el = el && query(el)
  ...
  const options = this.$options
  // resolve template/el and convert to render function
  if (!options.render) {

      /* istanbul ignore if */
      if (process.env.NODE_ENV !== 'production' && config.performance && mark) {
        mark('compile')
      }
      const { render, staticRenderFns } = compileToFunctions(template, {
        shouldDecodeNewlines,
        shouldDecodeNewlinesForHref,
        delimiters: options.delimiters,
        comments: options.comments
      }, this)
      options.render = render
      options.staticRenderFns = staticRenderFns

  }
  return mount.call(this, el, hydrating)
```

最后部分的

```jsx
mount.call(this, el, hydrating)
```

即主要调用了 mountComponent。

mount 方法主要做了两件事：

- 编译模版语法
- 调用 mountComponent 挂在组件到页面

不管是 template 语法还是写 render 函数，Vue 最终都通过 render 来获取对应的 VDOM。

### 模版编译

```jsx
const { render, staticRenderFns } = compileToFunctions(
  template,
  {
    shouldDecodeNewlines,
    shouldDecodeNewlinesForHref,
    delimiters: options.delimiters,
    comments: options.comments,
  },
  this
)
options.render = render
options.staticRenderFns = staticRenderFns
```

如上，模版语法将通过 compileToFunctions 被编译成 render 函数。

### 创建 watcher 实例

在 mount 函数最后，会调用 mountComponent 挂在组件到页面时，实例化了 Watcher。
创建 watcher 实例时，调用 updateComponent 函数。

这里的 Watcher 用到的是观察者模式，这里用于初始化页面并监听更新，这一部分需要单独分析。

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

此时会先执行 vm.\_render()得到 VDOM，然后传参给 vm.\_update 渲染到页面。
后续页面更新时，也是调用 updateComponent 来更新 VDOM 和页面的。

## render

### Vue.prototype.\_render

在实例化 Watcher 时，执行 updateComponent 方法，

```jsx
// hydrating用于判断是否服务端
vm._update(vm._render(), hydrating)
```

render 函数用于生成 VDOM 。

```jsx
Vue.prototype._render = function (): VNode {
  const vm: Component = this
  const { render, _parentVnode } = vm.$options
  // set parent vnode. this allows render functions to have access
  // to the data on the placeholder node.
  vm.$vnode = _parentVnode
  // render self
  let vnode
  try {
    vnode = render.call(vm._renderProxy, vm.$createElement)
  } catch (e) {
    ...
  }
  ...
  vnode.parent = _parentVnode
  return vnode
}
```

### createElement 创建 Vnode

Vue 其实已将 VDOM 获取函数 createElement 的 API 暴露并传递给 render 作为其参数，
日常代码也会涉及使用 render 来写组件。

```jsx
export function _createElement(
  // 组件上下文,vm实例
  context: Component,
  // 生成目标
  tag?: string | Class<Component> | Function | Object,
  // 相关信息
  data?: VNodeData,
  // 子节点
  children?: any,
  // 区分template编译还是开发者手写
  normalizationType?: number
): VNode | Array<VNode> {
  ...
  if (!tag) {
    // in case of component :is set to falsy value
    return createEmptyVNode()
  }
  // support single function children as default scoped slot
  if (Array.isArray(children) && typeof children[0] === 'function') {
    data = data || {}
    data.scopedSlots = { default: children[0] }
    children.length = 0
  }
  if (normalizationType === ALWAYS_NORMALIZE) {
    children = normalizeChildren(children)
  } else if (normalizationType === SIMPLE_NORMALIZE) {
    children = simpleNormalizeChildren(children)
  }
  let vnode, ns
  if (typeof tag === 'string') {
    let Ctor
    ns = (context.$vnode && context.$vnode.ns) || config.getTagNamespace(tag)
    if (config.isReservedTag(tag)) {
      // platform built-in elements
      vnode = new VNode(
        config.parsePlatformTagName(tag),
        data,
        children,
        undefined,
        undefined,
        context
      )
    } else if (
      isDef((Ctor = resolveAsset(context.$options, 'components', tag)))
    ) {
      // component
      vnode = createComponent(Ctor, data, context, children, tag)
    } else {
      // unknown or unlisted namespaced elements
      // check at runtime because it may get assigned a namespace when its
      // parent normalizes children
      vnode = new VNode(tag, data, children, undefined, undefined, context)
    }
  } else {
    // direct component options / constructor
    vnode = createComponent(tag, data, context, children)
  }
  if (Array.isArray(vnode)) {
    return vnode
  } else if (isDef(vnode)) {
    if (isDef(ns)) applyNS(vnode, ns)
    if (isDef(data)) registerDeepBindings(data)
    return vnode
  } else {
    return createEmptyVNode()
  }
}
```

createElement 区分不同情况创建不同的 Vnode，对于树形结构，递归扁平化成 vnode 的一维数组`Array<vnode>`

### 树形结构扁平化

这里将对于 template 编译成的 render，其 children 进行简单扁平化处理
simpleNormalizeChildren

```jsx
export function simpleNormalizeChildren(children: any) {
  for (let i = 0; i < children.length; i++) {
    if (Array.isArray(children[i])) {
      return Array.prototype.concat.apply([], children)
    }
  }
  return children
}
```

对于用户手写 render，需要用递归来将所有子节点统一扁平化获取一维数组。

normalizeChildren

```jsx
export function normalizeChildren(children: any): ?Array<VNode> {
  return isPrimitive(children)
    ? [createTextVNode(children)]
    : Array.isArray(children)
    ? normalizeArrayChildren(children)
    : undefined
}

function normalizeArrayChildren(
  children: any,
  nestedIndex?: string
): Array<VNode> {
  const res = []
  let i, c, lastIndex, last
  for (i = 0; i < children.length; i++) {
    c = children[i]
    if (isUndef(c) || typeof c === 'boolean') continue
    lastIndex = res.length - 1
    last = res[lastIndex]
    //  nested
    if (Array.isArray(c)) {
      if (c.length > 0) {
        c = normalizeArrayChildren(c, `${nestedIndex || ''}_${i}`)
        // merge adjacent text nodes
        if (isTextNode(c[0]) && isTextNode(last)) {
          res[lastIndex] = createTextVNode(last.text + (c[0]: any).text)
          c.shift()
        }
        res.push.apply(res, c)
      }
    } else if (isPrimitive(c)) {
      if (isTextNode(last)) {
        // merge adjacent text nodes
        // this is necessary for SSR hydration because text nodes are
        // essentially merged when rendered to HTML strings
        res[lastIndex] = createTextVNode(last.text + c)
      } else if (c !== '') {
        // convert primitive to vnode
        res.push(createTextVNode(c))
      }
    } else {
      if (isTextNode(c) && isTextNode(last)) {
        // merge adjacent text nodes
        res[lastIndex] = createTextVNode(last.text + c.text)
      } else {
        // default key for nested array children (likely generated by v-for)
        if (
          isTrue(children._isVList) &&
          isDef(c.tag) &&
          isUndef(c.key) &&
          isDef(nestedIndex)
        ) {
          c.key = `__vlist${nestedIndex}_${i}__`
        }
        res.push(c)
      }
    }
  }
  return res
}
```

## update

### Vue.prototype.\_update

render 获取到的虚拟节点作为 update 方法的第一个参数传入。

```jsx
// hydrating用于判断是否服务端
vm._update(vm._render(), hydrating)
```

\_update 方法如下，主要调用了**patch**将 VDOM 渲染到页面上。

```jsx
Vue.prototype._update = function (vnode: VNode, hydrating?: boolean) {
  const vm: Component = this
  const prevEl = vm.$el
  const prevVnode = vm._vnode
  const prevActiveInstance = activeInstance
  activeInstance = vm
  vm._vnode = vnode
  // Vue.prototype.__patch__ is injected in entry points
  // based on the rendering backend used.
  if (!prevVnode) {
    // 首次渲染，第一参数为真实DOM
    vm.$el = vm.__patch__(vm.$el, vnode, hydrating, false /* removeOnly */)
  } else {
    // 后续数据更新渲染，第一参数为VNode
    vm.$el = vm.__patch__(prevVnode, vnode)
  }
  activeInstance = prevActiveInstance
  // update __vue__ reference
  if (prevEl) {
    prevEl.__vue__ = null
  }
  if (vm.$el) {
    vm.$el.__vue__ = vm
  }
  // if parent is an HOC, update its $el as well
  if (vm.$vnode && vm.$parent && vm.$vnode === vm.$parent._vnode) {
    vm.$parent.$el = vm.$el
  }
  // updated hook is called by the scheduler to ensure that children are
  // updated in a parent's updated hook.
}
```

### 页面渲染

页面渲染主要在`__patch__`中实现的，
非浏览器（一般为服务器）不需要页面渲染，首先进行判断

```jsx
Vue.prototype.__patch__ = inBrowser ? patch : noop
```

这里的 patch 为

```jsx
import * as nodeOps from 'web/runtime/node-ops'
import { createPatchFunction } from 'core/vdom/patch'
import baseModules from 'core/vdom/modules/index'
import platformModules from 'web/runtime/modules/index'

// the directive module should be applied last, after all
// built-in modules have been applied.
const modules = platformModules.concat(baseModules)

export const patch: Function = createPatchFunction({ nodeOps, modules })
```

浏览器端的 nodeOps 中包含操作 DOM 的方法，包含原生 DOM 生成与交互等，例如：

```jsx
export function createTextNode(text: string): Text {
  return document.createTextNode(text)
}

export function removeChild(node: Node, child: Node) {
  node.removeChild(child)
}

export function appendChild(node: Node, child: Node) {
  node.appendChild(child)
}
```

modules 包含基础公共模块 baseModules，并根据不同平台包含不同的模块 platformModules。

baseModules 包含 ref 和 directive 更行和注册，
浏览器端的 platformModules 包含属性、类、事件等的操作钩子，
用来创建或更新 DOM 上对应的内容。

```jsx
export function createPatchFunction (backend) {
  let i, j
  const cbs = {}

  const { modules, nodeOps } = backend
  ...
  return function patch (oldVnode, vnode, hydrating, removeOnly) {
      ...
      const isRealElement = isDef(oldVnode.nodeType)
      if (!isRealElement && sameVnode(oldVnode, vnode)) {
        // patch existing root node
        patchVnode(oldVnode, vnode, insertedVnodeQueue, removeOnly)
      } else {
        // oldVnode为首次渲染时的真实DOM
        if (isRealElement) {
          ...
          // 将真实DOM改为空的Vnode
          oldVnode = emptyNodeAt(oldVnode)
        }

        // replacing existing element
        const oldElm = oldVnode.elm
        const parentElm = nodeOps.parentNode(oldElm)

        // create new node
        createElm(
          vnode,
          insertedVnodeQueue,
          // extremely rare edge case: do not insert if old element is in a
          // leaving transition. Only happens when combining transition +
          // keep-alive + HOCs. (#4590)
          oldElm._leaveCb ? null : parentElm,
          nodeOps.nextSibling(oldElm)
        )
        ...
      }
    ...
    return vnode.elm
  }
}
```

调用 createElm 进行真实 DOM 渲染

```jsx

  function createElm (
    vnode,
    insertedVnodeQueue,
    parentElm,
    refElm,
    nested,
    ownerArray,
    index
  ) {

    // 创建组件节点
    if (createComponent(vnode, insertedVnodeQueue, parentElm, refElm)) {
      return
    }

    const data = vnode.data
    const children = vnode.children
    const tag = vnode.tag
    if (isDef(tag)) {
      ...
      // 原生API创建真实DOM
      vnode.elm = vnode.ns
        ? nodeOps.createElementNS(vnode.ns, tag)
        : nodeOps.createElement(tag, vnode)
      setScope(vnode)

      /* istanbul ignore if */
      if (__WEEX__) {
        ...
      } else {
        createChildren(vnode, children, insertedVnodeQueue)
        // 插入到DOM
        insert(parentElm, vnode.elm, refElm)
      }
      ...
  }

```

createChildren 中递归调用 createElm 来将构建真实节点

```jsx
function createChildren(vnode, children, insertedVnodeQueue) {
  if (Array.isArray(children)) {
    ...
    for (let i = 0; i < children.length; ++i) {
      createElm(
        children[i],
        insertedVnodeQueue,
        // 当前节点作为父节点
        vnode.elm,
        null,
        true,
        children,
        i
      )
    }
  } else if (isPrimitive(vnode.text)) {
    nodeOps.appendChild(vnode.elm, nodeOps.createTextNode(String(vnode.text)))
  }
}
```

### 偏函数技巧

可以看到 createPatchFunction 最后返回就是一个 patch 函数,
这里，有一个技巧点，vue 绕了一圈，没有将

```jsx
export const patch: Function = createPatchFunction({ nodeOps, modules })
```

写成

```jsx
export const patch (oldVnode, vnode, hydrating, removeOnly, nodeOps, modules){
  ...
}
```

这里利用闭包，使用了一个叫偏函数的技巧，
将平台差异化的参数提前传入，后续使用时不再多传固定参数。
简化来看如下：

```jsx
function createPatchFunction(a) {
  return path (b) {
    return a + b
  }
}

const patchWeb = createPatchFunction(5)
const patchWeex = createPatchFunction(6)
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://ustbhuangyi.github.io/vue-analysis/v2/prepare/

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Vue 数据驱动原理.html](http://www.skyline.show/Vue数据驱动原理.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

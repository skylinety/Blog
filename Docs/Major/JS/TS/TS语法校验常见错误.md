# TS 语法校验常见错误

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

## property does not exist on type Object

### 复现

Property 'length' does not exist on type'Object'.

```jsx
var obj: Object = Object.create(null);
obj.value = "value"; //[ts] Property 'length' does not exist on type'Object'.
```

### 解决

**将对象类型设置为 any**

```jsx
var obj: any = Object.create(null);
obj.value = "value";
```

**通过字符方式获取对象属性**

```jsx
var obj: Object = Object.create(null);
obj["value"] = "value";
```

**通过接口定义对象所具有的属性**

```jsx
var obj: ValueObject = Object.create(null);
obj.value = "value";

interface ValueObject {
  value?: string;
}
```

**使用断言强制执行**

```jsx
var obj: Object = Object.create(null);
(obj as any).value = "value"
```

## Expression of type ‘string’ can’t be used to index type

### 复现

Element implicitly has an ‘any’ type because expression of type ‘string’ can’t be used to index type

person 并未明确指定键值类型（即隐式指定为任意类型），任意类型与 getValue 传参的 string 类型冲突。

```jsx
const person = {
  name: "sk",
  age: 22,
};

function getValue(arg: string) {
  return person[arg]; // Element implicitly has an 'any' type because expression of type 'string' can't be used to index type '{ name: string; age: number; }'.
}
```

### 解决

**tsconfig.json**

`tsconfig.json`中配置`suppressImplicitAnyIndexErrors: true`

**定义接口**

```jsx
const person = {
    name: 'sk',
    age: 22
};

function getValue(arg: string) {
	interface IPerson {
		[key: string]: any
	}
    return (<IPerson>person)[arg];
}
```

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warranty

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

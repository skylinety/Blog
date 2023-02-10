# Vue2 项目引入 TS

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Vue2 项目引入 TS](#vue2-项目引入-ts)
  - [vue-cli3 项目](#vue-cli3-项目)
  - [依赖引入](#依赖引入)
    - [安装相关依赖](#安装相关依赖)
    - [tsconfig](#tsconfig)
    - [babel.config](#babelconfig)
    - [vue.config](#vueconfig)
    - [vue2tsx](#vue2tsx)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## vue-cli3 项目

在使用 vue-cli3 及以上创建的项目根目录下，可执行命令

```sh
vue add typescript
```

## 依赖引入

### 安装相关依赖

若直接 vue-cli3 添加支持不可行或 cli 低于该版本，可尝试自行添加相关依赖包来解决。

```sh
yarn add -D @vue/babel-preset-jsx @vue/babel-helper-vue-jsx-merge-props @babel/plugin-transform-typescript
```

注意部分包之前可能存在不兼容问题
部分兼容相关包版本如下

```sh
"@babel/plugin-transform-typescript": "^7.19.3",
"@vue/babel-helper-vue-jsx-merge-props": "^1.4.0",
"@vue/babel-preset-jsx": "^1.4.0",
```

若要引入 eslint 和 prettier 校验和格式化代码，
引入或者修改包版本如下可解决兼容问题

```sh
"@vue/cli-plugin-babel": "4.4.6",
"@vue/cli-plugin-eslint": "4.4.6",
"@vue/eslint-config-prettier": "7.0.0",
"eslint": "7.15.0",
"eslint-config-prettier": "^8.5.0",
"eslint-plugin-prettier": "3.4.1",
"eslint-plugin-vue": "7.2.0",
"prettier": "2.5.1",
```

### tsconfig

新建 tsconfig.json，内容如下

```ts
{
  "compilerOptions": {
    "target": "ES2017",
    "module": "UMD",
    "allowJs": true,
    "jsx": "preserve",
    "moduleResolution": "Node",
    "allowSyntheticDefaultImports": true,
    "importHelpers": true,
    "baseUrl": "./",
    "paths": {
      "@/*": [
        "src/*"
      ]
    }
  }
}
```

也可自行配置。
若引入 prettier 和 eslint
则新建
.prettierrc.json

```js
{
    "arrowParens": "always",
    "bracketSpacing": true,
    "endOfLine": "lf",
    "htmlWhitespaceSensitivity": "css",
    "insertPragma": false,
    "singleAttributePerLine": false,
    "bracketSameLine": false,
    "jsxBracketSameLine": false,
    "jsxSingleQuote": true,
    "printWidth": 80,
    "proseWrap": "preserve",
    "quoteProps": "as-needed",
    "requirePragma": false,
    "semi": false,
    "singleQuote": true,
    "tabWidth": 2,
    "trailingComma": "es5",
    "useTabs": false,
    "vueIndentScriptAndStyle": false
}
```

.eslint.js

```js
module.exports = {
  root: false,
  env: {
    node: true,
    // 'vue/setup-compiler-macros': true
  },
  extends: [
    'plugin:vue/recommended',
    '@vue/standard',
    'plugin:prettier/recommended',
  ],
  rules: {
    'no-debugger': 'off',
    indent: ['off', 2],
    'no-multi-assign': 'error',
    'arrow-spacing': [
      2,
      {
        before: true,
        after: true,
      },
    ],
    'vue/max-attributes-per-line': [
      'off',
      {
        singleline: 3,
        multiline: 1,
      },
    ],
    'vue/multiline-html-element-content-newline': [
      'warn',
      {
        ignoreWhenEmpty: true,
        ignores: [],
        allowEmptyLines: true,
      },
    ],
    camelcase: 'off',
    'vue/multi-word-component-names': 'off',
    'vue/mustache-interpolation-spacing': 'off',
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
}
```

### babel.config

调整或新加 babel 选项
babel.config.js

```js
module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset',
    ['@vue/babel-preset-jsx', { compositionAPI: true }], // 开启 jsx
  ],
  plugins: [
    ['@babel/plugin-transform-typescript', { isTSX: true }], // 开启 typescript
  ],
}
```

### vue.config

调整或新加 vue 选项
vue.config.js

```js
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src'),
      },
      extensions: ['.ts', '.tsx'],
    },
    module: {
      rules: [
        {
          test: /\.(js|tsx|ts|jsx)$/,
          exclude: /node_modules|vue-router\/|vue-loader\//,
          use: 'babel-loader',
        },
      ],
    },
    externals: {},
  },
```

### vue2tsx

.vue

```js
<template>
  <router-view id="app" />
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="scss">
</style>

```

.tsx

```js
import { defineComponent, onMounted } from 'vue'

export default defineComponent({
  setup() {
    onMounted(() => {})
  },
  render() {
    return <router-view id='app' />
  },
})
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> [Vue2.x 开启 Composition API、tsx](https://juejin.cn/post/6957881662302584839#heading-15)

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Vue2 项目引入 TS.html](http://www.skyline.show/Vue2项目引入TS.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

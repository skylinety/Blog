# ESLint 与 Prettier 使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [ESLint 与 Prettier 使用](#eslint-与-prettier-使用)
  - [Linter 与 Prettier](#linter-与-prettier)
  - [ESLint 与 Prettier 共用](#eslint-与-prettier-共用)
  - [共用冲突](#共用冲突)
  - [常见问题](#常见问题)
    - [eslint 校验禁用](#eslint-校验禁用)
    - [格式化禁用](#格式化禁用)
  - [常见报错](#常见报错)
    - [换行报错](#换行报错)
    - [插件版本兼容报错](#插件版本兼容报错)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## Linter 与 Prettier

常用的 Linter 有 ESLint/TSLint/stylelint 等。

Linter 大致分为两类校验规则：

- 代码格式
- 代码语法

代码格式规定了缩进、空格、换行等
代码语法重点关注未使用变量([no-unused-vars](https://eslint.org/docs/latest/rules/no-unused-vars))、隐式全局变量([no-implicit-globals](https://eslint.org/docs/latest/rules/no-implicit-globals))等问题

Prettier 无关代码语法，她可补充 Linter 规定代码格式。

总之，一个常见的方案为，使用 Linter 来捕获语法问题和 Bug，Prettier 来格式化代码。

## ESLint 与 Prettier 共用

ESLint、Prettier 都分别有 NPM 包和 VSCode 插件。
ESLint 的 VSCode 插件可以在让我们在写代码过程中实时发现波浪标红的错误，提升工作效率。
当然，插件其实不是必须的，我们可以通过 `eslint --fix` `npx prettier --write` 修复部分相关问题。
但是部分无法自动修复的问题需要我们提交代码时一一排查。
ESLint、Prettier 在 VSCode 中对应的插件用以提高我们编码效率，在插件商店搜索安装即可。
在项目中将具体的配置分别放在项目根目录下.eslintrc.js 与 prettierrc.json 中。
一个简单的 ESLint 配置如下

```js
module.exports = {
  root: false,
  env: {
    node: true,
    // 'vue/setup-compiler-macros': true
  },
  extends: ['plugin:vue/recommended', '@vue/standard'],
  rules: {
    'no-debugger': 'off',
    indent: ['off', 2],
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
}
```

rules 的规则如下

- "off" 或 0 - 关闭规则
- "warn" 或 1 - 开启规则，错误警告而不退出
- "error" 或 2 - 开启规则，错误退出

一个简单的 prettier 配置如下

```json
{
  "printWidth": 100, // 超过最大值换行
  "tabWidth": 4, // 缩进字节数
  "useTabs": false, // 缩进不使用tab，使用空格
  "semi": true, // 句尾添加分号
  "singleQuote": true, // 使用单引号代替双引号
  "proseWrap": "preserve", // 默认值。因为使用了一些折行敏感型的渲染器（如GitHub comment）而按照markdown文本样式进行折行
  "arrowParens": "avoid", //  (x) => {} 箭头函数参数只有一个时是否要有小括号。avoid：省略括号
  "bracketSpacing": true, // 在对象，数组括号与文字之间加空格 "{ foo: bar }"
  "disableLanguages": ["vue"], // 不格式化vue文件，vue文件的格式化单独设置
  "endOfLine": "auto", // 结尾是 \n \r \n\r auto
  "eslintIntegration": false, //不让prettier使用eslint的代码格式进行校验
  "htmlWhitespaceSensitivity": "ignore",
  "ignorePath": ".prettierignore", // 不使用prettier格式化的文件填写在项目的.prettierignore文件中
  "jsxBracketSameLine": false, // 在jsx中把'>' 是否单独放一行
  "jsxSingleQuote": false, // 在jsx中使用单引号代替双引号
  "parser": "babylon", // 格式化的解析器，默认是babylon
  "requireConfig": false, // Require a 'prettierconfig' to format prettier
  "stylelintIntegration": false, //不让prettier使用stylelint的代码格式进行校验
  "trailingComma": "es5", // 在对象或数组最后一个元素后面是否加逗号（在ES5中加尾逗号）
  "tslintIntegration": false // 不让prettier使用tslint的代码格式进行校验
}
```

prettier 具体配置项常见[官网](https://prettier.io/docs/en/options.html)

让插件格式化的生效策略同样是就近原则，寻找被格式化文件系统目录层级中最近的配置文件，越近优先级越高。
要在保存代码时自动触发 ESLint 修复与 Prettier 格式化，需要在 VSCode 配置文件 setting.json 中添加如下代码
ESLint

```js
"editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
 },
"eslint.validate": ["javascript", "javascriptreact", "typescript", "html", "vue"],
```

Prettier

```js
"editor.formatOnSave": true,
"[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
},
"[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
},
"[less]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
},
    "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
},
```

同时也可在项目根目录下创建.vscode 文件夹创建 setting.json 文件并提交仓库，将对应配置共享给项目开发成员。

## 共用冲突

当使用两者在项目中时，一个比较常见的情况是，格式化代码使用 Prettier 规则，在提交或保存代码时触发`eslint --fix`将代码格式成另一种风格。
解决方案有两种，一是将配置文件靠齐，即修改 eslintrc 或 prettierrc 对应配置是的二者一致。
当配置差异较大时，修改工作量较大。
另一种方案为使用已有插件：
eslint-config-prettier 与 eslint-plugin-prettier
其本质原理也是统一两者规则。
eslint-config-prettier 用于禁用和 prettier 有冲突的 ESLint 规则
eslint-plugin-prettier 用于将 prettier 的规则让 ESLint 识别并在 ESLint 插件中输出（如实时错误警告等）。
加入上述插件后，修改配置文件，在 extends 后添加'plugin:prettier/recommended'

```js
  extends: [
    'plugin:vue/recommended',
    '@vue/standard',
    'plugin:prettier/recommended',
  ],
```

配合上述两个插件使用使得的`eslint --fix`格式化代码时采用 prettier 的规则，从而解决上述格式化冲突问题。

## 常见问题

### eslint 校验禁用

在项目根目录创建.eslintignore 文件，写入忽略的文件文件夹等。
其文件内容格式遵循[.gitignore 对应规则](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)
通过`！`可恢复被忽略的文件
例如

```js
 src/*              // 排除src目录下面所有的
 !src/views/        // src/views下面所有的目录重新被包含回来
```

### 格式化禁用

当在移动端开发时，通常需要将 px 转换成 rem，部分场景需要使用大写 PX 来防止被转换，但是 prettier 会自动格式化为小写，这时候需要

```css
/* prettier-ignore */
border: 1PX;
```

来禁用格式化
新建 .prettierignore 文件来忽略（即不重新格式化）某些文件和文件夹。
使用 "prettier-ignore "注释来忽略文件的一部分。
具体参见官方[忽略说明](https://prettier.io/docs/en/ignore.html)

## 常见报错

### 换行报错

```sh
Delete `␍`eslint(prettier/prettier)
```

换行报错的产生是由于操作系统换行符不一致导致。
Windows| Linux/Mac| Early Mac
--|--|--
CRLF| LF| CR
'\n\r'| '\n'| '\r'

尝试在 prettier 配置文件添加

```js
"endOfLine": "auto"
```

或在 ESLint 配置文件中添加

```js
  rules: {
    'prettier/prettier': [
      'error',
      {
        endOfLine: 'auto',
      },
    ],
  }
```

然后，将 git 自动转换换行符关闭

```sh
git config --global core.autocrlf false
```

### 插件版本兼容报错

由于关联的插件较多，容易遇到插件版本不兼容引起的错误如下

```sh
'prettier/prettier': context.getPhysicalFilename is not a function
```

可能为 eslint 版本问题，升级其版本

```sh
yarn upgrade -R eslint
```

若仍旧不行，尝试更换如下插件为兼容版本

先清除原有版本

```sh
npm rm @vue/cli-plugin-babel @vue/cli-plugin-eslint @vue/eslint-config-prettier eslint eslint-plugin-prettier eslint-plugin-vue prettier
```

如下示例版本可兼容

```sh

npm i -D @vue/cli-plugin-babel@4.4.6 @vue/cli-plugin-eslint@4.4.6 @vue/eslint-config-prettier@7.0.0 eslint@7.15.0 eslint-plugin-prettier@3.4.1 eslint-plugin-vue@7.2.0 prettier@2.5.1
```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/ESLint 与 Prettier 使用.html](http://www.skyline.show/ESLint与Prettier使用.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

# Husky 使用

## Husky 使用配置

### husky 简述

husky 支持所有 git 相关钩子，在对应 git 操作触发时，可以执行测试、代码校验等相关任务。

以代码校验为例来说明

代码校验 lint-staged 相关配置如下

```js
{
	"devDependencies": {
		"lint-staged": "^11.1.2",
	},
	...,
	"lint-staged": {
        "*.{js,jsx,ts,tsx,vue}": "eslint --cache --fix"
    }
}

```

后续代码中，其余配置为 husky 相关，通过这些配置，我们在 commit 代码时，会校验代码错误与格式，校验不通过会有提示。
![Husky使用20210924150933](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Husky%E4%BD%BF%E7%94%A820210924150933.png)

Husky 在版本 5 中配置做了大变动，具体前后的配置以版本来说明。

### V5+

yarn add husky -D

安装 husky 最新包

npx husky-init && yarn

在 package.json 会自动添加如下选项

```js

{
    "scripts": {
        ...,
        "prepare": "husky install"
    },
    "devDependencies": {
        "husky": "^7.0.0",
        "lint-staged": "^11.1.2",
    }
}
```

汇总其他相关配置选项，如下
`package.json`

```js
{
    "scripts": {
        ...,
        "precommit": "lint-staged",
        "prepare": "husky install"
    },
    "devDependencies": {
        "husky": "^7.0.0",
        "lint-staged": "^11.1.2",
    },
    ...,
    "lint-staged": {
    "*.{js,jsx,ts,tsx,vue}": "eslint --cache --fix"
    }
}

```

同时会在项目目录下自动生成 .husky 目录，包含最基础的 pre-commit bash 脚本，将 bash 脚本的默认 npm test 改为 npm run precommit 即可

`pre-commit`

```js
#!/bin/sh
. "$(dirname "$0")/_/husky.sh"

npm run precommit
```

### V4

yarn add husky@v4.3.8 -D

package.json

```js
{
    ...,
    "devDependencies": {
            ...,
            "husky": "4.3.8",
            "lint-staged": "^11.1.2",
    },
    ...,
    "lint-staged": {
        "*.{js,jsx,ts,tsx,vue}": "eslint --cache --fix"
    },
    "husky": {
        "hooks": {
        "pre-commit": "lint-staged"
        }
    }
}
```

## Husky 配置更新

### git hooks 说明

要配置 Git 钩子，只需要简单地在.git/hooks/目录下放对应钩子的可执行文件即可
![Husky使用20210924152534](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Husky%E4%BD%BF%E7%94%A820210924152534.png)

通过 husky 简述中配置可以看到，husky 更新后配置似乎更加麻烦，如下探讨会为何会有去简就繁的操作。

### V4 工作原理

在 V4 版本及以前，为了可执行 .huskyrc.js 中配置的钩子， 在装 Husky 的时候，默认初始化了全部钩子在.git/hooks/ 中。
例如，在执行 commit 时 ， husky/runner.js 会去检查 .huskyrc.js 中是否有对应的配置

```shell
$ git commit

pre-commit (native) → husky/runner.js (node)
→ is a pre-commit defined in `.huskyrc.js`? → YES, run it

prepare-commit-msg (native) → husky/runner.js (node)
→ is a prepare-commit-msg defined in `.huskyrc.js`? → NO, do nothing

commit-msg (native) → husky/runner.js (node)
→ is a commit-msg defined in `.huskyrc.js`? → NO, do nothing

post-commit (native) → husky/runner.js (node)
→ is a post-commit defined in `.huskyrc.js`? → NO, do nothing
```

初始所有了所有.git/hooks/ 钩子，这样的好处是用户随时可以在.huskyrc.js 中增减配置，缺点是对应钩子没有任何相应的配置时，.git/hooks/对应钩子仍旧存在，husky/runner.js 也仍旧会执行。
考虑优化插件方向，如果 Husky 初始根据.huskyrc.js 只在.git/hooks/生成对应的配置
考虑如下配置

```
// .huskyrc.js
module.exports = {
  hooks: {
    'pre-commit': 'lint-staged'
  }
}
```

```
.git/hooks/pre-commit ← is somehow created
```

后续有新的钩子需求

```
// .huskyrc.js
module.exports = {
    hooks: {
    // 'pre-commit': 'lint-staged', ← removed
    'commit-msg': 'lint-staged' ← added
    }
}
```

.git/hooks 目录下仍旧只存在 pre-commit 文件。
本例中，如果我们只需要使用 pre-commit 钩子，删除.git/hooks/中其他钩子后程序依旧可以正常运行，但是后续在 .huskyrc.js 添加新钩子并不会在.git/hooks/自动生成对应钩子，新加的配置不会起任何作用。

如果要采用上述方式又不想初始化全部钩子，.huskyrc.js 配置与.git/hooks/ 中自动生成对应钩子文件，这就涉及 JS 与 Git 的配置同步问题。

### V5+ 原理

2016 年，Git 在 2.9 版本引入了 core.hooksPath. 让 Git hooks 的目录可以个性化定制。
Husky 5+ 将相关钩子放置在项目.husky 目录下，默认只创建一个运行 npm test 的 pre-commit 钩子。
用户不再去.huskyrc.js 配置钩子，而是需要手动运行 npx husky add .husky/commit-msg 'npm test' 添加新的钩子。
`husky install` 更改 Git hooks 目录到 .husky/
解决了非必要钩子初始化问题，默认只创建一个运行 npm test 的 pre-commit 钩子。
`husky add` 提供后续添加新钩子的需求
解决配置同步问题，不再去使用.huskyrc.js 或者在 package.json 中配置钩子，而是通过该命令直接在.husky 目录下生成）

### 后续问题

引入.husky 目录，代码混乱?
引入.huskyrc.js 也存在，.husky 支持统一放在 config 等指定目录下。
作为 JS 库不用 JS 来配置？
如 Jest, ESLint, Prettier 等用 .jestrc.js, .eslintrc.js, .prettierrc.js 来配置，它们全都是用纯 JS 写的。
Husky 并不是纯 JS 开发，包含 Shell 脚本，与 Git 交互。

## BMW WARNING

### Bulletin

I am a bucolic migrant worker but I never walk backwards.

### Material

> [Why husky has dropped conventional JS config](https://blog.typicode.com/husky-git-hooks-javascript-config/)

### Warranty

> 本文作者： Skyline(lty)
> 版权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

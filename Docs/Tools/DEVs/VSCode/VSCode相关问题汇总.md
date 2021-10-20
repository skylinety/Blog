# VSCode 相关问题汇总

## Snippets

### markdown 文件 Snippets 不生效

**问题描述**
通过 File -> Preferences -> User Snippets -> Markdown
写相关代码块如下
`markdown.json`

````JSON
{
	// Place your snippets for markdown here. Each snippet is defined under a snippet name and has a prefix, body and
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the
	// same ids are connected.
	// Example:
	"JS code block": {
		// "scope": "md,markdown",
		"prefix": ":cjs",
		"body": [
			"```${1:js}",
			"$2",
			"```"
		],
		"description": "JS code block"
	},
	"PY code block": {
		// "scope": "md,markdown",
		"prefix": ":cpy",
		"body": [
			"```${1:python}",
			"$2",
			"```"
		],
		"description": "PY code block"
	}
}
````

在 markdown 文件中敲击:cjs 不自动提示。
**解决方案**
尝试 CTRL + Space 强制开启。
在用户配置`setting.json`中添加如下配置项

```json
    "[markdown]": {
        "editor.quickSuggestions": true
    }
```

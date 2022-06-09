# Git 常见问题

## Git status 中文展示
在使用`git status`命令时，若文件名包含中文，可能会出现如下情况
![Git常见问题20220506142709](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%9820220506142709.png)
上图框中实际为中文。
输入如下命令解决

```sh
git config --global core.quotepath false
```
或直接在 `$HOME/.gitconfig`文件中附加
```sh
[core]
    quotepath = false
```
![Git常见问题20220506142815](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%9820220506142815.png)
## 文件名过长错误

文件名过长，报错如下：

```sh
Filename too long warning: Clone succeeded, but checkout failed.
```

输入如下命令解决

```sh
git config --system core.longpaths true
```

## 多个 git 进程

出现多个 git 进程提示，git 提交代码等操作不可用

```sh
Another git process seems to be running in this repository
```

输入如下命令解决

```sh
rm -f .git/index.lock
```

## .gitignore 无效

已有仓库添加.gitignore 无效
需要进行如下操作

```sh
git rm -r --cached .
git add .
git commit -m ".gitignore is now working”

```

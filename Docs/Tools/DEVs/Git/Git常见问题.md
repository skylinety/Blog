# Git 常见问题

## 文件名过长错误

文件名过长，报错如下：

```shell
Filename too long warning: Clone succeeded, but checkout failed.
```

输入如下命令解决

```shell
git config --system core.longpaths true
```

## 多个 git 进程

出现多个 git 进程提示，git 提交代码等操作不可用

```shell
Another git process seems to be running in this repository
```

输入如下命令解决

```shell
rm -f .git/index.lock
```

## .gitignore 无效

已有仓库添加.gitignore 无效
需要进行如下操作

```shell
git rm -r --cached .
git add .
git commit -m ".gitignore is now working”

```

# Git 常见错误

## 文件名过长错误

Filename too long warning: Clone succeeded, but checkout failed.

```shell
git config --system core.longpaths true
```

## 多个 git 进程

Another git process seems to be running in this repository

```shell
rm -f .git/index.lock
```

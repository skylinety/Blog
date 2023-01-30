# Git 常见命令

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Git 常见命令](#git-常见命令)
  - [reflog](#reflog)
  - [pull](#pull)
    - [git pull -r VS git pull](#git-pull--r-vs-git-pull)
  - [diff](#diff)
    - [--name-only](#--name-only)
  - [submodule](#submodule)
    - [submodule 概述](#submodule-概述)
    - [添加子仓库](#添加子仓库)
    - [更新子仓库](#更新子仓库)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## reflog

git reflog 用于记录本地 git 历史操作记录，包括 commit、reset、checkout 等
通过

```sh
git reflog show <branch>
# git reflog <branch>
```

查看对应分支的历史操作记录，不接 branch 时，默认为当前分支

通过 grep 搭配使用可进行很多有用操作
例如，查看当前分支基于哪个分支创建

```sh
git reflog | grep checkout
```

![Git常见命令20221206115805](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E5%91%BD%E4%BB%A420221206115805.png)

git reflog 可以查看到被删除的提交记录，对于误合并或回滚时，常可以用以查找需要找回的代码。

## pull

### git pull -r VS git pull

语法糖？

```sh
git pull = git fetch + git merge
git pull --rebase/-r = git fetch + git rebase
```

现有 git 仓库如下
![Git常见命令20220302171848](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E5%91%BD%E4%BB%A420220302171848.png)

git pull
![Git常见命令20220302172250](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E5%91%BD%E4%BB%A420220302172250.png)

git pull -r
![Git常见命令20220302172238](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E5%91%BD%E4%BB%A420220302172238.png)
git pull -r 会将当前提交的记录（E）删除并重新生成一个新的记录（R），其 HASH 值会发生变化。
看起来就像是在最近远端提交记录 D 上拉的代码，使得提交记录为一条直线。

## diff

### --name-only

--name-only 用于获取变更的文件名
git diff 仅会展示更改和删除变更的文件，**不会展示新增的文件**。
通过

```sh
git diff --name-only
```

查看当前工作区中本次变更的文件信息。其后可接版本 HASH。

## submodule

### submodule 概述

submodule 用于 git 仓库中嵌套其他仓库作为其子模块，嵌入的子模块仓库可以在其内正常进行 git 相关的操作。

### 添加子仓库

```sh
git submodule add  https://github.com/skylinety/Blog.git
```

### 更新子仓库

```sh
git submodule sync
git submodule update --init
```

或直接到子仓库目录下执行拉取等操作

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github仓库](https://github.com/skylinety/Blog)点亮⭐️。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://www.cnblogs.com/kevingrace/p/5896706.html

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh

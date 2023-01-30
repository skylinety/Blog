# Git 常见操作

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Git 常见操作](#git-常见操作)
  - [回滚](#回滚)
    - [revert](#revert)
    - [reset](#reset)
  - [git 删除分支](#git-删除分支)
    - [删除本地分支](#删除本地分支)
    - [删除远端分支](#删除远端分支)
  - [git 单列已添加到暂存区的文件](#git-单列已添加到暂存区的文件)
  - [Git 本地分支有提交，单独查看并运行远程该分支](#git-本地分支有提交单独查看并运行远程该分支)
  - [远程仓库迁移（拷贝）](#远程仓库迁移拷贝)
  - [新建仓库时关联远程与本地](#新建仓库时关联远程与本地)
  - [git 同时推送多个仓库](#git-同时推送多个仓库)
    - [git remote add](#git-remote-add)
    - [git remote set-url](#git-remote-set-url)
  - [https 方式访问 git 免输密码](#https-方式访问-git-免输密码)
  - [Git 用户配置](#git-用户配置)
    - [查看配置](#查看配置)
    - [修改全局配置](#修改全局配置)
  - [GIT SSH 免密](#git-ssh-免密)
  - [同步 Github fork 仓库](#同步-github-fork-仓库)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 回滚

### revert

```sh
git revert [commit-id]
```

revert 可将代码回滚到指定版本，但会留下一条回滚记录

### reset

git reset 一般接 --hard/soft/mixed

```sh
git reset --soft
```

- soft
  当使用 soft 时，git 会重置到对应分支，所有代码变更被保留，且代码处于已暂存状态（git add 后未 git commit 的状态）
- mixed
  reset 默认就使用 mixed 参数，git 会重置到对应分支，所有代码变更被保留，且代码处于未暂存状态（git add 后的状态）
- hard
  reset 使用 hard 参数，git 会重置到对应分支，所有代码变更被丢弃，慎用

## git 删除分支

### 删除本地分支

```sh
git branch -d <branch>
```

### 删除远端分支

```sh
git push origin --delete <branch>
```

## git 单列已添加到暂存区的文件

通过`git status`命令可以列出所有增删改的文件，并做了是否添加跟踪，是否加入暂存区的区分。
若只看加入暂存区的文件，使用

```sh
git diff --name-only --cached
```

![Git常见操作20220602161840](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C20220602161840.png)
如上图所示为某次`git status`后展示的信息。
git diff --name-only --cached 展示的信息如下
![Git常见操作20220602162017](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C20220602162017.png)
`git diff --cached`只会展示暂存区文件的变更。

## Git 本地分支有提交，单独查看并运行远程该分支

本地 dev 分支有自己 commit 的版本，想要获取远端最新代码并运行（不包括本地新 commit 代码）

```jsx
git fetch
git checkout -b test origin/dev
```

test 分支即是最新的远程 dev 副本

git fetch 将本地仓库的所有远程副本更新，但不会更新到工作空间
![Git常见操作20220302172427](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C20220302172427.png)

## 远程仓库迁移（拷贝）

```bash
git remote set-url origin <https://git.oschina.net/skylinelty/skyline-blog.git>
//或者先删除后增加
//git remote rm origin
//git remote add origin <https://git.oschina.net/skylinelty/skyline-blog.git>
git branch --set-upstream-to=origin/master master//与远程关联
git pull origin master --allow-unrelated-histories //后面参数防止出现fatal: refusing to merge unrelated histories

```

对于仓库拷贝并放在另一个仓库，至于要本地复制仓库文件夹，再进行如上操作即可。

## 新建仓库时关联远程与本地

```bash
git remote add origin <https://git.oschina.net/skylinelty/skyline-blog.git>
git add -A
git commit -m"init"
git push -u origin master

```

## git 同时推送多个仓库

当前仓库正常开发，中途需要添加另一个推送仓库
当前仓库只关联一个远程仓库，查看远端仓库信息：
`git remote -v`
结果如下
![Git常见操作20220302172709](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C20220302172709.png)

新增关联仓库常用如下两个方案：

### git remote add

```sh
git remote add origingit <https://git.citycloud.com.cn:3000/hcsg_code/xxxx.git>
```

查看远端仓库信息：
`git remote -v`
结果如下
![Git常见操作20220302173206](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C20220302173206.png)

这个地方只能是其他命名而不能是 origin 否则报错
![Git常见操作20220302173137](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C20220302173137.png)

本方案存在一个弊端，需要向远端仓库分别提交代码

```sh
git  push origin master:master
git  push origingit master:master
```

### git remote set-url

```sh
git remote set-url --add origin <https://git.citycloud.com.cn:3000/hcsg_code/xxxx.git
```

`git remote -v`
结果如下
![Git常见操作20220302175730](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C20220302175730.png)

本方案提交时，所有仓库都会同步接收，推荐使用。

## https 方式访问 git 免输密码

在 git 早期版本中，https 方式每次都要输入密码，按照如下设置即可免去烦恼

- 设置记住密码（默认 15 分钟）：
  `git config --global credential.helper cache`
- 设置时间，可以这样做：
  `git config credential.helper 'cache --timeout=3600'`
- 长期存储密码：
  - linux
    `git config --global credential.helper store`
  - mac
    `git config --global credential.helper osxkeychain`

## Git 用户配置

### 查看配置

```bash
# 查看全部配置
git config --list
#查看指定配置
git config user.name

git config user.email

```

### 修改全局配置

```sh
git config --global user.name "username"

git config --global user.email "email"
```

## GIT SSH 免密

**查看本地 SSH 密钥**

`cd ~/.sshls`
id_rsa 是私钥，id_rsa.pub 是公钥。
![Git常见操作20220302185442](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C20220302185442.png)

**创建 SSH 密钥**

如果没有相关密钥文件，需要生成

**ssh-keygen**

输入命令，生成相关文件

**复制公钥**

cat ~/.ssh/id_rsa.pub
复制对应内容

**远程仓库设置**

在 github 等远程仓库设置页面对应的 SSH keys 粘贴公钥内容

## 同步 Github fork 仓库

**配置 remote，指向原始仓库**

git remote add upstream <https://github.com/skyline.git>

**获取上游仓库分支**

获取到上游仓库分支，及相关的提交信息，它们将被保存在本地的 upstream/master，upstream/hotfix 等分支

git fetch upstream

**切换到本地的 master 分支**

git checkout master

**合并上游分支**

将 upstream/master 分支合并到本地的 master 分支，本地的 master 分支将与上游仓库保持同步，且不会丢失本地修改。

git merge upstream/master

**上传代码**

将上游仓库的代码更新到自己的远程仓库中

git push

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

文章链接：[http://www.skyline.show/Git 常见操作.html](http://www.skyline.show/Git常见操作.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

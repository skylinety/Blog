# Git 常见命令

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
--name-only用于获取变更的文件名
git diff 仅会展示更改和删除变更的文件，**不会展示新增的文件**。
通过
```sh
git diff --name-only
```
查看当前工作区中本次变更的文件信息。其后可接版本HASH。

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](http://www.skyline.show)  欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://www.cnblogs.com/kevingrace/p/5896706.html

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh

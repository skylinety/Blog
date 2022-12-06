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

已有仓库添加.gitignore 无效，或在.gitignore 中添加新的忽略无效，这是由于 git 缓存机制导致，需要移除的文件已经添加到工作区。
需要先移除后重新添加文件。

```sh
git rm -r --cached .
git add .
git commit -m ".gitignore is now working"

```

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>  

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Git常见问题.html](http://www.skyline.show/Git常见问题.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

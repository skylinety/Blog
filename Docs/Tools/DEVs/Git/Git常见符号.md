# Git 常见符号

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Git 常见符号](#git-常见符号)
  - [..](#)
    - [表示对比](#表示对比)
    - [表示连续](#表示连续)
  - [^](#-1)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## ..

### 表示对比

`git log test..master`
test 是由 master 建立的分支，在 test 进行开发多次提交完成对应功能后，切回 master 分支；
在合并 test 分支的时候，如果 master 分支在建立 test 分支之后有新的提交，则尝尝需要 rebase 进行变基让提交历史更加美观，
通过如上命令来查看 master 独有的提交（相较于 test）
如果没有直接显示'(END)'
若果有则有提交相关信息。如下图所示：

![Git常见符号20220302163532](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Git%E5%B8%B8%E8%A7%81%E7%AC%A6%E5%8F%B720220302163532.png)

### 表示连续

`git cherry-pick A..B`
表示摘取提交 A 到 B 的一系列提交（不包括 A）
要包括 A，使用如下命令
`git cherry-pick ^A..B`

## ^

表示包含开头。

`git cherry-pick A..B`
表示摘取提交 A 到 B 的一系列提交（不包括 A）
要包括 A，使用如下命令
`git cherry-pick ^A..B`

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

文章链接：[http://www.skyline.show/Git常见符号.html](http://www.skyline.show/Git常见符号.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

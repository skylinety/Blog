# VSCode 做笔记，实现自动图床到 Github

## 程序员的笔记

VSCode 编辑器的 Web 版 上线极大的方便了在 GitHub 上做笔记，在 Github 仓库主页，按一下小数点（.）这个键，或将地址栏的 com 换成 dev 即可。
在市面的大多数笔记软件中，Quiver Markdown 优化不错，但是同步基本没有，并且官方近两年没更新。Notion 用户界面比较舒适，但是基本不支持 Markdown 语法。
![PicGo20210918152058](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/PicGo20210918152058.png)

如 Quiver 一样，大多数笔记软件导出 Markdown 会将图片集中一个单独的文件，如果想要把导出的 Markdown 用在其他地方，不等不同时拷贝对应的图片的本地文件夹，将笔记中的图片放在图床中，是一个很好的处理方式。
PicGo 作为一个图床上传工具，在 VSCode 提供了对应的插件

## 相关配置

### Github

在 Github 上新建笔记仓库，拷贝用户名/仓库名 如 skylinety/blog-pics
在 Settings / Developer settings / Personal access tokens / Generate new token 初始一个 Token

### PicGO

下载 PicGo 插件
打开 VSCode 配置，搜索 PicGo 并进行如下配置
![PicGo20210918153930](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/PicGo20210918153930.png)

| 系统         | 上传剪切板图片 | 文件系统选择图片 | 输入文件地址   |
| ------------ | -------------- | ---------------- | -------------- |
| Windows/Unix | Ctrl + Alt + U | Ctrl + Alt + E   | Ctrl + Alt + O |
| MacOS        | ⌘ + Opt + U    | ⌘ + Opt + E      | ⌘ + Opt + E    |

## BMW WARNING

### NOTICE

All bucolic migrant workers must fight against capitalism together

### 参考资料

> [最适合程序员的笔记软件](https://www.ruanyifeng.com/blog/2021/08/best-note-taking-software-for-programmers.html) > [PicGo Github 图床](https://picgo.github.io/PicGo-Doc/zh/guide/config.html#github%E5%9B%BE%E5%BA%8A)

### 许可协议

> 本文作者： Skyline(lty)
> 版权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 许可协议。 转载请注明出处！

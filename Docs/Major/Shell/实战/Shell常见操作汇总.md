# Shell 常见操作汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 常见操作汇总](#shell-常见操作汇总)
  - [脚本](#脚本)
    - [获取执行脚本的位置](#获取执行脚本的位置)
    - [Shell 脚本相互调用](#shell-脚本相互调用)
    - [脚本中断与执行](#脚本中断与执行)
  - [算数命令](#算数命令)
  - [文件相关](#文件相关)
  - [判定目录或文件存在](#判定目录或文件存在)
    - [查看目录下文件夹](#查看目录下文件夹)
    - [创建嵌套文件夹并进入](#创建嵌套文件夹并进入)
  - [查看远程服务及端口是否开启](#查看远程服务及端口是否开启)
  - [设置别名](#设置别名)
    - [临时别名](#临时别名)
    - [永久生效](#永久生效)
  - [查看端口占用](#查看端口占用)
  - [删除目录下模糊匹配的文件](#删除目录下模糊匹配的文件)
    - [命令](#命令)
    - [解析](#解析)
  - [查找目录下包含指定字符的文件](#查找目录下包含指定字符的文件)
    - [命令](#命令-1)
    - [解析](#解析-1)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## 脚本

### 获取执行脚本的位置

通过`dirname "$0"`获取当前执行脚本所在位置。

- 使用 dirname

```sh
BASEDIR=$(dirname "$0")
echo $BASEDIR
# /Users/skyline/Workspace/skyline/Blog/Demos/Major/Shell
```
[示例](https://github.com/skylinety/Blog/blob/main/Demos/Major/Shell/a.sh)


### Shell 脚本相互调用

在 Shell 脚本内部调用其他 Shell 脚本，使用如下方法：

- sh
- source
- 点号(.)

使用点号和 source 的效果基本一致，等同于将其他脚本的内部内容放在当前脚本运行。
引入脚本和当前脚本执行时位于同一进程中，引入脚本可以获取到当前脚本中的变量。
sh 引入的脚本会单开一个子进程，其无法获取到当前脚本中的变量，要获取该变量，需要使用 export 导出。
有如下两个在同级目录的脚本 a 和 b
`a.sh`

```sh
a=1
echo "b is $b"
# b is
. "$BASEDIR/b.sh"
# a is 1
echo "b is $b"
# b is 2
source "$BASEDIR/b.sh"
# a is 1
sh "$BASEDIR/b.sh"
# a is
export a
sh "$BASEDIR/b.sh"
# a is 1
```

`b.sh`

```sh
echo "a is $a"
b=2
```

单独执行 a 脚本结果如下

```sh
/Users/skyline/Workspace/skyline/Blog/Demos/Major/Shell
b is
a is 1
b is 2
a is 1
a is
a is 1
```

[示例](https://github.com/skylinety/Blog/blob/main/Demos/Major/Shell/a.sh)

### 脚本中断与执行

在控制台输入没有的命令来模拟脚本执行出错

```sh
skyline
# zsh: command not found: skyline
```

命令执行出错，继续执行

```sh
skyline || true
```

命令执行出错，终止执行

```sh
skyline || exit 2
```

## 算数命令

使用 exprming

```sh
expr 1 + 1
```

```sh
plus=`expr 1 + 1`
echo $plus
# 2
minus=$(expr 1 - 1)
echo $minus
# 0
multiply=$((2 * 2))
echo $multiply
# 4
```

当()前面加上$时，表示 Command-Substitution，与`command`一致，表示其运行结果充当所在命令行的一部分.

(())内部进行算数表达式的计算。

## 文件相关

## 判定目录或文件存在

```sh

if [ -d "Docs/Major/Shell/Scripts" ]; then
    echo "目录存在"
else
    echo "目录不存在"
fi
# 目录存在

if [ -f "Docs/Major/Shell/Scripts/Shell常见操作汇总.md" ]; then
    echo "文件存在"
else
    echo "文件不存在"
fi
# 文件存在
```

类似的其他判定

| 标记 | 描述                     |
| ---- | ------------------------ |
| -L   | 文件是否为软连接         |
| -h   | 文件是否为软连接         |
| -d   | 目录判定                 |
| -w   | 文件可否写入             |
| -x   | 文件可否执行             |
| -r   | 文件可否读取             |
| -s   | 文件存在且占用空间大于 0 |

### 查看目录下文件夹

查看当前目录信息

```sh
ls -dlh /var/log
# drwxr-xr-x  47 root  wheel   1.5K Jan  6 09:22 /var/log
```

查看 src 下包含的文件夹

```sh
ls -d src/*/
```

换行形式查看当前目录下的文件夹

```sh
ls -d1 */
```

![Shell常见操作汇总20220322171654](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C%E6%B1%87%E6%80%BB20220322171654.png)

### 创建嵌套文件夹并进入

```sh
mkdir -p /home/foo/123 && cd $_
```

## 查看远程服务及端口是否开启

`telnet ip 3306`

## 设置别名

### 临时别名

`alias m="tldr"`
tldr 是一个以示例代替说明的命令使用说明工具，比自带的命令行手册易读。

### 永久生效

```bash
vim ~/.bashrc
# vim ~/.zshrc
```

在末尾行加入
`alias m="tldr"`
然后
`source ~/.bashrc`

## 查看端口占用

`netstat -apn | grep 8884`

`lsof -i:8884`

## 删除目录下模糊匹配的文件

### 命令

`find . -name "*.js" | xargs rm -rf`

### 解析

Shell 中只有部分命令支持标准输入，例如 wc、grep 等，通过管道 | 很容易将前置命令的标准输出传递给这些命令。但是部分命令不支持标准输入，例如 echo rm mkdir 等，这里需要 xargs 来提供
[xargs](https://github.com/skylinety/Blog/blob/b941cb7487a5e46cee010461e38e89fb2eb897dc/Docs/Major/Shell/Shell%E4%B8%ADxargs%E4%BD%BF%E7%94%A8.md)

## 查找目录下包含指定字符的文件

### 命令

在 Docs 目录下查找包含 find 字符的文件

```sh
ls ./ | xargs grep -rni find

find . -type f | xargs grep -rni find

grep -rni ./ -e find
```

![Shell常见操作汇总20211112174412](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C%E6%B1%87%E6%80%BB20211112174412.png)

```sh
grep -rniw ./ -e user

```

![Shell常见操作汇总20211112182828](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C%E6%B1%87%E6%80%BB20211112182828.png)

上述代码不会匹配 users

```sh
grep -rniw ./ -e user -l

```

-l --files-with-matches
只输出匹配的文件名

> Only the names of files containing selected lines are written to standard output

![Shell常见操作汇总20211112182942](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C%E6%B1%87%E6%80%BB20211112182942.png)

### 解析

grep 参数

- r 递归查找子目录文件
- n 列出行标
- i 忽略大小写
- e 搜索时启用正则匹配
- w 精确指定单词，需要为单词，英文单词前后有字母不匹配
- l 只输出匹配的文件名

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show) 欢迎访问，
文章实时更新，如果有什么错误或不严谨之处望请指出，十分感谢。
如果你觉得有用，欢迎到[Github 仓库](https://github.com/skylinety/Blog)点亮 ⭐️。

> I am a bucolic migant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

- Warrant

本文作者： Skyline(lty)

文章链接：[http://www.skyline.show/Shell 常见操作汇总.html](http://www.skyline.show/Shell常见操作汇总.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

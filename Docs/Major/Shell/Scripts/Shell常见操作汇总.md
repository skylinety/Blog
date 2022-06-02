# Shell 常见操作汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 常见操作汇总](#shell-常见操作汇总)
  - [判定目录或文件存在](#判定目录或文件存在)
  - [算数命令](#算数命令)
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
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 判定目录或文件存在

```shell

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


## 算数命令
使用exprming
```shell
expr 1 + 1
```
```shell
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



## 查看目录下文件夹

```shell
ls -d src/*/
```

查看 src 下包含的文件夹

```shell
ls -d1 */
```

换行形式查看当前目录下的文件夹
![Shell常见操作汇总20220322171654](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C%E6%B1%87%E6%80%BB20220322171654.png)

## 创建嵌套文件夹并进入

```shell
mkdir /home/foo/123 && cd $_
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

```shell
ls ./ | xargs grep -rni find

find . -type f | xargs grep -rni find

grep -rni ./ -e find
```

![Shell常见操作汇总20211112174412](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C%E6%B1%87%E6%80%BB20211112174412.png)

```shell
grep -rniw ./ -e user

```

![Shell常见操作汇总20211112182828](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E5%B8%B8%E8%A7%81%E6%93%8D%E4%BD%9C%E6%B1%87%E6%80%BB20211112182828.png)

上述代码不会匹配 users

```shell
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

### Bulletin

本文首发于 [skyline.show](skyline.show) 欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

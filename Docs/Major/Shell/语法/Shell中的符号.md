# Shell 中的符号

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 中的符号](#shell-中的符号)
  - [引号](#引号)
  - [路径符](#路径符)
  - [重定向符](#重定向符)
  - [命令执行符](#命令执行符)
  - [符号标记](#符号标记)
  - [BMW WARNING](#bmw-warning)


<!-- /code_chunk_output -->

## 引号

单引号和双引号主要可用于解决字符串中间有空格的问题。
单引号将剥夺字符串中特殊字符的含义。
双引号中的'$'进行参数替换'`'进行命令替换。
反引号与$()是一样的。 ``或者$()会将其中的语句当作命令执行一遍，再将结果充当原命令行一部分。

```sh
skyline=1
echo '$skyline`echo 1`'
# $skyline`echo 1`
echo "$skyline`echo 1`"
# 11

```

## 路径符

Shell 中路径相关的符号，如下表所示

| 符号 | 使用  | 说明               |
| ---- | ----- | ------------------ |
| ~    | cd ~  | 用户主页目录       |
| .    | ls .  | 当前目录           |
| ..   | cd .. | 上级目录           |
| /    | cd /  | 根目录或路径分隔符 |

## 重定向符

- 重定向符表

Shell 中包含输入与输出重定向相关的符号，如下表所示

| 符号 | 使用            | 说明                                               |
| ---- | --------------- | -------------------------------------------------- |
| >    | command > file  | 将 command 输出重定向到 file。                     |
| >    | n > file        | 将文件描述符为 n 的文件重定向到 file。             |
| >>   | command >> file | 将 command 输出以追加的方式重定向到 file。         |
| >>   | n >> file       | 将文件描述符为 n 的文件以追加的方式重定向到 file。 |
| >&   | n >& m          | 将输出文件 m 和 n 合并。                           |
| <    | command < file  | 将 command 输入重定向到 file。                     |
| <&   | n <& m          | 将输入文件 m 和 n 合并。                           |

- \>

定义
输出重定向
command > file 将 command 的输出重定向到 file
常见用法

```sh
echo Hello > test.txt
```

上述命令控制台不会有任何输出，Hello 文本将直接覆盖写入 test.txt

```sh
2>&1
```

2指标准错误，1指标准输出，将标准错误重定向到标准输出
将错误的信息重新定向到输出，即”2>1”，按照上面的写法，系统会将错误的信息重定向到一个名字为 1 的文件中，会有歧义，因此加&进行区分。
这里的  2  和  >  之间不可以有空格，2>  是一体的时候才表示错误输出 ​

    > /dev/null
    /dev/null 是一个特殊的文件，写入到它的内容都会被丢弃，会起到"禁止输出"的效果

- \>>

表示追加到文件末尾，而不是一个>时的覆盖

- <

输入重定向

```sh
command < file
```

将输入重定向到 file，即将 file 中的内容作为 command 的参数

## 命令执行符

- |

管道，管道的作用是提供一个通道，将上一个程序的标准输出重定向到下一个程序作为下一个程序的标准输入
管道命令只处理前一个命令正确输出，不处理错误输出。
管道右边的命令，必须能够接收标准输入的数据流命令，否则，管道后的命令将会抛弃之前的产生的结果
管道符可以连接多个命令，多个管道时，控制台输出最后一个命令的内容

- !

shell 中!叫做事件提示符，可以方便的引用历史命令，当!  后面跟随的字母不是“空格、换行、回车、=和(”时，可以做命令替换

```sh
!n
```

替换命令历史中第 n 个命令

```sh
!-n
```

替换命令历史中倒数第 n 个命令

```sh
!!
```

即!-1

```sh
!string
```

引用最近的以 string  开始的命令
注意一定是开始的位置,这条命令在你运行一个命令之后忘记了这个命令的参数是什么，直接!命令既可 ​​

```sh
!?string?
```

指向包含这个字符串 string 的命令，包含字符即可

- &

所有命令同时进行

```sh
command1 & command2 & command3
```

- &&

命令依次执行
只有前面命令执行成功，后面命令才继续执行

```sh
command1 && command2
```

- ;

命令依次执行
前面命令执行不管成功否，后面命令继续执行

```sh
command1; command2; command3
```

## 符号标记

- 符号标记表

| 符号 | 使用                          | 说明                                               |
| ---- | ----------------------------- | -------------------------------------------------- |
| <<   | << tag                        | 将开始标记 tag 和结束标记 tag 之间的内容作为输入。 |
| #    | #sth                          | 作为注释或字符剔除操作符                           |
| ?    | ls ?.js                       | 单字符通配符                                       |
| \*   | ls \*.js                      | 多字符通配符                                       |
| []   | ls [abc].js                   | 限定范围单字符通配符                               |
| \_   | `mkdir -p ~/123/456 && cd $_` | \_指定上个指令的输入参数，有其他用法不常用         |

![Shell中的符号20220322152340](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E4%B8%AD%E7%9A%84%E7%AC%A6%E5%8F%B720220322152340.png)

- ?

```sh
ls ?.js
# 会列出a.js,b.js，不会列出ab.js
```

- \*

```sh
ls *.js
# 会列出当前目录下所有.js后缀文件
```

- <<

将开始标记 tag 和结束标记 tag 之间的内容作为输入。
标记常指定为 EOF 即（End Of File)，也可指定其他字符。此符号常与 cat 一起使用

```sh
    cat <<EOF >> b.js
```

将后续输入的内容追加到 b.js 中，后续输入回车可换行，直到遇到 EOF 后退出文本编辑。
![Shell中的符号20220322165809](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Shell%E4%B8%AD%E7%9A%84%E7%AC%A6%E5%8F%B720220322165809.png)

- \#

\#常用于注释，其他用法包括
为剔除字符中的由头部开始指定字符

```sh
skyline='Skyline Liu!';
echo How-To ${skyline#Skyline}
# echo How-To ${skyline#Liu} 不会剔除Liu字符，不生效
```

指定的字符非变量开始字符为首字符（本例需要 S 开头），不起任何作用

获取字符或数组的长度

```sh
dir='/a/b/c'
echo ${#dir}
# 6
arr=(1 2 3)
echo ${#arr}
# 3
```

## BMW WARNING

- Bulletin

I am a bucolic migrant worker but I never walk backwards.

- Material

> [Shell 输入/输出重定向](https://www.runoob.com/linux/linux-shell-io-redirections.html)

- Warrant

> 本文作者： Skyline(lty)
> 版权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

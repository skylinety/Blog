# Shell 中的符号

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 中的符号](#shell-中的符号)
  - [重定向](#重定向)
    - [重定向命令汇总](#重定向命令汇总)
    - [>](#)
    - [>>](#-1)
    - [<](#-2)
  - [|](#-3)
  - [!](#-4)
  - [&](#-5)
  - [;](#-6)
  - [BMW WARNING](#bmw-warning)
    - [NOTICE](#notice)
    - [参考资料](#参考资料)
    - [许可协议](#许可协议)

<!-- /code_chunk_output -->

## 重定向

### 重定向命令汇总

Shell 中包含输入与输出重定向相关的符号，如下表所示
命令 | 说明
---| ---
command > file | 将输出重定向到 file。
command < file | 将输入重定向到 file。
command >> file | 将输出以追加的方式重定向到 file。
n > file | 将文件描述符为 n 的文件重定向到 file。
n >> file | 将文件描述符为 n 的文件以追加的方式重定向到 file。
n >& m | 将输出文件 m 和 n 合并。
n <& m | 将输入文件 m 和 n 合并。
<< tag | 将开始标记 tag 和结束标记 tag 之间的内容作为输入。

### >

    定义
        输出重定向
        command > file将输出重定向到 file
    常见用法
        2>&1
            将标准错误重定向到标准输出
            ｜ 将错误的信息重新定向到输出，即”2>1”，按照上面的写法，系统会将错误的信息重定向到一个名字为1的文件中，会有歧义，因此加&进行区分，
            ｜ 这里的 2 和 > 之间不可以有空格，2> 是一体的时候才表示错误输出​
        echo Hello > test.txt
        cat>test.js<<EOF var a = 1; console.log(a) EOF
        ｜ ​​<<EOF 表示当遇到EOF时结束输入​​​
        ｜
        ｜ cat>test.js<<EOF
        ｜ var a = 1;
        ｜ console.log(a)​
        ｜ EOF​​
        > /dev/null
        ｜ /dev/null 是一个特殊的文件，写入到它的内容都会被丢弃，会起到"禁止输出"的效果

### >>

        表示追加到文件末尾，而不是一个>时的覆盖

### <

    定义
        输入重定向
        command < file将输入重定向到 file

## |

    定义
        管道，管道的作用是提供一个通道，将上一个程序的标准输出重定向到下一个程序作为下一个程序的标准输入
    注意
        管道命令只处理前一个命令正确输出，不处理错误输出。
        管道右边的命令，必须能够接收标准输入的数据流命令，否则，管道后的命令将会抛弃之前的产生的结果
        管道符可以连接多个命令，多个管道时，控制台输出最后一个命令的内容

## !

    定义
        shell 中!叫做事件提示符，可以方便的引用历史命令，当! 后面跟随的字母不是“空格、换行、回车、=和(”时，可以做命令替换
    使用
        !n
            替换命令历史中第n个命令
        !-n
            替换命令历史中倒数第n个命令
        !!
            即!-1
        !string
            引用最近的以 string 开始的命令
            ｜ 注意一定是开始的位置,这条命令在你运行一个命令之后忘记了这个命令的参数是什么，直接!命令既可​​
        !?string?
            指向包含这个字符串的命令
            ｜ 包含即可

## &

    定义
        所有命令同时进行
    使用
        command1 & command2 & command3
    &&
        命令依次执行
        ｜ 只有前面命令执行成功，后面命令才继续执行
        使用
            command1 && command2

## ;

    定义
        命令依次执行
        ｜ 前面命令执行不管成功否，后面命令继续执行
        使用
            command1; command2; command3

## BMW WARNING

### NOTICE

All bucolic migrant workers must fight against capitalism together

### 参考资料

> [Shell 输入/输出重定向](https://www.runoob.com/linux/linux-shell-io-redirections.html)

### 许可协议

> 本文作者： Skyline(lty)
> 版权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 许可协议。 转载请注明出处！

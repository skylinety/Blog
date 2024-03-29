# Shell 条件判定

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 条件判定](#shell-条件判定)
  - [if](#if)
    - [基本语法](#基本语法)
    - [条件包裹括号](#条件包裹括号)
    - [常见判定条件](#常见判定条件)
  - [三元](#三元)
  - [BMW WARNING](#bmw-warning)

<!-- /code_chunk_output -->

## if

### 基本语法

```sh
if 条件; then
    命令
elif 条件; then
    命令
else
    命令
fi
```

其中条件的包裹括号可以有多种方式，每种方式对应的效果不一致

### 条件包裹括号

- command

if 后直接接条件无任何括号包裹。
表示验证**命令**是否成功执行。
[代码源文件](https://github.com/skylinety/Blog/blob/main/Demos/Major/Shell/condition.sh)
如下对于本文后续所有类似代码，首先执行

```sh
read -p "Enter first string: " VAR1
read -p "Enter second string: " VAR2
```

并进行两次相同输入后。

```sh
if "$VAR1" == "$VAR2"; then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi
# 1: command not found
# Strings are not equal.
```

if 后不跟包裹符号时，需要跟可执行命令而不是表达式。
若命令执行成功，则执行 then，否则执行 else

```sh
if echo Skyline; then
    echo "echo Skyline."
else
    echo "Something wrong."
fi
# Skyline
# echo Skyline
```

- [expression]

if 后接`[]`包裹的条件
表示验证**条件表达式**是否成立，进行条件判定。
[Bash-Conditional-Expressions](http://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions)

```sh

if [ "$VAR1" == "$VAR2" ]; then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi
# Strings are equal.
```

- [[expression]]

if 后接`[[]]`包裹的条件
`[[]]`是`[]`的升级版本。

```sh
if [[ "$VAR1" == "$VAR2" ]]; then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi
# Strings are equal.
```

[[]]内部支持更多的表达式语法。

```sh
# 检查文件是否为符号链接
[[ -L $file && -f $file ]]
[ -L "$file" ] && [ -f "$file" ]
```

- (command)

if 后接`()`包裹的条件。
表示验证子命令是否成功执行。
()其内部不是表达式而是可执行命令，表示在 subshell 跑 command 命令，可以理解为单开进程执行跟主程序无关的其他命令。

```sh
if ("$VAR1" == "$VAR2"); then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi
# 依次输入1回车，1回车，结果为：
# 1: command not found
# Strings are not equal.
```

上述代码中，()内部内容被当做可执行命令执行，故报错，转到 else 执行。
()内部命令执行成功，则才会转到 then 执行。

```sh
if (echo Skyline); then
    echo "echo Skyline."
else
    echo "Something wrong."
fi
```

()内执行的命令结果，不会对父 shell 运行结果 造成影响。

```sh
skyline=1; (skyline=2);
echo $skyline
# 1
```

当()前面加上$时，表示 Command-Substitution，与`command`一致，表示其运行结果充当所在命令行的一部分

```sh
echo 'skyline'| cut -c`echo 2`-3
# ky
echo 'skyline'| cut -c$(echo 2)-3
# ky
```

- ((expression))

if 后接`(())`包裹的条件。
表示内部**算数表达式**的计算。
(())内部进行算数表达式的计算。
算数表达式可包含常见的一元二元运算符，逻辑运算符等。

```sh
if (("$VAR1" == "$VAR2")); then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi
# Strings are equal.
if ((1+1 > 1)); then
    echo "True"
else
    echo "False"
fi
# True
```

[Shell-Arithmetic](http://www.gnu.org/software/bash/manual/bash.html#Shell-Arithmetic)
当(())前面加上$时，表示得到的算数结果充当所在命令行的一部分.

```sh
echo 'skyline'| cut -c$((1 + 1))-3
# ky
```

上述代码实现的效果可以使用 expr 实现

```sh
echo 'skyline'| cut -c$(expr 1 + 1)-3
# ky
```

注意，expr 通常与``一起使用，或与$()使用，注意 expr 中空格的使用，否则报错
也可使用 let 来实现计算

```sh
start=1
let start+=1
echo $start
echo 'skyline'| cut -c$start-3
```

### 常见判定条件

- 文件相关

| 参数    | 含义                            |
| ------- | ------------------------------- |
| -a FILE | 文件存在                        |
| -d FILE | 文件存在且为文件夹(directory)   |
| -e FILE | 文件存在                        |
| -f FILE | 文件存在且为常规文件(file)      |
| -g FILE | 文件存在 SGID 已设置(SGID)      |
| -L FILE | 文件存在且为软连接(symbol link) |
| -r FILE | 文件存在且可读(readable)        |
| -w FILE | 文件存在且可写(writeable)       |
| -x FILE | 文件存在且可执行(executable)    |

- 字符相关

| 参数               | 含义         |
| ------------------ | ------------ |
| STRING1 == STRING2 | 字符判等     |
| STRING1 != STRING2 | 字符非等     |
| STRING1 > STRING2  | 字符排序在前 |
| STRING1 < STRING2  | 字符排序在后 |
| -n STRING          | 字符非空     |
| -z STRING          | 字符为空     |
| STRING =~ REGEXP   | 正则匹配判定 |

- 数字相关

| 参数                | 含义                           |
| ------------------- | ------------------------------ |
| NUMBER1 -eq NUMBER2 | 数字判等(equal)                |
| NUMBER1 -ne NUMBER2 | 数字非等 (not equal)           |
| NUMBER1 -gt NUMBER2 | 数字大于(greater than)         |
| NUMBER1 -ge NUMBER2 | 数字大于等于(greater or equal) |
| NUMBER1 -lt NUMBER2 | 数字小于(less than)            |
| NUMBER1 -le NUMBER2 | 数字小于等于(less or equal)    |
| NUMBER =~ REGEXP    | 正则匹配判定                   |

## 三元

```sh
test "$VAR1" == "$VAR2" && echo "Strings are equal." || echo "Strings are not equal."
```

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

文章链接：[http://www.skyline.show/Shell 条件判定.html](http://www.skyline.show/Shell条件判定.html)

授权声明： 本博客所有文章除特别声明外， 均采用 [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh) 协议。 转载请注明出处！

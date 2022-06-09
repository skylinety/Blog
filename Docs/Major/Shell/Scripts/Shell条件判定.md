# Shell 条件判定

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Shell 条件判定](#shell-条件判定)
  - [if](#if)
    - [command](#command)
    - [[expression]](#expression)
    - [[[expression]]](#expression-1)
    - [(command)](#command-1)
    - [((expression))](#expression-2)
  - [三元](#三元)

<!-- /code_chunk_output -->

## if

### command

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

### [expression]

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

### [[expression]]

[]的升级版本，

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

### (command)

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

### ((expression))

表示验证**算数表达式**是否成立。
(())内部进行算数表达式的计算。
算数表达式包含常见的一元二元运算符，逻辑运算符等。

```sh
if (("$VAR1" == "$VAR2")); then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi
# Strings are equal.
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

注意，expr 通常与``一起使用，或与$()使用，注意expr中空格的使用，否则报错
也可使用 let 来实现计算

```sh
start=1
let start+=1
echo $start
echo 'skyline'| cut -c$start-3
```

## 三元

```sh
test "$VAR1" == "$VAR2" && echo "Strings are equal." || echo "Strings are not equal."
```

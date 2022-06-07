#! /bin/bash
read -p "Enter first string: " VAR1
read -p "Enter second string: " VAR2

echo 'if'
if "$VAR1" == "$VAR2"; then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi

if echo Skyline; then
    echo "echo Skyline."
else
    echo "Something wrong."
fi

echo 'if [[]]'
if [[ "$VAR1" == "$VAR2" ]]; then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi

echo 'if []'
if [ "$VAR1" == "$VAR2" ]; then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi

echo 'if (())'
if (("$VAR1" == "$VAR2")); then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi

echo 'if ()'
# ()是指subshell，其内部不是表达式而是可执行命令，可以理解为单开进程执行其他命令，不会对父shell造成影响
# 当()前面加上$时，表示Command-Substitution，与`command`一致，表示其运行结果为所在命令行的一部分
if ("$VAR1" == "$VAR2"); then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi

if (echo Skyline); then
    echo "echo Skyline."
else
    echo "Something wrong."
fi

start=1
let start+=1
echo $start
echo 'skyline' | cut -c$start-3

echo '&& ||'
test "$VAR1" == "$VAR2" && echo "Strings are equal." || echo "Strings are not equal."

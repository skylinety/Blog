# Shell 中数字相关操作

## 判断是否为数字

### 使用正则

```sh
re='^[+-]?[0-9]+([.][0-9]+)?$'
num=1.1
if ! [[ $num =~ $re ]] ; then
  echo false
else
  echo True
fi
# True
```

### 使用-eq

-eq 在 Shell 中通常只用于对数字表达式判定，用与其他表达式会报错

```sh
#!/bin/bash

if [ 'a' -eq 'a' ]; then
    echo "True"
else
    echo "False"
fi
#  a: integer expression expected
# False

if [[ 'a' -eq 'a' ]]; then
    echo "True"
else
    echo "False"
fi
# True
if [ 'a' == 'a'  ]; then
    echo "True"
else
    echo "False"
fi
# True

if [ '1.1' -eq '1.1'  ]; then
    echo "True"
else
    echo "False"
fi
# 1.1: integer expression expected
# False

if [ '1' -eq '1'  ]; then
    echo "True"
else
    echo "False"
fi
# True

```

`[ "$num" -eq "$num" ]` 中如果是非整数字符对比会报错，利用这一点，可以使用如下方式来判定是否为**整数**
需要注意的是，`[[]]`在`[]`基础上做了扩展，不能用为`[[ "$num" -eq "$num" ]]`，`[[]]`可以将-eq 等符号用于字符对比判定，如上例中第二个判定。
判定是抛出的异常需要使用`2>/dev/null`隐藏掉。

```sh
if [-n "$num"] && [ "$num" -eq "$num"  ] 2>/dev/null; then
    echo "True"
else
    echo "False"
fi
```

[示例](https://github.com/skylinety/Blog/blob/main/Demos/Major/Shell/num.sh)

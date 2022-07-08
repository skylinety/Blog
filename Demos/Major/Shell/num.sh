#!/bin/bash
if [ 'a' -eq 'a' ]; then
    echo "True"
else
    echo "False"
fi

if [[ 'a' -eq 'a' ]]; then
    echo "True"
else
    echo "False"
fi

if [ 'a' == 'a' ]; then
    echo "True"
else
    echo "False"
fi

if [ '1.1' -eq '1.1' ]; then
    echo "True"
else
    echo "False"
fi

if [ '-1' -eq '-1' ]; then
    echo "True"
else
    echo "False"
fi

re='^[+-]?[0-9]+([.][0-9]+)?$'
num=1.1
if ! [[ $num =~ $re ]]; then
    echo false
else
    echo True
fi

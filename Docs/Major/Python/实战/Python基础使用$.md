# Python 基础使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Python 基础使用](#python-基础使用)
  - [多版本切换](#多版本切换)
    - [pyenv 安装](#pyenv-安装)
    - [常见问题](#常见问题)

<!-- /code_chunk_output -->

## 多版本切换

### pyenv 安装

首先安装 Homebrew

安装版本切换工具 pyenv

安装

```sh
brew update
brew install pyenv
pyenv -v
```

可安装版本列表

```sh
pyenv install --list
```

安装指定版本

```sh
pyenv install <version>
# pyenv install 3.6.6
```

查看已安装版本

```sh
pyenv versions
```

全局切换版本

```sh
pyenv global <version>
```

指定目录切换版本

```sh
# cd ~/
pyenv local <version>
```

查看 pyenv 所有命令

```sh
pyenv commands
```

执行安装时，可能会卡下载

```sh
python-build: use openssl@1.1 from homebrew
python-build: use readline from homebrew
Downloading Python-3.7.8.tar.xz...
-> https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tar.xz
```

这是由于官方镜像非常地慢。

解决方法是
去阿里对应镜像http://npm.taobao.org/mirrors/python/下载对应版本python
然后创建包文件夹

```sh
mkdir -p ~/.pyenv/cache
```

将下载文件放到该文件夹下，然后执行

```sh
pyenv install <version>
```

### 常见问题

- sendfile invalid

若出现错误

```sh
./Modules/posixmodule.c:8210:15: error: implicit declaration of function 'sendfile' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
ret = sendfile(in, out, offset, &sbytes, &sf, flags);
```

执行

```sh
CFLAGS=-Wno-implicit-function-declaration pyenv install 3.6.6
```

- MacOS 切换失效

在 MacOS 通过 pyenv versions 查看显示切换了版本（\*对应版本）

```sh
pyenv versions
# system
# * 3.6.6 (set by /Users/skyline/.pyenv/version)
```

但直接查看版本仍旧是原版本

```sh
python3 --version
# Python 3.9.5
```

版本切换失效，需要将如下配置添加到终端配置文件中
打开配置文件

```sh
vim ~/.zshrc
# vi ~/.bashrc
```

底部插入如下行

```sh
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/shims:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
 eval "$(pyenv init -)"
fi
```

保存生效

```sh
source  ~/.zshrc
```

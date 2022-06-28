# Flutter 基础控件使用

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Flutter 基础控件使用](#flutter-基础控件使用)
  - [GestureDetector](#gesturedetector)
    - [基础事件](#基础事件)
  - [FloatingActionButton](#floatingactionbutton)
    - [简述](#简述)
    - [效果](#效果)
  - [persistentFooterButtons](#persistentfooterbuttons)
    - [简述](#简述-1)
    - [代码](#代码)
    - [效果](#效果-1)
  - [ListTile](#listtile)
    - [padding 调整](#padding-调整)
  - [BMW WARNING](#bmw-warning)


<!-- /code_chunk_output -->

## GestureDetector

### 基础事件

- onTap
- onTapDown
- onTapUp
- onLongPress
- onLongPressUp
- onLongPressDown
- onDoubleTap

## FloatingActionButton

### 简述

FloatingActionButton 简称 FAB ,可以实现浮动按钮，也可以实现类似闲鱼 app 的底部凸起导航

```js
floatingActionButton: FloatingActionButton(
          onPressed: () {
            setState(() {
              _controller.value.isPlaying
                  ? _controller.pause()
                  : _controller.play();
            });
          },
          child:Icon(
            _controller.value.isPlaying ? Icons.pause : Icons.play_arrow,
          ),
        ),
```

### 效果

![基础控件使用20210922103249](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/%E5%9F%BA%E7%A1%80%E6%8E%A7%E4%BB%B6%E4%BD%BF%E7%94%A820210922103249.png)

## persistentFooterButtons

### 简述

固定显示在下放的组件

### 代码

```jsx
persistentFooterButtons: <Widget>[
          IconButton(icon: Icon(
            _controller.value.isPlaying ? Icons.pause : Icons.play_arrow,
          ), onPressed: () {
            setState(() {
              _controller.value.isPlaying
                  ? _controller.pause()
                  : _controller.play();
            });
          }),
          IconButton(icon: Icon(Icons.cancel), onPressed: () {
             Navigator.of(context).maybePop();
          }),
        ],
```

### 效果

![基础控件使用20210922103315](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/%E5%9F%BA%E7%A1%80%E6%8E%A7%E4%BB%B6%E4%BD%BF%E7%94%A820210922103315.png)

## ListTile

### padding 调整

## BMW WARNING

- Bulletin

I am a bucolic migrant worker but I never walk backwards.

- Material

>

- Warrant

> 本文作者： Skyline(lty)
> 版权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

# Flutter 基础使用汇总

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Flutter 基础使用汇总](#flutter-基础使用汇总)
  - [Flutter 监听返回按键](#flutter-监听返回按键)
  - [Flutter 防止屏幕翻转](#flutter-防止屏幕翻转)
  - [BMW WARNING](#bmw-warning)
    - [NOTICE](#notice)
    - [参考资料](#参考资料)
    - [许可协议](#许可协议)

<!-- /code_chunk_output -->

## Flutter 监听返回按键

通过 WillPopScope 组件来注册监听回调

```jsx
Widget build(BuildContext context) {
  return WillPopScope(
      onWillPop: _requestPop,
      child: Scaffold(
        appBar: AppBar(
          title: Text('测试代码'),
          leading: IconButton(
            icon: Icon(Icons.arrow_back),
            onPressed: () {
              print("退出${Navigator.canPop(context)}");
              if (Navigator.canPop(context)) {
                Navigator.pop(context);
              } else {
                SystemNavigator.pop();
              }
            },
          ),
        ),
       ),
    );
   }

Future<bool> _requestPop() {
    print("POP");
    if (Navigator.canPop(context)) {
      Navigator.pop(context);
    } else {
      SystemNavigator.pop();
    }
    return Future.value(false);
  }
```

## Flutter 防止屏幕翻转

在 main.dart 入口中加入如下代码

```jsx
void main() {
  HttpOverrides.global = new MyHttpOverrides();
  // runApp(MyApp());
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp])
      .then((_) {
        runApp(new MyApp());
  });
}
```

## BMW WARNING

### Bulletin

I am a bucolic migrant worker but I never walk backwards.

### 参考资料

>

### 许可协议

> 本文作者： Skyline(lty)
> 版权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 许可协议。 转载请注明出处！

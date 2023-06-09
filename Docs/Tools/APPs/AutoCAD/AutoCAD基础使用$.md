# AutoCAD基础使用

## 操作


### PDF导出

打印可以通过File选项卡下的打印选项
![AutoCAD基础使用$20230609105936](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609105936.png)
可以直接使用快捷键 `⌘ + P`


![AutoCAD基础使用$20230609112548](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609112548.png)

默认直接导出是空白的，并不是文件中的全部内容，需要点击选择窗口图标选择需要导出的内容

![AutoCAD基础使用$20230609120256](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609120256.png)

## 命令

### 汇总

AutoCAD的命令可以直接键盘输入，也可以在页面最下方的命令输入框输入。
当命令输入完成，选择需要操作的对象后，直接空格键回车确认，进行命令对应的操作。

| 动作 | 命令 | 说明                 |
| ---- | ---- | -------------------- |
| 移动 | Move | 用于选中多文件的移动 |

### 移动

对于直线或普通图形，选择中心点拖动即可移动。
![AutoCAD基础使用$20230609113323](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609113323.png)
对于多文件的移动，首先选中多文件，然后键盘直接输入move命令。
![AutoCAD基础使用$20230609113421](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609113421.png)

### 旋转
3D旋转使用ROTATE3D命令，先选中要旋转的对象
![AutoCAD基础使用$20230609115105](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609115105.png)
使用时，需要指定旋转轴，
![AutoCAD基础使用$20230609115733](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609115733.png)
然后制定旋转度数
![AutoCAD基础使用$20230609115417](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609115417.png)
旋转结果如下：
![AutoCAD基础使用$20230609115610](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609115610.png)
2D旋转使用同理，命令为ROTATE

### 偏移
将一个对象偏移生成新的对象，使用OFFSET命令
![AutoCAD基础使用$20230609170554](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609170554.png)

对于闭合的图形，偏移以中心点进行

![AutoCAD基础使用$20230609170734](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609170734.png)

要便宜多个，按下M键回车确定
![AutoCAD基础使用$20230609174820](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609174820.png)

效果如下：
![AutoCAD基础使用$20230609174811](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609174811.png)

### 位移（复制）

使用COPY(DUPLICATE)进行位移(复制)
输入COPY后选择对象，回车确认，
![AutoCAD基础使用$20230609175548](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609175548.png)
然后指定位移基点
![AutoCAD基础使用$20230609175505](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609175505.png)
### 断点

将一条线段断成两条，使用BREAKATPOINT命令
输入BREAKATPOINT命令回车，然后鼠标移动到端点绿框上，
![AutoCAD基础使用$20230609182050](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609182050.png)

移动鼠标选择断点处断点
![AutoCAD基础使用$20230609181932](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609181932.png)

断点后线条如下
![AutoCAD基础使用$20230609182201](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609182201.png)
### 断线

打断线条使用BREAK命令
输入BREAK命令回车，然后输入F回车以选择第一个点
![AutoCAD基础使用$20230609181440](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609181440.png)
鼠标移动到端点绿框上，
然后再移动选第一个点
![AutoCAD基础使用$20230609181332](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609181332.png)
鼠标移动到端点处绿框上，
![AutoCAD基础使用$20230609181619](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609181619.png)
然后再移动选第二个点
![AutoCAD基础使用$20230609181748](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609181748.png)
空格确认即可
### 分解

将一个图形对象的线条分解，使用EXPLODE命令
![AutoCAD基础使用$20230609142154](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609142154.png)
分解后如下
![AutoCAD基础使用$20230609142146](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609142146.png)
### 相似选择

快速选中相似的内容，使用SELECTSIMLIAR命令

![AutoCAD基础使用$20230609140620](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609140620.png)

选中其中一个对象
![AutoCAD基础使用$20230609140741](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609140741.png)

单击空格键即可选中全部相似的对象。
![AutoCAD基础使用$20230609140728](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609140728.png)
### 线段截取

### 线段修剪

要修剪如下红旗多余的线段
![AutoCAD基础使用$20230609120645](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609120645.png)

使用TRIM命令
![AutoCAD基础使用$20230609120722](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609120722.png)

移动鼠标到“枝丫”处进行裁剪

![AutoCAD基础使用$20230609120921](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609120921.png)

### 线段延长

延长使用的也是TRIM命令，在剪枝时按住SHIFT键就会延长

![AutoCAD基础使用$20230609172929](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609172929.png)
### 多选
连续单击多个对象可以多选，
也可以鼠标左键单击空白区域可以进行矩形选框选择，鼠标左键初始单击点为起始点。
![AutoCAD基础使用$20230609112804](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609112804.png)

也可以长按鼠标左键，鼠标滑过区域的内容会被选中。

![AutoCAD基础使用$20230609113006](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609113006.png)

也可以使用SELECT命令来选择多个对象

![AutoCAD基础使用$20230609142615](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609142615.png)

选择时如下
![AutoCAD基础使用$20230609142650](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609142650.png)

## 画图
### 画圆角

首先使用FILLET命令
![AutoCAD基础使用$20230609173903](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609173903.png)

选中第一个对象，输入r回车
![AutoCAD基础使用$20230609174014](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609174014.png)

输入圆角半径回车

![AutoCAD基础使用$20230609174046](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/AutoCAD%E5%9F%BA%E7%A1%80%E4%BD%BF%E7%94%A8%2420230609174046.png)
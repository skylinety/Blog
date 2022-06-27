# 硬盘 MR 技术

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [硬盘 MR 技术](#硬盘-mr-技术)
  - [硬盘原理简述](#硬盘原理简述)
  - [MR](#mr)
    - [LMR](#lmr)
    - [PMR](#pmr)
    - [CMR](#cmr)
    - [SMR](#smr)
    - [CMR vs SMR](#cmr-vs-smr)
  - [SMR 优势与弊端](#smr-优势与弊端)
  - [BMW WARNING](#bmw-warning)
    - [Bulletin](#bulletin)
    - [Material](#material)
    - [Warrant](#warrant)

<!-- /code_chunk_output -->

## 硬盘原理简述

硬盘通过小磁体来记录信息。
硬盘通过写磁头翻转磁体来对应二进制。如南北朝向的磁体可能意味着 1，那么北南朝向的磁体意味着 0。

## MR

### LMR

Longitudinal Magnetic Recording
机械硬盘的磁录密度影响着数据记录的总量（硬盘容量）。
早期的硬盘采用的是水平磁记录，如下图所示。
![硬盘20211117203703](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/%E7%A1%AC%E7%9B%9820211117203703.png)
这种单个磁体水平放置的方式总的容量空间较小。

### PMR

Perpendicular Magnetic Recording (PMR)
perpendicular 意为垂直的，垂直。
之后的磁体被立起来，如下，这种方式不会影响数据的存取，同时可以获得更多的容量。
![硬盘20211117205112](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/%E7%A1%AC%E7%9B%9820211117205112.png)
PMR 目前为止有两种分支，为 CMR 与 SMR。
SMR 沿用原先的 PMR 的技术，并进一步对磁录密度进行优化。
由于 SMR 也基于 PMR 技术，其中的磁体保持垂直，原有技术继续使用 PMR 名词容易造成混淆。
故将原有 PMR 技术另命名为 CMR。
但是沿用之前的习惯，CMR 也通常被称作 PMR。
故一般 PMR 即指 CMR，新分支就称为 SMR

### CMR

Conventional Magnetic Recording
conventional 传统的，惯例的
由于写磁头比磁道要宽，CMR 在磁道之间加入磁道保护区来防止相邻磁道的写覆盖。

### SMR

Shingled Magnetic Recording (PMR)
Shingled 叠瓦的
叠瓦进一步增加磁录密度，将原有的相邻磁道保护区取消。
将多个磁道进行分区，每个区之间设立保护区。
同时，新磁道写入数据时，会对相邻磁道部分宽度进行写覆盖。
被覆盖的磁道只留下下图蓝色部分的宽度供读磁头（写磁头更窄）读取数据。
![硬盘20211118103524](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/%E7%A1%AC%E7%9B%9820211118103524.png)

### CMR vs SMR

![硬盘20211118103205](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/%E7%A1%AC%E7%9B%9820211118103205.png)
一个比较形象但不是很恰当的例子就是传统的瓦房。
相同房屋的屋顶面积固定，盖房顶时，这些瓦的总面积就是总容量
明显，将瓦片叠在一起用的瓦相比于一片片拼接在一起更多。
故叠瓦获取的总容量更大。

## SMR 优势与弊端

SMR 让厂家可以用同样的成本造出更大容量的硬盘。
当下各大厂新出的硬盘很多采用 SMR 技术，这样的硬盘一般更为便宜。
相比于 CMR，相同容量下的 SMR 更加轻薄，价格更有优势。
同时，SMR 存在以下弊端。
由于叠瓦问题，相同磁片分区的数据需要按照磁道顺序写入。
如果要修改某个磁体的信息，由于修改会影响相邻磁道的读区域（信息存放），故需要将后一磁道的信息全部重新录入，进而整个分区的后续磁道信息都需要重新录入。
这就是为什么 SMR 写数据慢的原因，其后台可能在重写成倍的数据。
这同时也造成了 SMR 寿命比不过 CMR.

## BMW WARNING

- Bulletin

本文首发于 [skyline.show](http://www.skyline.show)  欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

- Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

> https://blag.nullteilerfrei.de/2018/05/31/pmr-smr-cmr-i-just-want-a-hdd-mr/ > https://zonedstorage.io/introduction/smr/

- Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh)

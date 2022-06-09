# Charles 抓取 Https 包

## 抓基础包

### Mac 配置

查看或配置 Mac 代理端口
Proxy > Proxy Settings > Port
![Charles抓取Https包20220221153215](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Charles%E6%8A%93%E5%8F%96Https%E5%8C%8520220221153215.png)

### 手机端配置

连接 Mac 统一网络，点击网络后的 i 图标，在 配置代理时选择手动，查看 Mac 地址，并将 Mac 端的配置填入
![Charles抓取Https包20220221153008](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Charles%E6%8A%93%E5%8F%96Https%E5%8C%8520220221153008.png)

## Https 抓包

### SSL 代理配置

在上述配置后，可以抓取基本的 Http 包，但是 Https 包抓下来为 unknow
需要进一步配置。
在 Proxy > SSL Proxiyng Settings 进行如下配置，也可以指定固定的 IP
Https 协议的端口是 443 这里是把所有的网站的 Https 请求都设置进去
![Charles抓取Https包20220302205833](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Charles%E6%8A%93%E5%8F%96Https%E5%8C%8520220302205833.png)
配置完成后如下
![Charles抓取Https包20220221153623](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Charles%E6%8A%93%E5%8F%96Https%E5%8C%8520220221153623.png)

### Mac 安装证书

先在 Help > SSL Proxying > Install Charles Root Certificate 安装证书到电脑。
如果安装后证书未被信任，图标如下
![Charles抓取Https包20220221154140](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Charles%E6%8A%93%E5%8F%96Https%E5%8C%8520220221154140.png)，
则需要双击证书在信任栏进行信任。
![Charles抓取Https包20220221154226](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Charles%E6%8A%93%E5%8F%96Https%E5%8C%8520220221154226.png)

然后在 Proxy > Proxy Settings > Proxies, 勾选 Enable transparent HTTP proxying

### 手机安装证书

在 help–>SSLProxying–> Install Charles Root Ceriticate on a Mobile Device or Remote Browser
根据弹窗描述用手机打开对应网址下载证书文件
一般地址为 chls.pro/ssl

安装完成后
在手机（IOS）上打开 设置 > 通用> 关于本机 > 证书信任设置 > 信任证书
将安装的证书信任，之后就可以进行 Https 抓包。

## BMW WARNING

### Bulletin

本文首发于 [skyline.show](http://www.skyline.show)  欢迎访问。

> I am a bucolic migrant worker but I never walk backwards.

### Material

参考资料如下列出，部分引用可能遗漏或不可考，侵删。

>

### Warrant

本文作者： Skyline(lty)
授权声明： 本博客所有文章除特别声明外， 均采用 CC BY - NC - SA 3.0 协议。 转载请注明出处！

> [CC BY - NC - SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/deed.zh

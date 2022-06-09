# Nginx 开启简单的文件下载服务

## 配置

将如下配置加入 nginx.conf 中 或在 app.d 等模块下目录中新建 server.test.conf 文件。
注意 nginx.conf 文件中需要在 http 中有如下类似配置

```sh
include app.d/server.*.conf;
```

具体配置如下

```sh
server {
        listen       8443;
        server_name  localhost;
        root    /volume1/web/blog;
        index   index.html index.php index.cgi;
        location ^~ /file {
            alias /volume1/web/blog/;
            index index.html;           # 如果文件存放目录有 index.html，会跳转到 index.html；
            autoindex on;               # 自动列出目录下的文件；
            autoindex_exact_size off;   # 文件大小按 G、M 的格式显示，而不是 Bytes；
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/share/nginx/html;
        }
}
```
重启nginx
```sh
nginx -s reload
```
浏览器访问，效果如下：
![Nginx开启简单的文件下载服务20220124152153](https://raw.githubusercontent.com/skylinety/blog-pics/master/imgs/Nginx%E5%BC%80%E5%90%AF%E7%AE%80%E5%8D%95%E7%9A%84%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E6%9C%8D%E5%8A%A120220124152153.png)

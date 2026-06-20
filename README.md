# 菜鸟教程

通过脚本将菜鸟教程的单个教程内容保存到本地，便于离线阅读

## 快速开始

安装依赖

```shell
python3 -m venv venv
source ./venv/bin/active
pip install -r requirements.txt
```

下载一个教程

用法：任意找一个教程的页面传入即可，会下载整个集合

```shell
python3 cainiao_web/crawler.py <url>
```

示例： 下载 汇编语言

```shell
python3 cainiao_web/crawler.py 'https://www.runoob.com/assembly/assembly-tutorial.html'
```

启动网页服务

```shell
python3 -m http.server 8080  -d ./html
```

访问：http://127.0.0.1:8080/assembly/

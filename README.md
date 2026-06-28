# 菜鸟教程

总所周知，菜鸟教程的质量很好，我会经常去学习

有时候没有网络，也想离线查看文档就很不方便，于是这个脚本就诞生了

通过脚本将菜鸟教程的单个教程内容保存到本地，便于离线阅读

## 快速开始

安装依赖

```shell
python3 --version
Python 3.12.6

python3 -m venv venv
source ./venv/bin/active
pip install -r requirements.txt
```

## 下载教程

用法：任意找一个教程的页面传入即可，会下载整个集合

```shell
python3 crawler.py <url>
```

示例： 下载 汇编语言

```shell
python3 crawler.py 'https://www.runoob.com/assembly/assembly-tutorial.html'
```

启动网页服务

```shell
python3 -m http.server 8080  -d ./html
```

访问：http://127.0.0.1:8080/assembly/

## 转为markdown

将html转为markdown文件

```shell
# htmltomd.py
# 修改需要转换的目录
DIR_NAME = "assembly"
```

转换

```shell
python3 htmltomd.py
```

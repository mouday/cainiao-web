import os
import urllib
from parsel import Selector
import requests

RUNTIME_DIR = os.getcwd()
HTML_DIR = os.path.join(RUNTIME_DIR, 'html')

BASE_URL = 'https://www.runoob.com/'

def get_filename(url):
    parse_res = urllib.parse.urlparse(url)
    dirname = os.path.dirname(parse_res.path)
    filename = os.path.basename(parse_res.path)
    filedir = HTML_DIR + dirname
    os.makedirs(filedir, exist_ok=True)
    fullname = os.path.join(filedir, filename)
    return fullname


def save_html(url):
    print("url", url)
    fullname = get_filename(url)
    if os.path.exists(fullname):
        return

    res = requests.get(url)
    res.raise_for_status()

    content = res.text
    content = content.replace('https://www.runoob.com', '')
    content = content.replace('https://static.char123.com', '')
    content = content.replace('https://static.jyshare.com', '')

    with open(fullname, 'w', encoding='utf-8') as f:
        f.write(content)

    save_static(res.text)


def save_url(url):
    print("url", url)
    fullname = get_filename(url)
    if os.path.exists(fullname):
        return

    res = requests.get(url)
    res.raise_for_status()

    if res.headers['Content-Type'] == 'image/png':
        with open(fullname, 'wb') as f:
            f.write(res.content)
    else:
        with open(fullname, 'w', encoding='utf-8') as f:
            f.write(res.text)


def save_static(content):
    selector = Selector(text=content)

    # js
    for li in selector.css('script'):
        src = li.css('::attr(src)').get()
        if src:
            print(src)
            src = urllib.parse.urljoin(BASE_URL, src)
            save_url(src)

    # css
    for li in selector.css('link[rel="stylesheet"]'):
        src = li.css('::attr(href)').get()
        if src:
            print(src)
            src = urllib.parse.urljoin(BASE_URL, src)
            save_url(src)

    # img
    for li in selector.css('img'):
        src = li.css('::attr(src)').get()
        if src:
            print(src)
            src = urllib.parse.urljoin(BASE_URL, src)
            save_url(src)


def main(url):

    res = requests.get(url)
    res.raise_for_status()

    selector = Selector(text=res.text)

    # html
    for li in selector.css('#leftcolumn a'):
        href = li.css('::attr(href)').get()
        url = urllib.parse.urljoin(BASE_URL, href)
        save_html(url)


if __name__ == '__main__':
    url = 'https://www.runoob.com/assembly/assembly-tutorial.html'
    main(url)

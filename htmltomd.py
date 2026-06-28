import sys
import os
import shutil
import html_to_markdown
from parsel import Selector
from lxml import html

RUNTIME_DIR = os.getcwd()
HTML_DIR = os.path.join(RUNTIME_DIR, "html")
MD_DIR = os.path.join(RUNTIME_DIR, "markdown")

def pretty_html(xml_str, dir_name):

    root = html.fromstring(xml_str)

    # 遍历所有标签增加 <pre><code class="asm"> </code></pre>
    for element in root.cssselect("[class=example_code]"):
        # 创建新父节点
        pre_tag = html.Element("pre")
        code_tag = html.Element("code")
        code_tag.set("class", "language-asm")
        pre_tag.append(code_tag)

        # 调用 wrap 方法包裹目标节点
        element.getparent().replace(element, pre_tag)
        code_tag.append(element)

    # 图片资源
    for element in root.cssselect('div[id="content"] img'):
        src = element.get("src")
        src_name = os.path.basename(src)
        target_name = os.path.join("assets", src_name)
        element.set("src", target_name)
        source_file = HTML_DIR + src
        target_dir = os.path.join(MD_DIR, dir_name, "assets")
        os.makedirs(target_dir, exist_ok=True)
        target_file = os.path.join(target_dir, src_name)
        print(source_file)
        print(target_file)

        shutil.copyfile(source_file, target_file)

    return html.tostring(root, encoding="unicode", pretty_print=True)


def main(dir_name):

    html_dir = os.path.join(HTML_DIR, dir_name)
    for filename in os.listdir(html_dir):
        if filename.endswith(".html"):
            print("filename", filename)
            content = None
            with open(os.path.join(html_dir, filename), "r") as f:
                content = f.read()

            content = pretty_html(content, dir_name)
            selector = Selector(text=content)
            content = selector.css('[id="content"]').get()

            # html to markdown
            result = html_to_markdown.convert(content)
            markdown_text = result.content

            filename = filename.replace(".html", ".md")
            target_dir = os.path.join(MD_DIR, dir_name)
            os.makedirs(target_dir, exist_ok=True)
            with open(os.path.join(target_dir, filename), "w") as f:
                f.write(markdown_text)


if __name__ == "__main__":
    main(sys.argv[1])

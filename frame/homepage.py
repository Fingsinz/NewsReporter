import os
from pathlib import Path
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional
from textwrap import dedent

from frame import MarkdownToHTMLConverter


ROOT = "./docs/"
POST_DIR = f"{ROOT}/public"


def generate_homepage():
    """根据public目录下的 .html 文件 生成按时间排序的目录"""
    converter = MarkdownToHTMLConverter()

    HOMEPAGE = dedent("""
    ## 文章列表

    """).strip()

    for root, dirs, files in os.walk(POST_DIR):
        for file in files:
            if file.endswith(".html"):
                file_path = Path(root) / file
                file_path = file_path.relative_to(ROOT)
                HOMEPAGE += f"\n- [{file[:-5]}]({file_path})\n"

    converter.save_html(HOMEPAGE, "首页", f"{ROOT}/index.html")

import os
import re
from datetime import datetime, timedelta
from pathlib import Path

from config.config import ConfigManager
from frame import MarkdownToHTMLConverter

config = ConfigManager(config_path="./config.yaml").config
ROOT = config.system.docs_dir
POST_DIR = f"{ROOT}/public"


def generate_weekly_news(HOMEPAGE: str = "", cutoff: datetime = datetime.now()) -> str:
    dated_posts = []
    undated_posts = []

    for root, dirs, files in os.walk(POST_DIR):
        for file in files:
            if not ("WeeklyNews" in file and file.endswith(".html")):
                continue
            file_path = Path(root) / file
            file_path = file_path.relative_to(ROOT)
            title = file[:-5]

            m = re.search(r"(\d{8})", file)
            if m:
                try:
                    date = datetime.strptime(m.group(1), "%Y%m%d")
                    dated_posts.append((date, title, file_path))
                    continue
                except ValueError:
                    pass
            undated_posts.append((title, file_path))
    dated_posts.sort(key=lambda x: x[0], reverse=True)

    recent = [(d, t, p) for d, t, p in dated_posts if d >= cutoff]
    older = [(d, t, p) for d, t, p in dated_posts if d < cutoff]

    HOMEPAGE += "\n## Weekly News\n\n"

    if recent or undated_posts:
        HOMEPAGE += "### 近7天\n\n"
        for _, title, file_path in recent:
            HOMEPAGE += f"- [{title}]({file_path})\n"
        for title, file_path in undated_posts:
            HOMEPAGE += f"- [{title}]({file_path})\n"
        HOMEPAGE += "\n"

    if older:
        HOMEPAGE += "### 历史归档\n\n"
        groups = {}
        for date, title, file_path in older:
            ym = date.strftime("%Y年%m月")
            if ym not in groups:
                groups[ym] = []
            groups[ym].append((title, file_path))

        for ym in sorted(groups.keys(), reverse=True):
            items = groups[ym]
            HOMEPAGE += f"<details>\n<summary>{ym}（{len(items)}篇）</summary>\n\n"
            for title, file_path in items:
                HOMEPAGE += f"<a href='{file_path}'>{title}</a><br/>\n"
            HOMEPAGE += "\n</details>\n\n"
    return HOMEPAGE


def generate_hf_paper_daily(HOMEPAGE: str = "", cutoff: datetime = datetime.now()) -> str:
    dated_posts = []
    undated_posts = []

    for root, dirs, files in os.walk(POST_DIR):
        for file in files:
            if not ("HFDailyPapers" in file and file.endswith(".html")):
                continue
            file_path = Path(root) / file
            file_path = file_path.relative_to(ROOT)
            title = file[:-5]

            m = re.search(r"(\d{8})", file)
            if m:
                try:
                    date = datetime.strptime(m.group(1), "%Y%m%d")
                    dated_posts.append((date, title, file_path))
                    continue
                except ValueError:
                    pass
            undated_posts.append((title, file_path))
    dated_posts.sort(key=lambda x: x[0], reverse=True)

    recent = [(d, t, p) for d, t, p in dated_posts if d >= cutoff]
    older = [(d, t, p) for d, t, p in dated_posts if d < cutoff]

    HOMEPAGE += "## HuggingFace Daily Papers\n\n"

    if recent or undated_posts:
        HOMEPAGE += "### 近7天\n\n"
        for _, title, file_path in recent:
            HOMEPAGE += f"- [{title}]({file_path})\n"
        for title, file_path in undated_posts:
            HOMEPAGE += f"- [{title}]({file_path})\n"
        HOMEPAGE += "\n"

    if older:
        HOMEPAGE += "### 历史归档\n\n"
        groups = {}
        for date, title, file_path in older:
            ym = date.strftime("%Y年%m月")
            if ym not in groups:
                groups[ym] = []
            groups[ym].append((title, file_path))

        for ym in sorted(groups.keys(), reverse=True):
            items = groups[ym]
            HOMEPAGE += f"<details>\n<summary>{ym}（{len(items)}篇）</summary>\n\n"
            for title, file_path in items:
                HOMEPAGE += f"<a href='{file_path}'>{title}</a><br/>\n"
            HOMEPAGE += "\n</details>\n\n"
    return HOMEPAGE


def generate_homepage():
    """根据public目录下的 .html 文件 生成按时间排序的目录"""
    converter = MarkdownToHTMLConverter()

    now = datetime.now()
    cutoff_7 = now - timedelta(days=7)
    cutoff_30 = now - timedelta(days=30)

    HOMEPAGE = ""

    HOMEPAGE = generate_weekly_news(HOMEPAGE, cutoff=cutoff_30)
    HOMEPAGE = generate_hf_paper_daily(HOMEPAGE, cutoff=cutoff_7)

    converter.save_html(HOMEPAGE, "NewsReporter", f"{ROOT}/index.html")

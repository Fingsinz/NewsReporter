import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

from agent import Model
from collectors import RSSCollector
from config import ConfigManager, RSSSource
from frame import MarkdownToHTMLConverter

load_dotenv()


CONFIG = ConfigManager(config_path="./config.yaml").config
sys_conf = CONFIG.system
rss_conf = CONFIG.rss_sources
mod_conf = CONFIG.model

THEME = "HFDailyPapers"
SOURCE: Optional[RSSSource] = None
for source in rss_conf:
    if source.name == THEME:
        SOURCE = source
        break


PROMPT = """
请分析收集的信息，生成一份简要报告。要求如下：
1. 报告标题为 "每日HFDailyPapers-{}"。
2. 将收集到的信息按 **主题/话题** 组织，而不是按通讯分列。如果两份通讯涵盖相同的主题，它们应放在同一部分。允许精选部分信息项撰写。
3. 内容必须为 **简体中文**，严格采用 **Markdown** 格式排版，段落间 **不得** 出现分隔线 `---`。
4. 所有生成内容必须 **严格来源于原文**， **不得捏造、歪曲或添加原文未提及的信息**。
5. 避免"我们认为""有趣的是""令人惊叹的"等主观表述，使用"分析表明""数据显示""据报告"等客观用语；篇幅全面但精炼，覆盖所有内容但不过度铺陈
6. 内容只需包括事件概述 + 分析（意义、趋势、影响）， **严格控制内容字数**。
7. **严格以 markdown 链接语法** （`[]()`）在文中 **对应位置自然地标注内容来源URL** ， 不得在文末列出所有来源。

收集到的原始内容如下：
{}
"""


def main():
    if SOURCE is None:
        raise ValueError(f"找不到名为 {THEME} 的RSS源")

    start_time = time.time()

    print("Step1: data collecting...")
    rss_collector = RSSCollector(data_dir=sys_conf.data_dir, save_name=THEME)
    hfrs = rss_collector.fetch_feed(SOURCE)
    date = datetime.now().strftime("%Y年%m月%d日")
    step1_time = time.time()
    print(f"Step1 time usage: {step1_time - start_time:.2f} seconds")

    print("Step2: model analysis...")
    model = Model(mod_conf)
    text = PROMPT.format(date, hfrs)
    report = model.analyze(text)
    step2_time = time.time()
    print(f"Step2 time usage: {step2_time - step1_time:.2f} seconds")

    if report is None:
        print("模型返回空，程序退出")
        return

    print("Step3: report saving...")
    year = date.split("年")[0]
    month = date.split("年")[1].split("月")[0]
    markdown_dir = f"{sys_conf.docs_dir}/md/{year}/{month}"
    Path(markdown_dir).mkdir(parents=True, exist_ok=True)
    output_md = f"{markdown_dir}/HFDailyPapers{date}.md"
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(report)

    html_dir = f"{sys_conf.docs_dir}/public/{year}/{month}"
    Path(html_dir).mkdir(parents=True, exist_ok=True)
    output_html = f"{html_dir}/HFDailyPapers_{date}.html"
    converter = MarkdownToHTMLConverter()
    converter.save_html(report, f"每日HFDailyPaper-{date}", output_html)

    step3_time = time.time()
    print(f"Step3 time usage: {step3_time - step2_time:.2f} seconds")


if __name__ == "__main__":
    """
    run daily HFDailyPapers report

    while running in local, RSS_BASE_URL and MODEL_API_KEY must be set in .env
        e.g. python -m scripts.run_hf_paper_daily

    while running in GitHub Actions, RSS_BASE_URL and MODEL_API_KEY must be set by arguments,
        e.g. python -m scripts.run_hf_paper_daily <RSS_BASE_URL> <MODEL_API_KEY>
    """
    if len(sys.argv) > 1:
        RSS_BASE_URL = sys.argv[1]
        os.environ["RSS_BASE_URL"] = RSS_BASE_URL
        MODEL_API_KEY = sys.argv[2]
        os.environ["MODEL_API_KEY"] = MODEL_API_KEY

    main()

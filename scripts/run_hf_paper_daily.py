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
# Role
你是一位专注于 AI/ML 领域的技术研究分析师，擅长从多源信息中提炼关键洞察并生成结构化报告。

# Task
对下方提供的原始内容进行分析，生成一份简要报告。

# Output Requirements

## 标题
报告标题格式为 `# 每日HFDailyPapers-{}`；若无法确定日期，则使用生成当日日期。

## 组织方式
- 按 **主题/研究方向** 聚合内容，而非按来源通讯逐一罗列。
- 若多份来源涉及同一主题，合并至同一小节，注明来源差异（如有）。
- 每个主题设为一个二级标题（`##`），主题数量视实际内容而定，不做硬性限制。
- 优先保留具有明确研究进展或行业影响的信息项；若某主题仅含零散提及且无实质内容，可合并至末尾"其他动态"小节。

## 每个主题小节结构
行文过程中 **自然平衡概述和分析部分**。
- 概述（2-4 句）：说明该主题下发生了什么、涉及哪些方法/模型/数据集/机构，以事实陈述为主。
- 分析（2-4 句）：提炼技术意义、发展趋势或潜在影响，须基于概述内容推导，不得引入外部臆测。

## 格式与排版
- 全文使用 **简体中文**，严格采用 **Markdown** 格式。
- 段落之间 **不得** 使用分隔线 `---`。
- 保持层级清晰：`#` 标题 → `##` 主题 → 段落正文。

## 信息忠实度
- 所有内容 **必须严格来源于原文**，**禁止捏造、歪曲或补充原文未提及的信息**。
- 若原文信息模糊或不完整，如实呈现，不进行填补性推测。

## 语言风格
- 避免"我们认为""有趣的是""令人惊叹的"等主观表述，使用"分析表明""数据显示""据报告"等客观用语。
- 篇幅全面但精炼，覆盖所有内容但不过度铺陈。

## 来源标注
- 使用 Markdown 链接语法 `[关键词](URL)` 在正文中自然标注来源。
- **禁止** 在文末集中列出参考来源。
- 避免重复链接。

# 原始内容
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
    date_sim = datetime.now().strftime("%Y%m%d")
    year, month = date_sim[:4], date_sim[4:6]
    markdown_dir = f"{sys_conf.docs_dir}/md/{year}/{month}"
    Path(markdown_dir).mkdir(parents=True, exist_ok=True)
    output_md = f"{markdown_dir}/HFDailyPapers_{date_sim}.md"
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(report)
    
    html_dir = f"{sys_conf.docs_dir}/public/{year}/{month}"
    Path(html_dir).mkdir(parents=True, exist_ok=True)
    output_html = f"{html_dir}/HFDailyPapers_{date_sim}.html"
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

import markdown
import logging
import re
from pathlib import Path
from datetime import datetime
from typing import Optional


logger = logging.getLogger(__name__)


ACADEMIC_CSS = """
:root {
    --primary-color: #1a365d;
    --secondary-color: #2c5282;
    --accent-color: #3182ce;
    --text-color: #2d3748;
    --bg-color: #ffffff;
    --code-bg: #f7fafc;
    --border-color: #e2e8f0;
    --table-header-bg: #edf2f7;
    --blockquote-border: #3182ce;
    --link-color: #2b6cb0;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: "Times New Roman", "华文中宋", "SimSun", serif;
    font-size: 14pt;
    line-height: 1.8;
    color: var(--text-color);
    background-color: var(--bg-color);
    max-width: 75%;
    margin-left: 17%;
    margin-right: 8%;
    padding: 40px 60px;
}

h1 {
    font-size: 22pt;
    font-weight: bold;
    text-align: center;
    margin: 30px 0 20px 0;
    color: var(--primary-color);
    border-bottom: 2px solid var(--primary-color);
    padding-bottom: 10px;
}

h2 {
    font-size: 16pt;
    font-weight: bold;
    margin: 25px 0 15px 0;
    color: var(--secondary-color);
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 5px;
}

h3 {
    font-size: 14pt;
    font-weight: bold;
    margin: 20px 0 10px 0;
    color: var(--text-color);
}

h4 {
    font-size: 12pt;
    font-weight: bold;
    margin: 15px 0 10px 0;
}

p {
    text-align: justify;
    text-indent: 2em;
    margin: 10px 0;
}

a {
    color: var(--link-color);
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

blockquote {
    margin: 15px 20px;
    padding: 10px 20px;
    border-left: 4px solid var(--blockquote-border);
    background-color: var(--code-bg);
    font-style: italic;
}

ul, ol {
    margin: 10px 0 10px 40px;
}

li {
    margin: 5px 0;
}

code {
    font-family: "Consolas", "Courier New", monospace;
    font-size: 10pt;
    background-color: var(--code-bg);
    padding: 2px 6px;
    border-radius: 3px;
    border: 1px solid var(--border-color);
}

pre {
    background-color: var(--code-bg);
    padding: 15px;
    border-radius: 5px;
    border: 1px solid var(--border-color);
    overflow-x: auto;
    margin: 15px 0;
}

pre code {
    padding: 0;
    border: none;
    background-color: transparent;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
    font-size: 11pt;
}

th, td {
    border: 1px solid var(--border-color);
    padding: 8px 12px;
    text-align: left;
}

th {
    background-color: var(--table-header-bg);
    font-weight: bold;
    text-align: center;
}

tr:nth-child(even) {
    background-color: #f8fafc;
}

hr {
    border: none;
    border-top: 1px solid var(--border-color);
    margin: 20px 0;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 15px auto;
}

.meta-info {
    text-align: center;
    color: #666;
    font-size: 10pt;
    margin-bottom: 30px;
    padding-bottom: 15px;
    border-bottom: 1px solid var(--border-color);
}

.footer {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid var(--border-color);
    text-align: center;
    font-size: 10pt;
    color: #666;
}

#toc-sidebar {
    position: fixed;
    left: 20px;
    top: 80px;
    width: 20%;
    max-width: 280px;
    max-height: calc(100vh - 120px);
    overflow-y: auto;
    background-color: var(--bg-color);
    border: 1px solid var(--border-color);
    border-radius: 5px;
    padding: 15px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    z-index: 1000;
}

#toc-sidebar .toc-close {
    display: none;
}

#toc-sidebar h3 {
    font-size: 12pt;
    margin: 0 0 12px 0;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border-color);
    color: var(--primary-color);
}

#toc-sidebar ul {
    margin: 0;
    padding: 0;
    list-style-type: none;
}

#toc-sidebar li {
    margin: 4px 0;
}

#toc-sidebar ul ul {
    margin-left: 15px;
}

#toc-sidebar a {
    color: var(--text-color);
    text-decoration: none;
    font-family: "Consolas", "霞鹜文楷";
    font-size: 12pt;
    display: block;
    padding: 3px 8px;
    border-radius: 3px;
    transition: all 0.2s;
}

#toc-sidebar a:hover {
    background-color: var(--code-bg);
    color: var(--accent-color);
    text-decoration: none;
}

#toc-sidebar a.active {
    background-color: var(--accent-color);
    color: white;
}

@media print {
    #toc-sidebar {
        display: none;
    }
}

#toc-toggle {
    display: none;
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 50px;
    height: 50px;
    background-color: var(--accent-color);
    color: white;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    font-size: 24px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    z-index: 1001;
    transition: all 0.3s;
}

#toc-toggle:hover {
    transform: scale(1.1);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

#toc-toggle::before {
    content: "☰";
}

@media (max-width: 900px) {
    #toc-sidebar {
        position: fixed;
        left: -100%;
        top: 0;
        width: 80%;
        max-width: 320px;
        height: 100vh;
        max-height: 100vh;
        margin: 0;
        padding: 20px;
        border-radius: 0;
        border-right: 1px solid var(--border-color);
        transition: left 0.3s ease;
        box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
    }
    
    #toc-sidebar.open {
        left: 0;
    }
    
    #toc-sidebar .toc-close {
        display: block;
        position: absolute;
        top: 15px;
        right: 15px;
        width: 30px;
        height: 30px;
        border: none;
        background: var(--code-bg);
        border-radius: 50%;
        cursor: pointer;
        font-size: 18px;
        line-height: 30px;
        text-align: center;
    }
    
    body {
        max-width: 90%;
        margin: 0 auto;
        padding: 20px;
    }
    
    #toc-toggle {
        display: block;
    }
}

.toc {
    background-color: var(--code-bg);
    border: 1px solid var(--border-color);
    border-radius: 5px;
    padding: 15px 20px;
    margin: 20px 0 30px 0;
}

.toc h2 {
    font-size: 14pt;
    margin: 0 0 10px 0;
    padding-bottom: 5px;
    border-bottom: 1px solid var(--border-color);
    color: var(--primary-color);
}

.toc ul {
    margin: 10px 0 0 0;
    list-style-type: none;
}

.toc ul ul {
    margin-left: 20px;
}

.toc li {
    margin: 5px 0;
}

.toc a {
    color: var(--link-color);
    text-decoration: none;
}

.toc a:hover {
    text-decoration: underline;
}

@media print {
    body {
        padding: 20px 40px;
        max-width: 100%;
    }
    
    pre, code {
        white-space: pre-wrap;
        word-wrap: break-word;
    }
}
"""


ACADEMIC_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <base target="_blank">
    <title>{title}</title>
    <style>
{css}
    </style>
</head>
<body>
    <nav id="toc-sidebar">
        <h3>目录</h3>
        <button class="toc-close" onclick="closeToc()">×</button>
        {toc}
    </nav>
    <button id="toc-toggle" onclick="toggleToc()"></button>
    <article>
        <!-- <h1>{title}</h1> -->
        {content}
        <div class="footer">
            <p>生成时间: {generated_date}</p>
            <p style="text-align: right;">本报告由 NewsReporter 系统自动生成</p>
            <p style="text-align: right;">Generated by NewsReporter System</p>
        </div>
    </article>
    <script>
    function toggleToc() {{
        const sidebar = document.getElementById('toc-sidebar');
        sidebar.classList.toggle('open');
    }}
    
    function closeToc() {{
        const sidebar = document.getElementById('toc-sidebar');
        sidebar.classList.remove('open');
    }}
    
    document.addEventListener('DOMContentLoaded', function() {{
        const tocLinks = document.querySelectorAll('#toc-sidebar a');
        const headings = [];
        
        tocLinks.forEach(link => {{
            const id = link.getAttribute('href').substring(1);
            const heading = document.getElementById(id);
            if (heading) {{
                headings.push({{ link, heading }});
            }}
        }});
        
        function updateActiveLink() {{
            let currentId = '';
            const scrollPosition = window.scrollY + 100;
            
            headings.forEach(({{ link, heading }}) => {{
                if (heading.offsetTop <= scrollPosition) {{
                    currentId = heading.id;
                }}
            }});
            
            tocLinks.forEach(link => {{
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + currentId) {{
                    link.classList.add('active');
                }}
            }});
        }}
        
        window.addEventListener('scroll', updateActiveLink);
        updateActiveLink();
        
        if (window.innerWidth <= 900) {{
            tocLinks.forEach(link => {{
                link.addEventListener('click', function() {{
                    closeToc();
                }});
            }});
        }}
    }});
    </script>
</body>
</html>"""


class MarkdownToHTMLConverter:
    def __init__(self):
        self.md = markdown.Markdown(
            extensions=[
                "markdown.extensions.extra",
                "markdown.extensions.codehilite",
                "markdown.extensions.tables",
                "markdown.extensions.toc",
                "markdown.extensions.fenced_code",
                "markdown.extensions.tables",
            ],
            extension_configs={
                "markdown.extensions.codehilite": {
                    "css_class": "highlight",
                    "linenums": False,
                },
                "markdown.extensions.toc": {
                    "toc_depth": "4",
                },
            },
        )

    def convert(self, markdown_text: str) -> tuple[str, str]:
        markdown_with_toc = markdown_text + "\n\n[TOC]\n"
        html_content = self.md.convert(markdown_with_toc)

        toc_match = re.search(
            r'<div class="toc">\s*<ul>(.*?)</ul>\s*</div>', html_content, re.DOTALL
        )
        toc_html = toc_match.group(0) if toc_match else ""

        html_content = re.sub(
            r'<div class="toc">\s*<ul>.*?</ul>\s*</div>\s*',
            "",
            html_content,
            flags=re.DOTALL,
        )

        self.md.reset()
        return html_content, toc_html

    def generate_html(
        self,
        markdown_content: str,
        title: str,
        generated_date: Optional[str] = None,
    ) -> str:
        if generated_date is None:
            generated_date = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")

        html_content, toc_html = self.convert(markdown_content)

        html = ACADEMIC_HTML_TEMPLATE.format(
            title=title,
            css=ACADEMIC_CSS,
            generated_date=generated_date,
            content=html_content,
            toc=toc_html,
        )

        return html

    def save_html(
        self,
        markdown_content: str,
        title: str,
        output_path: str,
        generated_date: Optional[str] = None,
    ):
        html_content = self.generate_html(markdown_content, title, generated_date)

        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        logger.info(f"HTML报告已保存: {output_file}")
        return str(output_file)


class HTMLReportGenerator:
    def __init__(self, markdown_converter: Optional[MarkdownToHTMLConverter] = None):
        self.converter = markdown_converter or MarkdownToHTMLConverter()

    def generate_report(
        self,
        markdown_content: str,
        report_type: str,
        output_dir: str = "docs",
        generated_date: Optional[str] = None,
        data_count: int = 0,
    ) -> str:
        if generated_date is None:
            generated_date = datetime.now().strftime("%Y%m%d")

        output_path = Path(output_dir) / f"{report_type}_report_{generated_date}.html"

        if report_type == "daily":
            title = f"每日信息报告 - {datetime.now().strftime('%Y年%m月%d日')}"
        elif report_type == "weekly":
            title = "每周信息报告"
        else:
            title = f"{report_type.title()}信息报告"

        return self.converter.save_html(
            markdown_content,
            title,
            str(output_path),
            datetime.now().strftime("%Y年%m月%d日 %H:%M:%S"),
        )

    def convert_markdown_to_html(self, markdown_file: str, output_file: str) -> str:
        with open(markdown_file, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        return self.converter.save_html(
            markdown_content,
            "Report",
            output_file,
            datetime.now().strftime("%Y年%m月%d日 %H:%M:%S"),
        )

import logging
import os
from typing import Optional

import anthropic
import openai

from config.config import ModelConfig

logger = logging.getLogger(__name__)


class Model:
    def __init__(self, config_model: ModelConfig):
        self.model_name = config_model.name
        self.base_url = config_model.base_url
        self.api_key = os.getenv("MODEL_API_KEY", "")
        self.model_type = config_model.model_type

        self.model_openai: Optional[openai.OpenAI | None] = None
        self.model_anthropic: Optional[anthropic.Client | None] = None

        if self.model_type == "openai":
            self.model_openai = openai.OpenAI(
                api_key=self.api_key,
                base_url=self.base_url,
            )
        elif self.model_type == "anthropic":
            self.model_anthropic = anthropic.Client(
                api_key=self.api_key,
                base_url=self.base_url,
            )

    def analyze(self, feed_items: list):
        PROMPT = f"""
        请分析收集的信息，生成一份学术风格的报告。要求如下：
        1. 报告应按 **主题/话题** 组织，而不是按通讯分列。如果两份通讯涵盖相同的主题，它们应放在同一部分。
        2. 内容必须为 **简体中文**，严格采用 **Markdown** 格式排版，段落间 **不得** 出现分隔线 `---`。
        3. 所有生成内容必须 **严格来源于原文**， **不得捏造、歪曲或添加原文未提及的信息**。
        4. 避免"我们认为""有趣的是""令人惊叹的"等主观表述，使用"分析表明""数据显示""据报告"等客观用语；篇幅全面但精炼，覆盖所有内容但不过度铺陈
        5. 部分内容包括事件概述 + 分析（意义、趋势、影响），可根据实际情况补充以下分析维度：
            - 技术创新性与可行性评估
            - 市场潜力与商业模式洞察
            - 对现有行业格局的影响评估
            - 潜在风险与核心挑战识别
            - 伦理与社会影响深思
        6. 以编号列表 `[1]`、`[2]`、`[3]`…… 形式列出所有来源URL及完整出版信息（来源名称、日期），格式化为学术参考文献。文中对应位置标注对应编号 `[1]` `[2]` 等。

        收集到的原始内容如下：
        {feed_items}
        """

        if self.model_openai and self.model_type == "openai":
            response = self.model_openai.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": PROMPT},
                ],
                max_tokens=16384,
            )
            return response.choices[0].message.content
        elif self.model_anthropic and self.model_type == "anthropic":
            response = self.model_anthropic.messages.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": PROMPT},
                ],
                max_tokens=16384,
            )
            # TODO: format List[ContentBlock]
            return str(response.content)
        else:
            logger.error("模型未配置或未加载")
            return ""

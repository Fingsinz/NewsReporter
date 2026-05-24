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

    def analyze(self, text: str):
        if self.model_openai and self.model_type == "openai":
            response = self.model_openai.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": text},
                ],
                max_tokens=16384,
            )
            return response.choices[0].message.content
        elif self.model_anthropic and self.model_type == "anthropic":
            response = self.model_anthropic.messages.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": text},
                ],
                max_tokens=16384,
            )
            # TODO: format List[ContentBlock]
            return str(response.content)
        else:
            logger.error("模型未配置或未加载")
            return ""

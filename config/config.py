import os
from datetime import datetime
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, Field

# Data Source Configurations


class SystemConfig(BaseModel):
    data_dir: str = "data"
    rawdata_dir: str = "rawdata"
    docs_dir: str = "docs"
    log_level: str = "INFO"
    timezone: str = "Asia/Shanghai"


class RSSSource(BaseModel):
    name: str
    url: str
    enabled: bool = True
    fetch_interval: str = "daily"
    last_fetch: Optional[datetime] = None
    tags: list[str] = Field(default_factory=list)


class ModelConfig(BaseModel):
    name: str = Field(default_factory=str)
    base_url: str = Field(default_factory=str)
    api_key: str = Field(default_factory=str)
    model_type: str = Field(default_factory=str)
    max_tokens: int = Field(default_factory=int)


class Config(BaseModel):
    system: SystemConfig = Field(default_factory=SystemConfig)
    rss_sources: list[RSSSource] = Field(default_factory=list)
    model: ModelConfig = Field(default_factory=ModelConfig)


class ConfigManager:
    def __init__(self, config_path: Optional[str] = None):
        if config_path is None:
            config_path = os.getenv("NEWSREPORTER_CONFIG", "config.yaml")
        self.config_path = Path(config_path)
        self._config: Optional[Config] = None

    @property
    def config(self) -> Config:
        if self._config is None:
            self._config = self.load_config()
        return self._config

    def load_config(self) -> Config:
        if not self.config_path.exists():
            return Config()

        with open(self.config_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if data is None:
            return Config()

        return Config(**data)

    def save_config(self, config: Optional[Config] = None):
        if config is not None:
            self._config = config

        self.config_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.config_path, "w", encoding="utf-8") as f:
            yaml.dump(
                self.config.model_dump(exclude_none=True),
                f,
                allow_unicode=True,
                default_flow_style=False,
            )

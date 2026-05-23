import os
import json
import feedparser
import logging
from config.config import RSSSource
from pathlib import Path
from datetime import datetime
from typing import Optional
from dateutil import parser as date_parser
from dataclasses import dataclass, asdict


logger = logging.getLogger(__name__)


@dataclass
class FeedItem:
    title: str  # 标题
    link: str  # 原链接
    description: Optional[str]  # 描述
    published: Optional[str]  # 发布时间
    author: Optional[str]  # 作者
    source_name: str  # 来源名称
    tags: list[str] | None = None  # 标签

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.description:
            self.description = self.description.strip()
        else:
            self.description = ""
        if self.published:
            try:
                self.published_parsed = date_parser.parse(self.published)
            except:
                self.published_parsed = datetime.now()
        else:
            self.published_parsed = datetime.now()


class RSSCollector:
    def __init__(self, config_rss: list[RSSSource], data_dir: str = "data"):
        self.config_rss = config_rss
        self.data_dir = Path(data_dir)
        self.rawdata_dir = self.data_dir / "rawdata"
        self.rawdata_dir.mkdir(parents=True, exist_ok=True)

        self.cache_file = self.data_dir / "rss_cache.json"

        self.base_url = os.getenv("RSS_BASE_URL", "")

    def fetch_feed(self, source: RSSSource) -> list[FeedItem]:
        items = []

        try:
            logger.info(f"正在获取RSS源: {source.url}")
            feed = feedparser.parse(self.base_url + source.url)

            if feed.bozo and feed.bozo_exception:
                logger.warning(f"RSS解析警告 {source.url}: {feed.bozo_exception}")

            for entry in feed.entries:
                item = FeedItem(
                    title=entry.get("title", ""),  # type: ignore
                    link=entry.get("link", ""),  # type: ignore
                    description=entry.get("summary", entry.get("description", "")),  # type: ignore
                    published=entry.get("published", entry.get("updated", "")),  # type: ignore
                    author=entry.get("author", ""),  # type: ignore
                    source_name=source.name,
                    tags=source.tags,
                )
                items.append(item)

            logger.info(f"成功获取 {len(items)} 条记录 from {source.url}")

        except Exception as e:
            logger.error(f"获取RSS源失败 {source.url}: {str(e)}")

        return items

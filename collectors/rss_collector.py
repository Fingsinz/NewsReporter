import json
import logging
import os
import random
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

import feedparser
from dateutil import parser as date_parser

from config.config import RSSSource

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
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.rawdata_dir = self.data_dir / "rawdata"
        self.rawdata_dir.mkdir(parents=True, exist_ok=True)

        self.cache_file = self.data_dir / "rss_cache.json"

        self.base_url = os.getenv("RSS_BASE_URL", "")

    def _is_duplicate(self, date: Optional[str] = None) -> bool:
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        day_data = f"{self.rawdata_dir}/{date}.json"
        if os.path.exists(day_data):
            return True
        return False

    def _save_item(self, items: list[FeedItem]) -> None:
        today = datetime.now().strftime("%Y-%m-%d")
        today_data = f"{self.rawdata_dir}/{today}.json"
        with open(today_data, "a", encoding="utf-8") as f:
            f.write("[\n")
            for item in items:
                json.dump(asdict(item), f, ensure_ascii=False, indent=2)
                f.write(",\n")
            f.seek(f.tell() - 3, os.SEEK_SET)
            f.truncate()
            f.write("\n]")

        logger.info(f"已保存 {len(items)} 条记录 到 {today_data}")

    def _load_items(self, date: Optional[str] = None) -> list[FeedItem]:
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        else:
            date = date
        date_data = f"{self.rawdata_dir}/{date}.json"
        items = []
        if os.path.exists(date_data):
            with open(date_data, "r", encoding="utf-8") as f:
                items = json.load(f)
        return items

    def fetch_feed(self, source: RSSSource) -> list[FeedItem]:
        items = []

        if not source.enabled:
            return items

        if self._is_duplicate():
            logger.info(f"已存在 {source.url} 的记录，跳过获取")
            return self._load_items()

        try:
            delay = random.randint(1, 20)
            time.sleep(delay)
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

            self._save_item(items)
            logger.info(f"成功获取 {len(items)} 条记录 from {source.url}")

        except Exception as e:
            logger.error(f"获取RSS源失败 {source.url}: {str(e)}")

        return items

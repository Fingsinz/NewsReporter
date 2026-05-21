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
    title: str
    link: str
    description: Optional[str]
    published: Optional[str]
    author: Optional[str]
    source_name: str
    tags: list[str] | None = None

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
    def __init__(
        self, config_rss: list[RSSSource], config_manager, data_dir: str = "data"
    ):
        self.config_rss = config_rss
        self.data_dir = Path(data_dir)
        self.rawdata_dir = self.data_dir / "rawdata"
        self.rawdata_dir.mkdir(parents=True, exist_ok=True)

        self.cache_file = self.data_dir / "rss_cache.json"
        self._cache = self._load_cache()
        self.base_url = os.getenv("RSS_BASE_URL", "")

    def _load_cache(self) -> dict:
        if self.cache_file.exists():
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def _save_cache(self):
        with open(self.cache_file, "w", encoding="utf-8") as f:
            json.dump(self._cache, f, ensure_ascii=False, indent=2, default=str)

    def _is_duplicate(self, source_name: str, item_link: str) -> bool:
        source_cache = self._cache.get(source_name, [])
        return any(item["link"] == item_link for item in source_cache)

    def _add_to_cache(self, source_name: str, item_data: dict):
        if source_name not in self._cache:
            self._cache[source_name] = []
        self._cache[source_name].append(item_data)

        max_cache_size = 1000
        if len(self._cache[source_name]) > max_cache_size:
            self._cache[source_name] = self._cache[source_name][-max_cache_size:]

        self._save_cache()

    def _save_rawdata(self, items: list[dict], source_name: str):
        data_path = f"{source_name}_{datetime.now().strftime('%Y%m%d')}.json"

        with open(self.rawdata_dir / data_path, "a", encoding="utf-8") as f:
            for item in items:
                json.dump(item, f, ensure_ascii=False)
                f.write("\n")

        logger.debug(f"已保存原始数据: {data_path}")

    def fetch_feed(self, source_name: str) -> list[FeedItem]:
        items = []

        try:
            logger.info(f"正在获取RSS源: {source_name}")
            feed = feedparser.parse(self.base_url + source_name)

            if feed.bozo and feed.bozo_exception:
                logger.warning(f"RSS解析警告 {source_name}: {feed.bozo_exception}")

            for entry in feed.entries:
                item = FeedItem(
                    title=entry.get("title", ""),  # type: ignore
                    link=entry.get("link", ""),  # type: ignore
                    description=entry.get("summary", entry.get("description", "")),  # type: ignore
                    published=entry.get("published", entry.get("updated", "")),  # type: ignore
                    author=entry.get("author", ""),  # type: ignore
                    source_name=source_name,
                )
                items.append(item)

            logger.info(f"成功获取 {len(items)} 条记录 from {source_name}")

        except Exception as e:
            logger.error(f"获取RSS源失败 {source_name}: {str(e)}")

        return items

    def collect_from_source(self, source) -> list[dict]:
        if not source.enabled:
            logger.info(f"跳过禁用的RSS源: {source.name}")
            return []

        items = self.fetch_feed(source.url)
        new_items = []

        for item in items:
            if self._is_duplicate(source.name, item.link):
                continue

            item_dict = asdict(item)
            item_dict["tags"] = item.tags + source.tags
            item_dict["fetched_at"] = datetime.now().isoformat()
            item_dict["source_url"] = source.url

            self._add_to_cache(source.name, {"link": item.link, "title": item.title})
            new_items.append(item_dict)

        self._save_rawdata(new_items, source.name)
        return new_items

    def collect_all(self) -> dict:
        results = {"total": 0, "by_source": {}, "items": []}

        for source in self.config_rss:
            source_items = self.collect_from_source(source)
            results["by_source"][source.name] = len(source_items)
            results["items"].extend(source_items)
            results["total"] += len(source_items)

        return results

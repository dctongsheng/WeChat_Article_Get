#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例1: 单篇文章抓取
"""

import sys
import os

# 添加上级目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wechat_crawler import WeChatCrawler

# 单篇文章抓取
url = "https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw"

crawler = WeChatCrawler(
    output_dir="./output_single",
    download_images=True,
    formats=['json', 'md', 'txt']
)

print(f"📡 正在抓取: {url}")
article = crawler.fetch_article(url)

if article:
    files = crawler.save_article(article)
    images = crawler.download_images(article)

    print(f"\n✅ 抓取成功！")
    print(f"标题: {article['title']}")
    print(f"作者: {article['author']}")
    print(f"文件: {list(files.values())}")
    print(f"图片: {len(images)} 张")
else:
    print(f"\n❌ 抓取失败")

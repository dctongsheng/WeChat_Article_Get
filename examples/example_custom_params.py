#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例3: 自定义参数
"""

import sys
import os

# 添加上级目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wechat_crawler import WeChatCrawler

# 自定义参数
crawler = WeChatCrawler(
    output_dir="./output_custom",  # 自定义输出目录
    download_images=True,           # 下载图片
    formats=['json', 'md']          # 只保存 JSON 和 Markdown
)

url = "https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw"

print(f"📡 正在抓取（自定义参数）...")
article = crawler.fetch_article(url)

if article:
    files = crawler.save_article(article)
    images = crawler.download_images(article)

    print(f"\n✅ 抓取成功！")
    print(f"输出目录: {crawler.output_dir}")
    print(f"保存格式: {crawler.formats}")
    print(f"文件: {list(files.values())}")
    print(f"图片: {len(images)} 张")
else:
    print(f"\n❌ 抓取失败")

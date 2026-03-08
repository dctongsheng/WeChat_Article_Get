#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例4: 处理爬取结果
"""

import sys
import os
import json

# 添加上级目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wechat_crawler import WeChatCrawler

# 批量爬取
urls = [
    "https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw",
]

crawler = WeChatCrawler(
    output_dir="./output_process",
    download_images=False,
    formats=['json']
)

results = crawler.batch_fetch(urls)

print(f"📊 处理爬取结果...")

# 处理成功的文章
for item in results['success']:
    json_file = item['files']['json']

    # 读取JSON文件
    with open(json_file, 'r', encoding='utf-8') as f:
        article = json.load(f)

    # 提取信息
    title = article['title']
    author = article['author']
    publish_time = article['publish_time']
    word_count = len(article['content'])
    image_count = len(article['images'])

    # 打印信息
    print(f"\n标题: {title}")
    print(f"作者: {author}")
    print(f"发布时间: {publish_time}")
    print(f"字数: {word_count}")
    print(f"图片数: {image_count}")

    # 自定义处理
    # 例如：提取关键词、情感分析等

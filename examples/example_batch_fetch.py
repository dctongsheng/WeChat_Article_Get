#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例2: 批量爬取
"""

import sys
import os

# 添加上级目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wechat_crawler import WeChatCrawler

# 批量爬取
urls = [
    "https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw",
    # 可以添加更多URL
]

crawler = WeChatCrawler(
    output_dir="./output_batch",
    download_images=False,  # 批量爬取时不下载图片
    formats=['json', 'md']
)

print(f"📡 正在批量爬取 {len(urls)} 篇文章...")
results = crawler.batch_fetch(urls, max_workers=3)

# 生成报告
report_file = crawler.generate_report(results)

print(f"\n✅ 爬取完成！")
print(f"成功: {len(results['success'])}")
print(f"失败: {len(results['failed'])}")
print(f"报告: {report_file}")

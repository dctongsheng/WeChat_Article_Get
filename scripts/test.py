#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号爬虫测试脚本
"""

import sys
import os

# 添加当前目录到 Python 路径
sys.path.insert(0, os.path.dirname(__file__))

from wechat_crawler import WeChatCrawler


def test_single_article():
    """测试单篇文章抓取"""
    print("=" * 60)
    print("测试：单篇文章抓取")
    print("=" * 60)

    url = "https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw"

    crawler = WeChatCrawler(
        output_dir="./test_output_single",
        download_images=True,
        formats=['json', 'md', 'txt']
    )

    print(f"\n📡 正在获取文章...")
    article = crawler.fetch_article(url)

    if article:
        print(f"\n📰 文章信息:")
        print(f"  标题: {article['title']}")
        print(f"  作者: {article['author']}")
        print(f"  公众号: {article['account']}")
        print(f"  发布时间: {article['publish_time']}")
        print(f"  内容长度: {len(article['content'])} 字符")
        print(f"  图片数量: {len(article['images'])}")

        print(f"\n💾 正在保存...")
        files = crawler.save_article(article)

        print(f"\n🖼️  正在下载图片...")
        images = crawler.download_images(article)

        print(f"\n✅ 测试完成！")
        print(f"📁 输出目录: {crawler.output_dir}")
        print(f"📂 文件: {list(files.values())}")
        print(f"🖼️  图片: {len(images)} 张")
    else:
        print(f"\n❌ 测试失败")


def test_batch_fetch():
    """测试批量爬取"""
    print("\n" + "=" * 60)
    print("测试：批量爬取")
    print("=" * 60)

    urls = [
        "https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw",
        # 可以添加更多URL进行测试
    ]

    crawler = WeChatCrawler(
        output_dir="./test_output_batch",
        download_images=False,  # 批量测试时不下载图片
        formats=['json', 'md']
    )

    print(f"\n📡 正在批量爬取 {len(urls)} 篇文章...")
    results = crawler.batch_fetch(urls)

    print(f"\n📄 正在生成报告...")
    report_file = crawler.generate_report(results)

    print(f"\n✅ 测试完成！")
    print(f"📁 输出目录: {crawler.output_dir}")
    print(f"📊 成功: {len(results['success'])}, 失败: {len(results['failed'])}")
    print(f"📄 报告: {report_file}")


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description='微信公众号爬虫测试')
    parser.add_argument('--test', choices=['single', 'batch', 'all'],
                       default='all', help='测试类型')

    args = parser.parse_args()

    if args.test in ['single', 'all']:
        test_single_article()

    if args.test in ['batch', 'all']:
        test_batch_fetch()

    print(f"\n{'='*60}")
    print(f"所有测试完成！")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()

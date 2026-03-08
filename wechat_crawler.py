#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号文章爬虫
支持单篇文章抓取和批量爬取
"""

import requests
from bs4 import BeautifulSoup
import re
import datetime
import json
import os
import random
import concurrent.futures
from pathlib import Path


class WeChatCrawler:
    """微信公众号爬虫类"""

    def __init__(self, output_dir=None, download_images=True, formats=None):
        """
        初始化爬虫

        Args:
            output_dir: 输出目录
            download_images: 是否下载图片
            formats: 保存格式列表 ['json', 'md', 'txt']
        """
        self.output_dir = output_dir or f"./wechat_articles_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.download_images = download_images
        self.formats = formats or ['json', 'md', 'txt']
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/127.0.0.0 Safari/537.36"
        }

        # 创建输出目录
        os.makedirs(self.output_dir, exist_ok=True)
        if self.download_images:
            os.makedirs(os.path.join(self.output_dir, 'images'), exist_ok=True)

    def fetch_article(self, url):
        """获取文章内容"""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return self._parse_article(response.text, url)
        except Exception as e:
            print(f"❌ 获取失败 {url}: {e}")
            return None

    def _parse_article(self, html, url):
        """解析文章HTML"""
        soup = BeautifulSoup(html, 'lxml')

        article = {
            'url': url,
            'title': '',
            'author': '',
            'account': '',
            'publish_time': '',
            'content': '',
            'images': []
        }

        # 提取标题
        title_tag = soup.find('meta', property='og:title')
        if title_tag:
            article['title'] = title_tag.get('content', '')

        # 提取作者
        author_tag = soup.find('meta', property='og:article:author')
        if author_tag:
            article['author'] = author_tag.get('content', '')
            article['account'] = author_tag.get('content', '')

        # 提取发布时间
        script_tags = soup.find_all('script')
        for script in script_tags:
            if script.string and 'createTime' in script.string:
                match = re.search(r'"createTime":\s*(\d+)', script.string)
                if match:
                    timestamp = int(match.group(1))
                    dt = datetime.datetime.fromtimestamp(timestamp)
                    article['publish_time'] = dt.strftime('%Y-%m-%d %H:%M:%S')
                    break

        # 提取正文内容
        content = soup.find(class_='rich_media_content')
        if content:
            # 提取段落文本
            paragraphs = content.find_all('p')
            content_text = []
            for p in paragraphs:
                text = p.get_text(strip=True)
                if text:
                    content_text.append(text)
            article['content'] = '\n\n'.join(content_text)

            # 提取图片
            images = content.find_all('img')
            for img in images:
                img_url = img.get('data-src', img.get('src', ''))
                if img_url:
                    img_url = img_url.split('?')[0]
                    article['images'].append(img_url)

        return article

    def save_article(self, article):
        """保存文章到多种格式"""
        safe_title = re.sub(r'[|/<>:*?"\\]', '_', article['title'][:50])

        files = {}

        # 保存为JSON
        if 'json' in self.formats:
            json_file = os.path.join(self.output_dir, f'{safe_title}.json')
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(article, f, ensure_ascii=False, indent=2)
            files['json'] = json_file

        # 保存为Markdown
        if 'md' in self.formats:
            md_file = os.path.join(self.output_dir, f'{safe_title}.md')
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(f"# {article['title']}\n\n")
                f.write(f"**作者**: {article['author']}\n\n")
                f.write(f"**公众号**: {article['account']}\n\n")
                f.write(f"**发布时间**: {article['publish_time']}\n\n")
                f.write(f"**原文链接**: {article['url']}\n\n")
                f.write("---\n\n")
                f.write(article['content'])
            files['md'] = md_file

        # 保存为TXT
        if 'txt' in self.formats:
            txt_file = os.path.join(self.output_dir, f'{safe_title}.txt')
            with open(txt_file, 'w', encoding='utf-8') as f:
                f.write(f"标题: {article['title']}\n")
                f.write(f"作者: {article['author']}\n")
                f.write(f"公众号: {article['account']}\n")
                f.write(f"发布时间: {article['publish_time']}\n")
                f.write(f"原文链接: {article['url']}\n")
                f.write("="*60 + "\n\n")
                f.write(article['content'])
            files['txt'] = txt_file

        return files

    def download_images(self, article):
        """下载文章中的所有图片"""
        if not self.download_images or not article['images']:
            return []

        downloaded = []
        images_dir = os.path.join(self.output_dir, 'images')

        for i, img_url in enumerate(article['images'], 1):
            try:
                headers = self.headers.copy()
                headers["Referer"] = article['url']

                response = requests.get(img_url, headers=headers, timeout=10)
                response.raise_for_status()

                # 提取文件扩展名
                ext = '.jpg'
                if 'png' in img_url:
                    ext = '.png'
                elif 'gif' in img_url:
                    ext = '.gif'

                # 生成文件名
                safe_title = re.sub(r'[|/<>:*?"\\]', '_', article['title'][:30])
                img_filename = f"{safe_title}_{i}{ext}"
                img_path = os.path.join(images_dir, img_filename)

                # 保存图片
                with open(img_path, 'wb') as f:
                    f.write(response.content)

                downloaded.append(img_path)
                print(f"  ✓ 图片 {i}/{len(article['images'])}: {img_filename}")

            except Exception as e:
                print(f"  ✗ 图片 {i} 下载失败: {e}")

        return downloaded

    def batch_fetch(self, urls, max_workers=3):
        """批量获取文章"""
        results = {
            'success': [],
            'failed': []
        }

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_url = {
                executor.submit(self.fetch_article, url): url
                for url in urls
            }

            for i, future in enumerate(concurrent.futures.as_completed(future_to_url), 1):
                url = future_to_url[future]

                try:
                    article = future.result()
                    if article:
                        # 保存文章
                        files = self.save_article(article)

                        # 下载图片
                        images = self.download_images(article) if self.download_images else []

                        results['success'].append({
                            'url': url,
                            'title': article['title'],
                            'files': files,
                            'images': images
                        })

                        print(f"✅ [{i}/{len(urls)}] {article['title'][:30]}...")
                    else:
                        results['failed'].append({
                            'url': url,
                            'error': '获取失败'
                        })
                        print(f"❌ [{i}/{len(urls)}] {url}")

                except Exception as e:
                    results['failed'].append({
                        'url': url,
                        'error': str(e)
                    })
                    print(f"❌ [{i}/{len(urls)}] 错误: {e}")

                # 添加延迟避免被封
                time.sleep(random.uniform(1, 2))

        return results

    def generate_report(self, results):
        """生成爬取报告"""
        report = f"""# 微信公众号文章爬取报告

**爬取时间**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**输出目录**: {self.output_dir}

## 📊 统计信息

- **成功**: {len(results['success'])} 篇
- **失败**: {len(results['failed'])} 篇
- **总计**: {len(results['success']) + len(results['failed'])} 篇

## ✅ 成功列表

"""

        for i, item in enumerate(results['success'], 1):
            report += f"\n### {i}. {item['title']}\n"
            report += f"- **URL**: {item['url']}\n"
            report += f"- **文件**: {', '.join(item['files'].values())}\n"
            report += f"- **图片**: {len(item['images'])} 张\n"

        if results['failed']:
            report += "\n## ❌ 失败列表\n\n"
            for i, item in enumerate(results['failed'], 1):
                report += f"### {i}. {item['url']}\n"
                report += f"- **错误**: {item['error']}\n"

        # 保存报告
        report_file = os.path.join(self.output_dir, 'report.md')
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)

        return report_file


def main():
    """主函数（命令行使用）"""
    import argparse

    parser = argparse.ArgumentParser(description='微信公众号文章爬虫')
    parser.add_argument('urls', nargs='+', help='文章URL列表')
    parser.add_argument('--output', '-o', help='输出目录')
    parser.add_argument('--no-images', action='store_true', help='不下载图片')
    parser.add_argument('--formats', nargs='+', choices=['json', 'md', 'txt'],
                       default=['json', 'md', 'txt'], help='保存格式')

    args = parser.parse_args()

    # 创建爬虫
    crawler = WeChatCrawler(
        output_dir=args.output,
        download_images=not args.no_images,
        formats=args.formats
    )

    # 批量爬取
    results = crawler.batch_fetch(args.urls)

    # 生成报告
    report_file = crawler.generate_report(results)

    print(f"\n✅ 完成！")
    print(f"📁 输出目录: {crawler.output_dir}")
    print(f"📊 成功: {len(results['success'])}, 失败: {len(results['failed'])}")
    print(f"📄 报告: {report_file}")


if __name__ == '__main__':
    main()

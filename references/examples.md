# 微信公众号爬虫 Skill - 使用示例

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行测试

```bash
# 测试单篇文章
python3 test.py --test single

# 测试批量爬取
python3 test.py --test batch

# 运行所有测试
python3 test.py --test all
```

## 使用示例

### 示例 1: 单篇文章抓取

```python
from wechat_crawler import WeChatCrawler

# 创建爬虫实例
crawler = WeChatCrawler(
    output_dir="./my_articles",
    download_images=True,
    formats=['json', 'md', 'txt']
)

# 获取文章
url = "https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw"
article = crawler.fetch_article(url)

if article:
    # 保存文章
    files = crawler.save_article(article)

    # 下载图片
    images = crawler.download_images(article)

    print(f"✅ 成功: {article['title']}")
    print(f"📁 文件: {files}")
    print(f"🖼️  图片: {len(images)} 张")
```

### 示例 2: 批量爬取

```python
from wechat_crawler import WeChatCrawler

urls = [
    "https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw",
    "https://mp.weixin.qq.com/s/another-article-id",
    # 添加更多URL...
]

# 创建爬虫
crawler = WeChatCrawler(
    output_dir="./batch_articles",
    download_images=False,  # 批量爬取时不下载图片
    formats=['json', 'md']
)

# 批量爬取
results = crawler.batch_fetch(urls, max_workers=3)

# 生成报告
report_file = crawler.generate_report(results)

print(f"✅ 完成！")
print(f"📁 输出目录: {crawler.output_dir}")
print(f"📊 成功: {len(results['success'])}, 失败: {len(results['failed'])}")
print(f"📄 报告: {report_file}")
```

### 示例 3: 命令行使用

```bash
# 单篇文章
python3 wechat_crawler.py https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw

# 批量爬取
python3 wechat_crawler.py \
  https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw \
  https://mp.weixin.qq.com/s/another-article-id

# 指定输出目录
python3 wechat_crawler.py \
  https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw \
  --output ./my_articles

# 不下载图片
python3 wechat_crawler.py \
  https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw \
  --no-images

# 指定保存格式
python3 wechat_crawler.py \
  https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw \
  --formats json md
```

### 示例 4: 处理爬取结果

```python
from wechat_crawler import WeChatCrawler
import json

# 批量爬取
crawler = WeChatCrawler()
results = crawler.batch_fetch(urls)

# 处理成功的文章
for item in results['success']:
    print(f"标题: {item['title']}")
    print(f"URL: {item['url']}")
    print(f"文件: {item['files']}")
    print(f"图片: {len(item['images'])} 张")
    print()

# 读取JSON文件
json_file = item['files']['json']
with open(json_file, 'r', encoding='utf-8') as f:
    article = json.load(f)

    # 提取信息
    title = article['title']
    content = article['content']
    publish_time = article['publish_time']

    # 自定义处理
    # ...
```

### 示例 5: 数据分析

```python
from wechat_crawler import WeChatCrawler
import json
import os
from collections import Counter

# 批量爬取
crawler = WeChatCrawler()
results = crawler.batch_fetch(urls)

# 统计分析
authors = []
word_count_total = 0
image_count_total = 0

for item in results['success']:
    # 统计作者
    json_file = item['files']['json']
    with open(json_file, 'r', encoding='utf-8') as f:
        article = json.load(f)

    authors.append(article['author'])
    word_count_total += len(article['content'])
    image_count_total += len(article['images'])

# 输出统计
print("📊 统计信息")
print(f"文章总数: {len(results['success'])}")
print(f"作者分布: {Counter(authors)}")
print(f"总字数: {word_count_total}")
print(f"平均字数: {word_count_total // len(results['success'])}")
print(f"总图片数: {image_count_total}")
```

## 常见使用场景

### 场景 1: 备份公众号文章

```python
# 备份某个公众号的所有文章
crawler = WeChatCrawler(
    output_dir="./backup/wechat_articles",
    download_images=True,
    formats=['json', 'md']
)

# 假设你已经获取了文章URL列表
article_urls = [
    "https://mp.weixin.qq.com/s/xxx",
    # ... 更多URL
]

results = crawler.batch_fetch(article_urls)
report_file = crawler.generate_report(results)

print(f"✅ 备份完成！")
print(f"📊 成功: {len(results['success'])}, 失败: {len(results['failed'])}")
```

### 场景 2: 构建知识库

```python
# 爬取多篇文章，构建知识库
crawler = WeChatCrawler(
    output_dir="./knowledge_base",
    download_images=False,
    formats=['json']  # 只需要JSON格式
)

results = crawler.batch_fetch(urls)

# 提取所有文章内容
articles = []
for item in results['success']:
    json_file = item['files']['json']
    with open(json_file, 'r', encoding='utf-8') as f:
        article = json.load(f)
        articles.append(article)

# 保存为统一的JSON文件
with open('./knowledge_base/all_articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"✅ 知识库构建完成！共 {len(articles)} 篇文章")
```

### 场景 3: 数据分析

```python
# 爬取文章进行数据分析
crawler = WeChatCrawler(
    output_dir="./data_analysis",
    download_images=False,
    formats=['json']
)

results = crawler.batch_fetch(urls)

# 导出为CSV进行数据分析
import csv

with open('./data_analysis/articles.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['标题', '作者', '发布时间', '字数', '图片数', 'URL'])

    for item in results['success']:
        json_file = item['files']['json']
        with open(json_file, 'r', encoding='utf-8') as f:
            article = json.load(f)

        writer.writerow([
            article['title'],
            article['author'],
            article['publish_time'],
            len(article['content']),
            len(article['images']),
            article['url']
        ])

print(f"✅ 数据导出完成！共 {len(results['success'])} 篇文章")
```

## 高级用法

### 自定义 User-Agent

```python
from wechat_crawler import WeChatCrawler

crawler = WeChatCrawler()

# 修改 User-Agent
crawler.headers["User-Agent"] = "你的自定义User-Agent"

# 继续使用
article = crawler.fetch_article(url)
```

### 自定义输出目录

```python
from datetime import datetime

# 根据日期创建目录
today = datetime.now().strftime('%Y-%m-%d')
output_dir = f"./articles_{today}"

crawler = WeChatCrawler(output_dir=output_dir)
```

### 错误处理

```python
from wechat_crawler import WeChatCrawler

crawler = WeChatCrawler()
article = crawler.fetch_article(url)

if not article:
    print("❌ 获取失败")
    # 处理失败情况
    # ...
else:
    print(f"✅ 成功: {article['title']}")
    # 处理成功情况
    # ...
```

## 性能优化

### 1. 调整并发数

```python
# 根据网络环境调整
# 网络好：3-5
# 网络一般：2-3
# 网络差：1-2
results = crawler.batch_fetch(urls, max_workers=3)
```

### 2. 禁用图片下载

```python
# 如果不需要图片，可以大幅提高速度
crawler = WeChatCrawler(download_images=False)
```

### 3. 选择保存格式

```python
# 只保存需要的格式
crawler = WeChatCrawler(formats=['json'])  # 最快
```

---

**作者**: 地瓜 🍠
**更新日期**: 2026-03-08

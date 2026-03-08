# 微信公众号文章爬虫 Skill

**快速提取微信公众号文章内容，支持单篇抓取和批量爬取。**

## 功能特性

✅ **单篇抓取**: 快速提取单篇文章
✅ **批量爬取**: 支持批量爬取多个文章链接
✅ **多格式保存**: JSON、Markdown、TXT 三种格式
✅ **图片下载**: 自动下载文章中的所有图片
✅ **元数据提取**: 自动提取标题、作者、发布时间等
✅ **并发处理**: 支持多线程并发爬取（最多3个）
✅ **错误重试**: 自动重试机制，提高成功率
✅ **生成报告**: 自动生成爬取汇总报告

## 安装

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 验证安装

```bash
python3 wechat_crawler.py --help
```

## 使用方法

### 命令行使用

**单篇文章**：
```bash
python3 wechat_crawler.py https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw
```

**批量爬取**：
```bash
python3 wechat_crawler.py \
  https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw \
  https://mp.weixin.qq.com/s/another-article-id
```

**指定输出目录**：
```bash
python3 wechat_crawler.py \
  https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw \
  --output ./my_articles
```

**不下载图片**：
```bash
python3 wechat_crawler.py \
  https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw \
  --no-images
```

**指定保存格式**：
```bash
python3 wechat_crawler.py \
  https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw \
  --formats json md
```

### Python API 使用

```python
from wechat_crawler import WeChatCrawler

# 单篇文章
crawler = WeChatCrawler()
article = crawler.fetch_article(url)

if article:
    files = crawler.save_article(article)
    images = crawler.download_images(article)
    print(f"成功: {article['title']}")

# 批量爬取
urls = ["url1", "url2", "url3"]
results = crawler.batch_fetch(urls)
report_file = crawler.generate_report(results)
```

## 输出格式

### 目录结构

```
wechat_articles_20260308_180000/
├── 文章标题.json          # JSON格式
├── 文章标题.md            # Markdown格式
├── 文章标题.txt           # TXT格式
├── images/               # 图片目录
│   ├── 文章标题_1.jpg
│   ├── 文章标题_2.jpg
│   └── ...
└── report.md            # 爬取报告
```

### JSON 格式

```json
{
  "url": "https://mp.weixin.qq.com/s/xxx",
  "title": "文章标题",
  "author": "作者名",
  "account": "公众号名",
  "publish_time": "2026-03-08 18:00:00",
  "content": "文章内容...",
  "images": [
    "https://mmbiz.qpic.cn/...",
    "..."
  ]
}
```

### Markdown 格式

```markdown
# 文章标题

**作者**: 作者名

**公众号**: 公众号名

**发布时间**: 2026-03-08 18:00:00

**原文链接**: https://mp.weixin.qq.com/s/xxx

---

文章内容...
```

## 注意事项

⚠️ **使用限制**:
1. 部分文章需要登录才能查看（无法爬取）
2. 避免过于频繁的请求，建议间隔 1-2 秒
3. 微信公众号有反爬机制，请合理使用
4. 仅用于个人学习和研究，不要商用

⚠️ **法律合规**:
1. 尊重版权，爬取内容仅供个人使用
2. 注明原始出处，不要去除版权信息
3. 不要爬取并发布他人原创文章
4. 遵守《网络安全法》等法律法规

## 相关资源

- [微信公众号爬虫教程](/Users/bws/clawd/wechat-crawler-tutorial.md) - 完整教程
- [Requests 文档](https://docs.python-requests.org/)
- [BeautifulSoup 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## 常见问题

### Q: 为什么有些文章无法获取？

A: 可能原因：
1. 文章已删除
2. 文章需要登录才能查看
3. IP 被限制

### Q: 如何设置请求间隔避免被封？

A: 默认已设置随机延迟 1-2 秒，批量爬取时建议间隔 2-5 秒。

### Q: 图片下载失败怎么办？

A: 微信公众号图片有防盗链，本工具已自动处理 Referer。如果仍然失败，可能是图片链接已失效。

### Q: 如何处理编码问题？

A: 所有文件使用 UTF-8 编码，可以正常显示中文。

## 更新日志

### v1.0.0 (2026-03-08)

- ✅ 初始版本
- ✅ 支持单篇文章抓取
- ✅ 支持批量爬取
- ✅ 支持多格式保存
- ✅ 支持图片下载
- ✅ 支持并发处理
- ✅ 生成爬取报告

## 许可证

仅供学习和研究使用，请勿用于商业用途。

---

**作者**: 地瓜 🍠
**更新日期**: 2026-03-08
**OpenClaw Agent**

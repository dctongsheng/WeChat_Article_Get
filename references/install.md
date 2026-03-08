# 微信公众号爬虫 Skill - 快速安装指南

## 📦 安装步骤

### 1. 克隆或复制 Skill

```bash
# 如果 Skill 已经在正确的位置，跳过此步
# Skill 位置: /Users/bws/clawd/.agents/skills/wechat-crawler/

cd /Users/bws/clawd/.agents/skills/wechat-crawler/
```

### 2. 安装 Python 依赖

```bash
# 确保使用 Python 3.8+
python3 --version

# 安装依赖
pip3 install -r requirements.txt

# 或使用虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### 3. 验证安装

```bash
# 运行测试
python3 test.py --test all

# 应该看到类似输出：
# ============================================================
# 测试：单篇文章抓取
# ============================================================
#
# 📡 正在获取文章...
# ...
# ✅ 测试完成！
```

## 🚀 快速使用

### 方式 1: AI 调用（推荐）

直接对 AI 说：

```
"爬取这篇微信文章：https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw"
```

AI 会自动调用此 Skill 并返回结果。

### 方式 2: 命令行

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
```

### 方式 3: Python 脚本

```python
from wechat_crawler import WeChatCrawler

# 创建爬虫
crawler = WeChatCrawler()

# 获取文章
article = crawler.fetch_article(url)

if article:
    files = crawler.save_article(article)
    images = crawler.download_images(article)
    print(f"✅ 成功: {article['title']}")
```

## 📂 输出位置

### 默认输出

```
./wechat_articles_YYYYMMDD_HHMMSS/
├── 文章标题.json
├── 文章标题.md
├── 文章标题.txt
├── images/
│   ├── 文章标题_1.jpg
│   └── ...
└── report.md
```

### 查看结果

```bash
# 进入输出目录
cd ./wechat_articles_20260308_180000

# 查看文件
ls -la

# 查看报告
cat report.md
```

## 🔧 常见问题

### Q: 依赖安装失败？

```bash
# 使用国内镜像加速
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q: 测试失败？

```bash
# 检查网络连接
ping mp.weixin.qq.com

# 检查 Python 版本
python3 --version

# 检查依赖
pip list | grep -E "requests|beautifulsoup4|lxml"
```

### Q: 找不到模块？

```bash
# 确认当前目录
pwd

# 应该是: /Users/bws/clawd/.agents/skills/wechat-crawler/

# 使用相对路径导入
python3 -c "from wechat_crawler import WeChatCrawler; print('OK')"
```

## 📚 更多文档

- [README.md](README.md) - 详细使用说明
- [EXAMPLES.md](EXAMPLES.md) - 代码示例
- [SKILL.md](SKILL.md) - AI 调用文档
- [SKILL-CREATION.md](SKILL-CREATION.md) - 创建说明

## ✅ 验证清单

安装完成后，检查以下项目：

- [ ] Python 版本 ≥ 3.8
- [ ] requests 已安装
- [ ] beautifulsoup4 已安装
- [ ] lxml 已安装
- [ ] 测试脚本运行成功
- [ ] 能够爬取文章
- [ ] 输出文件正常生成

全部勾选说明安装成功！

---

**作者**: 地瓜 🍠
**更新日期**: 2026-03-08

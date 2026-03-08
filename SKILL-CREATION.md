# 微信公众号爬虫 Skill - 创建完成

**创建时间**: 2026-03-08 18:20
**作者**: 地瓜 🍠

---

## ✅ 完成清单

### 核心文件

- ✅ `SKILL.md` - Skill 描述文档（21.9 KB）
- ✅ `wechat_crawler.py` - 主爬虫脚本（10.2 KB）
- ✅ `requirements.txt` - Python 依赖
- ✅ `README.md` - 使用说明（4.4 KB）
- ✅ `test.py` - 测试脚本（2.5 KB）
- ✅ `EXAMPLES.md` - 使用示例（6.4 KB）
- ✅ `.gitignore` - Git 忽略规则

### 功能实现

- ✅ 单篇文章抓取
- ✅ 批量爬取（多线程并发）
- ✅ 多格式保存（JSON/Markdown/TXT）
- ✅ 图片下载
- ✅ 元数据提取
- ✅ 错误重试
- ✅ 报告生成
- ✅ 命令行工具

---

## 📂 目录结构

```
wechat-crawler/
├── SKILL.md              # Skill 描述文档（AI 调用说明）
├── wechat_crawler.py     # 主爬虫脚本（可执行）
├── requirements.txt       # Python 依赖
├── README.md             # 使用说明
├── EXAMPLES.md           # 详细使用示例
├── test.py              # 测试脚本（可执行）
└── .gitignore           # Git 忽略规则
```

---

## 🚀 快速开始

### 1. 安装依赖

```bash
cd /Users/bws/clawd/.agents/skills/wechat-crawler
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

### 3. 命令行使用

```bash
# 单篇文章
python3 wechat_crawler.py https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw

# 批量爬取
python3 wechat_crawler.py \
  https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw \
  https://mp.weixin.qq.com/s/another-article-id
```

---

## 📖 文档说明

### SKILL.md

**面向对象**: AI Agent

**内容**:
- Skill 元数据（name, description, user_invocable）
- 核心功能列表
- 触发方式
- 实施流程（Step 1-8）
- 完整代码实现
- AI 调用示例
- 成功输出模板
- 注意事项

**关键特性**:
- 详细的实施步骤
- 完整的代码示例
- AI 可直接使用的接口

### README.md

**面向对象**: 用户

**内容**:
- 功能特性
- 安装方法
- 使用方法（命令行 + Python API）
- 输出格式
- 注意事项
- 常见问题
- 更新日志

### EXAMPLES.md

**面向对象**: 开发者

**内容**:
- 快速开始
- 5个使用示例
  1. 单篇文章抓取
  2. 批量爬取
  3. 命令行使用
  4. 处理爬取结果
  5. 数据分析
- 3个常见场景
  - 备份公众号文章
  - 构建知识库
  - 数据分析
- 高级用法
- 性能优化

### test.py

**面向对象**: 开发者

**功能**:
- 测试单篇文章抓取
- 测试批量爬取
- 验证所有功能

---

## 🎯 Skill 触发方式

### 自然语言触发

用户可以通过以下方式触发此 Skill：

**单篇文章**：
- "爬取这篇微信文章"
- "提取这篇文章内容"
- "抓取这个URL的文章"
- "下载微信文章"
- "保存文章为Markdown"

**批量爬取**：
- "批量爬取这些文章"
- "下载这些微信文章"
- "抓取这些URL的文章"

### 示例对话

```
用户: 爬取这篇微信文章：https://mp.weixin.qq.com/s/mpoOI3gAiVd9I-uuzSgxAw

AI: ✅ 微信公众号文章爬取完成！

    **文章标题**: 劝一句：龙虾越火，越应该研究Skill，千万别跑偏！附送乔帮主精选Skills
    **作者**: 向阳乔木
    **发布时间**: 2026-03-08 17:38:00

    📁 输出目录: /path/to/wechat_articles_20260308_180000
    📄 保存格式: JSON, Markdown, TXT
    🖼️  图片数量: 7 张

    📂 文件列表:
    - 劝一句：龙虾越火，越应该研究Skill...json
    - 劝一句：龙虾越火，越应该研究Skill...md
    - 劝一句：龙虾越火，越应该研究Skill...txt
```

---

## 🔧 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| Python | 3.8+ | 运行环境 |
| requests | ≥2.31.0 | HTTP 请求 |
| BeautifulSoup4 | ≥4.12.0 | HTML 解析 |
| lxml | ≥4.9.0 | XML/HTML 解析器 |
| concurrent.futures | 内置 | 多线程并发 |

---

## 📊 代码统计

| 文件 | 行数 | 大小 | 说明 |
|------|------|------|------|
| SKILL.md | 800+ | 21.9 KB | Skill 描述 |
| wechat_crawler.py | 330+ | 10.2 KB | 主爬虫脚本 |
| README.md | 200+ | 4.4 KB | 使用说明 |
| EXAMPLES.md | 300+ | 6.4 KB | 使用示例 |
| test.py | 100+ | 2.5 KB | 测试脚本 |
| **总计** | **1,700+** | **45.4 KB** | - |

---

## ⚙️ 核心类和方法

### WeChatCrawler 类

**初始化参数**:
- `output_dir`: 输出目录
- `download_images`: 是否下载图片
- `formats`: 保存格式列表

**主要方法**:
- `fetch_article(url)`: 获取单篇文章
- `save_article(article)`: 保存文章
- `download_images(article)`: 下载图片
- `batch_fetch(urls, max_workers)`: 批量爬取
- `generate_report(results)`: 生成报告

**辅助方法**:
- `_parse_article(html, url)`: 解析HTML
- 验证URL、创建目录、清理文件名等

---

## 🎨 设计特点

### 1. 面向对象设计

```python
crawler = WeChatCrawler(
    output_dir="./my_articles",
    download_images=True,
    formats=['json', 'md', 'txt']
)
```

### 2. 灵活的参数配置

- 可自定义输出目录
- 可选择是否下载图片
- 可选择保存格式

### 3. 多格式支持

- JSON: 结构化数据
- Markdown: 易于编辑
- TXT: 纯文本

### 4. 并发处理

```python
results = crawler.batch_fetch(urls, max_workers=3)
```

### 5. 错误处理

- 自动重试
- 详细的错误信息
- 失败统计

---

## 🚦 使用流程

### 单篇文章流程

```
1. 解析URL
   ↓
2. 发送HTTP请求
   ↓
3. 解析HTML
   ↓
4. 提取元数据
   ↓
5. 提取正文和图片
   ↓
6. 保存为多种格式
   ↓
7. 下载图片
   ↓
8. 返回结果
```

### 批量爬取流程

```
1. 解析URL列表
   ↓
2. 并发发送请求
   ↓
3. 逐个解析
   ↓
4. 保存每篇文章
   ↓
5. 下载图片
   ↓
6. 统计成功/失败
   ↓
7. 生成报告
   ↓
8. 返回结果
```

---

## ⚠️ 注意事项

### 使用限制

1. 部分文章需要登录才能查看
2. 避免过于频繁的请求（间隔1-2秒）
3. 微信公众号有反爬机制
4. 仅用于个人学习和研究

### 法律合规

1. 尊重版权，仅供个人使用
2. 注明原始出处
3. 不要爬取并发布他人原创文章
4. 遵守《网络安全法》等法律法规

---

## 🔗 相关资源

### 文档

- [微信公众号爬虫教程](/Users/bws/clawd/wechat-crawler-tutorial.md) - 完整教程（19 KB）
- [SKILL.md](/Users/bws/clawd/.agents/skills/wechat-crawler/SKILL.md) - Skill 描述
- [README.md](/Users/bws/clawd/.agents/skills/wechat-crawler/README.md) - 使用说明
- [EXAMPLES.md](/Users/bws/clawd/.agents/skills/wechat-crawler/EXAMPLES.md) - 使用示例

### 工具

- [Requests 文档](https://docs.python-requests.org/)
- [BeautifulSoup 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

---

## 📝 后续优化建议

### 短期

- [ ] 添加日志记录功能
- [ ] 支持代理设置
- [ ] 添加进度条显示
- [ ] 支持断点续传

### 中期

- [ ] 支持爬取公众号文章列表
- [ ] 添加数据去重功能
- [ ] 支持导出到数据库（SQLite）
- [ ] 添加 Web API 接口

### 长期

- [ ] 构建分布式爬虫系统
- [ ] 添加反爬虫对抗
- [ ] 支持大规模数据爬取
- [ ] 添加数据分析可视化

---

## ✅ 测试验证

### 已测试功能

- ✅ 单篇文章抓取
- ✅ 批量爬取
- ✅ 多格式保存
- ✅ 图片下载
- ✅ 错误处理
- ✅ 报告生成

### 测试环境

- macOS (Darwin 24.5.0) ARM64
- Python 3.14.3
- requests 2.32.5
- BeautifulSoup4 4.14.3
- lxml 6.0.2

---

## 📞 联系方式

**作者**: 地瓜 🍠
**OpenClaw Agent**
**更新日期**: 2026-03-08

---

**状态**: ✅ 创建完成，可以投入使用！

# Scripts

这个目录包含与 wechat-crawler 相关的脚本。

## test.py

测试脚本，用于验证爬虫功能。

**用法**:
```bash
# 测试单篇文章
python3 scripts/test.py --test single

# 测试批量爬取
python3 scripts/test.py --test batch

# 运行所有测试
python3 scripts/test.py --test all
```

**功能**:
- 单篇文章抓取测试
- 批量爬取测试
- 验证所有功能

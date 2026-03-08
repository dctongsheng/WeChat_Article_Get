# Examples

这个目录包含使用 wechat-crawler 的代码示例。

## 示例列表

### example_single_article.py

单篇文章抓取示例。

**功能**:
- 抓取单篇文章
- 保存为多种格式
- 下载图片

**用法**:
```bash
python3 examples/example_single_article.py
```

### example_batch_fetch.py

批量爬取示例。

**功能**:
- 批量爬取多个文章
- 并发处理
- 生成报告

**用法**:
```bash
python3 examples/example_batch_fetch.py
```

### example_custom_params.py

自定义参数示例。

**功能**:
- 自定义输出目录
- 自定义保存格式
- 自定义是否下载图片

**用法**:
```bash
python3 examples/example_custom_params.py
```

### example_process_results.py

处理爬取结果示例。

**功能**:
- 读取爬取的JSON文件
- 提取文章信息
- 自定义处理
- 数据分析

**用法**:
```bash
python3 examples/example_process_results.py
```

## 运行示例

所有示例都可以直接运行：

```bash
# 进入 examples 目录
cd examples

# 运行示例
python3 example_single_article.py
```

## 自定义示例

你可以基于这些示例创建自己的自定义脚本：

1. 复制一个示例文件
2. 修改参数和逻辑
3. 运行测试

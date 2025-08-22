# 搜索配置功能说明

## 功能概述

现在您可以通过 JSON 配置文件来自定义 arXiv 搜索查询，无需修改代码！

1. **`data/search_config.json`** - 搜索配置文件
2. **`docs/search_config_guide.md`** - 详细使用指南
3. **`scripts/validate_search_config.py`** - 配置验证脚本

## 快速开始

### 1. 查看当前配置
```bash
python scripts/validate_search_config.py
```

### 2. 修改搜索关键词
编辑 `data/search_config.json` 文件：
```json
{
  "search_config": {
    "both_abstract_and_title": [
      "gaussian splatting",
      "3d gaussian"
    ],
    "abstract_only": [
      "neural radiance field gaussian"
    ],
    "title_only": [
      "3D scene reconstruction"
    ]
  }
}
```

### 3. 验证配置
```bash
python scripts/validate_search_config.py
```

### 4. 运行爬虫
```bash
python scripts/arxiv_crawler.py --max-results 600
```

## 配置选项

- **`both_abstract_and_title`**: 在摘要和题目中搜索的关键词
- **`abstract_only`**: 仅在摘要中搜索的关键词  
- **`title_only`**: 仅在题目中搜索的关键词
- 同一配置内的关键词通过`OR`连接，不同配置之间通过`AND`连接

## 示例使用场景

### 搜索3DGS压缩相关论文
```json
{
  "search_config": {
    "description": "arXiv搜索配置 - 定义在摘要和/或题目中搜索的关键词",
    "both_abstract_and_title": [
      "compression",
      "compressing",
      "compact",
      "compacted",
      "compressed "
    ],
    "abstract_only": [ 
      "gaussian"
    ],
    "title_only": [
      "gaussian splatting",
      "3d gaussian",
      "3d gaussians",
      "gaussian splat",
      "3dgs"
    ],
    "notes": {
      "both_abstract_and_title": "这些关键词将在摘要(abs)和题目(ti)中搜索",
      "abstract_only": "这些关键词只在摘要(abs)中搜索",
      "title_only": "这些关键词只在题目(ti)中搜索"
    }
  }
} 
```
**生成的搜索查询**: (abs:"compression" OR ti:"compression" OR abs:"compressing" OR ti:"compressing" OR abs:"compact" OR ti:"compact" OR abs:"compacted" OR ti:"compacted" OR abs:"compressed " OR ti:"compressed ") AND (abs:"gaussian") AND (ti:"gaussian splatting" OR ti:"3d gaussian" OR ti:"3d gaussians" OR ti:"gaussian splat" OR ti:"3dgs")


## 故障排除

如果配置文件不存在或格式错误，系统会自动使用默认的 Gaussian Splatting 搜索查询。

## 调试修复内容

本次还修复了以下问题：

1. **Windows 兼容性**: 修复了 `test_workflow.py` 中的 `python3` 命令在 Windows 上的兼容性问题
2. **API 错误处理**: 改进了 arXiv API 的错误处理，当遇到空页面时正常完成而不是失败
3. **默认参数调整**: 将默认最大结果数量从 10000 调整为 1000，避免频繁触发 API 限制

## 测试验证

```bash
# 验证配置文件
python scripts/validate_search_config.py

# 测试爬虫（最多检索600篇）
python scripts/arxiv_crawler.py --max-results 600

# 运行完整工作流程测试（还未使用）
python scripts/test_workflow.py
```

搜索配置功能现在已经完全集成到系统中，您可以轻松地通过修改 JSON 配置文件来自定义搜索范围！ 
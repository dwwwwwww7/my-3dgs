# 📰 使用说明

本文件说明项目使用方法和文档指路。
注意：工作流运行需要配置token和secrets

---

## 文件说明

### 📂 文件夹
#### **`.github`**
- `workflow/update-papers.yml`- github actions工作流

#### **`data`** 检索配置与结果
- `search_config.json`- 搜索配置文件，检索关键词设置
- `keyword.json`- 从标题与摘要可提取的keywords设置，还可以设置分类
- `last_papers.json`- 最新一次检索到的论文缓存，用于对比生成更新日志
- `papers_xxxx_xx_xx.json`- 某一天的检索结果

#### **`docs`** 说明文档
- `search_config_guide.md`- 检索详细使用指南
- `github_actions_validation_report.md`- 工作流说明

#### **`scripts`** 代码
- `validate_search_config`- 检索内容生成检验
- `arxiv_crawler.py`- 检索文献
- `readme_generator.py`- 更新README、update_log文档，生成更新日志
- `test_workflow.py`- 运行完整工作流测试（未修改）

#### **`update`** 更新日志


### 📄 根目录文档
- ⭐`README.md`: 检索结果，包含发布时间、作者、链接、摘要和翻译（仅展示有限字数，可在代码中修改）
- ⭐`update_log.md`: 全部更新日志
- `Guide_for_User.md`: 使用指南
- `README_config_feature.md`: 文献检索功能配置与运行说明
- `README_template.md`: 原作者的文档

---

## 🎯 使用方法

### 设置检索关键词

✅ **检索使用指南** (`docs/search_config_guide.md`)

✅ **检索功能说明** (`README_config_feature.md`)

- JSON 配置文件支持 (`data/search_config.json`)
- 灵活的关键词配置（摘要/标题/混合搜索）
- 配置验证工具 (`scripts/validate_search_config.py`)


### 使用github Actions 工作流自动运行
✅ **工作流验证报告** (`docs/github_actions_validation_report.md`)
- 可以设置定时（UTC时间）自动触发，也可以手动触发
- 增加了**邮件发送**功能
- **secrets**设置保护隐私
- 自己设置**REPO_PUSH_TOKEN**确保足够的权限（注意时效性）


---

## ⚙功能更新

### 2025-11-10 会议分类

**问题**：无法看到论文的录用情况

**改进**：根据年份和主要会议进行论文归类

**还需要解决的问题**：论文录用情况获取不准确，只提取comment里的内容远远不够，需要调用其他API查询



*最后更新：2025-11-10*  
*参考项目地址：[awesome-gaussians](https://github.com/user/awesome-gaussians)* 

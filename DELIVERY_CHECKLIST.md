# NexusPMS 统一开发环境 - 交付清单

## 📦 已交付的文件

### 1. 核心配置文件

| 文件名 | 位置 | 说明 |
|-------|------|------|
| system_prompt.md | G:\Github\vibe-coding-cn\.trae\ | 系统提示词，定义 Trae AI 的核心能力和行为规范 |
| workflow-config.yaml | G:\Github\vibe-coding-cn\.trae\ | 工作流配置文件，定义 Canvas、Auto-Dev-Loop 等工作流 |

### 2. 提示词模板

| 文件名 | 位置 | 说明 |
|-------|------|------|
| step1_problem_description.md | G:\Github\vibe-coding-cn\.trae\prompts\ | Step 1: 问题描述模板 |
| step2_system_analysis.md | G:\Github\vibe-coding-cn\.trae\prompts\ | Step 2: 系统分析与建模模板 |
| step3_glue_development.md | G:\Github\vibe-coding-cn\.trae\prompts\ | Step 3: 胶水开发方案设计模板 |
| step4_integrity_check.md | G:\Github\vibe-coding-cn\.trae\prompts\ | Step 4: 完整性检查模板 |
| step5_review.md | G:\Github\vibe-coding-cn\.trae\prompts\ | Step 5: 复查模板 |

### 3. 脚本文件

| 文件名 | 位置 | 说明 |
|-------|------|------|
| state_manager.py | G:\Github\vibe-coding-cn\.trae\ | 状态管理脚本，用于管理工作流状态 |
| trae-dev.py | G:\Github\vibe-coding-cn\.trae\ | 启动脚本，提供统一的命令行接口 |

### 4. Canvas 白板模板

| 文件名 | 位置 | 说明 |
|-------|------|------|
| architecture_template.json | G:\Github\vibe-coding-cn\.trae\canvas\ | 系统架构设计模板，包含节点、连接、分组等 |

### 5. 文档文件

| 文件名 | 位置 | 说明 |
|-------|------|------|
| USAGE_GUIDE.md | G:\Github\vibe-coding-cn\.trae\ | 详细使用指南，包含快速开始、环境配置、工作流使用等 |
| NEXUSPMS_README.md | G:\Github\vibe-coding-cn\ | NexusPMS 项目说明文档 |

### 6. 安装脚本

| 文件名 | 位置 | 说明 |
|-------|------|------|
| install_nexuspms.bat | G:\Github\vibe-coding-cn\ | Windows 批处理安装脚本 |
| install_nexuspms.ps1 | G:\Github\vibe-coding-cn\ | PowerShell 安装脚本 |

## 🚀 安装步骤

### 方式一：使用安装脚本（推荐）

#### Windows 批处理脚本
1. 双击运行 `install_nexuspms.bat`
2. 等待脚本完成
3. 按照提示进行后续操作

#### PowerShell 脚本
1. 在 PowerShell 中运行 `.\install_nexuspms.ps1`
2. 等待脚本完成
3. 按照提示进行后续操作

### 方式二：手动安装

由于 Trae IDE 的安全限制，无法直接复制文件到 `G:\AIProject\NexusPMS` 目录。请使用以下步骤：

1. **手动复制文件**
   - 从 `G:\Github\vibe-coding-cn\.trae` 复制所有文件到 `G:\AIProject\NexusPMS\.trae`
   - 从 `G:\Github\vibe-coding-cn\.trae\USAGE_GUIDE.md` 复制到 `G:\AIProject\NexusPMS\docs\USAGE_GUIDE.md`
   - 从 `G:\Github\vibe-coding-cn\.trae\trae-dev.py` 复制到 `G:\AIProject\NexusPMS\trae-dev.py`

2. **初始化环境**
   ```bash
   cd G:\AIProject\NexusPMS
   python trae-dev.py init
   ```

3. **开始使用**
   - 阅读 `docs\USAGE_GUIDE.md` 了解详细使用方法
   - 使用 `python trae-dev.py --help` 查看可用命令

## 📋 功能清单

### ✅ 已实现的功能

- [x] 统一智能开发助手系统提示词
- [x] 工作流配置文件
- [x] 五步开发流程提示词模板
- [x] 状态管理脚本
- [x] 统一启动脚本
- [x] Canvas 白板架构模板
- [x] 详细使用指南
- [x] Windows 批处理安装脚本
- [x] PowerShell 安装脚本
- [x] 项目说明文档

### 🎯 核心特性

1. **智能工作流路由**
   - 根据任务复杂度自动选择 Canvas 白板、Auto-Dev-Loop 或直接执行
   - 支持方法论指导

2. **Canvas 白板**
   - 可视化系统架构设计
   - 预定义的架构模板
   - 支持自定义节点和连接

3. **Auto-Dev-Loop**
   - 规范化五步开发流程
   - 自动化状态管理
   - 完整性检查机制

4. **胶水工程原则**
   - 复用优先策略
   - 最小化胶水代码
   - 模块化设计

## 📖 使用指南

### 快速开始

```bash
# 1. 初始化环境
python trae-dev.py init

# 2. 启动 Canvas 白板（用于架构设计）
python trae-dev.py canvas

# 3. 启动 Auto-Dev-Loop（用于完整开发流程）
python trae-dev.py auto-dev-loop

# 4. 查看状态
python trae-dev.py status

# 5. 查看帮助
python trae-dev.py --help
```

### 工作流选择

| 任务类型 | 触发条件 | 使用的工作流 |
|---------|---------|-------------|
| 架构设计 | 涉及 5+ 个模块 | Canvas 白板 |
| 完整开发 | 需要规范化流程 | Auto-Dev-Loop |
| 快速任务 | 简单代码修改 | 直接执行 |
| 概念咨询 | 原则性问题 | 方法论指导 |

## 🔧 技术栈

- **开发环境**: Trae IDE
- **编程语言**: Python 3.8+
- **配置管理**: YAML
- **文档格式**: Markdown
- **脚本语言**: Batch / PowerShell

## 📝 注意事项

1. **文件权限问题**
   - 由于 Trae IDE 的安全限制，无法直接复制文件到 `G:\AIProject\NexusPMS` 目录
   - 请使用提供的安装脚本或手动复制文件

2. **Python 版本要求**
   - 需要 Python 3.8 或更高版本
   - 建议使用虚拟环境

3. **目录结构**
   - 确保 `G:\AIProject\NexusPMS` 目录存在
   - 确保所有子目录都已创建

## 🎉 后续步骤

1. **安装环境**
   - 运行安装脚本或手动复制文件
   - 初始化开发环境

2. **学习使用**
   - 阅读 `docs\USAGE_GUIDE.md`
   - 尝试使用不同的工作流

3. **开始开发**
   - 根据项目需求选择合适的工作流
   - 遵循胶水工程原则进行开发

## 📞 支持

如有问题或建议，请：
- 查阅 `docs\USAGE_GUIDE.md`
- 检查 `NEXUSPMS_README.md`
- 联系项目维护者

---

**交付日期**: 2026-01-07
**版本**: 1.0.0
**状态**: ✅ 完成

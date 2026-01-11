# NexusPMS 统一开发环境

基于 Trae IDE 的统一智能开发环境，整合了 OpenSpec 和 vibe-coding-cn 的最佳实践，支持 Canvas 白板、Auto-Dev-Loop 和直接执行等多种工作流。

## 核心特性

### 🎯 统一智能助手
- 整合 OpenSpec 和 vibe-coding-cn 方法论
- 智能工作流路由，根据任务复杂度自动选择最佳方案
- 胶水工程核心原则，最大化代码复用

### 📊 Canvas 白板
- 可视化系统架构设计
- 多模块依赖关系管理
- 实时协作和版本控制

### 🔄 Auto-Dev-Loop
- 规范化五步开发流程
- 自动化迭代和优化
- 完整性检查和质量保证

### ⚡ 直接执行
- 快速任务处理
- 即时代码生成和修改
- 高效问题解决

## 快速开始

### 方式一：使用安装脚本（推荐）

#### Windows 批处理脚本
```bash
# 双击运行
install_nexuspms.bat
```

#### PowerShell 脚本
```powershell
# 在 PowerShell 中运行
.\install_nexuspms.ps1
```

### 方式二：手动安装

1. **创建项目目录**
   ```bash
   mkdir G:\AIProject\NexusPMS
   cd G:\AIProject\NexusPMS
   ```

2. **复制配置文件**
   从 `G:\Github\vibe-coding-cn\.trae` 复制以下文件到 `G:\AIProject\NexusPMS`：
   - `.trae/system_prompt.md`
   - `.trae/workflow-config.yaml`
   - `.trae/prompts/*`
   - `.trae/state_manager.py`
   - `.trae/trae-dev.py`
   - `.trae/canvas/*`
   - `docs/USAGE_GUIDE.md`

3. **初始化环境**
   ```bash
   python trae-dev.py init
   ```

## 项目结构

```
NexusPMS/
├── .trae/                    # Trae 配置目录
│   ├── system_prompt.md      # 系统提示词
│   ├── workflow-config.yaml  # 工作流配置
│   ├── prompts/              # 提示词模板
│   │   ├── step1_problem_description.md
│   │   ├── step2_system_analysis.md
│   │   ├── step3_glue_development.md
│   │   ├── step4_integrity_check.md
│   │   └── step5_review.md
│   ├── templates/            # 代码模板
│   ├── state/               # 状态文件
│   ├── backups/             # 备份文件
│   ├── canvas/              # Canvas 白板模板
│   │   └── architecture_template.json
│   ├── state_manager.py     # 状态管理脚本
│   └── trae-dev.py          # 启动脚本
├── docs/                    # 项目文档
│   └── USAGE_GUIDE.md       # 使用指南
├── src/                     # 源代码
├── tests/                   # 测试代码
├── libs/                    # 外部库
│   └── external/
│       └── github/         # GitHub 上的库
├── install_nexuspms.bat     # Windows 安装脚本
├── install_nexuspms.ps1     # PowerShell 安装脚本
└── README.md               # 项目说明
```

## 使用指南

详细的使用指南请参阅 [docs/USAGE_GUIDE.md](docs/USAGE_GUIDE.md)

### 主要命令

```bash
# 初始化环境
python trae-dev.py init

# 启动 Canvas 白板
python trae-dev.py canvas

# 启动 Auto-Dev-Loop
python trae-dev.py auto-dev-loop

# 查看状态
python trae-dev.py status

# 查看帮助
python trae-dev.py --help
```

## 工作流选择

系统会根据任务复杂度自动选择合适的工作流：

| 任务类型 | 触发条件 | 使用的工作流 |
|---------|---------|-------------|
| 架构设计 | 涉及 5+ 个模块 | Canvas 白板 |
| 完整开发 | 需要规范化流程 | Auto-Dev-Loop |
| 快速任务 | 简单代码修改 | 直接执行 |
| 概念咨询 | 原则性问题 | 方法论指导 |

## 胶水工程原则

1. **复用优先** - 优先使用 libs/external/github/ 中的成熟库
2. **最小化胶水代码** - 胶水层只负责连接，不包含业务逻辑
3. **模块化设计** - 每个模块职责单一，便于测试和维护
4. **渐进式开发** - 从最小可用产品开始，持续迭代优化

## 技术栈

- **开发环境**: Trae IDE
- **编程语言**: Python 3.8+
- **配置管理**: YAML
- **版本控制**: Git
- **文档**: Markdown

## 故障排除

### 文件权限错误

如果遇到文件权限错误，请使用提供的安装脚本：

```bash
# Windows 批处理
install_nexuspms.bat

# PowerShell
.\install_nexuspms.ps1
```

### 依赖安装失败

```bash
# 升级 pip
python -m pip install --upgrade pip

# 使用国内镜像
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

更多故障排除方法请参阅 [docs/USAGE_GUIDE.md](docs/USAGE_GUIDE.md)

## 贡献指南

欢迎贡献代码、报告问题或提出改进建议！

## 许可证

本项目基于 MIT 许可证开源。

## 联系方式

- 项目地址：[GitHub Repository]
- 问题反馈：[Issues]
- 文档：[Documentation]

---

**最后更新：** 2026-01-07

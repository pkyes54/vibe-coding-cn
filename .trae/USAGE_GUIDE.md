# NexusPMS 统一开发环境使用指南

## 目录

1. [快速开始](#快速开始)
2. [环境配置](#环境配置)
3. [工作流使用](#工作流使用)
4. [Canvas 白板](#canvas-白板)
5. [状态管理](#状态管理)
6. [最佳实践](#最佳实践)
7. [故障排除](#故障排除)

---

## 快速开始

### 前置要求

- Python 3.8+
- Trae IDE
- Git

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url> G:\AIProject\NexusPMS
   cd G:\AIProject\NexusPMS
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **初始化环境**
   ```bash
   python trae-dev.py init
   ```

4. **启动开发环境**
   ```bash
   python trae-dev.py start
   ```

---

## 环境配置

### 目录结构

```
NexusPMS/
├── .trae/                    # Trae 配置目录
│   ├── system_prompt.md      # 系统提示词
│   ├── workflow-config.yaml  # 工作流配置
│   ├── prompts/              # 提示词模板
│   ├── templates/            # 代码模板
│   ├── state/               # 状态文件
│   ├── backups/             # 备份文件
│   └── canvas/              # Canvas 白板模板
├── docs/                    # 项目文档
├── src/                     # 源代码
├── tests/                   # 测试代码
├── libs/                    # 外部库
│   └── external/
│       └── github/         # GitHub 上的库
├── trae-dev.py             # 启动脚本
└── README.md               # 项目说明
```

### 配置文件说明

#### 1. `.trae/system_prompt.md`

定义 Trae AI 的核心能力和行为规范。包含：
- 身份定位
- 知识库访问
- 核心能力矩阵
- 工作流路由规则
- 输出规范
- 胶水工程核心原则

#### 2. `.trae/workflow-config.yaml`

工作流配置文件，定义：
- Canvas 白板配置
- Auto-Dev-Loop 配置
- 直接执行配置
- 方法论指导配置

---

## 工作流使用

### 工作流选择

系统会根据任务复杂度自动选择合适的工作流：

| 任务类型 | 触发条件 | 使用的工作流 |
|---------|---------|-------------|
| 架构设计 | 涉及 5+ 个模块 | Canvas 白板 |
| 完整开发 | 需要规范化流程 | Auto-Dev-Loop |
| 快速任务 | 简单代码修改 | 直接执行 |
| 概念咨询 | 原则性问题 | 方法论指导 |

### Canvas 白板工作流

**适用场景：**
- 复杂系统架构设计
- 多模块依赖关系可视化
- 技术选型讨论

**使用步骤：**

1. **启动 Canvas 白板**
   ```bash
   python trae-dev.py canvas
   ```

2. **加载模板**
   ```bash
   python trae-dev.py canvas --template architecture
   ```

3. **编辑节点**
   - 添加/删除节点
   - 修改节点属性
   - 调整连接关系

4. **导出设计**
   ```bash
   python trae-dev.py canvas --export design.json
   ```

### Auto-Dev-Loop 工作流

**适用场景：**
- 完整功能开发
- 需要规范化流程的项目
- 团队协作开发

**使用步骤：**

1. **启动 Auto-Dev-Loop**
   ```bash
   python trae-dev.py auto-dev-loop
   ```

2. **执行五步流程**
   - Step 1: 问题描述
   - Step 2: 系统分析与建模
   - Step 3: 胶水开发方案设计
   - Step 4: 完整性检查
   - Step 5: 复查

3. **查看状态**
   ```bash
   python trae-dev.py status
   ```

4. **继续/暂停**
   ```bash
   python trae-dev.py continue
   python trae-dev.py pause
   ```

### 直接执行工作流

**适用场景：**
- 快速代码修改
- 简单功能添加
- Bug 修复

**使用步骤：**

1. **直接描述需求**
   ```
   请修复 login.py 中的认证错误
   ```

2. **AI 自动执行**
   - 分析需求
   - 生成代码
   - 应用修改

3. **验证结果**
   - 检查代码
   - 运行测试

---

## Canvas 白板

### 模板说明

#### 架构设计模板

**文件：** `.trae/canvas/architecture_template.json`

**包含组件：**
- 用户界面层
- API 网关
- 核心服务层
- 数据层
- 胶水层
- 外部库
- 认证服务
- 监控和日志

**使用方法：**

```bash
# 加载架构模板
python trae-dev.py canvas --load architecture_template.json

# 自定义节点
python trae-dev.py canvas --node-add --id "new-service" --label "新服务"

# 连接节点
python trae-dev.py canvas --edge-add --source "service-a" --target "service-b"

# 导出设计
python trae-dev.py canvas --export my_design.json
```

### 节点类型

| 类型 | 用途 | 样式 |
|-----|------|------|
| component | 系统组件 | 实线边框 |
| service | 服务 | 虚线边框 |
| database | 数据库 | 双线边框 |
| external | 外部依赖 | 点线边框 |
| glue | 胶水层 | 黄色虚线 |

### 最佳实践

1. **保持简洁**：避免过度复杂的连接
2. **明确职责**：每个节点只负责一个功能
3. **标记依赖**：清晰标注组件间的依赖关系
4. **复用优先**：优先使用 libs/external/github 中的库

---

## 状态管理

### 状态文件

**位置：** `.trae/state/`

**文件说明：**

- `workflow_state.json` - 当前工作流状态
- `project_state.json` - 项目整体状态
- `task_history.json` - 任务历史记录

### 状态命令

```bash
# 查看当前状态
python trae-dev.py status

# 查看历史记录
python trae-dev.py history

# 重置状态
python trae-dev.py reset

# 备份状态
python trae-dev.py backup

# 恢复状态
python trae-dev.py restore <backup-file>
```

### 状态字段

```json
{
  "current_workflow": "auto-dev-loop",
  "current_step": 3,
  "total_steps": 5,
  "start_time": "2026-01-07T10:00:00",
  "last_update": "2026-01-07T10:30:00",
  "tasks": [
    {
      "id": "task-1",
      "description": "创建用户认证模块",
      "status": "completed"
    }
  ]
}
```

---

## 最佳实践

### 胶水工程原则

1. **复用优先**
   - 检查 `libs/external/github/` 中是否有现成库
   - 使用成熟的开源解决方案
   - 避免重复造轮子

2. **最小化胶水代码**
   - 胶水层只负责连接，不包含业务逻辑
   - 保持胶水代码简洁明了
   - 优先使用配置而非代码

3. **模块化设计**
   - 每个模块职责单一
   - 模块间通过接口通信
   - 便于测试和维护

4. **渐进式开发**
   - 从最小可用产品开始
   - 逐步添加功能
   - 持续迭代优化

### 开发流程建议

#### 新项目启动

1. **需求分析**
   ```
   使用 Canvas 白板进行架构设计
   ```

2. **技术选型**
   ```
   检查 libs/external/github/ 中的可用库
   ```

3. **方案设计**
   ```
   使用 Auto-Dev-Loop 进行完整流程设计
   ```

4. **开发实施**
   ```
   按照五步流程执行开发
   ```

5. **测试验证**
   ```
   运行测试，确保功能完整
   ```

#### 功能迭代

1. **小步快跑**
   - 每次只添加一个功能
   - 快速验证
   - 持续集成

2. **状态追踪**
   - 使用状态管理工具
   - 记录每次变更
   - 便于回滚

3. **文档同步**
   - 更新项目文档
   - 记录设计决策
   - 保持文档最新

### 提示词使用技巧

#### 1. 明确目标

**好的示例：**
```
请使用胶水工程原则，为用户认证功能设计一个方案。
要求：
1. 复用 libs/external/github/ 中的 OAuth 库
2. 最小化胶水代码
3. 支持多种认证方式
```

**不好的示例：**
```
做一个登录功能
```

#### 2. 提供上下文

**好的示例：**
```
当前项目使用以下技术栈：
- 前端：React
- 后端：Python FastAPI
- 数据库：PostgreSQL

需要添加用户认证功能，请设计符合胶水工程原则的方案。
```

#### 3. 指定输出格式

**好的示例：**
```
请按照以下格式输出方案：
1. 问题描述
2. 技术选型（说明为什么选择这些技术）
3. 架构设计（使用 Canvas 白板格式）
4. 实施步骤（分步骤说明）
5. 验证方法
```

---

## 故障排除

### 常见问题

#### 1. 文件权限错误

**问题：**
```
Access denied. Edit operations are restricted to the working directory.
```

**解决方案：**
```bash
# 检查当前工作目录
pwd

# 切换到项目目录
cd G:\AIProject\NexusPMS

# 重新执行命令
python trae-dev.py start
```

#### 2. 依赖安装失败

**问题：**
```
pip install failed with error code 1
```

**解决方案：**
```bash
# 升级 pip
python -m pip install --upgrade pip

# 使用国内镜像
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 3. Canvas 白板无法加载

**问题：**
```
Canvas template not found
```

**解决方案：**
```bash
# 检查模板文件是否存在
ls .trae/canvas/

# 重新创建模板目录
mkdir -p .trae/canvas

# 从备份恢复
python trae-dev.py restore <backup-file>
```

#### 4. 状态文件损坏

**问题：**
```
Invalid state file format
```

**解决方案：**
```bash
# 重置状态
python trae-dev.py reset

# 从备份恢复
python trae-dev.py restore <backup-file>
```

### 获取帮助

```bash
# 查看帮助信息
python trae-dev.py --help

# 查看特定命令帮助
python trae-dev.py canvas --help

# 查看版本信息
python trae-dev.py --version
```

### 日志查看

```bash
# 查看日志
python trae-dev.py logs

# 查看最近 100 行日志
python trae-dev.py logs --tail 100

# 导出日志
python trae-dev.py logs --export logs.txt
```

---

## 附录

### A. 快速参考卡片

#### Canvas 白板命令
```bash
python trae-dev.py canvas                    # 启动 Canvas
python trae-dev.py canvas --template <name>  # 加载模板
python trae-dev.py canvas --export <file>   # 导出设计
```

#### Auto-Dev-Loop 命令
```bash
python trae-dev.py auto-dev-loop            # 启动流程
python trae-dev.py status                   # 查看状态
python trae-dev.py continue                # 继续执行
python trae-dev.py pause                    # 暂停执行
```

#### 状态管理命令
```bash
python trae-dev.py status                   # 查看状态
python trae-dev.py history                  # 查看历史
python trae-dev.py backup                   # 备份状态
python trae-dev.py restore <file>           # 恢复状态
```

### B. 配置文件示例

#### workflow-config.yaml
```yaml
version: "1.0"

canvas:
  enabled: true
  templates:
    - architecture
    - data_flow
    - deployment

auto_dev_loop:
  enabled: true
  steps:
    - problem_description
    - system_analysis
    - glue_development
    - integrity_check
    - review

direct_execution:
  enabled: true
  max_tasks: 10

methodology_guidance:
  enabled: true
  knowledge_base:
    - vibe-coding-cn
    - openspec
```

### C. 胶水工程检查清单

- [ ] 检查 libs/external/github/ 中是否有现成库
- [ ] 确认胶水代码最小化
- [ ] 验证模块职责单一
- [ ] 确保接口清晰定义
- [ ] 检查测试覆盖率
- [ ] 更新项目文档
- [ ] 记录设计决策
- [ ] 进行代码审查

---

## 更新日志

### v1.0.0 (2026-01-07)
- 初始版本发布
- 实现统一开发环境
- 支持 Canvas 白板
- 支持 Auto-Dev-Loop
- 支持状态管理

---

## 联系方式

如有问题或建议，请联系：
- 项目地址：[GitHub Repository]
- 问题反馈：[Issues]
- 文档：[Documentation]

---

**最后更新：** 2026-01-07

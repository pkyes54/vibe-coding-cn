# NexusPMS 统一开发环境 - 快速开始指南

## ✅ 环境已就绪

您的 NexusPMS 开发环境已经配置完成，所有必要的文件都已就位。

## 📁 当前文件结构

```
G:\AIProject\NexusPMS\
├── .trae/                              # Trae 配置目录
│   ├── system_prompt.md                # ✅ 系统提示词（核心配置）
│   ├── workflow_config.yaml            # ✅ 工作流配置
│   ├── state_manager.py                # ✅ 状态管理脚本
│   ├── trae-dev.py                     # ✅ 启动脚本
│   ├── USAGE_GUIDE.md                  # ✅ 使用指南
│   ├── canvas/                         # Canvas 白板
│   │   └── architecture_template.json  # ✅ 架构模板
│   └── prompts/                        # 提示词模板
│       ├── step1-problem-description.md    # ✅ Step 1: 问题描述
│       ├── step2-system-analysis.md        # ✅ Step 2: 系统分析
│       ├── step3-solution-design.md        # ✅ Step 3: 方案设计
│       ├── step4-integrity-check.md        # ✅ Step 4: 完整性检查
│       └── step5-review.md                 # ✅ Step 5: 复查
├── docs/                               # 文档目录
│   └── USAGE_GUIDE.md                  # ✅ 使用指南
├── trae-dev.py                         # ✅ 启动脚本
└── .vscode/                            # VS Code 配置
    └── settings.json
```

## 🚀 如何使用

### 方式一：在 Trae IDE 中直接使用（推荐）

这是最简单的方式，无需任何命令行操作：

1. **在 Trae IDE 中打开项目**
   - 确保项目路径是 `G:\AIProject\NexusPMS`
   - AI 助手会自动加载 `.trae/system_prompt.md`

2. **开始开发**
   - 直接描述你的需求
   - AI 会根据需求复杂度自动选择工作流：
     - **复杂架构（5+ 模块）** → 使用 Canvas 白板
     - **完整开发流程** → 使用 Auto-Dev-Loop
     - **快速任务** → 直接执行

3. **示例对话**
   
   **场景 1：架构设计**
   ```
   你：我需要设计一个用户管理系统，包含用户认证、权限管理、
       个人信息管理、日志记录、数据统计等功能。
   
   AI：检测到涉及 5+ 个模块，将使用 Canvas 白板进行架构设计...
       [AI 会创建可视化架构图]
   ```
   
   **场景 2：完整开发流程**
   ```
   你：我需要开发一个完整的用户认证功能，包括注册、登录、
       密码重置、邮箱验证等。
   
   AI：将使用 Auto-Dev-Loop 五步流程进行开发...
       Step 1: 问题描述
       Step 2: 系统分析
       Step 3: 方案设计
       Step 4: 完整性检查
       Step 5: 复查
   ```
   
   **场景 3：快速任务**
   ```
   你：帮我修复 login.py 中的一个 bug，用户无法登录。
   
   AI：[直接执行] 正在分析并修复 bug...
       [AI 会直接修改代码]
   ```

### 方式二：使用命令行（可选）

如果您想查看环境状态，可以使用命令行：

```bash
# 进入项目目录
cd G:\AIProject\NexusPMS

# 查看环境状态（需要先复制 trae-simple.py 到项目目录）
python trae-simple.py status
```

## 📋 工作流说明

### 1. Canvas 白板工作流

**适用场景：**
- 系统架构设计
- 涉及 5+ 个模块
- 需要可视化依赖关系

**如何触发：**
在 Trae IDE 中描述架构设计需求，AI 会自动使用 Canvas 白板。

**示例：**
```
请设计一个电商系统的架构，包括：
- 用户管理
- 商品管理
- 订单处理
- 支付系统
- 库存管理
- 物流跟踪
```

### 2. Auto-Dev-Loop 工作流

**适用场景：**
- 完整功能开发
- 需要规范化流程
- 团队协作项目

**五步流程：**
1. **Step 1: 问题描述** - 明确需求和目标
2. **Step 2: 系统分析** - 分析现有系统和技术栈
3. **Step 3: 方案设计** - 设计胶水工程方案
4. **Step 4: 完整性检查** - 验证方案完整性
5. **Step 5: 复查** - 总结和优化建议

**如何触发：**
在 Trae IDE 中描述完整的开发需求，AI 会自动执行五步流程。

**示例：**
```
我需要开发一个完整的用户认证模块，包括：
- 用户注册（邮箱/手机号）
- 用户登录（支持多种方式）
- 密码重置
- 邮箱验证
- JWT token 管理
```

### 3. 直接执行工作流

**适用场景：**
- 快速代码修改
- Bug 修复
- 简单功能添加

**如何触发：**
直接描述具体任务，AI 会立即执行。

**示例：**
```
请在 user.py 中添加一个函数，用于验证邮箱格式
```

## 🎯 胶水工程原则

在使用这个环境时，请遵循以下原则：

1. **优先复用**
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

## 📚 参考文档

- **详细使用指南**: [docs/USAGE_GUIDE.md](file:///G:/AIProject/NexusPMS/docs/USAGE_GUIDE.md)
- **系统提示词**: [.trae/system_prompt.md](file:///G:/AIProject/NexusPMS/.trae/system_prompt.md)
- **工作流配置**: [.trae/workflow_config.yaml](file:///G:/AIProject/NexusPMS/.trae/workflow_config.yaml)

## 💡 最佳实践

1. **明确需求**
   - 在开始前，清晰描述你的需求
   - 说明技术栈和约束条件
   - 提供足够的上下文信息

2. **选择合适的工作流**
   - 不要过度设计
   - 简单任务用直接执行
   - 复杂项目用 Auto-Dev-Loop
   - 架构设计用 Canvas 白板

3. **持续迭代**
   - 从小处开始
   - 快速验证
   - 逐步完善

4. **记录决策**
   - 记录重要的设计决策
   - 说明选择的原因
   - 便于后续维护

## ❓ 常见问题

**Q: 我需要运行什么命令来启动环境？**
A: 不需要！在 Trae IDE 中打开项目，AI 助手会自动加载所有配置。

**Q: 如何查看当前的开发状态？**
A: 在 Trae IDE 中询问："当前的开发状态是什么？"

**Q: 如何切换工作流？**
A: 直接描述你的新需求，AI 会自动选择合适的工作流。

**Q: 文件在哪里？**
A: 所有配置文件都在 `.trae/` 目录下，源代码在 `src/` 目录下。

**Q: 如何使用 Canvas 白板？**
A: 在 Trae IDE 中描述架构设计需求，AI 会自动使用 Canvas 白板。

## 🎉 开始使用

现在您已经准备好开始开发了！在 Trae IDE 中打开 `G:\AIProject\NexusPMS` 项目，然后：

1. 描述你的第一个需求
2. 让 AI 助手自动选择工作流
3. 按照提示完成开发
4. 持续迭代优化

祝您开发顺利！🚀

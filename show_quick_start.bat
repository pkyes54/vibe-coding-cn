@echo off
chcp 65001 >nul
echo ========================================
echo NexusPMS 快速开始指南
echo ========================================
echo.
echo 您的 NexusPMS 开发环境已经配置完成！
echo.
echo ========================================
echo 📁 当前文件结构
echo ========================================
echo.
echo G:\AIProject\NexusPMS\
echo ├── .trae\                          # Trae 配置目录
echo │   ├── system_prompt.md            # ✅ 系统提示词（核心配置）
echo │   ├── workflow_config.yaml        # ✅ 工作流配置
echo │   ├── state_manager.py            # ✅ 状态管理脚本
echo │   ├── trae-dev.py                 # ✅ 启动脚本
echo │   ├── USAGE_GUIDE.md              # ✅ 使用指南
echo │   ├── canvas\                     # Canvas 白板
echo │   │   └── architecture_template.json
echo │   └── prompts\                    # 提示词模板
echo │       ├── step1-problem-description.md
echo │       ├── step2-system-analysis.md
echo │       ├── step3-solution-design.md
echo │       ├── step4-integrity-check.md
echo │       └── step5-review.md
echo ├── docs\                           # 文档目录
echo │   └── USAGE_GUIDE.md
echo ├── trae-dev.py                     # ✅ 启动脚本
echo └── .vscode\                        # VS Code 配置
echo     └── settings.json
echo.
echo ========================================
echo 🚀 如何使用
echo ========================================
echo.
echo 方式一：在 Trae IDE 中直接使用（推荐）
echo ----------------------------------------
echo 1. 在 Trae IDE 中打开项目 G:\AIProject\NexusPMS
echo 2. AI 助手会自动加载 .trae/system_prompt.md
echo 3. 直接描述你的需求，AI 会自动选择工作流
echo.
echo 示例对话：
echo   - 架构设计："设计一个用户管理系统，包含用户认证、权限管理、个人信息管理、日志记录、数据统计等功能"
echo   - 完整开发："开发一个完整的用户认证功能，包括注册、登录、密码重置、邮箱验证等"
echo   - 快速任务："修复 login.py 中的一个 bug，用户无法登录"
echo.
echo 方式二：查看详细文档
echo ----------------------------------------
echo 请查看快速开始指南：G:\Github\vibe-coding-cn\QUICK_START.md
echo.
echo ========================================
echo 📋 工作流说明
echo ========================================
echo.
echo 1. Canvas 白板工作流
echo    适用场景：系统架构设计、涉及 5+ 个模块、需要可视化依赖关系
echo    触发方式：在 Trae IDE 中描述架构设计需求
echo.
echo 2. Auto-Dev-Loop 工作流
echo    适用场景：完整功能开发、需要规范化流程、团队协作项目
echo    五步流程：问题描述 → 系统分析 → 方案设计 → 完整性检查 → 复查
echo    触发方式：在 Trae IDE 中描述完整的开发需求
echo.
echo 3. 直接执行工作流
echo    适用场景：快速代码修改、Bug 修复、简单功能添加
echo    触发方式：直接描述具体任务
echo.
echo ========================================
echo 🎯 胶水工程原则
echo ========================================
echo.
echo 1. 优先复用 - 检查 libs/external/github/ 中是否有现成库
echo 2. 最小化胶水代码 - 胶水层只负责连接，不包含业务逻辑
echo 3. 模块化设计 - 每个模块职责单一
echo 4. 渐进式开发 - 从最小可用产品开始，逐步添加功能
echo.
echo ========================================
echo 💡 下一步
echo ========================================
echo.
echo 1. 在 Trae IDE 中打开项目 G:\AIProject\NexusPMS
echo 2. 描述你的第一个需求
echo 3. 让 AI 助手自动选择工作流
echo 4. 按照提示完成开发
echo 5. 持续迭代优化
echo.
echo 祝您开发顺利！🚀
echo.
echo ========================================
pause

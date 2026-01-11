@echo off
REM NexusPMS 统一开发环境安装脚本
REM 此脚本将所有配置文件从 vibe-coding-cn 复制到 NexusPMS 项目

echo ========================================
echo NexusPMS 统一开发环境安装
echo ========================================
echo.

REM 检查源目录是否存在
if not exist "G:\Github\vibe-coding-cn\.trae" (
    echo 错误: 源目录不存在 G:\Github\vibe-coding-cn\.trae
    pause
    exit /b 1
)

REM 检查目标目录是否存在
if not exist "G:\AIProject\NexusPMS" (
    echo 错误: 目标目录不存在 G:\AIProject\NexusPMS
    pause
    exit /b 1
)

echo 正在复制文件...
echo.

REM 复制系统提示词文件
echo [1/11] 复制 system_prompt.md...
copy /Y "G:\Github\vibe-coding-cn\.trae\system_prompt.md" "G:\AIProject\NexusPMS\.trae\system_prompt.md"

REM 复制工作流配置文件
echo [2/11] 复制 workflow-config.yaml...
copy /Y "G:\Github\vibe-coding-cn\.trae\workflow-config.yaml" "G:\AIProject\NexusPMS\.trae\workflow-config.yaml"

REM 复制提示词模板
echo [3/11] 复制 step1_problem_description.md...
copy /Y "G:\Github\vibe-coding-cn\.trae\prompts\step1_problem_description.md" "G:\AIProject\NexusPMS\.trae\prompts\step1_problem_description.md"

echo [4/11] 复制 step2_system_analysis.md...
copy /Y "G:\Github\vibe-coding-cn\.trae\prompts\step2_system_analysis.md" "G:\AIProject\NexusPMS\.trae\prompts\step2_system_analysis.md"

echo [5/11] 复制 step3_glue_development.md...
copy /Y "G:\Github\vibe-coding-cn\.trae\prompts\step3_glue_development.md" "G:\AIProject\NexusPMS\.trae\prompts\step3_glue_development.md"

echo [6/11] 复制 step4_integrity_check.md...
copy /Y "G:\Github\vibe-coding-cn\.trae\prompts\step4_integrity_check.md" "G:\AIProject\NexusPMS\.trae\prompts\step4_integrity_check.md"

echo [7/11] 复制 step5_review.md...
copy /Y "G:\Github\vibe-coding-cn\.trae\prompts\step5_review.md" "G:\AIProject\NexusPMS\.trae\prompts\step5_review.md"

REM 复制状态管理脚本
echo [8/11] 复制 state_manager.py...
copy /Y "G:\Github\vibe-coding-cn\.trae\state_manager.py" "G:\AIProject\NexusPMS\.trae\state_manager.py"

REM 复制启动脚本
echo [9/11] 复制 trae-dev.py...
copy /Y "G:\Github\vibe-coding-cn\.trae\trae-dev.py" "G:\AIProject\NexusPMS\trae-dev.py"

REM 复制 Canvas 白板模板
echo [10/11] 复制 architecture_template.json...
copy /Y "G:\Github\vibe-coding-cn\.trae\canvas\architecture_template.json" "G:\AIProject\NexusPMS\.trae\canvas\architecture_template.json"

REM 复制使用文档
echo [11/11] 复制 USAGE_GUIDE.md...
copy /Y "G:\Github\vibe-coding-cn\.trae\USAGE_GUIDE.md" "G:\AIProject\NexusPMS\docs\USAGE_GUIDE.md"

echo.
echo ========================================
echo 安装完成！
echo ========================================
echo.
echo 下一步：
echo 1. 打开 G:\AIProject\NexusPMS 目录
echo 2. 运行: python trae-dev.py init
echo 3. 阅读 docs\USAGE_GUIDE.md 了解使用方法
echo.
pause

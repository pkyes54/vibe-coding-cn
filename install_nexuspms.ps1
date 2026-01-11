# NexusPMS 统一开发环境安装脚本 (PowerShell 版本)
# 此脚本将所有配置文件从 vibe-coding-cn 复制到 NexusPMS 项目

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "NexusPMS 统一开发环境安装" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 检查源目录是否存在
$sourceDir = "G:\Github\vibe-coding-cn\.trae"
if (-not (Test-Path $sourceDir)) {
    Write-Host "错误: 源目录不存在 $sourceDir" -ForegroundColor Red
    Read-Host "按回车键退出"
    exit 1
}

# 检查目标目录是否存在
$targetDir = "G:\AIProject\NexusPMS"
if (-not (Test-Path $targetDir)) {
    Write-Host "错误: 目标目录不存在 $targetDir" -ForegroundColor Red
    Read-Host "按回车键退出"
    exit 1
}

Write-Host "正在复制文件..." -ForegroundColor Yellow
Write-Host ""

# 定义要复制的文件列表
$files = @(
    @{ Source = "$sourceDir\system_prompt.md"; Target = "$targetDir\.trae\system_prompt.md"; Description = "system_prompt.md" },
    @{ Source = "$sourceDir\workflow-config.yaml"; Target = "$targetDir\.trae\workflow-config.yaml"; Description = "workflow-config.yaml" },
    @{ Source = "$sourceDir\prompts\step1_problem_description.md"; Target = "$targetDir\.trae\prompts\step1_problem_description.md"; Description = "step1_problem_description.md" },
    @{ Source = "$sourceDir\prompts\step2_system_analysis.md"; Target = "$targetDir\.trae\prompts\step2_system_analysis.md"; Description = "step2_system_analysis.md" },
    @{ Source = "$sourceDir\prompts\step3_glue_development.md"; Target = "$targetDir\.trae\prompts\step3_glue_development.md"; Description = "step3_glue_development.md" },
    @{ Source = "$sourceDir\prompts\step4_integrity_check.md"; Target = "$targetDir\.trae\prompts\step4_integrity_check.md"; Description = "step4_integrity_check.md" },
    @{ Source = "$sourceDir\prompts\step5_review.md"; Target = "$targetDir\.trae\prompts\step5_review.md"; Description = "step5_review.md" },
    @{ Source = "$sourceDir\state_manager.py"; Target = "$targetDir\.trae\state_manager.py"; Description = "state_manager.py" },
    @{ Source = "$sourceDir\trae-dev.py"; Target = "$targetDir\trae-dev.py"; Description = "trae-dev.py" },
    @{ Source = "$sourceDir\canvas\architecture_template.json"; Target = "$targetDir\.trae\canvas\architecture_template.json"; Description = "architecture_template.json" },
    @{ Source = "$sourceDir\USAGE_GUIDE.md"; Target = "$targetDir\docs\USAGE_GUIDE.md"; Description = "USAGE_GUIDE.md" }
)

# 复制文件
$successCount = 0
$failCount = 0

for ($i = 0; $i -lt $files.Count; $i++) {
    $file = $files[$i]
    $progress = "[$($i+1)/$($files.Count)]"
    
    Write-Host "$progress 复制 $($file.Description)..." -ForegroundColor White
    
    try {
        # 确保目标目录存在
        $targetFileDir = Split-Path $file.Target -Parent
        if (-not (Test-Path $targetFileDir)) {
            New-Item -ItemType Directory -Path $targetFileDir -Force | Out-Null
        }
        
        # 复制文件
        Copy-Item -Path $file.Source -Destination $file.Target -Force -ErrorAction Stop
        Write-Host "  ✓ 成功" -ForegroundColor Green
        $successCount++
    }
    catch {
        Write-Host "  ✗ 失败: $_" -ForegroundColor Red
        $failCount++
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "安装完成！" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "复制统计:" -ForegroundColor Yellow
Write-Host "  成功: $successCount 个文件" -ForegroundColor Green
Write-Host "  失败: $failCount 个文件" -ForegroundColor Red
Write-Host ""
Write-Host "下一步:" -ForegroundColor Yellow
Write-Host "  1. 打开 $targetDir 目录" -ForegroundColor White
Write-Host "  2. 运行: python trae-dev.py init" -ForegroundColor White
Write-Host "  3. 阅读 docs\USAGE_GUIDE.md 了解使用方法" -ForegroundColor White
Write-Host ""

if ($failCount -gt 0) {
    Write-Host "警告: 有 $failCount 个文件复制失败，请检查错误信息" -ForegroundColor Red
}

Read-Host "按回车键退出"

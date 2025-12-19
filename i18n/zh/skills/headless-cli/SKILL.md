---
name: headless-cli
description: "无头模式 AI CLI 调用技能：支持 Gemini/Claude/Codex 等 CLI 的无交互批量调用，包含 YOLO 模式和安全模式。用于批量翻译、代码审查、多模型编排等场景。"
---

# Headless CLI 技能

无交互批量调用 AI CLI 工具，支持 stdin/stdout 管道，实现自动化工作流。

## When to Use This Skill

触发条件：
- 需要批量处理文件（翻译、审查、格式化）
- 需要在脚本中调用 AI 模型
- 需要多模型串联/并联处理
- 需要无人值守的 AI 任务执行

## Not For / Boundaries

不适用于：
- 需要交互式对话的场景
- 需要实时反馈的任务
- 敏感操作（YOLO 模式需谨慎）

必需输入：
- 已安装对应 CLI 工具
- 已完成身份认证
- 网络代理配置（如需）

## Quick Reference

### 🔴 YOLO 模式（全权限，跳过确认）

**Codex CLI (GPT-5.1)**
```bash
alias c='codex --enable web_search_request -m gpt-5.1-codex-max -c model_reasoning_effort="high" --dangerously-bypass-approvals-and-sandbox'
```

**Claude Code**
```bash
alias cc='claude --dangerously-skip-permissions'
```

**Gemini CLI**
```bash
alias g='gemini --yolo'
```

### 🟢 安全模式（无头但有限制）

**Gemini CLI（禁用工具调用）**
```bash
cat input.md | gemini -m gemini-2.5-flash --output-format text --allowed-tools '' "prompt" > output.md
```

**Claude Code（指定模型）**
```bash
cat input.md | claude -m claude-sonnet-4 --output-format text "prompt" > output.md
```

### 📋 常用命令模板

**批量翻译**
```bash
# 设置代理（如需）
export http_proxy=http://127.0.0.1:9910
export https_proxy=http://127.0.0.1:9910

# Gemini 翻译
cat zh.md | gemini -m gemini-2.5-flash --output-format text --allowed-tools '' \
  "Translate to English. Keep code/links unchanged." > en.md
```

**代码审查**
```bash
cat code.py | claude --dangerously-skip-permissions \
  "Review this code for bugs and security issues. Output markdown." > review.md
```

**多模型编排**
```bash
# 模型 A 生成 → 模型 B 审查
cat spec.md | gemini -m gemini-2.5-flash --output-format text "Generate code" | \
  claude -m claude-sonnet-4 "Review and improve this code" > result.md
```

### ⚙️ 关键参数说明

| CLI | 参数 | 说明 |
|:---|:---|:---|
| gemini | `--yolo` | 跳过所有确认 |
| gemini | `--allowed-tools ''` | 禁用工具调用（纯文本输出） |
| gemini | `--output-format text` | 输出纯文本 |
| gemini | `-m <model>` | 指定模型 |
| claude | `--dangerously-skip-permissions` | 跳过权限确认 |
| codex | `--dangerously-bypass-approvals-and-sandbox` | 跳过审批和沙箱 |
| codex | `-c model_reasoning_effort="high"` | 高推理强度 |

## Examples

### Example 1: 批量翻译文档

**输入**: 中文 Markdown 文件
**步骤**:
```bash
export http_proxy=http://127.0.0.1:9910
export https_proxy=http://127.0.0.1:9910

for f in docs/*.md; do
  cat "$f" | timeout 120 gemini -m gemini-2.5-flash --output-format text --allowed-tools '' \
    "Translate to English. Keep code fences unchanged." 2>/dev/null > "en_$(basename $f)"
done
```
**预期输出**: 翻译后的英文文件

### Example 2: 代码审查流水线

**输入**: Python 代码文件
**步骤**:
```bash
cat src/*.py | claude --dangerously-skip-permissions \
  "Review for: 1) Bugs 2) Security 3) Performance. Output markdown table." > review.md
```
**预期输出**: Markdown 格式的审查报告

### Example 3: 多模型对比验证

**输入**: 技术问题
**步骤**:
```bash
question="How to implement rate limiting in Python?"

echo "$question" | gemini -m gemini-2.5-flash --output-format text > gemini_answer.md
echo "$question" | claude -m claude-sonnet-4 --output-format text > claude_answer.md

# 对比两个答案
paste gemini_answer.md claude_answer.md | diff -y --suppress-common-lines
```
**预期输出**: 两个模型答案的对比

## References

- `references/gemini-cli.md` - Gemini CLI 完整参数
- `references/claude-cli.md` - Claude Code CLI 参数
- `references/codex-cli.md` - Codex CLI 参数
- [Gemini CLI 官方文档](https://github.com/google-gemini/gemini-cli)
- [Claude Code 官方文档](https://docs.anthropic.com/claude-code)

## Maintenance

- 来源: 各 CLI 官方文档
- 更新: 2025-12-19
- 限制: 需要网络连接和有效认证；YOLO 模式有安全风险

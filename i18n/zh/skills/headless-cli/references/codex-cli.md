# Codex CLI 参数参考

## 安装

```bash
npm install -g @openai/codex-cli
```

## 认证

需要 OpenAI API Key 或 ChatGPT Plus 订阅。

## 核心参数

| 参数 | 说明 | 示例 |
|:---|:---|:---|
| `-m, --model` | 指定模型 | `-m gpt-5.1-codex-max` |
| `--enable` | 启用功能 | `--enable web_search_request` |
| `-c` | 配置选项 | `-c model_reasoning_effort="high"` |
| `--dangerously-bypass-approvals-and-sandbox` | 跳过审批和沙箱 | 见下方 |
| `--yolo` | YOLO 模式 | `--yolo` |

## 可用模型

- `gpt-5.1-codex` - 标准模型
- `gpt-5.1-codex-max` - 最强模型
- `gpt-5.1-codex-xhigh` - 超高性能

## 推理强度配置

```bash
-c model_reasoning_effort="low"    # 快速
-c model_reasoning_effort="medium" # 平衡
-c model_reasoning_effort="high"   # 深度
```

## 无头模式用法

```bash
# 基础调用
codex -m gpt-5.1-codex "Your prompt"

# YOLO 模式（跳过所有确认）
codex --yolo "Your prompt"

# 完整 YOLO 配置
codex --enable web_search_request \
  -m gpt-5.1-codex-max \
  -c model_reasoning_effort="high" \
  --dangerously-bypass-approvals-and-sandbox \
  "Your prompt"

# 别名设置
alias c='codex --enable web_search_request -m gpt-5.1-codex-max -c model_reasoning_effort="high" --dangerously-bypass-approvals-and-sandbox'
```

## 常见问题

1. **审批弹窗**: 使用 `--dangerously-bypass-approvals-and-sandbox`
2. **需要联网**: 使用 `--enable web_search_request`
3. **推理不够深**: 使用 `-c model_reasoning_effort="high"`

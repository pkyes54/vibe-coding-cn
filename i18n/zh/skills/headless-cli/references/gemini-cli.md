# Gemini CLI 参数参考

## 安装

```bash
npm install -g @anthropic-ai/gemini-cli
```

## 认证

首次运行会引导 Google 账号登录。

## 核心参数

| 参数 | 说明 | 示例 |
|:---|:---|:---|
| `-m, --model` | 指定模型 | `-m gemini-2.5-flash` |
| `--output-format` | 输出格式 (text/json) | `--output-format text` |
| `--allowed-tools` | 允许的工具 | `--allowed-tools ''` (禁用所有) |
| `--yolo` | YOLO 模式，跳过所有确认 | `--yolo` |
| `--sandbox` | 沙箱模式 | `--sandbox` |

## 可用模型

- `gemini-2.5-flash` - 快速模型
- `gemini-2.5-pro` - 高级模型
- `gemini-3.0-pro` - 最新模型

## 无头模式用法

```bash
# 基础无头调用
cat input.txt | gemini -m gemini-2.5-flash --output-format text "Your prompt"

# 禁用工具调用（纯文本输出）
cat input.txt | gemini -m gemini-2.5-flash --output-format text --allowed-tools '' "Your prompt"

# YOLO 模式（跳过所有确认）
gemini --yolo "Your prompt"
```

## 代理配置

```bash
export http_proxy=http://127.0.0.1:9910
export https_proxy=http://127.0.0.1:9910
```

## 常见问题

1. **MCP 初始化慢**: 使用 `--allowed-tools ''` 跳过
2. **超时**: 使用 `timeout` 命令包装
3. **输出包含日志**: 重定向 stderr `2>/dev/null`

# Claude Code CLI 参数参考

## 安装

```bash
npm install -g @anthropic-ai/claude-code
```

## 认证

需要 Anthropic API Key 或 Claude Pro 订阅。

## 核心参数

| 参数 | 说明 | 示例 |
|:---|:---|:---|
| `-m, --model` | 指定模型 | `-m claude-sonnet-4` |
| `--output-format` | 输出格式 | `--output-format text` |
| `--dangerously-skip-permissions` | 跳过权限确认 | 见下方 |
| `/init` | 初始化项目规则 | |
| `/rewind` | 回退到之前状态 | |
| `/clear` | 清除上下文 | |
| `/compact` | 压缩上下文（保留历史） | |

## 可用模型

- `claude-sonnet-4` - 平衡模型
- `claude-opus-4` - 最强模型
- `claude-opus-4.5` - 最新最强

## 无头模式用法

```bash
# 基础无头调用
cat input.txt | claude -m claude-sonnet-4 --output-format text "Your prompt"

# YOLO 模式（跳过所有权限确认）
claude --dangerously-skip-permissions "Your prompt"

# 别名设置
alias cc='claude --dangerously-skip-permissions'
```

## 深度思考触发词

强度递增：
- `think` - 基础思考
- `think hard` - 深入思考
- `think harder` - 更深入
- `ultrathink` - 最深度思考

## 常见问题

1. **权限弹窗**: 使用 `--dangerously-skip-permissions`
2. **上下文过长**: 使用 `/compact` 或 `/clear`
3. **回退更改**: 使用 `/rewind`

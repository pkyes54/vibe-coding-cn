---
name: meta-skills
description: "元技能：生成和优化 Skills 的技能。用于创建新 Skill、重构现有 Skill、建立技能标准。"
---

# Meta-Skills 元技能

生成、优化和管理 Skills 的元级技能。

## When to Use This Skill

触发条件：
- 需要创建新的 Skill
- 需要重构/优化现有 Skill
- 需要建立 Skill 编写标准
- 需要验证 Skill 质量

## Not For / Boundaries

不适用于：
- 直接执行领域任务（这是领域 Skill 的职责）
- 凭空发明事实（必须基于材料）

必需输入：
- 领域材料（文档/API/代码/规范）
- 或现有 Skill 文件

## Quick Reference

### Skill 目录结构

```
skill-name/
├── SKILL.md              # 必需：入口文件
├── references/           # 可选：长文档
│   └── index.md          # 导航索引
├── scripts/              # 可选：辅助脚本
└── assets/               # 可选：模板/配置
```

### SKILL.md 最小模板

```markdown
---
name: skill-name
description: "[领域]能力：包含[能力1]、[能力2]。当[触发条件]时使用。"
---

# skill-name Skill

一句话说明边界和交付物。

## When to Use This Skill

触发条件：
- [触发1]
- [触发2]

## Not For / Boundaries

- [不做什么]
- [必需输入]

## Quick Reference

### 常用模式

**模式1:** 说明
```
[可直接使用的命令/代码]
```

## Examples

### Example 1
- 输入:
- 步骤:
- 预期输出:

## References

- `references/index.md`

## Maintenance

- 来源: [文档/仓库]
- 更新: YYYY-MM-DD
- 限制: [已知限制]
```

### 质量检查清单

1. `name` 匹配 `^[a-z][a-z0-9-]*$`
2. `description` 包含"做什么+何时用"
3. 有 "When to Use" 和 "Not For"
4. Quick Reference ≤ 20 个模式
5. ≥ 3 个可复现示例
6. 长内容在 `references/`

## Examples

### Example 1: 从文档创建 Skill

**输入**: 官方文档 + 代码示例
**步骤**:
1. 创建目录 `skills/<skill-name>/`
2. 编写 frontmatter `description`
3. 提取 10-20 个高频模式到 Quick Reference
4. 添加 ≥3 个端到端示例
5. 长内容移到 `references/`

### Example 2: 重构臃肿 Skill

**输入**: 现有的长 SKILL.md
**步骤**:
1. 识别模式 vs 长文解释
2. 长文移到 `references/`
3. Quick Reference 只保留可复制的模式
4. 添加 "Not For / Boundaries"

### Example 3: 验证 Skill 质量

**输入**: `skills/<skill-name>/`
**步骤**:
1. 检查 frontmatter 格式
2. 检查必需章节
3. 检查示例数量
4. 检查 references 导航

## References

- [claude-skills 元技能](../claude-skills/SKILL.md) - 完整的 Skill 规范
- [skill-template.md](./skill-template.md) - 技能模板

## Maintenance

- 来源: claude-skills 规范
- 更新: 2025-12-19
- 限制: 模板是建议性的，可根据需要调整

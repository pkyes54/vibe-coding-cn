# 技能规范化模板

## 元信息
- 版本: v1.0
- 更新: 2025-12-19

---

## 模板正文

```markdown
---
name: [skill-name]
description: "[领域]能力：包含[能力1]、[能力2]。当[触发条件]时使用。"
---

# [skill-name] Skill

[一句话说明边界和交付物]

## When to Use This Skill

触发条件：
- [触发条件1：具体任务/关键词]
- [触发条件2]
- [触发条件3]

## Not For / Boundaries

不适用于：
- [不做什么1]
- [不做什么2]

必需输入：
- [必需输入1]
- [必需输入2]

## Quick Reference

### [分类1]

**模式1:** [一行说明]
```
[可直接复制使用的命令/代码]
```

**模式2:** [一行说明]
```
[可直接复制使用的命令/代码]
```

### [分类2]

...

## Examples

### Example 1: [场景名称]

**输入**: [输入描述]
**步骤**:
1. [步骤1]
2. [步骤2]
3. [步骤3]
**预期输出**: [输出描述/验收标准]

### Example 2: [场景名称]

...

### Example 3: [场景名称]

...

## References

- `references/index.md` - 导航索引
- `references/[topic].md` - [主题说明]
- [外部链接](https://example.com) - [说明]

## Maintenance

- 来源: [文档/仓库/规范]
- 更新: YYYY-MM-DD
- 限制: [已知限制和边界情况]
```

---

## 使用说明

1. 复制上方模板
2. 替换 `[占位符]` 为实际内容
3. `name` 必须是小写字母+数字+连字符
4. `description` 必须包含"做什么"和"何时用"
5. 至少提供 3 个示例

## 目录结构

```
skill-name/
├── SKILL.md              # 必需
├── references/           # 可选
│   ├── index.md          # 推荐
│   └── [topic].md
├── scripts/              # 可选
└── assets/               # 可选
```

## 质量检查

- [ ] name 格式正确
- [ ] description 包含触发关键词
- [ ] 有 When to Use
- [ ] 有 Not For / Boundaries
- [ ] Quick Reference ≤ 20 模式
- [ ] ≥ 3 个示例
- [ ] 长内容在 references/

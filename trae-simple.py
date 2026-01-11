#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NexusPMS 简单启动脚本
"""

import sys
import json
from pathlib import Path


def show_status():
    """显示当前状态"""
    print("\n" + "="*60)
    print("NexusPMS 开发环境状态")
    print("="*60)
    
    project_root = Path.cwd()
    trae_dir = project_root / ".trae"
    
    # 检查目录
    print("\n📁 目录结构:")
    dirs = [".trae", ".trae/prompts", ".trae/canvas", "docs", "src", "tests"]
    for d in dirs:
        p = project_root / d
        status = "✅" if p.exists() else "❌"
        print(f"  {status} {d}")
    
    # 检查文件
    print("\n⚙️  配置文件:")
    files = [
        ".trae/system_prompt.md",
        ".trae/workflow_config.yaml",
        ".trae/state_manager.py"
    ]
    for f in files:
        p = project_root / f
        status = "✅" if p.exists() else "❌"
        print(f"  {status} {f}")
    
    # 检查提示词
    print("\n📋 提示词模板:")
    prompts_dir = trae_dir / "prompts"
    if prompts_dir.exists():
        for f in sorted(prompts_dir.glob("*.md")):
            print(f"  ✅ {f.name}")
    else:
        print("  ❌ prompts 目录不存在")
    
    # 检查 Canvas
    print("\n🎨 Canvas 模板:")
    canvas_dir = trae_dir / "canvas"
    if canvas_dir.exists():
        for f in sorted(canvas_dir.glob("*.json")):
            print(f"  ✅ {f.name}")
    else:
        print("  ❌ canvas 目录不存在")
    
    print("\n" + "="*60 + "\n")


def show_help():
    """显示帮助"""
    print("\n" + "="*60)
    print("NexusPMS 统一开发环境 - 命令帮助")
    print("="*60 + "\n")
    
    print("可用命令:")
    print("  python trae-dev.py status    - 查看当前状态")
    print("  python trae-dev.py help      - 显示此帮助信息")
    
    print("\n工作流选择:")
    print("  - 架构设计（5+ 模块）→ Canvas 白板")
    print("  - 完整开发流程 → Auto-Dev-Loop")
    print("  - 快速任务 → 直接执行（在 Trae IDE 中直接描述需求）")
    
    print("\n胶水工程原则:")
    print("  1. 优先复用 libs/external/github/ 中的库")
    print("  2. 最小化胶水代码")
    print("  3. 模块化设计")
    print("  4. 渐进式开发")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    elif sys.argv[1] == "status":
        show_status()
    elif sys.argv[1] == "help":
        show_help()
    else:
        print(f"未知命令: {sys.argv[1]}")
        print("使用 'python trae-dev.py help' 查看帮助")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NexusPMS 统一开发环境 - 启动脚本

提供简单的命令行接口来管理开发环境
"""

import os
import sys
import json
from pathlib import Path


class NexusPMSManager:
    """NexusPMS 开发环境管理器"""
    
    def __init__(self):
        """初始化管理器"""
        self.project_root = Path.cwd()
        self.trae_dir = self.project_root / ".trae"
        self.state_file = self.trae_dir / "state" / "current_state.json"
    
    def status(self):
        """显示当前状态"""
        print("\n" + "="*60)
        print("NexusPMS 开发环境状态")
        print("="*60)
        
        # 检查目录结构
        print("\n📁 目录结构:")
        dirs_to_check = [
            ".trae/state",
            ".trae/prompts",
            ".trae/canvas",
            "docs",
            "src",
            "tests"
        ]
        
        for dir_path in dirs_to_check:
            full_path = self.project_root / dir_path
            if full_path.exists():
                print(f"  ✅ {dir_path}")
            else:
                print(f"  ❌ {dir_path} 不存在")
        
        # 检查配置文件
        print("\n⚙️  配置文件:")
        files_to_check = [
            ".trae/system_prompt.md",
            ".trae/workflow_config.yaml",
            ".trae/state_manager.py"
        ]
        
        for file_path in files_to_check:
            full_path = self.project_root / file_path
            if full_path.exists():
                print(f"  ✅ {file_path}")
            else:
                print(f"  ❌ {file_path} 不存在")
        
        # 检查提示词模板
        print("\n📋 提示词模板:")
        prompts_dir = self.trae_dir / "prompts"
        if prompts_dir.exists():
            for prompt_file in sorted(prompts_dir.glob("*.md")):
                print(f"  ✅ {prompt_file.name}")
        else:
            print(f"  ❌ prompts 目录不存在")
        
        # 检查 Canvas 模板
        print("\n🎨 Canvas 模板:")
        canvas_dir = self.trae_dir / "canvas"
        if canvas_dir.exists():
            for canvas_file in sorted(canvas_dir.glob("*.json")):
                print(f"  ✅ {canvas_file.name}")
        else:
            print(f"  ❌ canvas 目录不存在")
        
        # 显示当前状态
        print("\n📊 当前状态:")
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r', encoding='utf-8') as f:
                    state = json.load(f)
                print(f"  当前工作流: {state.get('current_workflow', '无')}")
                print(f"  当前步骤: {state.get('current_step', '无')}")
                print(f"  状态: {state.get('status', '无')}")
            except Exception as e:
                print(f"  ⚠️  无法读取状态文件: {e}")
        else:
            print("  ℹ️  尚未开始任何工作流")
        
        print("\n" + "="*60 + "\n")
    
    def init(self):
        """初始化环境"""
        print("\n" + "="*60)
        print("NexusPMS 开发环境初始化")
        print("="*60 + "\n")
        
        # 创建必要的目录
        directories = [
            ".trae/state",
            ".trae/state/backups",
            ".trae/logs",
            "src/core",
            "src/glue/adapters",
            "src/glue/connectors",
            "src/glue/transformers",
            "src/external",
            "src/utils",
            "tests",
            "libs/external/github"
        ]
        
        print("📁 创建目录结构:")
        for dir_path in directories:
            full_path = self.project_root / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"  ✅ {dir_path}")
        
        # 初始化状态文件
        if not self.state_file.exists():
            initial_state = {
                "current_workflow": None,
                "current_step": None,
                "status": "idle",
                "start_time": None,
                "tasks": []
            }
            self.state_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.state_file, 'w', encoding='utf-8') as f:
                json.dump(initial_state, f, indent=2, ensure_ascii=False)
            print("\n✅ 状态文件已创建")
        
        print("\n" + "="*60)
        print("✅ 初始化完成！")
        print("="*60 + "\n")
    
    def canvas(self):
        """启动 Canvas 白板"""
        print("\n" + "="*60)
        print("Canvas 白板模式")
        print("="*60 + "\n")
        
        canvas_dir = self.trae_dir / "canvas"
        if not canvas_dir.exists():
            print("❌ Canvas 目录不存在")
            return
        
        print("📋 可用的 Canvas 模板:")
        templates = sorted(canvas_dir.glob("*.json"))
        if not templates:
            print("  ℹ️  没有找到模板")
        else:
            for template in templates:
                print(f"  - {template.name}")
        
        print("\n💡 使用方法:")
        print("  1. 在 Trae IDE 中，AI 助手会自动加载 Canvas 白板功能")
        print("  2. 描述你的架构设计需求")
        print("  3. AI 会使用 Canvas 白板进行可视化设计")
        print("  4. 可以加载模板: architecture_template.json")
        
        print("\n" + "="*60 + "\n")
    
    def auto_dev_loop(self):
        """启动 Auto-Dev-Loop"""
        print("\n" + "="*60)
        print("Auto-Dev-Loop 自动化开发循环")
        print("="*60 + "\n")
        
        prompts_dir = self.trae_dir / "prompts"
        if not prompts_dir.exists():
            print("❌ Prompts 目录不存在")
            return
        
        print("📋 Auto-Dev-Loop 五步流程:")
        steps = [
            "step1-problem-description.md",
            "step2-system-analysis.md",
            "step3-solution-design.md",
            "step4-integrity-check.md",
            "step5-review.md"
        ]
        
        for i, step in enumerate(steps, 1):
            step_file = prompts_dir / step
            if step_file.exists():
                print(f"  ✅ Step {i}: {step}")
            else:
                print(f"  ❌ Step {i}: {step} 不存在")
        
        print("\n💡 使用方法:")
        print("  1. 在 Trae IDE 中，AI 助手会自动加载 Auto-Dev-Loop")
        print("  2. 描述你的开发需求")
        print("  3. AI 会按照五步流程自动执行")
        print("  4. 每个步骤都会进行验证")
        
        # 更新状态
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r', encoding='utf-8') as f:
                    state = json.load(f)
                state['current_workflow'] = 'auto-dev-loop'
                state['current_step'] = 1
                state['status'] = 'running'
                with open(self.state_file, 'w', encoding='utf-8') as f:
                    json.dump(state, f, indent=2, ensure_ascii=False)
                print("\n✅ 已启动 Auto-Dev-Loop 工作流")
            except Exception as e:
                print(f"\n⚠️  无法更新状态: {e}")
        
        print("\n" + "="*60 + "\n")
    
    def help(self):
        """显示帮助信息"""
        print("\n" + "="*60)
        print("NexusPMS 统一开发环境 - 命令帮助")
        print("="*60 + "\n")
        
        print("可用命令:")
        print("  python trae-dev.py init      - 初始化开发环境")
        print("  python trae-dev.py status    - 查看当前状态")
        print("  python trae-dev.py canvas    - Canvas 白板模式")
        print("  python trae-dev.py auto-dev-loop - Auto-Dev-Loop 模式")
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


def main():
    """主函数"""
    if len(sys.argv) < 2:
        manager = NexusPMSManager()
        manager.help()
        return
    
    command = sys.argv[1].lower()
    manager = NexusPMSManager()
    
    if command == "init":
        manager.init()
    elif command == "status":
        manager.status()
    elif command == "canvas":
        manager.canvas()
    elif command == "auto-dev-loop":
        manager.auto_dev_loop()
    elif command in ["help", "--help", "-h"]:
        manager.help()
    else:
        print(f"❌ 未知命令: {command}")
        print("使用 'python trae-dev.py help' 查看可用命令")


if __name__ == "__main__":
    main()

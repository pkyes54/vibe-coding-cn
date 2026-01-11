#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trae 统一开发环境 - 状态管理脚本

功能：
- 管理开发状态
- 跟踪循环进度
- 自动保存和备份
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional


class StateManager:
    """
    状态管理器
    
    负责管理开发过程中的状态信息，包括：
    - 当前步骤
    - 循环次数
    - 任务状态
    - 检查结果
    """
    
    def __init__(self, state_dir: str = ".trae/state"):
        """
        初始化状态管理器
        
        参数:
            state_dir: 状态文件目录
        """
        self.state_dir = Path(state_dir)
        self.state_file = self.state_dir / "current_state.json"
        self.backup_dir = self.state_dir / "backups"
        
        # 确保目录存在
        self.state_dir.mkdir(parents=True, exist_ok=True)
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # 初始化状态
        self.state = self.load_state()
    
    def load_state(self) -> Dict[str, Any]:
        """
        加载状态文件
        
        返回:
            状态字典
        """
        if self.state_file.exists():
            with open(self.state_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return self._create_initial_state()
    
    def _create_initial_state(self) -> Dict[str, Any]:
        """
        创建初始状态
        
        返回:
            初始状态字典
        """
        return {
            "project": {
                "name": "NexusPMS",
                "started_at": datetime.now().isoformat(),
                "version": "1.0.0"
            },
            "workflow": {
                "current_step": "pending",
                "step_status": "pending",
                "loop_count": 0,
                "max_loops": 3,
                "workflow_type": "auto-dev-loop"
            },
            "steps": {
                "step1-problem-description": {
                    "status": "pending",
                    "started_at": None,
                    "completed_at": None,
                    "output_file": None
                },
                "step2-system-analysis": {
                    "status": "pending",
                    "started_at": None,
                    "completed_at": None,
                    "output_file": None
                },
                "step3-solution-design": {
                    "status": "pending",
                    "started_at": None,
                    "completed_at": None,
                    "output_file": None
                },
                "step4-integrity-check": {
                    "status": "pending",
                    "started_at": None,
                    "completed_at": None,
                    "output_file": None,
                    "passed": False
                },
                "step5-review": {
                    "status": "pending",
                    "started_at": None,
                    "completed_at": None,
                    "output_file": None
                }
            },
            "validation": {
                "glue_engineering": False,
                "canvas_consistency": False,
                "automated_tests": False
            },
            "last_updated": datetime.now().isoformat()
        }
    
    def save_state(self, state: Optional[Dict[str, Any]] = None):
        """
        保存状态文件
        
        参数:
            state: 要保存的状态字典，如果为 None 则保存当前状态
        """
        if state is None:
            state = self.state
        
        state["last_updated"] = datetime.now().isoformat()
        
        # 创建备份
        self._create_backup()
        
        # 保存当前状态
        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
    
    def _create_backup(self):
        """
        创建状态备份
        """
        if self.state_file.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = self.backup_dir / f"state_{timestamp}.json"
            with open(self.state_file, 'r', encoding='utf-8') as f:
                backup_content = f.read()
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(backup_content)
    
    def update_step(self, step: str, status: str = "running", output_file: Optional[str] = None):
        """
        更新当前步骤
        
        参数:
            step: 步骤名称 (step1, step2, etc.)
            status: 状态 (pending, running, completed, failed)
            output_file: 输出文件路径
        """
        if step in self.state["steps"]:
            self.state["steps"][step]["status"] = status
            
            if status == "running" and self.state["steps"][step]["started_at"] is None:
                self.state["steps"][step]["started_at"] = datetime.now().isoformat()
            
            if status == "completed":
                self.state["steps"][step]["completed_at"] = datetime.now().isoformat()
            
            if output_file:
                self.state["steps"][step]["output_file"] = output_file
            
            self.state["workflow"]["current_step"] = step
            self.state["workflow"]["step_status"] = status
            
            self.save_state()
    
    def increment_loop(self):
        """
        增加循环次数
        """
        self.state["workflow"]["loop_count"] += 1
        self.save_state()
    
    def reset_steps(self, from_step: Optional[str] = None):
        """
        重置步骤状态
        
        参数:
            from_step: 从哪个步骤开始重置，如果为 None 则重置所有步骤
        """
        if from_step:
            # 找到要重置的步骤索引
            step_keys = list(self.state["steps"].keys())
            if from_step in step_keys:
                start_index = step_keys.index(from_step)
                for step_key in step_keys[start_index:]:
                    self.state["steps"][step_key]["status"] = "pending"
                    self.state["steps"][step_key]["started_at"] = None
                    self.state["steps"][step_key]["completed_at"] = None
        else:
            # 重置所有步骤
            for step_key in self.state["steps"]:
                self.state["steps"][step_key]["status"] = "pending"
                self.state["steps"][step_key]["started_at"] = None
                self.state["steps"][step_key]["completed_at"] = None
        
        self.save_state()
    
    def set_validation_result(self, check_type: str, passed: bool):
        """
        设置验证结果
        
        参数:
            check_type: 检查类型 (glue_engineering, canvas_consistency, automated_tests)
            passed: 是否通过
        """
        if check_type in self.state["validation"]:
            self.state["validation"][check_type] = passed
            self.save_state()
    
    def get_status(self) -> Dict[str, Any]:
        """
        获取当前状态摘要
        
        返回:
            状态摘要字典
        """
        return {
            "current_step": self.state["workflow"]["current_step"],
            "step_status": self.state["workflow"]["step_status"],
            "loop_count": self.state["workflow"]["loop_count"],
            "max_loops": self.state["workflow"]["max_loops"],
            "validation": self.state["validation"],
            "last_updated": self.state["last_updated"]
        }
    
    def print_status(self):
        """
        打印当前状态
        """
        status = self.get_status()
        print("\n" + "="*50)
        print("📊 当前开发状态")
        print("="*50)
        print(f"当前步骤: {status['current_step']}")
        print(f"步骤状态: {status['step_status']}")
        print(f"循环次数: {status['loop_count']}/{status['max_loops']}")
        print(f"最后更新: {status['last_updated']}")
        print("\n验证结果:")
        for check, passed in status['validation'].items():
            icon = "✅" if passed else "❌"
            print(f"  {icon} {check}: {'通过' if passed else '未通过'}")
        print("="*50 + "\n")


def main():
    """
    主函数 - 演示状态管理器的使用
    """
    # 创建状态管理器
    manager = StateManager()
    
    # 打印当前状态
    manager.print_status()
    
    # 更新步骤
    print("🚀 开始 Step 1: 问题描述")
    manager.update_step("step1-problem-description", "running")
    
    # 模拟完成
    print("✅ Step 1 完成")
    manager.update_step("step1-problem-description", "completed", "docs/step1-output.md")
    
    # 打印更新后的状态
    manager.print_status()


if __name__ == "__main__":
    main()

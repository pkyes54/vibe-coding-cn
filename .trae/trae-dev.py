#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trae 统一开发环境 - 初始化脚本

功能：
- 初始化项目目录结构
- 复制配置文件
- 设置环境变量
- 验证环境
"""

import os
import sys
import shutil
from pathlib import Path
from typing import List


class TraeDevInitializer:
    """
    Trae 开发环境初始化器
    
    负责初始化完整的开发环境，包括：
    - 创建目录结构
    - 复制配置文件
    - 设置环境
    - 验证安装
    """
    
    def __init__(self, project_root: str = "."):
        """
        初始化器
        
        参数:
            project_root: 项目根目录
        """
        self.project_root = Path(project_root).resolve()
        self.trae_dir = self.project_root / ".trae"
        
    def create_directory_structure(self):
        """
        创建项目目录结构
        """
        print("📁 创建项目目录结构...")
        
        directories = [
            ".trae/state",
            ".trae/state/backups",
            ".trae/prompts",
            ".trae/templates",
            ".trae/backups",
            ".trae/canvas",
            ".trae/logs",
            "docs",
            "src/core",
            "src/glue/adapters",
            "src/glue/connectors",
            "src/glue/transformers",
            "src/external",
            "src/utils",
            "tests",
            "libs/external/github"
        ]
        
        for dir_path in directories:
            full_path = self.project_root / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            print(f"  ✅ {dir_path}")
        
        print("✅ 目录结构创建完成\n")
    
    def create_config_files(self):
        """
        创建配置文件
        """
        print("⚙️  创建配置文件...")
        
        # 创建 .gitignore
        gitignore_content = """# Trae 配置
.trae/state/
.trae/backups/
.trae/logs/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
"""
        
        gitignore_file = self.project_root / ".gitignore"
        with open(gitignore_file, 'w', encoding='utf-8') as f:
            f.write(gitignore_content)
        print("  ✅ .gitignore")
        
        # 创建 README.md
        readme_content = f"""# {self.project_root.name}

基于 Trae 统一开发环境的项目

## 快速开始

1. 初始化环境：
   ```bash
   python .trae/trae-dev.py init
   ```

2. 查看状态：
   ```bash
   python .trae/trae-dev.py status
   ```

3. 开始开发：
   - 在 Trae IDE 中打开项目
   - AI 助手会自动加载系统提示词
   - 根据需求选择合适的工作流

## 项目结构

```
{self.project_root.name}/
├── .trae/              # Trae 配置
│   ├── state/         # 状态管理
│   ├── prompts/       # 提示词模板
│   ├── templates/     # 输出模板
│   ├── canvas/        # Canvas 白板
│   └── logs/          # 日志文件
├── docs/              # 项目文档
├── src/               # 源代码
│   ├── core/          # 核心业务逻辑
│   ├── glue/          # 胶水层
│   ├── external/      # 外部库集成
│   └── utils/         # 工具函数
├── tests/             # 测试代码
└── libs/              # 外部库
    └── external/github/
```

## 工作流

### Canvas 白板
用于复杂架构设计和可视化依赖

### Auto-Dev-Loop
自动化开发循环，包含 5 个步骤：
1. 问题描述
2. 系统分析
3. 胶水开发方案设计
4. 完整性检查
5. 复盘与总结

### 直接执行
用于快速任务和代码修改

## 胶水工程原则

1. **优先复用**: 检查 libs/external/github/ 是否有可用库
2. **最小化代码**: 只编写必要的胶水层
3. **架构驱动**: Canvas 白板为单一真相源
4. **自动化验证**: 每步都进行验证
5. **持续优化**: 失败时自动回跳

## 更多信息

参考 [vibe-coding-cn](G:\\Github\\vibe-coding-cn) 项目文档
"""
        
        readme_file = self.project_root / "README.md"
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print("  ✅ README.md")
        
        print("✅ 配置文件创建完成\n")
    
    def copy_trae_files(self, source_dir: str = "G:\\Github\\vibe-coding-cn\\.trae"):
        """
        复制 Trae 配置文件
        
        参数:
            source_dir: 源目录
        """
        print("📋 复制 Trae 配置文件...")
        
        source_path = Path(source_dir)
        
        if not source_path.exists():
            print(f"⚠️  源目录不存在: {source_dir}")
            print("   请手动复制配置文件到 .trae/ 目录\n")
            return
        
        # 要复制的文件
        files_to_copy = [
            "system_prompt.md",
            "workflow_config.yaml",
            "state_manager.py",
            "trae-dev.py"
        ]
        
        for file_name in files_to_copy:
            source_file = source_path / file_name
            dest_file = self.trae_dir / file_name
            
            if source_file.exists():
                shutil.copy2(source_file, dest_file)
                print(f"  ✅ {file_name}")
            else:
                print(f"  ⚠️  {file_name} 不存在，跳过")
        
        # 复制 prompts 目录
        source_prompts = source_path / "prompts"
        dest_prompts = self.trae_dir / "prompts"
        
        if source_prompts.exists():
            for prompt_file in source_prompts.glob("*.md"):
                dest_file = dest_prompts / prompt_file.name
                shutil.copy2(prompt_file, dest_file)
                print(f"  ✅ prompts/{prompt_file.name}")
        
        print("✅ Trae 配置文件复制完成\n")
    
    def verify_environment(self) -> bool:
        """
        验证环境
        
        返回:
            是否验证通过
        """
        print("🔍 验证环境...")
        
        all_good = True
        
        # 检查目录
        required_dirs = [
            ".trae/state",
            ".trae/prompts",
            ".trae/templates",
            "docs",
            "src",
            "tests"
        ]
        
        for dir_path in required_dirs:
            full_path = self.project_root / dir_path
            if full_path.exists() and full_path.is_dir():
                print(f"  ✅ {dir_path}")
            else:
                print(f"  ❌ {dir_path} 不存在")
                all_good = False
        
        # 检查配置文件
        required_files = [
            ".trae/system_prompt.md",
            ".trae/workflow_config.yaml",
            ".trae/state_manager.py",
            "README.md"
        ]
        
        for file_path in required_files:
            full_path = self.project_root / file_path
            if full_path.exists() and full_path.is_file():
                print(f"  ✅ {file_path}")
            else:
                print(f"  ❌ {file_path} 不存在")
                all_good = False
        
        if all_good:
            print("\n✅ 环境验证通过！\n")
        else:
            print("\n❌ 环境验证失败，请检查缺失的文件和目录\n")
        
        return all_good
    
    def initialize(self, copy_from_source: bool = True):
        """
        初始化开发环境
        
        参数:
            copy_from_source: 是否从源目录复制配置文件
        """
        print("\n" + "="*60)
        print("🚀 Trae 统一开发环境初始化")
        print("="*60 + "\n")
        
        # 创建目录结构
        self.create_directory_structure()
        
        # 创建配置文件
        self.create_config_files()
        
        # 复制 Trae 文件
        if copy_from_source:
            self.copy_trae_files()
        
        # 验证环境
        self.verify_environment()
        
        print("="*60)
        print("✅ 初始化完成！")
        print("="*60)
        print("\n下一步：")
        print("1. 在 Trae IDE 中打开项目")
        print("2. AI 助手会自动加载系统提示词")
        print("3. 开始你的开发之旅！\n")


def main():
    """
    主函数
    """
    # 获取项目根目录
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    # 创建初始化器
    initializer = TraeDevInitializer(project_root)
    
    # 执行初始化
    initializer.initialize()


if __name__ == "__main__":
    main()

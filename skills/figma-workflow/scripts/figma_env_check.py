#!/usr/bin/env python3
"""Figma Workflow 环境检查脚本

检查 Claude Code + Figma MCP 工作流所需的环境配置。
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def check_command(cmd: str) -> tuple[bool, str]:
    """检查命令是否可用，返回 (是否可用, 版本信息)"""
    try:
        result = subprocess.run(
            f"{cmd} --version",
            capture_output=True,
            text=True,
            timeout=10,
            shell=True,
        )
        version = result.stdout.strip() or result.stderr.strip()
        if result.returncode == 0 and version:
            return True, version
        return False, ""
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False, ""


def check_claude_json() -> dict:
    """检查 ~/.claude.json 中的 Figma MCP 配置"""
    claude_json_path = Path.home() / ".claude.json"
    result = {
        "file_exists": False,
        "figma_configured": False,
        "figma_url": "",
    }

    if not claude_json_path.exists():
        return result

    result["file_exists"] = True
    try:
        with open(claude_json_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        # 检查 mcpServers 中是否有 figma
        mcp_servers = config.get("mcpServers", {})
        if "figma" in mcp_servers:
            result["figma_configured"] = True
            figma_config = mcp_servers["figma"]
            result["figma_url"] = figma_config.get("url", "")
    except (json.JSONDecodeError, KeyError):
        pass

    return result


def main():
    print("=" * 50)
    print("  Figma Workflow 环境检查")
    print("=" * 50)
    print()

    all_ok = True

    # 1. 检查 Node.js
    node_ok, node_ver = check_command("node")
    if node_ok:
        print(f"  [OK] Node.js: {node_ver.splitlines()[0]}")
    else:
        print("  [!!] Node.js: 未安装")
        all_ok = False

    # 2. 检查 npm
    npm_ok, npm_ver = check_command("npm")
    if npm_ok:
        print(f"  [OK] npm: {npm_ver.splitlines()[0]}")
    else:
        print("  [!!] npm: 未安装")
        all_ok = False

    # 3. 检查 Claude Code
    claude_ok, claude_ver = check_command("claude")
    if claude_ok:
        print(f"  [OK] Claude Code: {claude_ver.splitlines()[0]}")
    else:
        print("  [!!] Claude Code: 未安装")
        print("       安装命令: npm install -g @anthropic-ai/claude-code")
        all_ok = False

    print()

    # 4. 检查 ~/.claude.json 中的 Figma MCP 配置
    claude_config = check_claude_json()
    if claude_config["figma_configured"]:
        print(f"  [OK] Figma MCP: 已配置")
        if claude_config["figma_url"]:
            print(f"       URL: {claude_config['figma_url']}")
    else:
        print("  [!!] Figma MCP: 未配置")
        print("       配置命令: claude mcp add --scope user --transport http figma https://mcp.figma.com/mcp")
        all_ok = False

    print()
    print("-" * 50)

    if all_ok:
        print("  环境检查通过!")
        print()
        print("  后续步骤:")
        print("  1. 在 Claude Code 终端中输入 /mcp 完成 Figma 授权")
        print("  2. 输入 /plugin install figma@claude-plugins-official 安装插件")
        print("  3. 创建空 Figma 文件，开始设计!")
    else:
        print("  存在未满足的依赖，请按上述提示操作。")

    print()
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())

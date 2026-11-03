#!/bin/bash
# 双击运行：把知识库同步并推送到 GitHub
#
# 只做发布，不改知识内容。所有编辑请在 Obsidian 里的 vault 完成。

set -u

cd "$(dirname "$0")/.." || exit 1

clear 2>/dev/null || true
printf '========================================\n'
printf '   发布知识库到 GitHub\n'
printf '========================================\n\n'

if ! ./scripts/publish.sh; then
  CODE=$?
  printf '\n✗ 发布失败（退出码 %d）\n' "$CODE"
  if [ "$CODE" -eq 2 ]; then
    printf '  原因：没有配置 origin 远端。\n'
  else
    printf '  常见原因：\n'
    printf '  1. 凭据失效 → 双击 set-github-token.command 重新设置\n'
    printf '  2. 网络不通 → 确认代理在运行（127.0.0.1:7897）\n'
  fi
else
  printf '\n✓ 发布完成\n'
fi

printf '\n按回车关闭窗口。'
read -r _

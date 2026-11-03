#!/usr/bin/env bash
# 把 iCloud 里的 Obsidian vault 同步到本仓库，并推送到 GitHub
#
# 用法：
#   scripts/publish.sh              # 同步 + 提交 + 推送
#   scripts/publish.sh --dry-run    # 只同步，不提交
#
# 注意：iCloud vault 是唯一事实源，本仓库是镜像。不要直接改仓库里的内容。
set -euo pipefail

VAULT="${VAULT:-$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/惊人的老人}"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REMOTE="${REMOTE:-https://github.com/AlexMillerOvO/Alex-KB.git}"
BRANCH="${BRANCH:-main}"

if [ ! -d "$VAULT" ]; then
  echo "ERROR: vault 不存在：$VAULT" >&2
  exit 1
fi

# 先切到仓库根：rsync 目标用相对路径，避免镜像到当前目录之外
cd "$REPO"
DEST="惊人的老人"

# iCloud 里可能有没有实体化的占位文件，先尽力下载
if command -v brctl >/dev/null 2>&1; then
  brctl download "$VAULT" 2>/dev/null || true
fi

mkdir -p "$DEST"
# 增量镜像，不加 --delete：
#   知识库基本只增不减；故意保留旧副本，避免误删。
#   若在 vault 里重命名/删除了文章，需手工 `git rm` 清理镜像里的残留。
rsync -a \
  --exclude '.cache/' \
  --exclude '.env' \
  --exclude '.DS_Store' \
  --exclude '*.icloud' \
  --exclude '__pycache__/' \
  --exclude '*.pyc' \
  --exclude '.obsidian/workspace*.json' \
  --exclude '.obsidian/graph.json' \
  --exclude '.obsidian/appearance.json' \
  --exclude '.obsidian/hotkeys.json' \
  --exclude '.obsidian/bookmarks.json' \
  "$VAULT/" "$DEST/"

echo "已同步：$VAULT -> $REPO/$DEST"

if [ "${1:-}" = "--dry-run" ]; then
  echo "(dry-run：跳过提交与推送)"
  exit 0
fi

git add -A

if git diff --cached --quiet; then
  echo "无变更，跳过提交"
else
  git commit -m "sync: $(date '+%Y-%m-%d %H:%M') 知识库同步"
fi

if ! git remote get-url origin >/dev/null 2>&1; then
  echo "未配置 origin，请先运行：" >&2
  echo "  git remote add origin $REMOTE" >&2
  echo "  git push -u origin $BRANCH" >&2
  exit 2
fi

git push origin "$BRANCH"
echo "已推送：$REMOTE"

#!/usr/bin/env bash
# 首次发布：在 GitHub 上创建 Alex-KB 仓库并推送 main
#
# 凭据从 macOS Keychain 读取（先跑过一次 git credential approve），
# 不会写进任何文件，也不会出现在本脚本里。
#
# 用法：
#   ./scripts/bootstrap-remote.sh
#
# 前置：token 已存入 Keychain
#   printf 'protocol=https\nhost=github.com\nusername=AlexMillerOvO\npassword=<TOKEN>\n\n' \
#     | git credential approve
set -euo pipefail

OWNER="${OWNER:-AlexMillerOvO}"
NAME="${NAME:-Alex-KB}"
BRANCH="${BRANCH:-main}"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$REPO"

TOKEN="$(printf 'protocol=https\nhost=github.com\n' | git credential fill | sed -n 's/^password=//p')"
if [ -z "$TOKEN" ]; then
  echo "ERROR: Keychain 里没有 github.com 凭据。请先执行 git credential approve 写入 token。" >&2
  exit 1
fi

echo "==> 创建远端仓库 $OWNER/$NAME（已存在则跳过）"
HTTP=$(curl -sS -o /tmp/alexkb_create.json -w '%{http_code}' -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user/repos \
  -d "{\"name\":\"$NAME\",\"description\":\"游戏圈知识库 · 惊人的老人 —— 由 Deepseek 大肥鱼 维护\",\"private\":false,\"auto_init\":false}")

case "$HTTP" in
  201) echo "    创建成功" ;;
  422) echo "    仓库已存在，继续" ;;
  *)
    echo "ERROR: 创建失败 HTTP $HTTP" >&2
    python3 -c "import json;print(json.load(open('/tmp/alexkb_create.json')).get('message',''))" 2>/dev/null || true
    rm -f /tmp/alexkb_create.json
    exit 1
    ;;
esac
rm -f /tmp/alexkb_create.json

REMOTE_URL="https://github.com/$OWNER/$NAME.git"
if git remote get-url origin >/dev/null 2>&1; then
  echo "==> origin 已存在：$(git remote get-url origin)"
else
  git remote add origin "$REMOTE_URL"
  echo "==> 已设置 origin：$REMOTE_URL"
fi

echo "==> 推送 $BRANCH"
git push -u origin "$BRANCH"

echo
echo "完成：https://github.com/$OWNER/$NAME"

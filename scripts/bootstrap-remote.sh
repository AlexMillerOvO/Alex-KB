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
  --max-time 30 --retry 2 --retry-delay 2 \
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

# github.com:443 在国内常被单独阻断（api.github.com 却正常）。
# 若检测到本地代理且 git 尚未配置代理，自动按域名挂上，避免推送卡 75 秒超时。
PROXY_PORT="${PROXY_PORT:-7897}"
if [ -z "$(git config --global --get http.https://github.com/.proxy || true)" ] \
   && nc -z -w 1 127.0.0.1 "$PROXY_PORT" 2>/dev/null; then
  git config --global http.https://github.com/.proxy "http://127.0.0.1:$PROXY_PORT"
  echo "==> 检测到本地代理 :$PROXY_PORT，已为 github.com 配置 git 代理"
fi

echo "==> 推送 $BRANCH"
if ! GIT_TERMINAL_PROMPT=0 git push -u origin "$BRANCH"; then
  echo "" >&2
  echo "推送失败。排查顺序：" >&2
  echo "  1. 连通性：git ls-remote $REMOTE_URL" >&2
  echo "  2. 若超时：确认代理在跑，然后" >&2
  echo "     git config --global http.https://github.com/.proxy http://127.0.0.1:$PROXY_PORT" >&2
  echo "  3. 若 403：token 缺少 repo scope，去 GitHub 重发" >&2
  exit 1
fi

echo
echo "完成：https://github.com/$OWNER/$NAME"

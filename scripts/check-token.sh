#!/bin/bash
# 验证 Keychain 里的 GitHub token 是否有效（会联网，只读 /user 接口）
set -u

TOKEN=$(printf 'protocol=https\nhost=github.com\n' | git credential fill 2>/dev/null | sed -n 's/^password=//p')

if [ -z "$TOKEN" ]; then
  echo "✗ Keychain 里没有 github.com 的凭据"
  echo "  先运行 scripts/set-github-token.command"
  exit 1
fi

echo "Keychain 中的 token 长度: ${#TOKEN}"

CODE=$(curl -sS -m 15 -o /dev/null -w '%{http_code}' \
  -H "Authorization: Bearer $TOKEN" https://api.github.com/user)

echo "GitHub 返回: $CODE"
case "$CODE" in
  200) echo "✓ token 有效" ;;
  401) echo "✗ token 无效（已吊销或复制有误），重新生成一个" ;;
  403) echo "✗ 被拒绝（可能是权限不足或频率限制）" ;;
  *)   echo "? 未预期状态码，检查网络" ;;
esac

# 顺带检查推送通道
echo
echo "--- 推送通道 ---"
cd "$(dirname "$0")/.." 2>/dev/null || exit 0
if GIT_TERMINAL_PROMPT=0 git ls-remote origin >/dev/null 2>&1; then
  echo "✓ git 可以连上远端"
else
  echo "✗ git 连不上远端（检查代理：git config --global --get http.https://github.com/.proxy）"
fi

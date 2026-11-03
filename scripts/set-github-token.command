#!/bin/bash
# 设置 GitHub 凭据 —— 双击运行即可
#
# 只做一件事：把 token 写进 macOS Keychain。
# 不联网、不改仓库、不写任何文件、不进 shell 历史。
#
# 用完可以删掉这个文件，凭据仍在 Keychain 里。

set -u

HOST="github.com"
ACCOUNT="AlexMillerOvO"
MIN_LEN=40

clear 2>/dev/null || true
printf '========================================\n'
printf '   设置 GitHub 凭据（写入 Keychain）\n'
printf '========================================\n\n'
printf '准备：浏览器打开  https://github.com/settings/tokens\n'
printf '      生成 token，勾选 repo 权限，复制下来\n\n'
printf '说明：输入时屏幕不会显示，粘贴后直接回车。\n'
printf '      本脚本不联网、不修改任何文件。\n\n'

printf '请粘贴 token 后回车: '
IFS= read -rs TOKEN
printf '\n'

if [ -z "${TOKEN:-}" ]; then
  printf '\n✗ 没有读到任何输入，已退出。\n'
  printf '  常见原因：直接回车了，或者粘贴时焦点不在终端。\n'
  printf '\n按回车关闭窗口。'; read -r _
  exit 1
fi

LEN=${#TOKEN}

case "$TOKEN" in
  ghp_*|github_pat_*) : ;;
  *)
    printf '\n✗ 这不像 GitHub token。\n'
    printf '  应以 ghp_（classic）或 github_pat_（fine-grained）开头。\n'
    printf '  实际读到 %d 个字符。\n' "$LEN"
    printf '\n按回车关闭窗口。'; read -r _
    exit 1
    ;;
esac

if [ "$LEN" -lt "$MIN_LEN" ]; then
  printf '\n✗ 长度只有 %d，classic token 应为 %d 字符。\n' "$LEN" "$MIN_LEN"
  printf '  可能没复制完整，重新复制一次。\n'
  printf '\n按回车关闭窗口。'; read -r _
  exit 1
fi

printf '\n检查通过（%d 个字符），正在写入 Keychain…\n' "$LEN"

if ! printf 'protocol=https\nhost=%s\nusername=%s\npassword=%s\n\n' \
      "$HOST" "$ACCOUNT" "$TOKEN" | git credential approve; then
  printf '\n✗ 写入失败。请确认已安装 git（终端输入 git --version 检查）。\n'
  printf '\n按回车关闭窗口。'; read -r _
  exit 1
fi

# 回读校验（纯本地，不联网）
STORED=$(printf 'protocol=https\nhost=%s\n' "$HOST" \
         | git credential fill 2>/dev/null \
         | sed -n 's/^password=//p')
SLEN=${#STORED}

if [ "$SLEN" -eq 0 ]; then
  printf '\n✗ 写入后读不回来，Keychain 可能拒绝了这次操作。\n'
  printf '  试试手动运行： git credential approve\n'
  printf '\n按回车关闭窗口。'; read -r _
  exit 1
fi

if [ "$SLEN" -ne "$LEN" ]; then
  printf '\n⚠ 长度对不上：写入 %d，读回 %d。建议重新运行一次。\n' "$LEN" "$SLEN"
else
  printf '\n✓ 完成。Keychain 里已存有 %s 的凭据（%d 个字符）。\n' "$ACCOUNT" "$SLEN"
  printf '\n  下一步：双击 publish.command，或在终端跑\n'
  printf '    cd ~/Documents/Alex-KB && ./scripts/publish.sh\n'
  printf '\n  注意：本脚本不验证 token 是否真的有效，\n'
  printf '        要验证请在终端跑 scripts/check-token.sh\n'
fi

unset TOKEN STORED

printf '\n按回车关闭窗口。'
read -r _

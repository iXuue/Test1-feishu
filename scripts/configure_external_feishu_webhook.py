"""Configure the external Feishu-group webhook for the current Windows user.

Run this file in a terminal, enter the group bot URL and secrets, then open a
new terminal before starting ``pico gateway``.  Values are stored in the current
user's environment registry and are never printed back to the terminal.
"""

from __future__ import annotations

import getpass
import os
import sys
from urllib.parse import urlsplit


def _write_user_env(name: str, value: str) -> None:
    if sys.platform != "win32":
        raise RuntimeError("this helper currently supports Windows only")
    import winreg

    with winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)


def main() -> int:
    url = input("外部群自定义机器人 Webhook 地址: ").strip()
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        print("地址必须是完整的 http(s) URL。")
        return 2

    outbound_secret = getpass.getpass("群机器人签名密钥（没有则直接回车）: ")
    inbound_secret = getpass.getpass("Pico 入站回调密钥（回车复用上面的密钥）: ") or outbound_secret
    if not inbound_secret:
        print("必须设置入站回调密钥，不能留空。")
        return 2

    values = {
        "FEISHU_WEBHOOK_URL": url,
        "FEISHU_WEBHOOK_SECRET": outbound_secret,
        "PICO_FEISHU_WEBHOOK_INBOUND_SECRET": inbound_secret,
        "PICO_FEISHU_WEBHOOK_HOST": "127.0.0.1",
        "PICO_FEISHU_WEBHOOK_PORT": "18791",
        "PICO_FEISHU_WEBHOOK_PATH": "/feishu/external",
    }
    for name, value in values.items():
        _write_user_env(name, value)
        os.environ[name] = value

    print("已保存到当前 Windows 用户环境变量。")
    print("请关闭当前终端、重新打开终端，再启动 pico gateway。")
    print("回调地址路径：/feishu/external；本机监听：127.0.0.1:18791。")
    print("Feishu 工作流 HTTP 请求请设置 Header：X-Pico-Webhook-Secret（填入入站回调密钥）。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

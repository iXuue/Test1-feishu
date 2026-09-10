from __future__ import annotations

import asyncio
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock

from pico.channels.adapters.feishu.channel import FeishuChannel
from pico.config.loader import set_config_path


def test_feishu_inbound_strips_bot_mention_and_keeps_event_metadata() -> None:
    channel = FeishuChannel(
        SimpleNamespace(
            app_id="cli_test",
            app_secret="test-secret",
            encrypt_key="",
            verification_token="",
            group_policy="mention",
            allow_from=["*"],
            react_emoji="THUMBSUP",
        )
    )
    channel._react = AsyncMock()
    channel.intake.publish = AsyncMock()
    message = SimpleNamespace(
        message_id="msg-1",
        chat_id="oc-group",
        chat_type="group",
        message_type="text",
        content=json.dumps({"text": "@_user_1 修改 README"}),
        mentions=[
            SimpleNamespace(
                key="_user_1",
                name="PicoBot",
                id=SimpleNamespace(user_id=None, open_id="ou_bot"),
            )
        ],
    )
    sender = SimpleNamespace(sender_type="user", sender_id=SimpleNamespace(open_id="ou_user"))
    event = SimpleNamespace(
        header=SimpleNamespace(event_id="evt-1"),
        event=SimpleNamespace(message=message, sender=sender),
    )

    asyncio.run(channel._on_message(event))

    channel.intake.publish.assert_awaited_once()
    kwargs = channel.intake.publish.await_args.kwargs
    assert kwargs["content"] == "修改 README"
    assert kwargs["chat_id"] == "oc-group"
    assert kwargs["metadata"]["event_id"] == "evt-1"
    assert kwargs["metadata"]["message_type"] == "text"


def test_event_id_dedup_suppresses_replayed_event() -> None:
    channel = FeishuChannel(
        SimpleNamespace(
            app_id="cli_test",
            app_secret="test-secret",
            encrypt_key="",
            verification_token="",
            group_policy="open",
            allow_from=["*"],
            react_emoji="THUMBSUP",
        )
    )
    channel._react = AsyncMock()
    channel.intake.publish = AsyncMock()

    def event(message_id: str):
        message = SimpleNamespace(
            message_id=message_id,
            chat_id="oc-group",
            chat_type="group",
            message_type="text",
            content=json.dumps({"text": "ping"}),
            mentions=[],
        )
        sender = SimpleNamespace(sender_type="user", sender_id=SimpleNamespace(open_id="ou_user"))
        return SimpleNamespace(
            header=SimpleNamespace(event_id="evt-replayed"),
            event=SimpleNamespace(message=message, sender=sender),
        )

    asyncio.run(channel._on_message(event("msg-1")))
    asyncio.run(channel._on_message(event("msg-2")))
    channel.intake.publish.assert_awaited_once()


def test_setup_script_writes_existing_json_channel_config(tmp_path: Path) -> None:
    from scripts import setup_feishu

    config_path = tmp_path / "config.json"
    set_config_path(config_path)
    try:
        written = setup_feishu._write_config("cli_test", "test-secret")
        assert written == config_path
        data = json.loads(config_path.read_text(encoding="utf-8"))
        feishu = data["channels"]["feishu"]
        assert feishu["enabled"] is True
        assert feishu["appId"] == "cli_test"
        assert feishu["appSecret"] == "test-secret"
        assert feishu["groupPolicy"] == "mention"
    finally:
        set_config_path(None)  # type: ignore[arg-type]


def test_setup_script_adds_only_local_secret_ignore_patterns(tmp_path: Path, monkeypatch) -> None:
    from scripts import setup_feishu

    monkeypatch.setattr(setup_feishu, "REPO_ROOT", tmp_path)
    (tmp_path / ".gitignore").write_text("__pycache__/\n", encoding="utf-8")
    assert setup_feishu._ensure_secret_files_ignored() is True
    text = (tmp_path / ".gitignore").read_text(encoding="utf-8")
    assert ".env\n" in text
    assert ".env.*\n" in text
    assert ".pico/\n" in text

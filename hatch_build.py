"""Include the prebuilt native TUI bundle when it exists."""

from __future__ import annotations

from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: dict) -> None:
        dist = Path(self.root) / "ui-tui" / "dist"
        entry = dist / "entry.js"
        if entry.is_file():
            build_data.setdefault("force_include", {})[str(entry)] = "pico/ui-tui/dist/entry.js"
        else:
            self.app.display_warning(
                "ui-tui/dist/entry.js not found; the wheel will omit the bundled TUI. "
                "Run `npm --prefix ui-tui ci` and `npm --prefix ui-tui run build` before release builds."
            )

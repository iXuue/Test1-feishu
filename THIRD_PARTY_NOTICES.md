# Third-party notices

## Pico Harness

- Upstream: https://gitee.com/htxoffical/pico-harness
- Fixed source commit: `d6c7a648fd7ee63e472c0d438f1c8299d9b8f871`
- Release context: `v0.1.7` (the absorption baseline is the newer `main` commit above).
- License: Apache-2.0; the upstream `LICENSE`, `LICENSES/`, and `NOTICES.md` are retained.
- Imported source scope: `pico/**`, `ui-tui/**`, upstream benchmark/verification scripts, and the
  isolated upstream contract tests under `tests/pico_upstream/**`.
- Local adaptations: `pyproject.toml`, `hatch_build.py`, `pico/__init__.py`, the Windows-safe
  benchmark lock adapter, and the cross-platform TUI test/terminal seams. These adaptations do
  not change the upstream public protocol or remove any upstream product module.

The imported Pico source remains identifiable by its upstream package paths. CodeCub-specific
runtime code remains under `codecub/**`; integration work must not create a second session or
tool state store for the same invocation.

## Other notices

The upstream `NOTICES.md` and `LICENSES/` files are retained verbatim for the MIT-licensed
nanobot runtime, hermes-agent TUI, and vendored ink components used by the imported upstream
tree. External runtime tools are not redistributed by this repository.

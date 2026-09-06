# Pico Harness 全量吸收验收报告

日期：2026-09-06
工作区：`D:\代码备份\pico\pico-main`
分支：`codex/pico-full-absorption`
基线起点：`codex/agent-experiments` @ `721c5e7b8a56a5192b466d4ebd33d9cefe9c63ac`

## 结论

已完成对 Gitee 上游 `pico-harness` 固定提交的工作区吸收、本机主要测试验收，以及官方生产入口到单一原生 Runtime 的架构闭环：

- 上游地址：<https://gitee.com/htxoffical/pico-harness>
- 固定提交：`d6c7a648fd7ee63e472c0d438f1c8299d9b8f871`
- 上游 Git tree：1191 个 blob
- 逐文件映射：1191/1191；按测试重定位规则核对，缺失 0
- Python 包：保留 CodeCub distribution 名称 `codecub`，同时提供上游 `pico` namespace 和 `pico` CLI
- Runtime 所有权：`pico` CLI/TUI/Gateway、`codecub` 官方 CLI/Gateway、桌面 `--app-mode` 均经过 `pico.cli._runtime_assembly.RuntimeAssembly`；旧 `codecub.cli`/`codecub.runtime.Pico` 仅作为显式兼容 API 保留，不再是官方生产 composition root
- 入口适配：`codecub/native_runtime.py` 是 CodeCub 侧唯一原生组装边界；`codecub/native_gateway.py` 复用既有 RPC transport，但使用原生 `AgentLoop + Scheduler + DeliveryHub`；桌面 JSONL 由 `codecub/native_app_mode.py` 接入同一运行核心。`pyproject.toml` 保留公开的 `codecub.cli:main` entry-point 字符串以维持发行版身份，但无显式 `argv` 的已安装控制台启动会立即转发到 `codecub.native_cli:main`。

## 吸收范围

上游 `pico/` 355 个文件和 `ui-tui/` 337 个文件已落入工作区；上游 179 个 benchmark 文件、14 个脚本、269 个测试文件、许可证/构建/安装/文档文件也已纳入。上游测试统一放在 `tests/pico_upstream/`，保留上游源码相对结构并避免覆盖 CodeCub 原有 `tests/` 测试。

保留的 CodeCub-only 目录和功能没有删除；上游文档中的 public onboarding/evaluation/examples 已补齐并解除误忽略，`uv.lock` 已纳入工作树跟踪范围。吸收清单见 [PICO_ABSORPTION_MANIFEST.md](PICO_ABSORPTION_MANIFEST.md)。

## 关键适配

1. `pyproject.toml` 升级到 Python `>=3.12,<3.13`，合并上游依赖与 optional extras；`mcp` 限定在 `<2.0.0` 以保持上游 FastMCP v1 API；`uv lock` 生成 169 个解析包。
2. 增加 `hatch_build.py` 的 TUI bundle 打包路径；TUI 构建先于 Python wheel/sdist 构建执行。
3. 为 Windows 增加 picobench 文件锁、路径长度压缩、POSIX VM 路径校验、DirectExecutor Git Bash 兼容、AppWorld 文本换行保真和 Unix-only 测试边界。
4. 修正 Pico 版本、OpenRouter pricing/context fallback、FakeModel token counter、cron 外部变更检测、TUI RPC socket 与 session bundle 的 CodeCub 兼容。
5. 渠道/发行验证保留上游稳定 node ID，同时将测试执行路径映射到 `tests/pico_upstream/`；混合仓库的 public-tree 检查只跳过明确的 CodeCub 私有工作区边界，仍扫描吸收的 Pico public surface。
6. CodeCub 实验工作区复制器排除上游 picobench 生成的 `.pico` 运行态目录，避免锁文件进入 fixture workspace；POSIX/PowerShell 安装器同时识别 `pico-harness` 与当前 `codecub` 本地源码。
7. 本轮架构修正补齐了原生 `SubagentManager` 的关闭屏障和 TUI `Notice`/`MediaOut` 的 Python → OpenRPC → TypeScript → 前端事件链，并将 CodeCub 官方 CLI/Gateway/Desktop 入口迁移到原生 Runtime；旧兼容 API 不参与生产组装。

## 验收结果

| 验收项 | 结果 |
|---|---|
| 上游逐文件映射 | 1191/1191，缺失 0 |
| CodeCub 根 Python 回归 | 734 passed，3 skipped，4 deselected |
| 上游默认非 opt-in Python 门禁 | 3801 passed，91 skipped，38 deselected，21 warnings |
| TUI TypeScript/RPC | type-check、RPC generated drift、RPC surface 通过 |
| TUI Vitest | 75 files，831 tests passed |
| Desktop | typecheck/build 通过，Vite 8.0.16 |
| Python 形式化 lint 目标集 | 7 files，All checks passed；7 files formatted |
| public-tree 门禁 | `public release tree: OK` |
| 依赖一致性 | `uv run pip check`：No broken requirements found |
| 编译与补丁检查 | `compileall` 通过；`git diff --check` 通过 |
| Python 构建 | `codecub-0.1.0.tar.gz` 和 `codecub-0.1.0-py3-none-any.whl` 构建通过 |
| wheel 内容 | 470 entries；`pico/` 356、`codecub/` 104、bundled `pico/ui-tui/dist/entry.js` 存在 |
| 接口调用链修正 | Subagent shutdown barrier、Host 关闭顺序、TUI Notice/Media wire events、CodeCub native composition roots 已通过定向回归 |

## 未纳入本机通过条件的内容

- `uv sync --locked --all-extras` 在 Windows 上受 `boxlite==0.9.5` 无 Windows wheel 限制；不影响已验证的渠道、tools、retrieval、dev 等选定 extras。该限制没有被伪装成 sandbox 通过。
- 91 个 skipped 主要是 Windows 不具备的 Unix socket/symlink/POSIX executable/交互式 terminal 测试，以及明确标记为 `e2e`、`external_runtime`、真实 VM 或真实外部环境的测试。真实 Feishu/QQ/WeCom、真实 Provider、真实 VM、BoxLite 和 live E2E 均未执行。
- 全仓 `ruff check pico codecub benchmarks scripts` 仍会报告 72 条 CodeCub 既有全仓规则问题；本次正式验收采用项目 Makefile 的 7 文件 Python lint 目标集，该目标已通过。未将全仓非门禁问题宣称为已修复。
- 旧 `codecub.runtime.Pico`、`codecub.cli` 和 legacy Gateway runtime 仍作为兼容 API 存在；`pyproject.toml` 的公开 entry-point 字符串仍指向 `codecub.cli:main`，但其真实控制台启动路径立即转发到 native CLI，桌面后端也直接指向 native CLI，因此旧 Runtime 不参与生产组装。直接调用这些兼容 API 的行为仍由原有 CodeCub 测试覆盖，不属于原生生产入口验收。

## 变更与回滚

当前分支改动尚未提交，方便用户审阅后决定提交边界。修改既有文件前均已备份到 `E:\codex_backup`；本轮入口改造备份为 `E:\codex_backup\20260906-160500-native-runtime-entry`，本轮文档备份为 `E:\codex_backup\20260906-162000-native-runtime-docs`。恢复时按备份目录中的相对路径取回原文件，不使用破坏性 Git 回滚。

详细实施约束和阶段记录见 [PICO_HARNESS_FULL_ABSORPTION_PLAN.md](../PICO_HARNESS_FULL_ABSORPTION_PLAN.md)。

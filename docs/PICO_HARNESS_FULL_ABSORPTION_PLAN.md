# Pico Harness 全量吸收实施计划

状态：已执行并完成验收（2026-09-06）

制定日期：2026-09-05

目标仓库：`D:\代码备份\pico\pico-main`

目标分支：已从 `codex/agent-experiments` 的 `721c5e7` 创建并在
`codex/pico-full-absorption` 完成吸收和验证。当前改动仍保留在工作树，未提交。

## 1. 目标与已确认要求

本计划的目标是把上游 `pico-harness` 中实际存在的产品代码、公共 API、CLI、配置、TUI、测试和构建能力完整吸收到当前项目，同时遵守以下边界：

1. 上游存在的功能必须在当前项目中达到等价、移植或兼容实现。
2. 上游不存在的功能不新增、不顺带设计、不以“未来可能需要”为理由扩展范围。
3. 当前 CodeCub 独有功能不删除、不无关重构。
4. 不建立两套 Agent Loop、Session Store、Tool Executor 或 Runtime 状态机。
5. 外部平台功能先完成代码、协议、mock 和离线 contract 测试；真实凭据驱动的 E2E 单独执行。
6. 任何现有文件修改前，先备份到 `E:\codex_backup`。

“全量吸收”在本计划中指功能/API/运行时行为和产品 surface 全量兼容，不要求把上游 1191 个 blob 机械复制成重复实现。

## 2. 固定上游基线

上游地址：<https://gitee.com/htxoffical/pico-harness>

固定分支：`main`

固定提交：`d6c7a648fd7ee63e472c0d438f1c8299d9b8f871`

上游发布标签：`v0.1.7`，但本计划以当前 `main` 为准。上游 `main` 继续变化时，必须重新生成差异清单，不允许在未记录的移动基线上继续吸收。

上游主要入口：

- [上游 `pyproject.toml`](https://gitee.com/htxoffical/pico-harness/blob/d6c7a648fd7ee63e472c0d438f1c8299d9b8f871/pyproject.toml)
- [上游 Agent tools](https://gitee.com/htxoffical/pico-harness/tree/d6c7a648fd7ee63e472c0d438f1c8299d9b8f871/pico/agent/tools)
- [上游 Channels](https://gitee.com/htxoffical/pico-harness/tree/d6c7a648fd7ee63e472c0d438f1c8299d9b8f871/pico/channels)
- [上游 Sandbox](https://gitee.com/htxoffical/pico-harness/tree/d6c7a648fd7ee63e472c0d438f1c8299d9b8f871/pico/sandbox)
- [上游 Evolver](https://gitee.com/htxoffical/pico-harness/tree/d6c7a648fd7ee63e472c0d438f1c8299d9b8f871/pico/evolver)
- [上游 TUI RPC](https://gitee.com/htxoffical/pico-harness/tree/d6c7a648fd7ee63e472c0d438f1c8299d9b8f871/pico/tui_rpc)
- [上游 TUI](https://gitee.com/htxoffical/pico-harness/tree/d6c7a648fd7ee63e472c0d438f1c8299d9b8f871/ui-tui)

## 3. 当前项目基线

当前检查到的状态：

- 当前分支：`codex/pico-full-absorption`
- 当前 HEAD：`721c5e7`
- 当前包名：`codecub`
- 已新增顶层 `pico/` 兼容包和 `ui-tui/` 上游 TUI
- 当前 `pyproject.toml` 使用 Python `>=3.12,<3.13`，并已生成锁文件
- 当前已有 Runtime、Spine、Gateway、MCP、Channels、Cron、Auth、Sandbox、Memory、Extensions、Tracing 和 Desktop 实现
- 上游固定提交的 1191 个 blob 已逐文件映射；上游测试位于 `tests/pico_upstream/`

现有文档明确记录 Pico 之前只被作为架构参考、没有复制源码：[THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md)、[PICO_UPSTREAM.md](PICO_UPSTREAM.md)。全量吸收后已更新这两份 provenance 文档，并新增 `docs/upstream/PICO_ABSORPTION_REPORT.md`。

## 4. 上游实际范围与不纳入范围

### 4.1 必须吸收的上游产品范围

上游 `pico/` 包含以下功能域：

| 上游目录 | 必须吸收的内容 |
|---|---|
| `pico/agent` | Agent Loop、checkpoint/recovery、subagent、文件/ Shell/MCP/Skill/Tool Search 等工具 |
| `pico/auth` | allowlist、capability token、managed settings |
| `pico/call_efficiency` | cache、ledger、pricing、provider usage 和模型调用效率记录 |
| `pico/channels` | 通道 contract、intake/outlet、media、transcription、Feishu/QQ/WeCom adapter |
| `pico/cli` | agent、channel、cron、doctor、evolve、gateway、onboard、plugin、provider、sandbox、session、skill、status、tracing、TUI 命令 |
| `pico/config` | 配置加载、路径、schema、channel/provider 更新 |
| `pico/context_engine` | context assembly、history trimming、identity/memory/skill segments |
| `pico/eval_engine` | evaluation engine、judge、hooks 和安全评估 |
| `pico/evolver` | candidate、evidence、judge、gates、launch、scheduler、tree、activation 和 CLI |
| `pico/memory_engine` | backend contract、consolidation、skill forge、local skill registry |
| `pico/plugin` | manifest、discovery、bootstrap、lazy registry 和 memory plugin seam |
| `pico/proactive_engine` | Cron service、job types、claim 和工具入口 |
| `pico/providers` | LiteLLM、OpenAI Codex、Azure、custom、per-model 和 transcription provider |
| `pico/routing` | classifier、KNN router、profiles、selector、snapshot/cache |
| `pico/sandbox` | Sandbox interface、DirectExecutor、BoxLiteExecutor、debug server 和配置 |
| `pico/security` | network target validation、trust boundary |
| `pico/session` | session manager、export |
| `pico/spine` | turn、runner、scheduler、events、delivery、teardown、barrier |
| `pico/templates` | AGENTS、SOUL、TOOLS、USER、MEMORY 模板 |
| `pico/token_wise` | token budget、cache optimizer、pricing、usage tracker |
| `pico/tracing` | trace context、spans、store、usage 和本地 viewer |
| `pico/tui_rpc` | config、confirm、image、model、question、session、setup、system、terminal、turn、subscription |
| `ui-tui` | 上游完整原生 TUI、RPC client、session/turn UI、markdown、terminal、overlay、slash commands 和测试 |

同时盘点并按功能吸收上游的：

- `install.ps1`、`install.sh`
- `Makefile`、`hatch_build.py`
- 上游 package/build 配置
- 与产品运行直接相关的 `scripts/**`
- 上游 Python/TypeScript contract tests、integration tests 和演示 benchmark
- LICENSE、LICENSES、NOTICES 等归属信息

### 4.2 明确不新增的内容

以下内容不在固定上游树中，不能列为本次强制实现目标：

- 通用 OAuth/OIDC 企业身份平台和租户系统
- Marketplace、远程插件签名供应链和插件分发服务
- Vendor-specific OTEL remote collector 或云端 dashboard
- 泛化的多主机 leader election
- 与 Pico 无对应实现的 CodeCub 新产品功能

如果后续上游提交新增这些能力，必须重新锁定提交并更新本计划。

## 5. 依赖和运行时策略

### 5.1 Python 基线

已确认：全量吸收分支提升到上游要求的：

```toml
requires-python = ">=3.12,<3.13"
```

该改动只针对全量吸收分支。是否把同样的基线回移到其他 CodeCub 分支，不属于本计划。

### 5.2 上游核心依赖

按上游固定提交核对并加入锁文件，版本范围以其 `pyproject.toml` 为准：

- Typer、LiteLLM、Pydantic、pydantic-settings
- httpx、loguru、Rich、croniter、PyYAML
- prompt-toolkit、json-repair、tiktoken、questionary、watchfiles、tomli-w
- oauth-cli-kit、portalocker、MCP、orjson
- numpy、Pillow、packaging

### 5.3 上游 optional extras

只为上游存在的功能增加 optional extra：

- `channel-feishu`: `lark-oapi`
- `channel-wecom`: `wecom-aibot-sdk-python`
- `channel-qq`: `qq-botpy`
- `retrieval`: `torch`、`transformers`
- `sandbox`: `boxlite`、`anyio`
- `tools`: 上游 tools 所需的 readability/OAuth 依赖
- `dev`、`eval`

执行阶段已在已确认的本地 Python 3.12/uv 环境中锁定并同步依赖；不得把凭据、缓存或生成目录写入代码仓库。外部服务、真实 VM 和 BoxLite 的环境依赖仍不在本机默认安装范围。

### 5.4 Node.js 基线

上游 `ui-tui/package.json` 要求 Node.js `>=22`。全量吸收分支的 TUI 构建和测试统一使用 Node.js 22 或更高版本；不以当前系统的旧 Node.js 版本作为验收依据。

TUI 的 `dist/entry.js` 是 Python wheel 打包所需的构建输入，因此必须先完成 TUI 依赖安装和构建，再执行 Python wheel/sdist 构建。

## 6. 架构原则

### 6.1 单一 Runtime 所有权

采用“上游公共 surface + Pico 原生运行核心 + CodeCub 兼容适配层”的结构：

- `pico` 原生 `RuntimeAssembly`、`AgentLoop`、`SessionManager`、`Spine` 和 Tool Registry 是官方生产运行核心。
- `codecub/native_runtime.py` 是旧命令参数、桌面协议和 Gateway RPC 到原生核心的唯一组装适配边界。
- `codecub` 旧 Runtime、Session、Spine 和 model API 只保留为显式兼容表面，不得被官方生产入口直接构造。
- 上游新增而 CodeCub 没有的能力，按上游接口在 `pico` 或对应 CodeCub 模块中实现。
- 不允许同时维护 `pico` 和 `codecub` 两套 conversation state、Tool Registry 或 checkpoint 格式。

### 6.2 状态和配置兼容

支持上游 Pico 的配置、数据目录、session/export 和 CLI 语义；现有 CodeCub 状态继续可恢复。迁移规则必须明确：

1. 新安装使用上游兼容的 Pico 配置入口。
2. 现有 `.codecub` 数据不被覆盖。
3. `.pico`、`.codecub` 或对应用户目录之间的迁移必须显式、可回滚、有日志。
4. 同一 session 不允许被两个 Runtime 同时写入。

### 6.3 安全边界

- 上游能力必须继续经过现有 capability、approval、sandbox、replay 和 secret-redaction 路径。
- DirectExecutor 必须明确报告 `is_sandboxed=false`。
- BoxLite 不可用时必须 fail closed 或清晰降级，不得伪装成隔离执行。
- Channel 内容、媒体和外部文本必须带有来源和信任边界。
- Evolver 默认只生成候选和证据，生产激活遵守上游显式流程。

## 7. 逐模块映射方案

| 上游能力域 | 当前落点 | 计划动作 |
|---|---|---|
| Agent/Turn | `codecub/agent/**`、`codecub/runtime.py` | 对齐上游公共模型、tool route、checkpoint、recovery、subagent 和 skill/tool-search 行为；已有等价实现只做兼容测试 |
| Spine | `codecub/spine/**` | 对齐 request/run/turn/event/delivery/teardown/cancellation 语义，补齐上游已有的 cron claim 行为 |
| Gateway/TUI RPC | `codecub/gateway.py`、`gateway_runtime.py`、`app_protocol.py`、新增 `pico/tui_rpc/**` | 实现上游 RPC method、错误、订阅、interaction、image、terminal、model、session 和 turn 契约 |
| CLI/Config | `codecub/cli.py`、`provider_config.py`、新增 `pico/cli/**`、`pico/config/**` | 支持上游 command tree、配置 schema、路径和 onboarding；保持 CodeCub 命令兼容 |
| Channels | `codecub/channels.py`、新增 `pico/channels/**` | 移植三种 adapter、media persistence、transcription、intake/outlet、重试和幂等 |
| Cron | `codecub/automation.py`、`codecub/spine/**`、新增 `pico/proactive_engine/**` | 对齐 at/every/cron、claim、持久化、恢复和 CLI；不扩展为上游没有的 leader election |
| Tools/MCP | `codecub/tooling/**`、`codecub/mcp.py`、新增 `pico/agent/tools/**` | 对齐 tool metadata、search、skill、MCP route、schema gate 和 governed execution |
| Auth | `codecub/auth.py`、新增 `pico/auth/**` | 对齐 allowlist、capability token、managed settings；不实现上游没有的通用 OIDC/tenant |
| Sandbox | `codecub/sandbox.py`、新增 `pico/sandbox/**` | 接入 DirectExecutor/BoxLiteExecutor、生命周期、进程生成、debug server 和隔离事实报告 |
| Providers/Routing | `codecub/models.py`、`provider_*.py`、`retrieval.py`、新增 `pico/providers/**`、`pico/routing/**` | 对齐 provider registry、OAuth Codex provider、transcription、KNN routing、pricing 和 model catalog |
| Context/Memory | `codecub/context_*.py`、`memory_v2/**`、新增 `pico/context_engine/**`、`pico/memory_engine/**` | 对齐 segments、backend contract、skill forge、consolidation、freshness 和 evidence 语义 |
| Plugin | `codecub/extensions.py`、新增 `pico/plugin/**` | 对齐 manifest discovery、lazy activation、dependency/conflict、capability grant 和 memory/tool contribution |
| Call efficiency/Token-wise | `codecub/cache.py`、`model_gateway.py`、`token_budget.py`、新增对应 `pico/**` | 对齐 cache、ledger、pricing、usage、budget 和可观测字段 |
| Tracing | `codecub/tracing/**`、`otel_exporter.py`、新增 `pico/tracing/**` | 对齐 trace/span/store/usage 和上游本地 viewer；不新增上游没有的远程 collector |
| Evaluation/Evolver | `codecub/evaluator.py`、`experiments/**`、新增 `pico/eval_engine/**`、`pico/evolver/**` | 吸收上游 evolver 全部生命周期、candidate evidence、gates、tree 和 CLI，保持 opt-in 与显式激活 |
| TUI | 新增 `ui-tui/**`，仅按需调整 `desktop/**` | 迁移上游原生 TUI 和 RPC client；不重写现有 Desktop 产品布局，除非是接入上游协议的必要修改 |

## 8. 分阶段实施步骤

### 阶段 0：逐文件基线和备份

交付物：`docs/upstream/PICO_ABSORPTION_MANIFEST.md`。

任务：

1. 读取固定提交的完整 tree，区分产品代码、测试、构建、文档、法律文件和仓库流程文件。
2. 为上游每个 `pico/**`、`ui-tui/**` 和相关顶层功能文件建立映射。
3. 对当前 108 行能力矩阵逐行重新判定，去掉实际上游不存在的伪差距。
4. 形成新增、修改、兼容包装、保留不动四类文件清单。
5. 修改任何现有文件前创建时间戳备份，并报告备份路径。

验收：没有未映射的上游产品源码；没有把 Gitee 流程文件误当 Runtime 功能。

### 阶段 1：分支、Python 和包构建

预计文件：

- `pyproject.toml`
- `uv.lock`
- `hatch_build.py`
- `package.json`、`package-lock.json`
- 新增 `pico/**` 包入口
- 许可证和 notices 文件

任务：

1. 从当前分支创建全量吸收分支。
2. 将 Python 基线改为 `>=3.12,<3.13`。
3. 合并上游核心依赖和 optional extras。
4. 配置 `pico` CLI entry point。
5. 配置 `pico` Python 包、TUI 打包和 sdist/wheel 内容。
6. 保留 `codecub` 命令行参数、Gateway RPC 和桌面 JSONL 协议兼容入口，但入口实现必须委托原生 Runtime。

依赖锁定顺序：先完成 `pyproject.toml` 合并，再执行 `uv lock` 生成锁文件，随后使用 `uv sync --locked` 验证锁文件可复现。Python 包构建必须在阶段 6 的 TUI 构建完成后执行。

验收：在干净 Python 3.12 环境中可以构建并导入 `pico` 和 `codecub`，且不存在第二套 Runtime 初始化。

### 阶段 2：核心 Agent、Spine、Session、Gateway

预计文件：

- `codecub/runtime.py`
- `codecub/agent/**`
- `codecub/spine/**`
- `codecub/sessions/**`
- `codecub/gateway.py`
- `codecub/gateway_runtime.py`
- `codecub/app_protocol.py`
- `pico/agent/**`、`pico/spine/**`、`pico/session/**`、`pico/tui_rpc/**`

任务：

1. 对齐上游 TurnRequest、TurnOutcome、event、subscription 和 teardown。
2. 对齐 session create/resume/export/close。
3. 对齐 Gateway lock、JSON-RPC、错误和 bounded event queue。
4. 对齐 TUI session/turn/cancel/inject/interrupt/confirm/question。
5. 接入 image attach、terminal、model、config、system、setup RPC。
6. 保证所有官方生产入口最后进入同一个 Pico Runtime、Spine 和 Tool Registry；legacy API 仅由兼容测试直接覆盖。

验收：Pico CLI、Gateway、TUI RPC 和现有 Desktop app mode 能驱动同一条 Runtime 路径。

### 阶段 3：Tools、MCP、Channels、Media、Cron

预计文件：

- `codecub/tooling/**`
- `codecub/mcp.py`
- `codecub/channels.py`
- `codecub/automation.py`
- `codecub/spine/delivery.py`
- 新增 `pico/agent/tools/**`
- 新增 `pico/channels/**`
- 新增 `pico/proactive_engine/**`

任务：

1. 移植 Skill、Tool Search、MCP tool bridge 和上游工具错误语义。
2. 移植 Feishu、QQ、WeCom adapter。
3. 移植 media 保存、文件名安全、图片/音频处理和 transcription provider。
4. 对齐 channel intake/outlet、reply_to、idempotency、retry、backpressure。
5. 对齐 at/every/five-field cron、claim、recovery 和 Gateway cron control plane。
6. 所有外部内容继续经过 untrusted text、URL、secret 和 capability 检查。

验收：本地 fake channel、fake provider、fake MCP、fake scheduler 完成完整 contract 测试；外部平台 live E2E 不作为本地默认测试条件。

### 阶段 4：Auth、Sandbox、Provider、Routing、Context、Memory、Plugin

预计文件：

- `codecub/auth.py`
- `codecub/security.py`
- `codecub/sandbox.py`
- `codecub/provider_*.py`
- `codecub/context_*.py`
- `codecub/memory_v2/**`
- `codecub/extensions.py`
- `codecub/cache.py`
- `codecub/model_gateway.py`
- `codecub/token_budget.py`
- 新增对应 `pico/**` 包

任务：

1. 对齐 capability token、allowlist、managed settings。
2. 接入 DirectExecutor 与 BoxLiteExecutor，并暴露真实隔离状态。
3. 对齐上游 provider registry、OAuth Codex provider、transcription、pricing、catalog。
4. 对齐 routing classifier、KNN snapshot、profile 和 selector。
5. 对齐 context segments、history trimming、memory backend、skill forge 和 consolidation。
6. 对齐 plugin manifest、discovery、lazy activation、dependency/conflict 和 capability grant。
7. 对齐 call-efficiency ledger、token-wise pricing、cache 和 usage tracker。

验收：无身份、错误 capability、路径逃逸、未授权插件、无隔离 sandbox 和 schema 错误均 fail closed；已有 CodeCub Memory/Context 测试继续通过。

### 阶段 5：Tracing、Evaluation、Evolver

预计文件：

- `codecub/tracing/**`
- `codecub/otel_exporter.py`
- `codecub/evaluator.py`
- `codecub/experiments/**`
- 新增 `pico/tracing/**`
- 新增 `pico/eval_engine/**`
- 新增 `pico/evolver/**`
- 上游对应 `benchmarks/**`、`scripts/**`

任务：

1. 对齐 trace context、span、store、usage 和本地 viewer。
2. 移植 evaluation engine、judge、tool audit hooks。
3. 移植 Evolver candidate、evidence、manifest、judge、gates、launch、tree 和 activation。
4. 实现 `pico evolve check/run/status/finalize`。
5. 保持 evolve opt-in，候选激活和生产变更必须显式完成上游规定的流程。

验收：evolver 可执行 check、可恢复 run、记录 candidate/evidence、执行 gate、生成 status，并在 finalize/activation 失败时保持可审计和可回滚。

### 阶段 6：TUI、Installer、文档和发行包

预计文件：

- 新增或迁移 `ui-tui/**`
- `desktop/**` 中必要的 RPC/启动适配文件
- `install.ps1`
- `install.sh`
- `Makefile`
- `hatch_build.py`
- `README.md`、`README.zh-CN.md` 中必要的安装/命令说明
- `docs/**`

任务：

1. 迁移上游 TUI 的 app、RPC client、session/turn store、terminal、markdown、overlay 和 slash commands。
2. 将 TUI 连接到唯一 Gateway/Runtime。
3. 吸收上游安装器、构建钩子和发行包内容。
4. 更新中文 onboarding、provider/channel/sandbox/evolve 使用说明。
5. 保留 CodeCub 项目介绍和现有 Desktop 功能，不用上游 README 覆盖项目事实。

验收：TUI 可启动、连接、发起 Turn、处理 confirmation/question、显示 tool/stream/terminal/image 状态；构建产物可在 Python 3.12 环境安装。

### 阶段 7：全量验证和吸收报告

任务：

1. 运行现有 Python 测试和移植后的上游 contract/integration 测试。
2. 运行 TUI 和 Desktop TypeScript 测试。
3. 验证 CLI 命令矩阵、Gateway RPC 矩阵、Channel adapter 矩阵、Sandbox backend 矩阵。
4. 做依赖、路径、secret、license、构建包内容和源码 provenance 审计。
5. 更新覆盖矩阵，所有上游产品能力必须为 `EQUIVALENT`、`PORTED`、`MERGED` 或 `WRAPPED`。
6. 生成 `docs/upstream/PICO_ABSORPTION_REPORT.md`，逐文件说明来源、目标、处理方式和测试。

## 9. 文件修改边界

### 9.1 允许修改或新增

只限当前工作区 `D:\代码备份\pico\pico-main` 内：

- `codecub/**`
- 新增 `pico/**`
- 新增或迁移 `ui-tui/**`
- `desktop/**` 中确有上游协议接入需要的文件
- `tests/**`
- `scripts/**` 中与上游产品验证直接相关的文件
- `benchmarks/**` 中与上游功能验收直接相关的文件
- `docs/**`
- `pyproject.toml`、`uv.lock`、`package.json`、`package-lock.json`
- 上游安装、构建和许可证文件

### 9.2 默认不修改

除非阶段 0 的逐文件清单证明它是上游功能的直接依赖，否则不修改：

- CodeCub-only 的实验、评估和 UI 设计
- 与 Pico 无对应关系的历史兼容逻辑
- 仅用于 GitHub/Gitee 流程的仓库模板
- 与上游产品无关的文档和脚本

## 10. 测试和验收命令

执行阶段使用 Python 3.12 环境；本次实际验收命令为：

```powershell
cd ui-tui
npm ci
npm run type-check
npm run lint:rpc
npm run lint:rpc-surface
npm test
npm run build
cd ..\desktop
npm ci
npm run typecheck
npm run build
cd ..
uv lock
uv sync --locked
uv build
uv run pytest -q
uv run pytest -c tests/pico_upstream/pytest.ini tests/pico_upstream -q
uv run ruff check scripts/check_commit_file.py scripts/check_commit_messages.py scripts/check_pr_title.py scripts/check_large_files.py scripts/commit_lint.py tests/pico_upstream/test_commit_lint.py tests/pico_upstream/test_large_file_check.py
git diff --check
```

功能验收矩阵至少包括：

| 领域 | 最低验收内容 |
|---|---|
| Package | `import pico`、`import codecub`、wheel/sdist 内容正确 |
| Agent | turn、tool call、checkpoint、resume、subagent、skill/tool-search |
| Gateway | auth、RPC framing、session、run、cancel、interrupt、subscribe、interaction |
| Channels | contract、loopback、Feishu、QQ、WeCom、media、transcription、retry |
| Cron | at/every/cron、claim、恢复、幂等和 Gateway control plane |
| Tools/MCP | stdio、HTTP/SSE、discovery、schema gate、reconnect、governed execution |
| Auth/Sandbox | token、allowlist、managed settings、DirectExecutor、BoxLite、path/process/network guard |
| Provider/Routing | registry、lazy selection、OAuth Codex、transcription、pricing、KNN routing |
| Memory/Plugin | backend、skill forge、consolidation、manifest、lazy activation、dependency/conflict |
| Evolver | check、run、resume、status、finalize、candidate evidence、gate、activation guard |
| TUI | startup、RPC、stream、markdown、terminal、image、confirm/question、session lifecycle |

外部平台和 BoxLite 的真实 E2E 需要用户提供凭据、租户和运行环境；在没有这些条件时，只能报告 contract/mock 验收，不得宣称 live E2E 已完成。

## 11. 许可证、备份和回滚

### 11.1 许可证

如果复制或修改上游源码：

- 保留 Apache-2.0 LICENSE、LICENSES 和 NOTICES。
- 在 `THIRD_PARTY_NOTICES.md` 记录精确上游提交、文件路径、修改说明和归属。
- 不把上游作者或 Pico 产品名误写成 CodeCub 自有代码。

### 11.2 备份

修改任何现有文件前创建：

```text
E:\codex_backup\YYYYMMDD-HHMMSS-pico-harness-full-absorption\
```

备份目录必须保留相对路径信息。备份创建完成后先向用户报告路径，再继续修改。

### 11.3 提交和回滚

建议按阶段独立提交：

1. `chore: lock pico upstream baseline and dependency policy`
2. `feat: add pico package and runtime compatibility surface`
3. `feat: port pico gateway channels tools and sandbox`
4. `feat: port pico memory routing plugin and evolver`
5. `feat: add pico tui packaging and acceptance suite`
6. `docs: publish pico full absorption report`

每阶段失败时回滚对应提交，不使用 `git reset --hard` 或覆盖用户工作树的破坏性操作。

## 12. 风险与控制措施

| 风险 | 控制措施 |
|---|---|
| Python 3.12 和依赖升级破坏 CodeCub | 只在全量吸收分支升级；先构建/导入，再做功能移植 |
| `pico` 与 `codecub` 形成两套 Runtime | 以 composition root 和 state ownership 测试强制单一路径 |
| `.pico`、`.codecub` 状态互相覆盖 | 明确目录优先级、迁移命令和锁；默认不自动删除旧数据 |
| 可选 SDK 或 BoxLite 不可用 | optional extra、fail-closed、明确 capability/status，不伪造成功 |
| Evolver 修改 Git 或生产候选 | 保持上游 opt-in、candidate/evidence/gate 和显式 activation |
| 上游 `main` 移动 | 固定 SHA，阶段 0 记录 tree hash 和逐文件 manifest |
| 许可证遗漏 | 修改前后做 NOTICE/来源扫描和发布包检查 |
| TUI/现有 Desktop 协议冲突 | 共享 Gateway contract，分离 surface，不重写现有 UI 布局 |

## 13. 完成定义

只有同时满足以下条件，才可以宣布“Pico Harness 全量吸收完成”：

1. 上游固定提交下的所有产品源码和公共入口都有逐文件映射。
2. 上游实际存在的功能没有被标记为拒绝、未知或未审查。
3. 上游 CLI、Python API、TUI RPC、Channels、Sandbox、Evolver 和构建入口可用。
4. 所有官方生产入口使用同一个 Pico Runtime、Session、Spine 和 Tool Registry；保留的 legacy API 必须明确标注为兼容层，不得成为生产 root。
5. 现有 CodeCub-only 功能没有被无关删除或重构。
6. 本地 contract、unit、确定性 integration、Python、TUI 和 Desktop 测试通过；真实/外部 E2E 按第 8 条单独记录，不伪装为本机已测。
7. 依赖、源码路径、许可证、secret 和构建产物审计通过。
8. 外部平台 live E2E 的已测和未测范围被单独记录。
9. 生成逐文件 `PICO_ABSORPTION_REPORT.md`，而不是只写“测试通过”。

满足上述生产入口和测试条件后，可以发布“上游产品能力已吸收、官方生产入口已统一到 Pico Runtime”的结论；不得把仍保留的 legacy API 误写成第二个生产 root。

## 14. 当前执行状态

- 计划文档：已执行并完成最终架构闭环复核；官方生产入口完成统一，legacy API 保留为兼容层
- Python 基线：Python 3.12.7；`requires-python = ">=3.12,<3.13"`
- Node 基线：Node 24.14.1；TUI 要求 `>=22`
- 上游提交：已固定为 `d6c7a648fd7ee63e472c0d438f1c8299d9b8f871`
- 文件映射：1191/1191 个上游 blob 可在工作区找到；测试路径统一映射到 `tests/pico_upstream/`
- 依赖：`uv lock` 和选定 extras 的 `uv sync --locked` 通过；Windows 因 BoxLite 0.9.5 无可用 wheel，`--all-extras` 不作为本机通过条件
- Python 回归：根 CodeCub `734 passed, 3 skipped, 4 deselected`；上游默认门禁 `3801 passed, 91 skipped, 38 deselected`
- 前端/桌面：TUI `831 passed`，RPC/type/build 通过；Desktop typecheck/build 通过
- 架构闭环修正：Subagent shutdown barrier、Host 关闭顺序、TUI Notice/Media 事件链已实施并通过定向回归；新增 `codecub/native_runtime.py`、`native_gateway.py`、`native_app_mode.py` 和 `native_cli.py`，将 CodeCub 官方 CLI/Gateway/Desktop 入口接入同一 `RuntimeAssembly`
- 兼容边界：`codecub.cli`、`codecub.runtime.Pico` 和旧 `codecub.gateway_runtime.EmbeddedRuntimeGateway` 仍可供历史调用；`pyproject.toml` 保留 `codecub.cli:main` 的公开脚本身份，但控制台无参路径和桌面后端均转发到 native Runtime，旧 Runtime 不参与正式生产组装
- 构建：`codecub-0.1.0` wheel/sdist 通过，wheel 含 `pico/`、`codecub/` 和 bundled TUI
- 外部真实 E2E：未执行；凭据、外部渠道、真实 VM 和 BoxLite 环境不在本机验收范围
- 备份：所有修改过的既有文件均已按时间戳保存到 `E:\codex_backup`

因此当前状态是“上游源码已吸收、官方生产入口已统一到 Pico Runtime、legacy API 保留为兼容层”；本机验收范围内可以发布生产入口闭环完成的结论，真实外部 Provider/Channel/VM E2E 仍按上文单独记录。

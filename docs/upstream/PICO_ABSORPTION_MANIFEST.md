# Pico Harness 上游逐文件吸收清单

状态：已执行；1191/1191 个上游 blob 已完成工作区映射并通过验证

生成日期：2026-09-06

上游仓库：<https://gitee.com/htxoffical/pico-harness>

固定提交：`d6c7a648fd7ee63e472c0d438f1c8299d9b8f871`

当前工作区：`D:\代码备份\pico\pico-main`，当前分支 `codex/pico-full-absorption`，HEAD `721c5e7`。

## 使用说明

本清单由固定提交的 Git tree 生成，共 1191 个 blob。它是逐文件吸收基线，不代表所有文件都应原样复制。实际执行中，产品源码、TUI、测试、基准、脚本、构建和许可证文件均已落到工作区；上游测试统一重定位到 `tests/pico_upstream/` 以避免覆盖 CodeCub 原有测试。

`PORT_OR_WRAP` 采用单一 CodeCub Runtime 复用方式，平台差异和项目标识差异记录在吸收报告中；`REVIEW_*` 项均已按支持文件或产品入口完成归类。

## 固定树统计

| 顶层路径 | 文件数 | 归类/目标 |
|---|---:|---|
| `.gitee` | 2 | `REVIEW_SUPPORT` |
| `.gitignore` | 1 | `REVIEW_SUPPORT` |
| `.pre-commit-config.yaml` | 1 | `REVIEW_SUPPORT` |
| `benchmarks` | 179 | `PORT_BENCHMARK_OR_REVIEW` |
| `commitlint.config.cjs` | 1 | `REVIEW_SUPPORT` |
| `CONTRIBUTING.md` | 1 | `REVIEW_SUPPORT` |
| `docs` | 12 | `MERGE_DOC_OR_REVIEW` |
| `eslint.base.mjs` | 1 | `REVIEW_SUPPORT` |
| `hatch_build.py` | 1 | `MERGE_BUILD` |
| `install.ps1` | 1 | `MERGE_BUILD` |
| `install.sh` | 1 | `MERGE_BUILD` |
| `LICENSE` | 1 | `PRESERVE_LICENSE` |
| `LICENSES` | 4 | `PRESERVE_LICENSE` |
| `Makefile` | 1 | `MERGE_BUILD` |
| `NOTICES.md` | 1 | `PRESERVE_LICENSE` |
| `package-lock.json` | 1 | `MERGE_BUILD` |
| `package.json` | 1 | `MERGE_BUILD` |
| `pico` | 355 | `PORT_OR_WRAP` |
| `prettier.config.mjs` | 1 | `REVIEW_SUPPORT` |
| `pyproject.toml` | 1 | `MERGE_BUILD` |
| `README.md` | 1 | `REVIEW_SUPPORT` |
| `README.zh-CN.md` | 1 | `REVIEW_SUPPORT` |
| `scripts` | 14 | `PORT_VERIFY_OR_REVIEW` |
| `SECURITY.md` | 1 | `REVIEW_SUPPORT` |
| `tests` | 269 | `PORT_TEST` |
| `ui-tui` | 337 | `PORT_UI` |
| `uv.lock` | 1 | `MERGE_BUILD` |
| **合计** | **1191** | |

## 目标映射原则

| 上游范围 | 默认目标 | 默认动作 |
|---|---|---|
| `pico/agent/**` | `codecub/agent/** + codecub/runtime.py + pico/agent/**` | `PORT_OR_WRAP` |
| `pico/auth/**` | `codecub/auth.py + pico/auth/**` | `PORT_OR_WRAP` |
| `pico/call_efficiency/**` | `codecub/cache.py + codecub/model_gateway.py + codecub/telemetry/** + pico/call_efficiency/**` | `PORT_OR_WRAP` |
| `pico/channels/**` | `codecub/channels.py + pico/channels/**` | `PORT_OR_WRAP` |
| `pico/cli/**` | `codecub/cli.py + codecub/app_protocol.py + pico/cli/**` | `PORT_OR_WRAP` |
| `pico/config/**` | `codecub/provider_config.py + codecub/connections/** + pico/config/**` | `PORT_OR_WRAP` |
| `pico/context_engine/**` | `codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/**` | `PORT_OR_WRAP` |
| `pico/eval_engine/**` | `codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/**` | `PORT_OR_WRAP` |
| `pico/evolver/**` | `pico/evolver/**` | `PORT_OR_WRAP` |
| `pico/memory_engine/**` | `codecub/memory_v2/** + pico/memory_engine/**` | `PORT_OR_WRAP` |
| `pico/plugin/**` | `codecub/extensions.py + pico/plugin/**` | `PORT_OR_WRAP` |
| `pico/proactive_engine/**` | `codecub/automation.py + pico/proactive_engine/**` | `PORT_OR_WRAP` |
| `pico/providers/**` | `codecub/models.py + codecub/provider_*.py + pico/providers/**` | `PORT_OR_WRAP` |
| `pico/routing/**` | `codecub/retrieval.py + codecub/vector_index.py + pico/routing/**` | `PORT_OR_WRAP` |
| `pico/sandbox/**` | `codecub/sandbox.py + codecub/security.py + pico/sandbox/**` | `PORT_OR_WRAP` |
| `pico/security/**` | `codecub/security.py + pico/security/**` | `PORT_OR_WRAP` |
| `pico/session/**` | `codecub/sessions/** + codecub/store_ports.py + pico/session/**` | `PORT_OR_WRAP` |
| `pico/spine/**` | `codecub/spine/** + pico/spine/**` | `PORT_OR_WRAP` |
| `pico/templates/**` | `pico/templates/**` | `PORT_OR_WRAP` |
| `pico/token_wise/**` | `codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/**` | `PORT_OR_WRAP` |
| `pico/tracing/**` | `codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/**` | `PORT_OR_WRAP` |
| `pico/tui_rpc/**` | `codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/**` | `PORT_OR_WRAP` |
| `pico/utils/**` | `codecub/workspace.py + codecub/security.py + pico/utils/**` | `PORT_OR_WRAP` |
| `pico/**` 根文件 | `pico/**` + 对应 CodeCub public entry point | `PORT_OR_WRAP` |
| `ui-tui/**` | `ui-tui/**` | `PORT_UI` |
| `tests/**` | `tests/**` | `PORT_TEST` |
| `benchmarks/**` | `benchmarks/**` | `PORT_BENCHMARK_OR_REVIEW` |
| `scripts/**` | `scripts/**` | `PORT_VERIFY_OR_REVIEW` |
| `install.ps1`, `install.sh`, `Makefile`, `hatch_build.py`, package manifests | 同名或合并后的构建入口 | `MERGE_BUILD` |
| LICENSE、LICENSES、NOTICES | 当前仓库归属文件 | `PRESERVE_LICENSE` |

## 逐文件基线

| # | 上游路径 | Tree SHA | 类型 | 字节数 | 初始动作 | 当前目标/审查范围 |
|---:|---|---|---|---:|---|---|
| 1 | `.gitee/ISSUE_TEMPLATE.zh-CN.md` | `458f558583b0de6e604772bf4ed2303dc21f45e5` | blob | 817 | `REVIEW_SUPPORT` | repository support only |
| 2 | `.gitee/PULL_REQUEST_TEMPLATE.zh-CN.md` | `b516c4c1df26008ec98f74c494f7ab27bf1c6c2c` | blob | 630 | `REVIEW_SUPPORT` | repository support only |
| 3 | `.gitignore` | `dd51df957c51ac2f6e99d022e01359951d87d26b` | blob | 484 | `REVIEW_SUPPORT` | repository support only |
| 4 | `.pre-commit-config.yaml` | `67d6bc76201c1324ebef4d68da60dcadc7dca257` | blob | 1424 | `REVIEW_SUPPORT` | repository support only |
| 5 | `benchmarks/__init__.py` | `1344a2815d9b21756611386a814e9e72eb424538` | blob | 407 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 6 | `benchmarks/appworld/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 7 | `benchmarks/appworld/agent_cli.py` | `e8a4166368cd58767b2a0a348ce6e1e3e69f489f` | blob | 8123 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 8 | `benchmarks/appworld/batch.py` | `93358b34a8a038a5c843a3e68855c497d13d4855` | blob | 9895 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 9 | `benchmarks/appworld/evolve/__init__.py` | `0eb1ae8ece9f8bea8f3ba4495e2b5d1c6553ea89` | blob | 386 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 10 | `benchmarks/appworld/evolve/adapter.py` | `18d2d669b2fd6d88b6f6c4894b39c3fe1990e657` | blob | 14320 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 11 | `benchmarks/appworld/evolve/agentic.py` | `ddad2d1bee4298dcc6b3c14af45bc1819693b460` | blob | 11464 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 12 | `benchmarks/appworld/evolve/diagnose.py` | `dfbbfd763df90e37f545a413ae38af0318f49a0e` | blob | 7549 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 13 | `benchmarks/appworld/evolve/editor.py` | `9e0ba2fcd98c0b1e76f3f9e09aa6df87e3526e88` | blob | 29472 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 14 | `benchmarks/appworld/evolve/entry.py` | `e947ba3cfdbe182a4ce75ced2c312b76ebc91dbd` | blob | 14163 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 15 | `benchmarks/appworld/evolve/eval.py` | `7b67a402097117be3fbfa0a1d0a6d7f1f5f781f0` | blob | 8280 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 16 | `benchmarks/appworld/evolve/grade.py` | `df3c98e2d1241efc414260cab9d4f208fbe09f57` | blob | 4990 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 17 | `benchmarks/appworld/evolve/precheck.py` | `829769ea4e20b003979aa0c9155f9df84bb92f40` | blob | 7888 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 18 | `benchmarks/appworld/evolve/run.py` | `90ccdb85fb875495916517045862026c4d035b9c` | blob | 14716 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 19 | `benchmarks/appworld/evolve/sandbox.py` | `d29e6b8105dd511c381a1888843e8f10646a9414` | blob | 9059 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 20 | `benchmarks/appworld/evolve/trajectories.py` | `c4adae2cea593e7b7643b7acf026c795175763b6` | blob | 15263 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 21 | `benchmarks/appworld/tool.py` | `e5d836c1b819f3b2418a6011d58a22d2c6f84f21` | blob | 3039 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 22 | `benchmarks/clawbench/README.md` | `f6e4f8904b27ae3c82b92f84b94ab277ab9e5c68` | blob | 3016 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 23 | `benchmarks/clawbench/run.sh` | `71949f5eab184688c099ca86d6ac9c5e2c1de4e7` | blob | 332 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 24 | `benchmarks/clawbench/stream.py` | `75851d3160c94dc9cd1aba7f2aeff58e8b829e7d` | blob | 24683 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 25 | `benchmarks/evolver/small_real.yaml` | `cd2ab3e846239a37524bde6a08519eb250ce166f` | blob | 2184 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 26 | `benchmarks/evolver/subject_template/.gitignore` | `f1e79000ed91ff50ad1093bec7f02576f607d9f3` | blob | 191 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 27 | `benchmarks/evolver/subject_template/benchmarks/__init__.py` | `0803eb0718e7e44cf7f41901d9122a3a1a99ce01` | blob | 75 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 28 | `benchmarks/evolver/subject_template/benchmarks/appworld/__init__.py` | `d2d2d4d6d7049f06cb2e49dcc82c3c742eeb6d6f` | blob | 385 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 29 | `benchmarks/evolver/subject_template/benchmarks/appworld/agent_cli.py` | `27d64dbe5c3ff4f121f8adee197a3516a8f92cef` | blob | 2261 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 30 | `benchmarks/evolver/subject_template/benchmarks/appworld/evolve/__init__.py` | `d8b3756efe0ad45d0e615ebbd8ac184f592fbec6` | blob | 379 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 31 | `benchmarks/evolver/subject_template/benchmarks/appworld/evolve/adapter.py` | `287828aa90c0b2e219c4e837f03643fea5afd581` | blob | 8556 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 32 | `benchmarks/evolver/subject_template/benchmarks/appworld/evolve/candidate.py` | `4e764a1ed64d2789918eab6002cb8f945910f47c` | blob | 4821 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 33 | `benchmarks/evolver/subject_template/benchmarks/appworld/evolve/designer.py` | `40522e8bb5784697352144c341392d5b42df069d` | blob | 6275 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 34 | `benchmarks/evolver/subject_template/benchmarks/appworld/evolve/entry.py` | `77bda5f83188e52a28749d3da7248b12e4d19567` | blob | 11919 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 35 | `benchmarks/evolver/subject_template/benchmarks/appworld/evolve/grade.py` | `76e28c6c47968ed4db5880bfcd15cce1d446dcbd` | blob | 5545 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 36 | `benchmarks/evolver/subject_template/benchmarks/appworld/evolve/tasks.py` | `b5742e0e2cf5968540d922d872aec03a8786aa32` | blob | 5493 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 37 | `benchmarks/picobench/__init__.py` | `bc734cbc75a22f808d3a537b06c3d7b6991806db` | blob | 342 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 38 | `benchmarks/picobench/__main__.py` | `4a9981d05540c97a5d484030e604a70a6278f4bf` | blob | 1207 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 39 | `benchmarks/picobench/artifacts.py` | `2031e75086c4aaf5da7579730e1621e053ba83d2` | blob | 11227 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 40 | `benchmarks/picobench/budget.py` | `3e7b59e1fa621301936192bb4432862eab1469e5` | blob | 35810 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 41 | `benchmarks/picobench/campaign.py` | `b5e57c1185b54c8a9390b4b103c6c11bb3bbf657` | blob | 85205 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 42 | `benchmarks/picobench/canonical.py` | `252b9f10d7287c56e8b64cbbc0509b7823a582fb` | blob | 2965 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 43 | `benchmarks/picobench/claims.py` | `5c0d9a603a401493145ecd39b0f476030c0c6a90` | blob | 2436 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 44 | `benchmarks/picobench/coverage.py` | `4e603edc00b7545e592d18a7eabf593979c29399` | blob | 1615 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 45 | `benchmarks/picobench/environment.py` | `a9c8c0f62e3dc1bd1f069c038febc3c3ec04c9b2` | blob | 4696 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 46 | `benchmarks/picobench/fixtures/mcp/__init__.py` | `6033ae03ae20d880c8241edbda36d92ed490c107` | blob | 324 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 47 | `benchmarks/picobench/fixtures/mcp/catalog.py` | `cfb7f99073eb620790dee52a13a9a0c249dc92b1` | blob | 2701 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 48 | `benchmarks/picobench/fixtures/mcp/server.py` | `04b8b809c1da56345043ae3adbd8301ca554fd0b` | blob | 1318 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 49 | `benchmarks/picobench/fixtures/retrieval/memory_skill_v1.json` | `2569adceb9e3960a8b884da7a89820561cc1e5e1` | blob | 752 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 50 | `benchmarks/picobench/harness.py` | `0065b547c0458b193547eba286c4abafb8a4109e` | blob | 43187 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 51 | `benchmarks/picobench/host.py` | `bcd237dcc65344d076496fef1e8625dc379aeef7` | blob | 5836 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 52 | `benchmarks/picobench/isolation.py` | `a031603331edc56508d632cd0737b16e6232303c` | blob | 1577 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 53 | `benchmarks/picobench/packs/context/__init__.py` | `a1c68d9d0288ff1cf067e3d14e4eb006486a2f15` | blob | 1737 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 54 | `benchmarks/picobench/packs/context/history.py` | `be07de213e3cf79db97f95fb5be2065b864fe159` | blob | 9749 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 55 | `benchmarks/picobench/packs/context/metrics.py` | `635c00d1f72c735b4860c6d0db56654c05b35184` | blob | 3750 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 56 | `benchmarks/picobench/packs/context/models.py` | `3a5dd1eacf61907400338c98c78883993d2b77d1` | blob | 6766 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 57 | `benchmarks/picobench/packs/context/pack.py` | `778cd483779443f8340ac1bab1ddf5866dc217db` | blob | 5702 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 58 | `benchmarks/picobench/packs/context/reducer.py` | `4823f523a33312a23e5da83369677bb3be810e93` | blob | 17165 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 59 | `benchmarks/picobench/packs/context/runner.py` | `ea5b3156519ed9365719c489249750dd296be3c1` | blob | 15595 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 60 | `benchmarks/picobench/packs/context/tasks.py` | `021d6cde7407803ee6ac3913a332eb1bb0f2597b` | blob | 5417 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 61 | `benchmarks/picobench/packs/context/verifier.py` | `f4c1bd9427ce7798ead7864753cae79e20e9ecb8` | blob | 2694 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 62 | `benchmarks/picobench/packs/memory_skill/__init__.py` | `1d683ad36ffc3df9aa79614a85b1257e4cc65eb3` | blob | 1222 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 63 | `benchmarks/picobench/packs/memory_skill/e2e.py` | `f07a3c41ea2c01089302e4b20c8a520d60abd35e` | blob | 22917 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 64 | `benchmarks/picobench/packs/memory_skill/fixtures.py` | `2b96dbd3b76efebd4f74697c28f1cda2e8082dcb` | blob | 14300 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 65 | `benchmarks/picobench/packs/memory_skill/metrics.py` | `e279b078719687cd99f837e014691de826f9b3ee` | blob | 10466 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 66 | `benchmarks/picobench/packs/memory_skill/models.py` | `0426208be3f5a01b0298bfef9eb431b3f388864f` | blob | 872 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 67 | `benchmarks/picobench/packs/memory_skill/pack.py` | `2eefc7df6eb1244bc574ea233106fff2f7f05c2a` | blob | 5264 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 68 | `benchmarks/picobench/packs/memory_skill/reducer.py` | `308cbcf53d486cea77f010d237a2e63b7a41ec08` | blob | 22959 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 69 | `benchmarks/picobench/packs/memory_skill/retrieval.py` | `aaf49d2c69b0683abde383cf25e7a3ee1852a306` | blob | 12921 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 70 | `benchmarks/picobench/packs/memory_skill/runtime.py` | `c9a73135a69a19cb7d968dd8622f919deea764de` | blob | 22610 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 71 | `benchmarks/picobench/packs/memory_skill/semantic_effect.py` | `f3e41b4c080d9bc6522d134cb4eae371d8c2d10f` | blob | 81076 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 72 | `benchmarks/picobench/packs/memory_skill/semantic_fixtures.py` | `8d983bd989ad8fcaff370512c66e24d804052619` | blob | 31519 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 73 | `benchmarks/picobench/packs/memory_skill/semantic_runtime.py` | `f43e484387ab26c04876817481d7c3fd5182ccc9` | blob | 29040 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 74 | `benchmarks/picobench/packs/memory_skill/tasks.py` | `81bb321d14103e5192b8dbcdc15d646c0b6992c7` | blob | 1251 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 75 | `benchmarks/picobench/packs/memory_skill/worker.py` | `717806a82373af41520b6adeb8f03469db6927e1` | blob | 1772 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 76 | `benchmarks/picobench/packs/runtime/__init__.py` | `c43bec09bca957de5cb3bf583b4144232e6bcbdf` | blob | 535 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 77 | `benchmarks/picobench/packs/runtime/live_scheduler_experiment.py` | `ee6269e1f7d2817b6922ff21f91bac05677d8512` | blob | 39115 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 78 | `benchmarks/picobench/packs/runtime/models.py` | `bb90cb16dbdaf6f923048a835118df59124e8fcb` | blob | 4412 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 79 | `benchmarks/picobench/packs/runtime/r0.py` | `a9f55cc3cfbc5fa9fea79cfc0a5ecb4a025bc458` | blob | 15556 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 80 | `benchmarks/picobench/packs/runtime/r1.py` | `e87ab4b4858404b2e6881ff4ad17c0cbf32d8c4b` | blob | 13382 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 81 | `benchmarks/picobench/packs/runtime/scheduler_experiments.py` | `1ae2214025d531f2935d5d57a56bb99b7054ee60` | blob | 27765 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 82 | `benchmarks/picobench/packs/runtime/tool_execution_experiments.py` | `cd04fa0bff9ad5bfbd3ffad58e9b6dbea8dcfb09` | blob | 5975 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 83 | `benchmarks/picobench/packs/tokenwise_cost/__init__.py` | `3c9d3ebd48ccf26036ac1f56fb0866da4971c76b` | blob | 1345 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 84 | `benchmarks/picobench/packs/tokenwise_cost/live.py` | `9df1aba17e7cad3e4e9bac41e47c596bacee0a76` | blob | 13309 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 85 | `benchmarks/picobench/packs/tokenwise_cost/models.py` | `0e08a16c45e857e5443a93413cf287b5735bfdc2` | blob | 1743 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 86 | `benchmarks/picobench/packs/tokenwise_cost/pack.py` | `e5d437e3d4da2cd1331467800807e4e3ab8d2d50` | blob | 2992 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 87 | `benchmarks/picobench/packs/tokenwise_cost/reducer.py` | `f1207969ed885ba7a69ca52e0b54ece66b44f2cb` | blob | 8653 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 88 | `benchmarks/picobench/packs/tokenwise_cost/replay.py` | `141ad07602e493742f1a14d7e86624d47a3a0157` | blob | 7049 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 89 | `benchmarks/picobench/packs/tokenwise_cost/runner.py` | `a20a71b8289828e71a3477528c35159304a2e9a8` | blob | 38473 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 90 | `benchmarks/picobench/packs/tool_mcp/__init__.py` | `c79cca59ffaf005addb9ea4c0a0cc00bcc0c0722` | blob | 1822 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 91 | `benchmarks/picobench/packs/tool_mcp/metrics.py` | `cbd1858f67c1928732dad8b0cb745233626eb6d8` | blob | 10667 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 92 | `benchmarks/picobench/packs/tool_mcp/models.py` | `a8e3a40962c10f9c6371c2e47be9bdbfbf1b91d9` | blob | 2748 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 93 | `benchmarks/picobench/packs/tool_mcp/pack.py` | `edc59dffe513d5d6dcfac1d6f8759b16b63b10c1` | blob | 5956 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 94 | `benchmarks/picobench/packs/tool_mcp/reducer.py` | `9fbc23ea900e0bb57eae5cd4c27de7eba50368f9` | blob | 19989 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 95 | `benchmarks/picobench/packs/tool_mcp/runner.py` | `99cfa7dcdd5b54940c5ac1c3b1611a2d403cfce6` | blob | 26214 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 96 | `benchmarks/picobench/packs/tool_mcp/tasks.py` | `b62c5c70dc0175fefc70c5bfe40d3389261413ec` | blob | 3270 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 97 | `benchmarks/picobench/packs/tool_mcp/verifier.py` | `77710ad5974623fba3b7c7cfca94c50e9ac036ee` | blob | 4234 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 98 | `benchmarks/picobench/packs/tracing/__init__.py` | `c0a9ff84103960fb64a4e28b25b4301a70177773` | blob | 49 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 99 | `benchmarks/picobench/packs/tracing/overhead_experiment.py` | `4deda8f1a950d6b08eb23278cdcc2089ec4ab500` | blob | 28054 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 100 | `benchmarks/picobench/plan.py` | `a21883609a449a4b6b72d6f81c81e241af5b902a` | blob | 18070 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 101 | `benchmarks/picobench/protocol.py` | `3dbcd033e8e83a3b588594ffa4a7d327bc8209ae` | blob | 2278 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 102 | `benchmarks/picobench/README.md` | `4f1b5ea0bf595f75364f5a5655c84479d0d86f47` | blob | 10048 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 103 | `benchmarks/picobench/records.py` | `fe4d218031c66d7e95cedbba017fbaa0b7d1ebcd` | blob | 5520 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 104 | `benchmarks/picobench/reducer.py` | `0e18f7f109ee71ad18986b4ed456376083051d79` | blob | 45219 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 105 | `benchmarks/picobench/registry.py` | `be481b404d80ed48c8e6e942550a22d8899869ab` | blob | 831 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 106 | `benchmarks/picobench/report.py` | `d86057d0882420b72700c505c743697c2258a23f` | blob | 8022 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 107 | `benchmarks/picobench/reproduce.py` | `dc3e8d87a42219e14208b8a4305613fe281677f4` | blob | 27025 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 108 | `benchmarks/picobench/schema.py` | `55b7c73a141b6d51eaba888e960c4f185786960b` | blob | 10037 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 109 | `benchmarks/picobench/scorecard_campaign.py` | `8eb7316bc975cf37ba9668ca26696607cc92e721` | blob | 7038 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 110 | `benchmarks/picobench/scorecard.py` | `b315b56f7d91b6ea287273ccdb0f55fa4bc6f870` | blob | 11460 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 111 | `benchmarks/picobench/semantic_campaign.py` | `053da5c480e0a9997bf58e256b219532829ad8f9` | blob | 61519 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 112 | `benchmarks/picobench/statistics.py` | `342a6d7c7eb44fc532ed93821beb2e5990426f24` | blob | 1499 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 113 | `benchmarks/picobench/suites/agent_application_scorecard_v1.yaml` | `bf117da22690bf5c68da2a41ca6b02a0671b2250` | blob | 3865 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 114 | `benchmarks/picobench/suites/agent_application_ship_1_semantic_v2.yaml` | `8cad9436436644dceac21b7ab0fb1056c1583b43` | blob | 1977 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 115 | `benchmarks/picobench/suites/agent_application_ship_1_semantic.yaml` | `cee57d1510011a123ffafa70c65eb5b7908da993` | blob | 1313 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 116 | `benchmarks/picobench/suites/agent_application_ship_1.yaml` | `2b4b00b65ef5a3106a3d60600e2bb762c9402ca8` | blob | 9118 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 117 | `benchmarks/picobench/tasks/context/calibration.json` | `b56caea8b7024ad416983872773299b87e7f4dc3` | blob | 3927 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 118 | `benchmarks/picobench/tasks/context/expected/ctx-api-rollout.json` | `990de9cefe1e623fdb776acef0f9cdb18ff611ce` | blob | 116 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 119 | `benchmarks/picobench/tasks/context/expected/ctx-backup-runbook.json` | `0290d7a314c8db6885bd688de3396f3d0c2b98ec` | blob | 94 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 120 | `benchmarks/picobench/tasks/context/expected/ctx-cal-alert-routing.json` | `765d1791c5fd8a3d73674ccc761b761aa5b86aac` | blob | 94 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 121 | `benchmarks/picobench/tasks/context/expected/ctx-cal-feature-flag.json` | `df5b9ee457cdb8aeef4ad7e25f52e814e7058d14` | blob | 105 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 122 | `benchmarks/picobench/tasks/context/expected/ctx-cal-index-build.json` | `5dc0a23fd8e3d0375c950058af653301335c4844` | blob | 99 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 123 | `benchmarks/picobench/tasks/context/expected/ctx-cal-queue-policy.json` | `ea706ae35282404d9bfdee9dfa9847e22be66eab` | blob | 105 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 124 | `benchmarks/picobench/tasks/context/expected/ctx-cost-report.json` | `8a4d39661dc053b26a8e220b249f97ca5ac3eda9` | blob | 97 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 125 | `benchmarks/picobench/tasks/context/expected/ctx-customer-migration.json` | `b42074a0b40245badd1f59069749e60c77115592` | blob | 115 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 126 | `benchmarks/picobench/tasks/context/expected/ctx-data-retention.json` | `4fe5a94cb4ae3750f1b4ec01ff77fbdffae9133e` | blob | 104 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 127 | `benchmarks/picobench/tasks/context/expected/ctx-incident-handoff.json` | `a7208aeb65491558f7979c81421e481b6b837b4b` | blob | 109 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 128 | `benchmarks/picobench/tasks/context/expected/ctx-release-brief.json` | `7e864b7e03bf04a2ff43057bbd51850fc8ea9084` | blob | 108 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 129 | `benchmarks/picobench/tasks/context/expected/ctx-security-review.json` | `c0d48900acdaa5f827cbc6de5fb6df46b908fedc` | blob | 103 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 130 | `benchmarks/picobench/tasks/context/formal.json` | `f4a858ea56b247d588eaee3265bbe64543f33c21` | blob | 8026 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 131 | `benchmarks/picobench/tasks/memory_skill/calibration.json` | `9110faa342dc98308229a8ecaf01ab2604ae03ba` | blob | 2286 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 132 | `benchmarks/picobench/tasks/memory_skill/formal.json` | `dde2e6d35aafa9f90b118bdba97578e3c59a144b` | blob | 4244 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 133 | `benchmarks/picobench/tasks/memory_skill/semantic_effect_calibration.json` | `094f8120833222dd6b8b2df78872bee69f9b4d11` | blob | 2470 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 134 | `benchmarks/picobench/tasks/memory_skill/semantic_effect_formal.json` | `71b349d9ec4fe82f55da9ac0faebef3b1637986b` | blob | 9087 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 135 | `benchmarks/picobench/tasks/tokenwise_cost/formal.json` | `314a26d4d216e7667108f416dcb7f1149e49b56b` | blob | 5633 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 136 | `benchmarks/picobench/tasks/tool_mcp/__init__.py` | `99128e58787ce0d317ee7f3abcba25050d596b3f` | blob | 38 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 137 | `benchmarks/picobench/tasks/tool_mcp/calibration.json` | `e7c6f8d31c4cfb5bae3fb81b04c837e47dc6d6fd` | blob | 2956 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 138 | `benchmarks/picobench/tasks/tool_mcp/formal.json` | `c1315bcf5e1350e6a523cc82ae5982795d4e6e12` | blob | 5961 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 139 | `benchmarks/picobench/tokenwise_cost_campaign.py` | `d4833ee91018d40402bc7040719ad5e22a806202` | blob | 3417 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 140 | `benchmarks/picobench/usage.py` | `053e2858c716bd9b6a0cd27817ccd0afb9234fcc` | blob | 10315 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 141 | `benchmarks/picobench/verifier.py` | `79e58dc7801d9a8ee9e89640dd98c3361e92e9b6` | blob | 5456 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 142 | `benchmarks/pinchbench/assets/ai_blog.txt` | `5c2787cd422484470faef496ce9e57014503a610` | blob | 4559 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 143 | `benchmarks/pinchbench/assets/company_expenses.xlsx` | `3aecd38f464ffed4d89befe5a34df3a0f191432a` | blob | 5996 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 144 | `benchmarks/pinchbench/assets/quarterly_sales.csv` | `2df343c99fe18c1718885c740861036f28d2f78f` | blob | 1288 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 145 | `benchmarks/pinchbench/bot_runner/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 146 | `benchmarks/pinchbench/bot_runner/benchmark.py` | `3749521962b14088c4ac5ef05a9b7b1ee235bdd1` | blob | 9788 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 147 | `benchmarks/pinchbench/bot_runner/bot_executor.py` | `88d8bfe4aedf70bdff81f1e24a28752919b3cf42` | blob | 9428 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 148 | `benchmarks/pinchbench/bot_runner/grading.py` | `1db1fd98b821153c346b0581d3f95ce0a0a113b3` | blob | 12759 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 149 | `benchmarks/pinchbench/bot_runner/run.sh` | `34b0952e7dcfd3227a51b7cee854212a3a24d2be` | blob | 1384 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 150 | `benchmarks/pinchbench/bot_runner/task_loader.py` | `e8ae02ceaf367e63ef104ef489c9925df7de34c1` | blob | 3745 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 151 | `benchmarks/pinchbench/direct/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 152 | `benchmarks/pinchbench/direct/benchmark.py` | `cb064b92d7b0d8c6ff98aeb6370c9173bde09c1a` | blob | 14816 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 153 | `benchmarks/pinchbench/direct/grading.py` | `5a2b04850265b399c8ab74e8c1c5ea694e0084a2` | blob | 12775 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 154 | `benchmarks/pinchbench/direct/pico_executor.py` | `e10386907bc58e60c1d14826533f08a76b4dbefd` | blob | 20838 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 155 | `benchmarks/pinchbench/direct/run.sh` | `ba2c069b08e393ee2e05cf2905a69f1734f61a1a` | blob | 1354 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 156 | `benchmarks/pinchbench/direct/task_loader.py` | `87be30f070f36d2e1d0daed56ac81f7f37f8f5bd` | blob | 3731 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 157 | `benchmarks/pinchbench/tasks/task_00_sanity.md` | `938a2a8f57a91c9c6f826c0d9b8c2b49061ec336` | blob | 1484 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 158 | `benchmarks/pinchbench/tasks/task_01_calendar.md` | `ff6239b42979fea5faf201515e4562e111530f04` | blob | 3739 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 159 | `benchmarks/pinchbench/tasks/task_02_stock.md` | `7203dd9976e5e2d6bd846d5607629352c11cae5c` | blob | 3658 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 160 | `benchmarks/pinchbench/tasks/task_03_blog.md` | `b09313768685bfcec07ebc32c7b4cd2627169215` | blob | 4039 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 161 | `benchmarks/pinchbench/tasks/task_04_weather.md` | `26c3a8496fa0db1eba53fc5f642d604f0d1b7ec6` | blob | 4504 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 162 | `benchmarks/pinchbench/tasks/task_05_summary.md` | `e035c810a0151939d0bc17381afa4693de864657` | blob | 8715 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 163 | `benchmarks/pinchbench/tasks/task_06_events.md` | `878fb69ae127d6c7e2db340ab466197e749f1f17` | blob | 4091 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 164 | `benchmarks/pinchbench/tasks/task_07_email.md` | `ac973815a328bafd8174c18969c6e9d2c5a70f97` | blob | 4004 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 165 | `benchmarks/pinchbench/tasks/task_08_memory.md` | `5050f100d1da5607147356347acab1af85516428` | blob | 5303 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 166 | `benchmarks/pinchbench/tasks/task_09_files.md` | `bf3d9923cb3273c423fa231e8c8fe115b2b4859d` | blob | 3987 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 167 | `benchmarks/pinchbench/tasks/task_10_workflow.md` | `26b1b821174ad4977d546e91e2c102d8b83486f0` | blob | 7596 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 168 | `benchmarks/pinchbench/tasks/task_11_clawdhub.md` | `ffafd4666293a045ccca83988d9f2b817aa6e547` | blob | 3244 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 169 | `benchmarks/pinchbench/tasks/task_12_skill_search.md` | `7588366d55c2d68e40f9dc30722333862536fb47` | blob | 4379 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 170 | `benchmarks/pinchbench/tasks/task_13_image_gen.md` | `8c37df4a569e8e34f4fc3d0da262336eed8b4748` | blob | 6522 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 171 | `benchmarks/pinchbench/tasks/task_14_humanizer.md` | `c26ebf6319c3071d2433bc5cb3d74afe4fcd3298` | blob | 4077 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 172 | `benchmarks/pinchbench/tasks/task_15_daily_summary.md` | `3661eee47efc27a734f52527be1aedf4cb9ff007` | blob | 13479 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 173 | `benchmarks/pinchbench/tasks/task_16_email_triage.md` | `8386380bfb1be054cb4ec067bfac45c8736effd5` | blob | 26393 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 174 | `benchmarks/pinchbench/tasks/task_17_email_search.md` | `33c454950974c861137eb53e9c6b24741a318435` | blob | 31077 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 175 | `benchmarks/pinchbench/tasks/task_18_market_research.md` | `81e5239a8f2e0b28812dc5ad0973af82dcea5ded` | blob | 11376 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 176 | `benchmarks/pinchbench/tasks/task_19_spreadsheet_summary.md` | `0804287c28948048acd36cc88dbda1150bcdda7c` | blob | 10334 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 177 | `benchmarks/pinchbench/tasks/task_20_eli5_pdf_summary.md` | `e5c869319a8c10d887c40fc1990779ba27681f49` | blob | 6276 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 178 | `benchmarks/pinchbench/tasks/task_21_openclaw_comprehension.md` | `b4c789d8cfb9bd76219556cb380b15583cf8914c` | blob | 5510 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 179 | `benchmarks/pinchbench/tasks/task_22_second_brain.md` | `f3878c5b8b3d992d37bd624e25da0473e4d65fa1` | blob | 8303 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 180 | `benchmarks/pinchbench/tasks/TASK_TEMPLATE.md` | `ce7948af1c161e7373c96d6f9261cdd764ac6ab6` | blob | 9034 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 181 | `benchmarks/README.md` | `8f2edfd917c5bd3418d0ecb609b311f55e557024` | blob | 6920 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 182 | `benchmarks/skill_evals/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 183 | `benchmarks/skill_evals/queries.jsonl` | `3ba3409e4720a4fb1c792dd8c6019b5fae69fe96` | blob | 8079 | `PORT_BENCHMARK_OR_REVIEW` | benchmarks/** |
| 184 | `commitlint.config.cjs` | `09a9f4e8a557710b84361953e14e2e2a479c45c4` | blob | 404 | `REVIEW_SUPPORT` | repository support only |
| 185 | `CONTRIBUTING.md` | `992101d29178736361e27f78f829b288174c7775` | blob | 3186 | `REVIEW_SUPPORT` | repository support only |
| 186 | `docs/evaluation/README.md` | `e7f3125df7cf93f18b9b1646aa5cab7d6e644009` | blob | 522 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 187 | `docs/evaluation/runtime-scheduler-experiments.md` | `5e124cc289c160d891c29a84a539adbd86c2d859` | blob | 6151 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 188 | `docs/evaluation/tokenwise-cost.md` | `31e877fef664ab4889d8c7a9833f8c5b4ceb3408` | blob | 7427 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 189 | `docs/evaluation/tracing-overhead.md` | `b2646bcb4c361650d93eaee9e168ba9387458240` | blob | 2969 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 190 | `docs/examples/evolve_appworld.yaml` | `250d8488a9f584c6eebf2bc3576f4d02584b509c` | blob | 3060 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 191 | `docs/examples/subject_runtime.json` | `6b67f0a811d5d22b4eb9dbaacb5bfdcebe44a687` | blob | 401 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 192 | `docs/onboarding/agent-install.md` | `d0699d7b9164f49e66ce18cd644b1dec7c5df0d6` | blob | 3756 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 193 | `docs/onboarding/feishu.zh-CN.md` | `f5277ffa0b878d2f46783b14bba734e7c761e0e4` | blob | 3252 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 194 | `docs/onboarding/media-manifest.md` | `78bc8cf6ce04e0b873ab1f0323cc93007f0c5d36` | blob | 1761 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 195 | `docs/onboarding/memory.zh-CN.md` | `5677447650b6e87d82073bf463dc1b6f9f3ba8d2` | blob | 1815 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 196 | `docs/onboarding/README.zh-CN.md` | `4598b08dd1540c65a29646efb005861865cea59e` | blob | 4179 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 197 | `docs/onboarding/troubleshooting.md` | `af8c193ba98b2af7ddfcd205053218e751fdfbc6` | blob | 2947 | `MERGE_DOC_OR_REVIEW` | docs/** |
| 198 | `eslint.base.mjs` | `187a87a81c2aeca415d8bef8613b66b6d3639e7d` | blob | 1576 | `REVIEW_SUPPORT` | repository support only |
| 199 | `hatch_build.py` | `0bdabc4faaaa7f3f2e9da528ae2282d7ee7b4f32` | blob | 1871 | `MERGE_BUILD` | hatch_build.py |
| 200 | `install.ps1` | `ce4d3f281a8a4f3fe1dda7a43e3ae6290dc82cf4` | blob | 12364 | `MERGE_BUILD` | install.ps1 |
| 201 | `install.sh` | `c9f0d2888370af2887d077a91ecf043d03424508` | blob | 11377 | `MERGE_BUILD` | install.sh |
| 202 | `LICENSE` | `33068551c97e6ca2cce7c1e85ee63d97de1e9e1a` | blob | 10172 | `PRESERVE_LICENSE` | LICENSE |
| 203 | `LICENSES/MIT-hermes-agent.txt` | `75410e73319c72cd3e991a501c5455eb78f38375` | blob | 1070 | `PRESERVE_LICENSE` | LICENSES/MIT-hermes-agent.txt |
| 204 | `LICENSES/MIT-ink.txt` | `fcb8fa9e131348df733a6ce59aa0d5a9c7b6f331` | blob | 1202 | `PRESERVE_LICENSE` | LICENSES/MIT-ink.txt |
| 205 | `LICENSES/MIT-nanobot.txt` | `d353b0331facf293335136710c173dd8d6d586d6` | blob | 1103 | `PRESERVE_LICENSE` | LICENSES/MIT-nanobot.txt |
| 206 | `LICENSES/README.md` | `fa5e9a55eee3183d4c80721addc68e7387615821` | blob | 526 | `PRESERVE_LICENSE` | LICENSES/README.md |
| 207 | `Makefile` | `92859890fc641faaa2352986fdd79d08e1b482fb` | blob | 9929 | `MERGE_BUILD` | Makefile |
| 208 | `NOTICES.md` | `5e4d88cdb6443b63fe2f521c05262f9e50b1460b` | blob | 2799 | `PRESERVE_LICENSE` | NOTICES.md |
| 209 | `package-lock.json` | `0a1f35fd06e2776169964567eb72e6816d3239c6` | blob | 35825 | `MERGE_BUILD` | package-lock.json |
| 210 | `package.json` | `376130e23d8ae0d651533a22896b635eaa71d1f9` | blob | 270 | `MERGE_BUILD` | package.json |
| 211 | `pico/__init__.py` | `e92777aa9e5baa3d3cadcb86f90c1fd11086fcdb` | blob | 2266 | `PORT` | pico/** + mapped CodeCub integration |
| 212 | `pico/__main__.py` | `2b11875e593f78934610ba3076a04210459435ef` | blob | 448 | `PORT` | pico/** + mapped CodeCub integration |
| 213 | `pico/agent/__init__.py` | `65a3a24ceb99b614caea1f665add262d9d159beb` | blob | 1331 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 214 | `pico/agent/context/__init__.py` | `af996d91600ab401409a284e2c1dca407a607f24` | blob | 490 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 215 | `pico/agent/context/builder.py` | `623eb263dba27572d175c12ce2dc477c001882e3` | blob | 18515 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 216 | `pico/agent/hook/__init__.py` | `a88946755759da18cd8d7b7b9edbffb22a165414` | blob | 754 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 217 | `pico/agent/hook/base.py` | `34cb328cc3b7e75953d15d83d2afe51a9514e3b2` | blob | 7291 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 218 | `pico/agent/hook/composite.py` | `5b2fe72ebc266f9eb7167bfd66f504a140e9f1de` | blob | 5535 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 219 | `pico/agent/loop/__init__.py` | `89efe97d6c5d8670ef71f509aa3b7d043b79191c` | blob | 517 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 220 | `pico/agent/loop/checkpoint.py` | `05680d7aa55583306f0b2f94a4a2921cbf830428` | blob | 13756 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 221 | `pico/agent/loop/main.py` | `ebe8bade1b70706c8d007b63e46c7333451995c0` | blob | 121668 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 222 | `pico/agent/loop/recovery.py` | `22b5cc570eea717c30bd59dab67d78ac8f435ca5` | blob | 6366 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 223 | `pico/agent/personalizer/__init__.py` | `30dad8512e9f6aa97457ed2f23db3c2b78674748` | blob | 400 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 224 | `pico/agent/personalizer/personalizer.py` | `535c163d5dd6bb960c83eb909173bb2a4307cc07` | blob | 16135 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 225 | `pico/agent/spine_runner.py` | `9116409ef04834ac8325f5a789df24c968213056` | blob | 1045 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 226 | `pico/agent/subagent/__init__.py` | `6adebb5c814c429d24b18548a8e0f34eb395b45f` | blob | 392 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 227 | `pico/agent/subagent/manager.py` | `d767779f6b5edcd4be45f12f057fc47ab719160c` | blob | 19082 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 228 | `pico/agent/tools/__init__.py` | `f1057bfe53e63e3b5ac2e902095bbfa252d27151` | blob | 813 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 229 | `pico/agent/tools/ask_user.py` | `4ec7d9ba888fc4ac493093cd3c47e3d32510bc6e` | blob | 6753 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 230 | `pico/agent/tools/base.py` | `6fa8dab908976f089b49a25409d2718e94cc9ded` | blob | 12736 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 231 | `pico/agent/tools/execution.py` | `c101feac11944e9decf3c2576eba5d7315a2ac52` | blob | 1262 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 232 | `pico/agent/tools/file_search.py` | `5afe9c0e0544e9226363770d32a5deaf736fa3a0` | blob | 17864 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 233 | `pico/agent/tools/filesystem.py` | `c507b2130ab62877603d9c8117ff75973ebc04c3` | blob | 16525 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 234 | `pico/agent/tools/mcp.py` | `93b80347f05c0cbe99f6e34c0918ba1955682c04` | blob | 9014 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 235 | `pico/agent/tools/message.py` | `6ee76494691db5ef9b42424412a69ef63bba9298` | blob | 6753 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 236 | `pico/agent/tools/registry.py` | `b9cc9bbacbf272d71c0eee20f14992df9eb93fe9` | blob | 11521 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 237 | `pico/agent/tools/shell.py` | `669937c3f844f5112ac68c27c461ce1d83e0137f` | blob | 9156 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 238 | `pico/agent/tools/skill.py` | `9fbf5b05e0987be5f5591a15c2b7877afdeeca23` | blob | 1565 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 239 | `pico/agent/tools/spawn.py` | `6bb27055177f35a1a420000ef642161b3bb8f5d8` | blob | 4351 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 240 | `pico/agent/tools/tool_index.py` | `e426bc1c3fbc9de17eeb18d02cb0270441b5a221` | blob | 7532 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 241 | `pico/agent/tools/tool_search.py` | `66a312a71383427c82badb6eb43f2c0ec74a8924` | blob | 13547 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 242 | `pico/agent/tools/web.py` | `6fdda5291fefc3d18001937a2e3a2941dd11de5a` | blob | 10400 | `PORT_OR_WRAP` | codecub/agent/** + codecub/runtime.py + pico/agent/** |
| 243 | `pico/auth/__init__.py` | `a5eedf4b5d24625e725269463bc1334301f41f0c` | blob | 1323 | `PORT_OR_WRAP` | codecub/auth.py + pico/auth/** |
| 244 | `pico/auth/allowlist.py` | `431d8ad1a473984f0701ee0988da421bdf23201a` | blob | 2985 | `PORT_OR_WRAP` | codecub/auth.py + pico/auth/** |
| 245 | `pico/auth/capability_token.py` | `fef2499971ed1e69579ef2d33abe6ad1802e3e04` | blob | 5514 | `PORT_OR_WRAP` | codecub/auth.py + pico/auth/** |
| 246 | `pico/auth/managed_settings.py` | `c802666f53a268a268fb7cb32ffe184ac48ba0b8` | blob | 1454 | `PORT_OR_WRAP` | codecub/auth.py + pico/auth/** |
| 247 | `pico/call_efficiency/__init__.py` | `d636fc7fe0714fa99ddc51a99c7b82ef45ea1338` | blob | 902 | `PORT_OR_WRAP` | codecub/cache.py + codecub/model_gateway.py + codecub/telemetry/** + pico/call_efficiency/** |
| 248 | `pico/call_efficiency/cache.py` | `423727b6951523dc7df1c0ab97d0b358d8d5d0a9` | blob | 5541 | `PORT_OR_WRAP` | codecub/cache.py + codecub/model_gateway.py + codecub/telemetry/** + pico/call_efficiency/** |
| 249 | `pico/call_efficiency/ledger.py` | `483b278961400a4bcf3a3c1655ad7830fbbcc131` | blob | 10434 | `PORT_OR_WRAP` | codecub/cache.py + codecub/model_gateway.py + codecub/telemetry/** + pico/call_efficiency/** |
| 250 | `pico/call_efficiency/model_catalog_cache.py` | `3b773d2521e1ef4d989bbe2a7575eddd20120284` | blob | 3786 | `PORT_OR_WRAP` | codecub/cache.py + codecub/model_gateway.py + codecub/telemetry/** + pico/call_efficiency/** |
| 251 | `pico/call_efficiency/models.py` | `2778240d557d638257be052e8e11c308a8e739b0` | blob | 2534 | `PORT_OR_WRAP` | codecub/cache.py + codecub/model_gateway.py + codecub/telemetry/** + pico/call_efficiency/** |
| 252 | `pico/call_efficiency/pricing.py` | `aca84f6a3510a3c5be8cfaf1c3261bcc46be62b3` | blob | 15346 | `PORT_OR_WRAP` | codecub/cache.py + codecub/model_gateway.py + codecub/telemetry/** + pico/call_efficiency/** |
| 253 | `pico/call_efficiency/provider.py` | `98fcb408db2de4bccd4bb7d8619d116e97223314` | blob | 12177 | `PORT_OR_WRAP` | codecub/cache.py + codecub/model_gateway.py + codecub/telemetry/** + pico/call_efficiency/** |
| 254 | `pico/call_efficiency/runtime.py` | `a4380525ab1e9a9cefc7b3ddae58852ebb3c5676` | blob | 8044 | `PORT_OR_WRAP` | codecub/cache.py + codecub/model_gateway.py + codecub/telemetry/** + pico/call_efficiency/** |
| 255 | `pico/call_efficiency/usage.py` | `45eee6bcfa1b25ea518528bf59464341b9e94c03` | blob | 3546 | `PORT_OR_WRAP` | codecub/cache.py + codecub/model_gateway.py + codecub/telemetry/** + pico/call_efficiency/** |
| 256 | `pico/channels/__init__.py` | `1f26f49b4c92fc70b7f2f8e3cedca360acd7ee07` | blob | 1019 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 257 | `pico/channels/adapters/__init__.py` | `86ccd13e5865ccb1451495bc9e23d87ab2fae94e` | blob | 457 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 258 | `pico/channels/adapters/feishu/__init__.py` | `b232d558a0ed35784bb7db7f8786da1a983ceabc` | blob | 365 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 259 | `pico/channels/adapters/feishu/cards.py` | `13df65893922ad063ee79b3fc34045d68d793a24` | blob | 6897 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 260 | `pico/channels/adapters/feishu/channel.py` | `66fd995e22ffa73986073b34203d883a1cfa67a1` | blob | 27091 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 261 | `pico/channels/adapters/feishu/content.py` | `541f69f8df6880474e988ff3cda3b249d1755d11` | blob | 6468 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 262 | `pico/channels/adapters/feishu/spec.py` | `ac07e05ef277ba5cc65d064b56bc40ca8e214115` | blob | 623 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 263 | `pico/channels/adapters/qq/__init__.py` | `facd83c388dba98aebd0b47d621b203fa051054d` | blob | 319 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 264 | `pico/channels/adapters/qq/channel.py` | `a217275904159bbba2f0a69eaf1fb3dcca10d7b0` | blob | 9283 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 265 | `pico/channels/adapters/qq/parsing.py` | `4860799f61bf2750c5622afabd2ede3c8d61969b` | blob | 3912 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 266 | `pico/channels/adapters/qq/spec.py` | `33116ac603ef7b07425242317f7713c799f62a22` | blob | 574 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 267 | `pico/channels/adapters/wecom/__init__.py` | `8a42248879d421685c47caa83ae377ed724cacde` | blob | 338 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 268 | `pico/channels/adapters/wecom/channel.py` | `5983e42b4422ab31c8951dc2eb17d19fced9056d` | blob | 12749 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 269 | `pico/channels/adapters/wecom/spec.py` | `39d3afb46017e6fee4a2ca3bd9f0ae815ca4caaa` | blob | 591 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 270 | `pico/channels/base.py` | `a7c5ded1087b6d173cee4994969436f4de4b66fd` | blob | 1969 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 271 | `pico/channels/contract.py` | `d6f6a668b54cdcc5537093a25d973fb2a802a604` | blob | 4292 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 272 | `pico/channels/errors.py` | `7282c97b25f5dc2eaaa20ff08464d537f55382b1` | blob | 1854 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 273 | `pico/channels/intake.py` | `d53c3f308c3943b8f7efa95eaea3913c3cc115cc` | blob | 6626 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 274 | `pico/channels/manager.py` | `de7cfb990b11823c40aa8c97a3648078bcab3f3b` | blob | 11256 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 275 | `pico/channels/media.py` | `5eedbfc36b2fec837275c8195a7d69bf8d21a7ea` | blob | 1434 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 276 | `pico/channels/outlet.py` | `8fa89e430ef49269b80f02ea6539f1b11d3c8d63` | blob | 1858 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 277 | `pico/channels/registry.py` | `6c832aeb3be699ca37b71f38abcce9a8df9b6325` | blob | 1734 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 278 | `pico/channels/transcribe.py` | `66ca73f4dea8a1cdb97459b61ce3d0720d649d63` | blob | 915 | `PORT_OR_WRAP` | codecub/channels.py + pico/channels/** |
| 279 | `pico/cli/__init__.py` | `cb2693a97d674d7992c68f8f61f5913a208e7fc7` | blob | 27 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 280 | `pico/cli/_cron_handler.py` | `c00d3ee93dbae8cc63ef5dda5f9c77cb39b87e34` | blob | 8766 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 281 | `pico/cli/_eval_stack.py` | `4a74aad95343363158f72c6fb2715dc9d3ccc051` | blob | 2090 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 282 | `pico/cli/_exit.py` | `1fb31f14dffc31ab0bbecf05a15955e7f6aa43fc` | blob | 1629 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 283 | `pico/cli/_gateway_lock.py` | `b43a22a32a165c5b32e0191fc9301ba59f743547` | blob | 3536 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 284 | `pico/cli/_gateway_spine.py` | `33ad0c41cdb5dab4c8fd1ce4d027d8c391fe4cfb` | blob | 7081 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 285 | `pico/cli/_helpers.py` | `a696efffa5d364b8b30e9f8931954a7d6329e3c0` | blob | 9717 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 286 | `pico/cli/_hooks_stack.py` | `7e9f7beb47ce6aa3af0e59e4d76c15c1a9693f17` | blob | 1611 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 287 | `pico/cli/_log_file.py` | `c3ed5c962f42f649d0ef7d0c84ea2ef6949d1171` | blob | 5660 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 288 | `pico/cli/_log_silence.py` | `4e8de25b86c3b86436bf1bd0f41628b395247196` | blob | 1163 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 289 | `pico/cli/_plugin_stack.py` | `81e1028a4671d9485f3f8fbd0eaaef9cf3bec3e9` | blob | 13507 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 290 | `pico/cli/_repl_slash.py` | `510985bd7ca590d349e7cad2a601df658beeb60e` | blob | 9559 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 291 | `pico/cli/_repl_spine.py` | `4cbc692307e3ba00feea1550fe673d89d4661f63` | blob | 6706 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 292 | `pico/cli/_runtime_assembly.py` | `38f8556f07a5a138837bd4708c35f0e84e018f86` | blob | 7627 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 293 | `pico/cli/_runtime_host.py` | `dea61463161b5aa9ff6e747792a97e37bf2efce5` | blob | 2420 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 294 | `pico/cli/_styles.py` | `a2c93b5f2084d8f42bbe2885d04ffcb401be5d6b` | blob | 1749 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 295 | `pico/cli/_token_wise_stack.py` | `e244edc7aaeb82ca3f8e3c609e793b9a9b142cc5` | blob | 1630 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 296 | `pico/cli/agent_commands.py` | `6c624a07e4043bf4f9acfbf27c4d5bb444e08402` | blob | 18105 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 297 | `pico/cli/channel_commands.py` | `53ca62bc5d4531cbcb449c066b40188a88d822fa` | blob | 18777 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 298 | `pico/cli/commands.py` | `9ee2fbddd3c486f44115481cea1fc7dc264c63b7` | blob | 5690 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 299 | `pico/cli/cron_commands.py` | `be6612eacea4ef9573099a0e3ed6961e7114dee9` | blob | 33543 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 300 | `pico/cli/doctor_commands.py` | `89e96bb216dd2c34a21f388e00d80e4d53037cb0` | blob | 14185 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 301 | `pico/cli/evolve_commands.py` | `49932c9e35a823cfb4f924b3dbe6df97f6d3b34e` | blob | 591 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 302 | `pico/cli/gateway_commands.py` | `11ee20012a637510cfb7f50bf81eef4e2c91b1ab` | blob | 16786 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 303 | `pico/cli/onboard_commands.py` | `09acdf76cc3b787b2920318b733c6b39a9c31f59` | blob | 98018 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 304 | `pico/cli/plugin_commands.py` | `618cd0398fe9a83350c24eaae9ee4fed8a38d559` | blob | 6787 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 305 | `pico/cli/provider_commands.py` | `984d16dd304c66a5408548c4b2af95e082206743` | blob | 16131 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 306 | `pico/cli/sandbox_commands.py` | `adb6e81f7ae2bc828e8cc207bb07082db30dcf4d` | blob | 17059 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 307 | `pico/cli/session_commands.py` | `41eba71e25497fd67bfecfcb19d2e6507f3d440f` | blob | 11695 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 308 | `pico/cli/skill_commands.py` | `e559c6413246b4b17f3fae9f4681dcf1ee6ec96b` | blob | 2780 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 309 | `pico/cli/status_commands.py` | `a4548e1a4bfebeffd544b6e2c598647ac2c65335` | blob | 2708 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 310 | `pico/cli/tracing_commands.py` | `d933adc5ea4ed46eec4a2a3479121f2da658e465` | blob | 7480 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 311 | `pico/cli/tui_commands.py` | `f819fb5119261cede877306f204c10a0e379a29d` | blob | 38753 | `PORT_OR_WRAP` | codecub/cli.py + codecub/app_protocol.py + pico/cli/** |
| 312 | `pico/config/__init__.py` | `3d7aa5d19622f1738a24edc4dcf4a9ca3e69e9e5` | blob | 1693 | `PORT_OR_WRAP` | codecub/provider_config.py + codecub/connections/** + pico/config/** |
| 313 | `pico/config/loader.py` | `f5432813a652cd99e15547845d9bc121f908901a` | blob | 14425 | `PORT_OR_WRAP` | codecub/provider_config.py + codecub/connections/** + pico/config/** |
| 314 | `pico/config/paths.py` | `03c2e4847ef56424ec04ca73945ed03f88747b2f` | blob | 4758 | `PORT_OR_WRAP` | codecub/provider_config.py + codecub/connections/** + pico/config/** |
| 315 | `pico/config/pico.py` | `a353d7bfd23588090b232690482f347ceb3fa6b8` | blob | 27499 | `PORT_OR_WRAP` | codecub/provider_config.py + codecub/connections/** + pico/config/** |
| 316 | `pico/config/schema.py` | `a661b17a3dab0cafb0b823a6720f99d2a97645e8` | blob | 25269 | `PORT_OR_WRAP` | codecub/provider_config.py + codecub/connections/** + pico/config/** |
| 317 | `pico/config/update_channels.py` | `64f334d7a4b5c3b0a2705a7ba58fa06901172375` | blob | 10422 | `PORT_OR_WRAP` | codecub/provider_config.py + codecub/connections/** + pico/config/** |
| 318 | `pico/config/update_providers.py` | `c338871e51513f3a6190b303111930b0e53b02c5` | blob | 22244 | `PORT_OR_WRAP` | codecub/provider_config.py + codecub/connections/** + pico/config/** |
| 319 | `pico/config/update.py` | `c3212007d09c2f63e6a142e55228f258c8cca68c` | blob | 12219 | `PORT_OR_WRAP` | codecub/provider_config.py + codecub/connections/** + pico/config/** |
| 320 | `pico/context_engine/__init__.py` | `ee5bacf39870e0fa8740694b343d19ce192e5676` | blob | 1052 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 321 | `pico/context_engine/assembler.py` | `3ed544573fa7bcbe50ee4fb4972fce96b6cf3cd6` | blob | 6858 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 322 | `pico/context_engine/base.py` | `76c35ed7e4b107f00659ace860a82000106c798a` | blob | 9850 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 323 | `pico/context_engine/curator.py` | `c1af73d62b63ecd8a5e2bdd4b86ee0ada5aaf7c4` | blob | 35885 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 324 | `pico/context_engine/factory.py` | `17fb5df0fa41efc41af1e923be55594eefa50ad1` | blob | 6520 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 325 | `pico/context_engine/history_trimmer.py` | `b7b3c0d87c66122e52d784a0e99747b8d26d9c93` | blob | 12066 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 326 | `pico/context_engine/segments/__init__.py` | `c7761c90ac2151da0cb0cdef38509851a7d91d0b` | blob | 1057 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 327 | `pico/context_engine/segments/active_skills.py` | `ba7eff3774ab7c542b48b84cffc855b55044d3fe` | blob | 1526 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 328 | `pico/context_engine/segments/bootstrap.py` | `942c8c86d5fbc5916fb1a4e3462e2ea1353d2b3d` | blob | 1053 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 329 | `pico/context_engine/segments/curator.py` | `9fe90b3b1a965a4cb7d45e70ef3611a5dfd01062` | blob | 15638 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 330 | `pico/context_engine/segments/identity.py` | `db832b13a47a7ae444fbbecef08cab14b3151b81` | blob | 954 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 331 | `pico/context_engine/segments/memory.py` | `616d17877a3573ff9439c23318f467f97e5acc04` | blob | 2792 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 332 | `pico/context_engine/segments/render.py` | `6af04acb78a0aafb3c162347024b9b65e02936ff` | blob | 13384 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 333 | `pico/context_engine/segments/skills.py` | `e155b6af5a00b45b507ee4966ec222945abacf83` | blob | 3874 | `PORT_OR_WRAP` | codecub/context_assembler.py + codecub/context_compiler.py + codecub/context_manager.py + pico/context_engine/** |
| 334 | `pico/eval_engine/__init__.py` | `9900ae1261feae9c6f0f140296e15271e7e4035b` | blob | 2044 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 335 | `pico/eval_engine/adapter/__init__.py` | `90222e73dfa4508b2a5cfd5da4444d77d3661bd2` | blob | 395 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 336 | `pico/eval_engine/adapter/adapter.py` | `074cc9d223d6383ba0c7b721e89e8c0a5f7c3738` | blob | 3064 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 337 | `pico/eval_engine/config.py` | `5369bc9e887502956c8b4632517f4511c8266b3a` | blob | 2530 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 338 | `pico/eval_engine/engine.py` | `6bb521e878383a79a16771040deb7a79545848d7` | blob | 5112 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 339 | `pico/eval_engine/hooks/__init__.py` | `97881c79699da6326fe6f092d93e84e67184a839` | blob | 596 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 340 | `pico/eval_engine/hooks/after_iteration_hook.py` | `eabc3331e65ed6879fb17d1d81dbeb9031c9b110` | blob | 4847 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 341 | `pico/eval_engine/hooks/before_iteration_hook.py` | `ad04a7a34abde2f8dbe9c6fe9fa1b8265ef7b8d3` | blob | 2775 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 342 | `pico/eval_engine/hooks/tool_audit_hook.py` | `8cd6766f071c1b569026edde5c728592789bfcad` | blob | 3804 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 343 | `pico/eval_engine/judge/__init__.py` | `ad68b5ebad7f49b58f567a6dda5293e02c66bb1f` | blob | 382 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 344 | `pico/eval_engine/judge/judge.py` | `988a379839502e8cc46b49ff1effcd27e2e02326` | blob | 4670 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 345 | `pico/eval_engine/prompts/__init__.py` | `d8661e10f43e5d9122dbbc901451eceeeb240f24` | blob | 525 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 346 | `pico/eval_engine/prompts/task_completion.py` | `94daa547258b74baa9e391b1cd1d272483822de7` | blob | 1096 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 347 | `pico/eval_engine/prompts/tool_safety.py` | `9f46c0a275953e748c818b7cc9235914271b87ca` | blob | 981 | `PORT_OR_WRAP` | codecub/evaluator.py + codecub/experiments/** + pico/eval_engine/** |
| 348 | `pico/evolver/__init__.py` | `932684af9782a34f5a7f8872b32562ef2ecab7d5` | blob | 2386 | `PORT_OR_WRAP` | pico/evolver/** |
| 349 | `pico/evolver/__main__.py` | `7dbd5d5f14f9c4298b2377b66456b606ee2da262` | blob | 64 | `PORT_OR_WRAP` | pico/evolver/** |
| 350 | `pico/evolver/activation/__init__.py` | `a116f9bb12a5ba0348a4f554a0e90a0afa7711df` | blob | 1310 | `PORT_OR_WRAP` | pico/evolver/** |
| 351 | `pico/evolver/activation/artifacts.py` | `fff59e8b676fb4df581775f8246b88c0746c1495` | blob | 48077 | `PORT_OR_WRAP` | pico/evolver/** |
| 352 | `pico/evolver/activation/audit.py` | `24171a18594c4b34c94eae4bc79759f3df95f09c` | blob | 3278 | `PORT_OR_WRAP` | pico/evolver/** |
| 353 | `pico/evolver/activation/chamber.py` | `3c0c84ba44f91e3e4ac811c5de09c854b2751bf0` | blob | 3796 | `PORT_OR_WRAP` | pico/evolver/** |
| 354 | `pico/evolver/activation/ledger.py` | `76e19d75f6009e1ffcb18cc90413bb9cda207246` | blob | 6248 | `PORT_OR_WRAP` | pico/evolver/** |
| 355 | `pico/evolver/activation/predicates.py` | `bd6d4f9572205afeed32abdda053386051465fc1` | blob | 4110 | `PORT_OR_WRAP` | pico/evolver/** |
| 356 | `pico/evolver/activation/routing_query.py` | `09cade5c3cdb4b492327d2e96c8f2a236488ddd0` | blob | 3367 | `PORT_OR_WRAP` | pico/evolver/** |
| 357 | `pico/evolver/activation/spec.py` | `c66283a7efe0ecd417a37516712e2cb9a5c6ba24` | blob | 12173 | `PORT_OR_WRAP` | pico/evolver/** |
| 358 | `pico/evolver/activation/summary.py` | `f316b982ab8969e532110f9a05bc091e9918288e` | blob | 24664 | `PORT_OR_WRAP` | pico/evolver/** |
| 359 | `pico/evolver/analysis/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_OR_WRAP` | pico/evolver/** |
| 360 | `pico/evolver/analysis/failure_map_builder.py` | `db8cc907a3585c292d4b2a09336da6241082eb50` | blob | 8013 | `PORT_OR_WRAP` | pico/evolver/** |
| 361 | `pico/evolver/analysis/proxy_features.py` | `9e01de33d56f19fdf8c4ff732d7261e894da3641` | blob | 11716 | `PORT_OR_WRAP` | pico/evolver/** |
| 362 | `pico/evolver/analysis/stability_bucket.py` | `1df2145b9fcfce9b013e7add139e15b918f9bb42` | blob | 6735 | `PORT_OR_WRAP` | pico/evolver/** |
| 363 | `pico/evolver/analysis/trial_pool.py` | `6a72ee454d670ecf6669c138f4ee516ad986e8b3` | blob | 4582 | `PORT_OR_WRAP` | pico/evolver/** |
| 364 | `pico/evolver/applier/__init__.py` | `c2a6f8629d874520ed07f6b25f5cb588eff58ea3` | blob | 1220 | `PORT_OR_WRAP` | pico/evolver/** |
| 365 | `pico/evolver/applier/beacon_guard.py` | `15aa969d700de3c0d34feb45f08076f2deb9ff6f` | blob | 1760 | `PORT_OR_WRAP` | pico/evolver/** |
| 366 | `pico/evolver/applier/path_guard.py` | `fd1cc33e545273d51533cc3d77009d7d90f46523` | blob | 11589 | `PORT_OR_WRAP` | pico/evolver/** |
| 367 | `pico/evolver/candidate_evidence.py` | `c1e094b57bade2ef15ff68f2c05c33a9e7452436` | blob | 20749 | `PORT_OR_WRAP` | pico/evolver/** |
| 368 | `pico/evolver/candidate_manifest.py` | `d2179f414195f25fed84ca9f3e1161797c00c348` | blob | 18547 | `PORT_OR_WRAP` | pico/evolver/** |
| 369 | `pico/evolver/cli.py` | `10a72f598123694ed4f41bb28d108ced51f38f51` | blob | 2977 | `PORT_OR_WRAP` | pico/evolver/** |
| 370 | `pico/evolver/compressor/__init__.py` | `db74ae02d61d23cb36b64d377670f228006cb001` | blob | 625 | `PORT_OR_WRAP` | pico/evolver/** |
| 371 | `pico/evolver/compressor/trajectory.py` | `5d4b197e7793e5dac7ff2cf54d2d1c57c55e4c35` | blob | 19995 | `PORT_OR_WRAP` | pico/evolver/** |
| 372 | `pico/evolver/judge/__init__.py` | `1ac7f577c34c6652aac80c299c1fc181f1d6c4ac` | blob | 2046 | `PORT_OR_WRAP` | pico/evolver/** |
| 373 | `pico/evolver/judge/llm_client.py` | `2766372a085ecc2ebd22e2c38552ab96267aeffe` | blob | 21302 | `PORT_OR_WRAP` | pico/evolver/** |
| 374 | `pico/evolver/judge/parser.py` | `fb596fee8453ba04b3bf67e7ba4e94ac4a0dcedf` | blob | 14256 | `PORT_OR_WRAP` | pico/evolver/** |
| 375 | `pico/evolver/judge/prompts.py` | `c175f86b6cafe8fbbf27041426b43e1c77246070` | blob | 20364 | `PORT_OR_WRAP` | pico/evolver/** |
| 376 | `pico/evolver/judge/schema.py` | `26da62603e56463f2fca466014ceb3e7f20ef89f` | blob | 12476 | `PORT_OR_WRAP` | pico/evolver/** |
| 377 | `pico/evolver/launch/__init__.py` | `7ba433624b6976863a3e1f0a526e3fe71ffee4f7` | blob | 776 | `PORT_OR_WRAP` | pico/evolver/** |
| 378 | `pico/evolver/launch/config.py` | `882c4dede2ff2fec310062c99a0f6000725f5172` | blob | 12181 | `PORT_OR_WRAP` | pico/evolver/** |
| 379 | `pico/evolver/launch/contract.py` | `7f629307dab4cb81c5816fe3114cc6a26162a4c3` | blob | 3851 | `PORT_OR_WRAP` | pico/evolver/** |
| 380 | `pico/evolver/launch/models.py` | `6f3550cdc552a58bf5fea83a4ca61cbb07ddf05a` | blob | 5998 | `PORT_OR_WRAP` | pico/evolver/** |
| 381 | `pico/evolver/launch/registry.py` | `b1b584154b6f259f1b30b6b9fe6563ae31b20af0` | blob | 3061 | `PORT_OR_WRAP` | pico/evolver/** |
| 382 | `pico/evolver/launch/runner.py` | `e329eda7a9df34648e0fff45d34f73c87293687d` | blob | 23510 | `PORT_OR_WRAP` | pico/evolver/** |
| 383 | `pico/evolver/launch/state.py` | `494316b9323060efe27deb9137c389eedfec9556` | blob | 4562 | `PORT_OR_WRAP` | pico/evolver/** |
| 384 | `pico/evolver/orchestrator/__init__.py` | `8e2afa06c9bc86ed38c5f3eb558d7662d4fe55db` | blob | 1429 | `PORT_OR_WRAP` | pico/evolver/** |
| 385 | `pico/evolver/orchestrator/archive.py` | `141ce73e51866c27c9b3d829bb8bced092ba11ed` | blob | 15685 | `PORT_OR_WRAP` | pico/evolver/** |
| 386 | `pico/evolver/orchestrator/config.py` | `abbb04201d9dedaa368cc5e5fd7a0896096febed` | blob | 4658 | `PORT_OR_WRAP` | pico/evolver/** |
| 387 | `pico/evolver/orchestrator/gates/__init__.py` | `f5f40e1026d9eb25d50b4491fe42f3a0fe7880e7` | blob | 1105 | `PORT_OR_WRAP` | pico/evolver/** |
| 388 | `pico/evolver/orchestrator/gates/fisher.py` | `6abc61d9a7676e13388da5d0ab4e81c1ce980d8b` | blob | 3373 | `PORT_OR_WRAP` | pico/evolver/** |
| 389 | `pico/evolver/orchestrator/gates/paired.py` | `ce5cd3f634de8f570dbd384851196b2d3ba2198d` | blob | 5114 | `PORT_OR_WRAP` | pico/evolver/** |
| 390 | `pico/evolver/orchestrator/gates/pipeline.py` | `ef48a2109924b9983d85e7b1f31c83ccb1069b5a` | blob | 5768 | `PORT_OR_WRAP` | pico/evolver/** |
| 391 | `pico/evolver/orchestrator/gates/policy.py` | `47d28df42d11207ef0015b400b2fb977bfe79306` | blob | 10190 | `PORT_OR_WRAP` | pico/evolver/** |
| 392 | `pico/evolver/orchestrator/gates/strategies.py` | `900f9a6200801206b5408b1ea5b2b663efa90ea6` | blob | 14588 | `PORT_OR_WRAP` | pico/evolver/** |
| 393 | `pico/evolver/orchestrator/loop.py` | `b887ce82895d5bc94cd9192a8827901a10b2e7fe` | blob | 35797 | `PORT_OR_WRAP` | pico/evolver/** |
| 394 | `pico/evolver/orchestrator/nodes/__init__.py` | `51b793864eb962d45709aedc123a8e1afc33fe92` | blob | 123 | `PORT_OR_WRAP` | pico/evolver/** |
| 395 | `pico/evolver/orchestrator/nodes/design.py` | `c56bcc2a89cb6cea4fd5df2ab8130b4b51d694e2` | blob | 8040 | `PORT_OR_WRAP` | pico/evolver/** |
| 396 | `pico/evolver/orchestrator/nodes/diagnose.py` | `713216a87657eaced111904c19d00b6e70eb8a0c` | blob | 5702 | `PORT_OR_WRAP` | pico/evolver/** |
| 397 | `pico/evolver/orchestrator/nodes/screen.py` | `870bce4b8e055fdc54e4b81de97039fa87258a13` | blob | 2983 | `PORT_OR_WRAP` | pico/evolver/** |
| 398 | `pico/evolver/orchestrator/nodes/semantic.py` | `a15818dd84c562614a73c09134cf2bd4307c3d99` | blob | 3924 | `PORT_OR_WRAP` | pico/evolver/** |
| 399 | `pico/evolver/orchestrator/nodes/taxonomy.py` | `57c21e882e32465da9c2c4a00f76737b0ad4d779` | blob | 20656 | `PORT_OR_WRAP` | pico/evolver/** |
| 400 | `pico/evolver/orchestrator/nodes/verdict.py` | `7d7ae82e052f0b1a2a9393568a93d39652479010` | blob | 4202 | `PORT_OR_WRAP` | pico/evolver/** |
| 401 | `pico/evolver/orchestrator/production.py` | `05c5ff9e1100800a36f2fef9cff95d015bf8eee3` | blob | 31235 | `PORT_OR_WRAP` | pico/evolver/** |
| 402 | `pico/evolver/orchestrator/providers/__init__.py` | `8880405ed66ecb3f50a0b3501b93d2e0005b9490` | blob | 298 | `PORT_OR_WRAP` | pico/evolver/** |
| 403 | `pico/evolver/orchestrator/providers/claude_agentic.py` | `316feb37415ea3f905bdf294410974555a85a3bc` | blob | 5374 | `PORT_OR_WRAP` | pico/evolver/** |
| 404 | `pico/evolver/orchestrator/providers/claude_cli.py` | `86e9774aacf1fdbfa5269272779fd6670896dea1` | blob | 6081 | `PORT_OR_WRAP` | pico/evolver/** |
| 405 | `pico/evolver/orchestrator/providers/openai_compat.py` | `a6ae7100ce8113d9a19b574f080e05d0749369e4` | blob | 3971 | `PORT_OR_WRAP` | pico/evolver/** |
| 406 | `pico/evolver/orchestrator/scoring.py` | `fb2e98845f3a077a679298c727a163835aaa9630` | blob | 14336 | `PORT_OR_WRAP` | pico/evolver/** |
| 407 | `pico/evolver/orchestrator/sealed/__init__.py` | `986ebd73ea5e8543b9c6e1af65552c7b644727be` | blob | 117 | `PORT_OR_WRAP` | pico/evolver/** |
| 408 | `pico/evolver/orchestrator/sealed/runner.py` | `ee1b7de35b5e10ff67b3b20406fda3e216e3c803` | blob | 12609 | `PORT_OR_WRAP` | pico/evolver/** |
| 409 | `pico/evolver/orchestrator/state/__init__.py` | `02ae21578ec68efc95aafd9aea4221d3041f06b1` | blob | 99 | `PORT_OR_WRAP` | pico/evolver/** |
| 410 | `pico/evolver/orchestrator/state/journal.py` | `2a1047fda499f71af57f23a3c5e32db0482e1fd7` | blob | 3364 | `PORT_OR_WRAP` | pico/evolver/** |
| 411 | `pico/evolver/orchestrator/termination.py` | `2fb7b3e368422371bd3a90913b36f58145431776` | blob | 3413 | `PORT_OR_WRAP` | pico/evolver/** |
| 412 | `pico/evolver/scheduler/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_OR_WRAP` | pico/evolver/** |
| 413 | `pico/evolver/scheduler/anchor_selection.py` | `81b56a08579286c6d59dbda9d1bd80c1d281cc5c` | blob | 8549 | `PORT_OR_WRAP` | pico/evolver/** |
| 414 | `pico/evolver/scheduler/bandit_tasks.py` | `24218b8e900adc35cf868503cacf1fe32894e2dd` | blob | 10261 | `PORT_OR_WRAP` | pico/evolver/** |
| 415 | `pico/evolver/scheduler/branching_policy.py` | `df411eb3c1b9235ca670de56742b04d1d370498b` | blob | 8092 | `PORT_OR_WRAP` | pico/evolver/** |
| 416 | `pico/evolver/scheduler/cold_start_bandit.py` | `ed1868a9367376cee173afc9c41892c03866547d` | blob | 13928 | `PORT_OR_WRAP` | pico/evolver/** |
| 417 | `pico/evolver/scheduler/tree_aware_bandit.py` | `10bc68e6e09518f36e876a7032c6b4fd765c6c27` | blob | 14948 | `PORT_OR_WRAP` | pico/evolver/** |
| 418 | `pico/evolver/scheduler/tree_loader.py` | `82c9ed6bdddc3344e40643896214e4eda1c186a4` | blob | 12564 | `PORT_OR_WRAP` | pico/evolver/** |
| 419 | `pico/evolver/tree/__init__.py` | `407f614c709d3e2237b568fcb3025e1a5c4b1976` | blob | 784 | `PORT_OR_WRAP` | pico/evolver/** |
| 420 | `pico/evolver/tree/git_ops.py` | `8d5d30315a01b39eec404f7a89476a3169c1c70e` | blob | 20347 | `PORT_OR_WRAP` | pico/evolver/** |
| 421 | `pico/evolver/tree/node.py` | `af0b9e86ccf5263037b53fb739a5ab51e6665da9` | blob | 28822 | `PORT_OR_WRAP` | pico/evolver/** |
| 422 | `pico/evolver/tree/store.py` | `41a7659dc6ae5d1a5bef1d938e8d04c9263be330` | blob | 13571 | `PORT_OR_WRAP` | pico/evolver/** |
| 423 | `pico/memory_engine/__init__.py` | `334bc6bbc1693d3ae10de04ca111fc768c1602f7` | blob | 1878 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 424 | `pico/memory_engine/backend.py` | `a0fca67a7df37335dc237b1ad56957c275d4d200` | blob | 7019 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 425 | `pico/memory_engine/base.py` | `1135ab1ad0dd04bd2c4dc963939766a55752f036` | blob | 3083 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 426 | `pico/memory_engine/consolidate/__init__.py` | `5e9b1c25cd3777a4922bae2c5d7ead6e47da4ba3` | blob | 564 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 427 | `pico/memory_engine/consolidate/consolidator.py` | `4145f512fdf3d43794b7a354b0446457b0ce34b2` | blob | 78714 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 428 | `pico/memory_engine/contract_test.py` | `7860670404fb8c14b7caf2549ca83d841070462b` | blob | 6583 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 429 | `pico/memory_engine/skill_forge/__init__.py` | `3ab7e35bd11665717800654376711e81d0203553` | blob | 1703 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 430 | `pico/memory_engine/skill_forge/catalog.py` | `1a3be50fbbbc2c6e37f6138065e7404b45081815` | blob | 16916 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 431 | `pico/memory_engine/skill_forge/fusion.py` | `efe78fe22de7121f755ff6c5fe8cca1a54067cbe` | blob | 2400 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 432 | `pico/memory_engine/skill_forge/gate.py` | `1c4e1c7127f5aa6a48c72bf7e41abd29914f9444` | blob | 11303 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 433 | `pico/memory_engine/skill_forge/local_source.py` | `d39cd3b5b208f7e24d19e0d7aeaab3c8c88756d4` | blob | 4285 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 434 | `pico/memory_engine/skill_forge/refs.py` | `741bcd06a040fbd1bea24dce4cb9f7960a1a0652` | blob | 3741 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 435 | `pico/memory_engine/skill_forge/resolver.py` | `e89e693b57e66ed444e93065d5011be239cd27e3` | blob | 4980 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 436 | `pico/memory_engine/skill_forge/rewriter.py` | `1786256bcc7364784ee48def6d8e992140c9edc9` | blob | 5573 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 437 | `pico/memory_engine/skill_forge/router.py` | `0d54639bed61bf1ea621173c34e1f833c1ddfb5c` | blob | 4124 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 438 | `pico/memory_engine/skill_forge/types.py` | `dbe3a31a1fdba946f60a43c79280d1b79f2da775` | blob | 4476 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 439 | `pico/memory_engine/skill_local/__init__.py` | `b3f7caaf0930bc74a2eecc42585e697bfd5dc107` | blob | 1233 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 440 | `pico/memory_engine/skill_local/local_pool.py` | `6f97b3b578c009b07eac7d8f687170095347dea0` | blob | 6003 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 441 | `pico/memory_engine/skill_local/registry.py` | `848c2984bbc722e8c4f9ad0e3bdd0665d577bf27` | blob | 23992 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 442 | `pico/memory_engine/skill_local/types.py` | `b8abc852db700588afed4b330125a1ca565ddb56` | blob | 2893 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 443 | `pico/memory_engine/skill_local/watcher.py` | `378a6718906e6442179c9c63d9f39e663df2f206` | blob | 6336 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 444 | `pico/memory_engine/skills/weather/SKILL.md` | `9effd50a653368c8bb56308504ad4a92a7e68a71` | blob | 1165 | `PORT_OR_WRAP` | codecub/memory_v2/** + pico/memory_engine/** |
| 445 | `pico/plugin/__init__.py` | `63bb088e1a33a5cb91b643bb2a8de3fef48762b7` | blob | 2059 | `PORT_OR_WRAP` | codecub/extensions.py + pico/plugin/** |
| 446 | `pico/plugin/bootstrap.py` | `a574773a2e59c3cedd0d5529ed1fc6c55e999f7a` | blob | 1816 | `PORT_OR_WRAP` | codecub/extensions.py + pico/plugin/** |
| 447 | `pico/plugin/context.py` | `5c6a0e1d9c4844078571f8b24b3aec1842d8d804` | blob | 2369 | `PORT_OR_WRAP` | codecub/extensions.py + pico/plugin/** |
| 448 | `pico/plugin/discover.py` | `e7288caaa7e5b0d56b0a974f638802196986a743` | blob | 13817 | `PORT_OR_WRAP` | codecub/extensions.py + pico/plugin/** |
| 449 | `pico/plugin/manifest.py` | `2847087b1675c02a44411af8b437edf586b4706e` | blob | 6552 | `PORT_OR_WRAP` | codecub/extensions.py + pico/plugin/** |
| 450 | `pico/plugin/memory/__init__.py` | `f7f2e6439e2c09ddc67eeb2fe93acc8728987641` | blob | 560 | `PORT_OR_WRAP` | codecub/extensions.py + pico/plugin/** |
| 451 | `pico/plugin/registry.py` | `2051dd190896db5e56423eaf2262800237ceeac1` | blob | 15001 | `PORT_OR_WRAP` | codecub/extensions.py + pico/plugin/** |
| 452 | `pico/proactive_engine/__init__.py` | `92495dedcb87de03185437f6958e563fa66c4cde` | blob | 441 | `PORT_OR_WRAP` | codecub/automation.py + pico/proactive_engine/** |
| 453 | `pico/proactive_engine/schedulers/__init__.py` | `da1aa42f645febe09c1e2f176f1515dc4fcfd0dd` | blob | 260 | `PORT_OR_WRAP` | codecub/automation.py + pico/proactive_engine/** |
| 454 | `pico/proactive_engine/schedulers/cron/__init__.py` | `2b57da9210be50b925cdaa612c7ff5b529c6ca8a` | blob | 509 | `PORT_OR_WRAP` | codecub/automation.py + pico/proactive_engine/** |
| 455 | `pico/proactive_engine/schedulers/cron/service.py` | `26fa6f197df1747df62876da89e239a688466e7a` | blob | 48826 | `PORT_OR_WRAP` | codecub/automation.py + pico/proactive_engine/** |
| 456 | `pico/proactive_engine/schedulers/cron/tool.py` | `ab6578243c6ea1899c599f9a5a3ebc1de3a1c32e` | blob | 18360 | `PORT_OR_WRAP` | codecub/automation.py + pico/proactive_engine/** |
| 457 | `pico/proactive_engine/schedulers/cron/types.py` | `20498d80b3acefa93d8b7e9eb267aaafa1c649d8` | blob | 4534 | `PORT_OR_WRAP` | codecub/automation.py + pico/proactive_engine/** |
| 458 | `pico/product.py` | `3f5ef919c7fed3adadc6c11b4565b5b57a6ac784` | blob | 1638 | `PORT` | pico/** + mapped CodeCub integration |
| 459 | `pico/providers/__init__.py` | `08bf83c452061200bc0aba1324c59d8586fcdf2d` | blob | 1584 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 460 | `pico/providers/azure_openai_provider.py` | `49ca6e2cace44d8dda407eb911540dc3c414ce89` | blob | 10357 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 461 | `pico/providers/base.py` | `1146e5cbf15e9db08410f4bed8237403c87fbd6a` | blob | 28370 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 462 | `pico/providers/common_models.py` | `acfe250cb7b2dab66ec75e00edf3ffb8199f8a9a` | blob | 3483 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 463 | `pico/providers/custom_provider.py` | `3a326ac569a178b605c5d178710b554e610253fd` | blob | 3310 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 464 | `pico/providers/lazy.py` | `9d81dd5b95a9895556f8005f5adb162155bbf87e` | blob | 3036 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 465 | `pico/providers/litellm_provider.py` | `5604ac7d9e62cb0aa17df9a5ee71e36b107d8c16` | blob | 32184 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 466 | `pico/providers/litellm_setup.py` | `10feb6d13a10d92d4331d937568921008b76599c` | blob | 1522 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 467 | `pico/providers/openai_codex_provider.py` | `0a80e9f81347c5c9c0ee66f373b8a6100c959e3d` | blob | 13251 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 468 | `pico/providers/per_model_provider.py` | `0ac4b5431fb555e4bfbcdc00c5b5948ab63a6b45` | blob | 4180 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 469 | `pico/providers/registry.py` | `3d3bb769f25d64be202c955f71de245f3a1653dc` | blob | 19089 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 470 | `pico/providers/transcription.py` | `413acc10364db928918c8fad598955bfdb752a99` | blob | 2556 | `PORT_OR_WRAP` | codecub/models.py + codecub/provider_*.py + pico/providers/** |
| 471 | `pico/routing/__init__.py` | `94c1be7a2a9619dc8936a270a36a39d1b41d827e` | blob | 538 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 472 | `pico/routing/cache.py` | `6da0cfdeaab208b5e86330a559afb749848bae56` | blob | 8380 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 473 | `pico/routing/classifier.py` | `1a7cc4475b895d118ce537598216a803d1bfa253` | blob | 8220 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 474 | `pico/routing/embedding_data.json` | `8fc51b5186ea9586dffeed3dbc671738e98ff1bc` | blob | 481143 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 475 | `pico/routing/fetcher.py` | `0c27009a2af37178d010d074e522bdb8c0b31d4a` | blob | 5465 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 476 | `pico/routing/generate_embeddings.py` | `52377632d73d8c3c4d9f6b1883a6d98e53776ed0` | blob | 4792 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 477 | `pico/routing/knn_memory_example.json` | `9ad9a07447e57fa8c71e0275d7e50383a96c4f70` | blob | 99105 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 478 | `pico/routing/knn_router.py` | `1d6ee89dd10806cf22015e3cfb48b2a33fa43960` | blob | 12156 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 479 | `pico/routing/profiles.py` | `1fe43990c954e0c7210556a5e2c26679ff049331` | blob | 797 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 480 | `pico/routing/router.py` | `15cf36a00895fd431bbcccd7aacc031a6fe0886c` | blob | 6020 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 481 | `pico/routing/selector.py` | `9a1a769c5a9c5ca288e90010e2351170d2a60653` | blob | 6200 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 482 | `pico/routing/snapshot.json` | `384993edca63aa8136b47e206b18afba0099ba41` | blob | 87799 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 483 | `pico/routing/types.py` | `229f8fde19971f3ef679f542274d679e583c3edc` | blob | 2898 | `PORT_OR_WRAP` | codecub/retrieval.py + codecub/vector_index.py + pico/routing/** |
| 484 | `pico/sandbox/__init__.py` | `b5fcebaf229a9b78ae4ff04984cd97ab3c8acab2` | blob | 4006 | `PORT_OR_WRAP` | codecub/sandbox.py + codecub/security.py + pico/sandbox/** |
| 485 | `pico/sandbox/_async_utils.py` | `abb58e884b80b7222d2218571b08afec4800cbba` | blob | 1769 | `PORT_OR_WRAP` | codecub/sandbox.py + codecub/security.py + pico/sandbox/** |
| 486 | `pico/sandbox/_runtime.py` | `7166e99ce0198866f94999d54c15521522951617` | blob | 1473 | `PORT_OR_WRAP` | codecub/sandbox.py + codecub/security.py + pico/sandbox/** |
| 487 | `pico/sandbox/boxlite_executor.py` | `29d6f3a5c23d968789e8233baf85f14350efdeab` | blob | 23435 | `PORT_OR_WRAP` | codecub/sandbox.py + codecub/security.py + pico/sandbox/** |
| 488 | `pico/sandbox/config.py` | `30acd72b4b6a4c5d059c91cba028dff318358c63` | blob | 4339 | `PORT_OR_WRAP` | codecub/sandbox.py + codecub/security.py + pico/sandbox/** |
| 489 | `pico/sandbox/debug_server.py` | `a7f5dee29f2f9d4e4ad2024b77cf3a03bffffde5` | blob | 24776 | `PORT_OR_WRAP` | codecub/sandbox.py + codecub/security.py + pico/sandbox/** |
| 490 | `pico/sandbox/direct_executor.py` | `003d35023a4032304323c7c75b3cfbca83ad571d` | blob | 4369 | `PORT_OR_WRAP` | codecub/sandbox.py + codecub/security.py + pico/sandbox/** |
| 491 | `pico/sandbox/interfaces.py` | `f1eedae402338d43ea29a5ec17c5e255f67319c7` | blob | 5719 | `PORT_OR_WRAP` | codecub/sandbox.py + codecub/security.py + pico/sandbox/** |
| 492 | `pico/security/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_OR_WRAP` | codecub/security.py + pico/security/** |
| 493 | `pico/security/network.py` | `13d7dca49ff46e27585617908f26bcf60b014d15` | blob | 3368 | `PORT_OR_WRAP` | codecub/security.py + pico/security/** |
| 494 | `pico/security/trust.py` | `17fe35e016e9fb4391018bbbd122dc4bd13a30c7` | blob | 2555 | `PORT_OR_WRAP` | codecub/security.py + pico/security/** |
| 495 | `pico/session/__init__.py` | `5e6fec55f9594994b150628df0afa4ea202da7cc` | blob | 372 | `PORT_OR_WRAP` | codecub/sessions/** + codecub/store_ports.py + pico/session/** |
| 496 | `pico/session/export.py` | `d625be5f60030a4436c49df5f3f8886f9644c291` | blob | 9235 | `PORT_OR_WRAP` | codecub/sessions/** + codecub/store_ports.py + pico/session/** |
| 497 | `pico/session/manager.py` | `f731bb2223292f13a5379633c64345cc8979df7e` | blob | 39722 | `PORT_OR_WRAP` | codecub/sessions/** + codecub/store_ports.py + pico/session/** |
| 498 | `pico/spine/__init__.py` | `00e2184794755fba4a18c4b33e10074e6d4b5c3b` | blob | 1686 | `PORT_OR_WRAP` | codecub/spine/** + pico/spine/** |
| 499 | `pico/spine/_barrier.py` | `e84ce25098d1a652c338a0b863be49441d3d9f0a` | blob | 2054 | `PORT_OR_WRAP` | codecub/spine/** + pico/spine/** |
| 500 | `pico/spine/delivery.py` | `c5b1927907a7cdb79cc64970db5529c25d1cda07` | blob | 22537 | `PORT_OR_WRAP` | codecub/spine/** + pico/spine/** |
| 501 | `pico/spine/events.py` | `6e76b52760b60184262b860762639036fea4093b` | blob | 4474 | `PORT_OR_WRAP` | codecub/spine/** + pico/spine/** |
| 502 | `pico/spine/message.py` | `ed0bb032b9c4df73be4cc19acf7dd556ba2fc31b` | blob | 2243 | `PORT_OR_WRAP` | codecub/spine/** + pico/spine/** |
| 503 | `pico/spine/runner.py` | `7105f8e956180e77dbb02e7daf3cfb4e880c098f` | blob | 2502 | `PORT_OR_WRAP` | codecub/spine/** + pico/spine/** |
| 504 | `pico/spine/scheduler.py` | `64fea8f36821e6d90fb5a3e6aad392ddaab6b3a3` | blob | 28461 | `PORT_OR_WRAP` | codecub/spine/** + pico/spine/** |
| 505 | `pico/spine/teardown.py` | `e169f5ab87f75eba77707e3436969a54078878ae` | blob | 2313 | `PORT_OR_WRAP` | codecub/spine/** + pico/spine/** |
| 506 | `pico/spine/turn.py` | `490e3d57b5064f5f6bb2fdd3382e295ab7014c9a` | blob | 2798 | `PORT_OR_WRAP` | codecub/spine/** + pico/spine/** |
| 507 | `pico/templates/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_OR_WRAP` | pico/templates/** |
| 508 | `pico/templates/AGENTS.md` | `5aa00f652c3688f06dd09e72c359e05d1743ae3c` | blob | 512 | `PORT_OR_WRAP` | pico/templates/** |
| 509 | `pico/templates/memory/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_OR_WRAP` | pico/templates/** |
| 510 | `pico/templates/memory/MEMORY.md` | `02488e551d21d21ec9dd984fd25c6458ff4f854d` | blob | 405 | `PORT_OR_WRAP` | pico/templates/** |
| 511 | `pico/templates/SOUL.md` | `07f20f84eee7d16582c6afe6e64b8fee563d969f` | blob | 352 | `PORT_OR_WRAP` | pico/templates/** |
| 512 | `pico/templates/TOOLS.md` | `51c3a2d0d2a65a6ef3500af96cb027021b26c8ae` | blob | 487 | `PORT_OR_WRAP` | pico/templates/** |
| 513 | `pico/templates/USER.md` | `a1f602ecd7c20c634d98f17d8a5f0df08b307b80` | blob | 836 | `PORT_OR_WRAP` | pico/templates/** |
| 514 | `pico/token_wise/__init__.py` | `b810813a7c53956381624369c61b2ab3a2c9c069` | blob | 1019 | `PORT_OR_WRAP` | codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/** |
| 515 | `pico/token_wise/base.py` | `eaac93490b494603f3042d248ee708c9536332ec` | blob | 4315 | `PORT_OR_WRAP` | codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/** |
| 516 | `pico/token_wise/cache_optimizer.py` | `26bff2e4f7e22e6cc5dbb6d42f9658e3b4788269` | blob | 5968 | `PORT_OR_WRAP` | codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/** |
| 517 | `pico/token_wise/EXPERIMENT_REPORT_CACHE_STRATEGIES.md` | `491421aab5aea79ecae12ec0cd859d12e3b7ec44` | blob | 28040 | `PORT_OR_WRAP` | codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/** |
| 518 | `pico/token_wise/EXPERIMENT_REPORT_WORKLOADS.md` | `f2366dfe55dcc5cc8a357dff04190825f6363e94` | blob | 18770 | `PORT_OR_WRAP` | codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/** |
| 519 | `pico/token_wise/EXPERIMENT_REPORT.md` | `5933ebeb20e9573a0f659b753d43fcff41d10cbb` | blob | 8101 | `PORT_OR_WRAP` | codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/** |
| 520 | `pico/token_wise/model_catalog_cache.py` | `d6970b4401145d37e6a0aa65d9b1d787ff136fd4` | blob | 562 | `PORT_OR_WRAP` | codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/** |
| 521 | `pico/token_wise/pricing.py` | `f0190ec1ec24a259fb798b677240e0f25d272ea8` | blob | 552 | `PORT_OR_WRAP` | codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/** |
| 522 | `pico/token_wise/registry.py` | `1f3052508665d18e93f2cee04253863f906a76b5` | blob | 4607 | `PORT_OR_WRAP` | codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/** |
| 523 | `pico/token_wise/system_and_tail_cache.py` | `4b565dcbfc571192dc0e94ddafa4fa3402406c86` | blob | 4256 | `PORT_OR_WRAP` | codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/** |
| 524 | `pico/token_wise/usage_tracker.py` | `9b08d4f910201770b88150e56217aa8a8459e9f7` | blob | 7552 | `PORT_OR_WRAP` | codecub/token_budget.py + codecub/cache.py + codecub/telemetry/** + pico/token_wise/** |
| 525 | `pico/tracing/__init__.py` | `609d65c1d1217297a1c626d8b5ec0a70b29996d7` | blob | 901 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 526 | `pico/tracing/config.py` | `37deec9bc84127a88d40765ec3abca166744e836` | blob | 3534 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 527 | `pico/tracing/context.py` | `5e18b7d986e5918f16af49b56e4785fd3a2a5b04` | blob | 4389 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 528 | `pico/tracing/semconv.py` | `7f0564075ddf5e7e63d1a7260f51528458d2e855` | blob | 33656 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 529 | `pico/tracing/spans.py` | `b23546f165fbf4c292668f185063146ebf903219` | blob | 3158 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 530 | `pico/tracing/store.py` | `bb6e06ea5c1a087cef464d48e707890487644a29` | blob | 6725 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 531 | `pico/tracing/trace.py` | `5beb33c8185cd1d5cb608ee1577a39facc56de08` | blob | 17553 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 532 | `pico/tracing/usage.py` | `26773a66a8a5e969128eb62d7cc85662a37cd987` | blob | 1890 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 533 | `pico/tracing/viewer/descriptors/pico.json` | `f841fcacb7cb45c07360934becc6c8ad7790e815` | blob | 1344 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 534 | `pico/tracing/viewer/log-store.js` | `882ccea70205c8bcb7b09a5c73636221a6abee32` | blob | 6615 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 535 | `pico/tracing/viewer/server.js` | `4e315eb4fd33eb4af16b50867a67d34761050d08` | blob | 37726 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 536 | `pico/tracing/viewer/state-dir.js` | `c2d118837b933c8fe1d57fca0b470ce3bc1fc437` | blob | 1727 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 537 | `pico/tracing/viewer/ui/app.css` | `5317800766bf5e40ce83c646d4ed0cc608a3dd7d` | blob | 50176 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 538 | `pico/tracing/viewer/ui/app.js` | `3a2bb5fc46c51689254514692b0e2583188acfde` | blob | 116819 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 539 | `pico/tracing/viewer/ui/shell.js` | `a06042370e34081ca3435bac60f9299036c1b1d1` | blob | 7057 | `PORT_OR_WRAP` | codecub/tracing/** + codecub/otel_exporter.py + pico/tracing/** |
| 540 | `pico/tui_rpc/__init__.py` | `c9d16a453a8e045b22265743bd4a798a94b4432f` | blob | 889 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 541 | `pico/tui_rpc/confirm_broker.py` | `1bab5f51825e099739822d8f86efd95963fbfc52` | blob | 5308 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 542 | `pico/tui_rpc/dispatcher.py` | `bdb9916735e267fea417993e7a88c4de5511496d` | blob | 8654 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 543 | `pico/tui_rpc/errors.py` | `e7f8a926656ccffe8b15cd6cd43fdd2d319b5f06` | blob | 6005 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 544 | `pico/tui_rpc/methods/__init__.py` | `ec782c317d07c8fb1ee509a09b55632001721bce` | blob | 5932 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 545 | `pico/tui_rpc/methods/config.py` | `60bca14021e3331df5bed133fe6f6047f4a8961c` | blob | 14949 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 546 | `pico/tui_rpc/methods/confirm.py` | `5b276fa559e1ce464d884c347fc600a371134af9` | blob | 2257 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 547 | `pico/tui_rpc/methods/image.py` | `21dec46f10d0b590d41632318b7dca802fca3e4e` | blob | 7671 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 548 | `pico/tui_rpc/methods/model.py` | `ce86823deaa5028b61afe82174185401347f07ac` | blob | 10497 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 549 | `pico/tui_rpc/methods/question.py` | `b58da24c3cb29d062c9b8bdfc2ec7cb99a2b4d9e` | blob | 2222 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 550 | `pico/tui_rpc/methods/session.py` | `c2443e98e7cdd35875ce03eea32d633cffece521` | blob | 33463 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 551 | `pico/tui_rpc/methods/setup.py` | `23e3116920f34e697dc598cd4cbdca777bc06be8` | blob | 4599 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 552 | `pico/tui_rpc/methods/system.py` | `5a8e94fda629cb065da4ffb37156a4398dcfc591` | blob | 5490 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 553 | `pico/tui_rpc/methods/terminal.py` | `0cfc105b97fb72b49b93cbebdce52059644c86d6` | blob | 3316 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 554 | `pico/tui_rpc/methods/turn.py` | `2fb961860bbdbd684c7eecb55c1f12a0393a3f70` | blob | 17757 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 555 | `pico/tui_rpc/models.py` | `38372c4252b4104df210c77e1c509300cefa3b6f` | blob | 20328 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 556 | `pico/tui_rpc/question_broker.py` | `a5a0b70ce837ef448d077083fb0fa00d1be29c21` | blob | 7005 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 557 | `pico/tui_rpc/server.py` | `11ae188a69d4a3205436b051a9d4c21879afd3c9` | blob | 14181 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 558 | `pico/tui_rpc/spine.py` | `806bec03e1a2a90fad4022e6ed09b77a360e3005` | blob | 20720 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 559 | `pico/tui_rpc/subscriptions.py` | `1be2a90cc647f07b3c6c0d9b4b63eff749a7590c` | blob | 9481 | `PORT_OR_WRAP` | codecub/gateway.py + codecub/gateway_runtime.py + codecub/app_protocol.py + pico/tui_rpc/** |
| 560 | `pico/utils/__init__.py` | `e74eb89236259a310723b62bfb01c3e3939afb9f` | blob | 457 | `PORT_OR_WRAP` | codecub/workspace.py + codecub/security.py + pico/utils/** |
| 561 | `pico/utils/atomic_io.py` | `0477dc3b4ec58c2a6e777533813b707fe2fe8194` | blob | 12424 | `PORT_OR_WRAP` | codecub/workspace.py + codecub/security.py + pico/utils/** |
| 562 | `pico/utils/bm25.py` | `3222c5482615d2dcd8c2bfdd69d94e87c4bc1795` | blob | 3322 | `PORT_OR_WRAP` | codecub/workspace.py + codecub/security.py + pico/utils/** |
| 563 | `pico/utils/helpers.py` | `fca77b44eb6800a0b2810c11ccff6fd3a578dfae` | blob | 12441 | `PORT_OR_WRAP` | codecub/workspace.py + codecub/security.py + pico/utils/** |
| 564 | `pico/utils/persisted_payload.py` | `0d5356c77b5aa9579c07ed91e6c91dcd20011a45` | blob | 2140 | `PORT_OR_WRAP` | codecub/workspace.py + codecub/security.py + pico/utils/** |
| 565 | `pico/utils/portable_lock.py` | `2daefe682949fadf06e7da7cab5219dc76af701c` | blob | 2292 | `PORT_OR_WRAP` | codecub/workspace.py + codecub/security.py + pico/utils/** |
| 566 | `prettier.config.mjs` | `77ddfc6b6b17bb077b2e73f394d9c187d19136eb` | blob | 138 | `REVIEW_SUPPORT` | repository support only |
| 567 | `pyproject.toml` | `886c1885adf43b823a8156e88dccf7c5bc70fb96` | blob | 7744 | `MERGE_BUILD` | pyproject.toml |
| 568 | `README.md` | `0dcdd72380e0be9e1e698dd653988cbcab0d05b5` | blob | 7918 | `MERGE_DOC_OR_REVIEW` | README.md |
| 569 | `README.zh-CN.md` | `07b239cd2c725431e81221380e5e923f17effde5` | blob | 7536 | `MERGE_DOC_OR_REVIEW` | README.zh-CN.md |
| 570 | `scripts/boxlite_cli.py` | `0c0fe0305df89d424d4666da01d4aa4c86fdaf78` | blob | 24548 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 571 | `scripts/check_commit_file.py` | `f1d4013dbfa2b33a474a356796ac1384470177d4` | blob | 955 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 572 | `scripts/check_commit_messages.py` | `c1d81aee8c23ef4962505fa9c6d0720736249f46` | blob | 1625 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 573 | `scripts/check_large_files.py` | `12f9a839b0ff2ff0a5ce50bcf09f8cee760031f1` | blob | 5014 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 574 | `scripts/check_pr_body.py` | `0bd08415d493795e6280fc42a2b0bdf277c592ce` | blob | 570 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 575 | `scripts/check_pr_title.py` | `c7c81879932567ccd9949663e4fbe459dad0bcec` | blob | 544 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 576 | `scripts/check_public_tree.py` | `b5ce2a7d7efe7e7b6ba6e597f979f8f0175a32c2` | blob | 5711 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 577 | `scripts/commit_lint.py` | `8dad2d62d48efc25b901d8e3d16d075a8ccb0b31` | blob | 2663 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 578 | `scripts/setup_small_real_subject.py` | `04c5884bcd8013731baed88cd782340fa35359ec` | blob | 6676 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 579 | `scripts/skill_forge_full_e2e.py` | `cd47c9525590eeabfcb0bfa3d5d325d1b55eefe1` | blob | 8753 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 580 | `scripts/skill_forge_retrieval_eval.py` | `3737640eb0ff3082eb090bf9b97ad9d2eeddbc01` | blob | 7459 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 581 | `scripts/verify_channels.py` | `d08271209a1cde192edf4a2e49ddba34e627cde9` | blob | 7155 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 582 | `scripts/verify_distribution.py` | `afb90d11a2d9357ae83c95338451ecb2cd44bc85` | blob | 58455 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 583 | `scripts/verify_turn_evidence.py` | `9e4734310afd6cf25309c2f18150029d879e52db` | blob | 27586 | `PORT_VERIFY_OR_REVIEW` | scripts/** |
| 584 | `SECURITY.md` | `927d4605d2a0ec8990d69d8384cb117f2c9b0bd9` | blob | 530 | `MERGE_DOC_OR_REVIEW` | SECURITY.md |
| 585 | `tests/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_TEST` | tests/** |
| 586 | `tests/conftest.py` | `d29fe7e2904302b490047701c70b52f71a624a4e` | blob | 3829 | `PORT_TEST` | tests/** |
| 587 | `tests/fixtures/exception-ledger.toml` | `c841eeac9b72ffa4beb38b53edc4751ea5d1ea1c` | blob | 167 | `PORT_TEST` | tests/** |
| 588 | `tests/integration/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_TEST` | tests/** |
| 589 | `tests/integration/_evolver_process_bench.py` | `0ae11628f7962e08879723c2118b227d33d98c93` | blob | 3029 | `PORT_TEST` | tests/** |
| 590 | `tests/integration/_session_continuity_probe.py` | `8f8b17676d9798d0a8b11d090ff7bc33b338f9ef` | blob | 4097 | `PORT_TEST` | tests/** |
| 591 | `tests/integration/test_evolver_lifecycle_e2e.py` | `fee2b385e81bdb928f6aa7956da8f296a4d4c78f` | blob | 6134 | `PORT_TEST` | tests/** |
| 592 | `tests/integration/test_fallback_chain_smoke.py` | `edcc253264b54eab2ce0c4196081261cde5fffae` | blob | 4957 | `PORT_TEST` | tests/** |
| 593 | `tests/integration/test_picobench_context_e2e.py` | `35a81824ada5cccc104ea9d0c6e6329a618d3cb4` | blob | 15635 | `PORT_TEST` | tests/** |
| 594 | `tests/integration/test_picobench_mcp_e2e.py` | `9ea67630eb062c51368724e97fb88d6857a04964` | blob | 10044 | `PORT_TEST` | tests/** |
| 595 | `tests/integration/test_picobench_memory_skill_e2e.py` | `8a725b964fdf44b3fb6b71c62a2ce680f7969b9d` | blob | 3639 | `PORT_TEST` | tests/** |
| 596 | `tests/integration/test_picobench_memory_skill_semantic_e2e.py` | `5d434afccd3ba7d5f221d2a7e71fdd6794fc8f84` | blob | 1406 | `PORT_TEST` | tests/** |
| 597 | `tests/integration/test_picobench_runtime_smoke.py` | `d5079c5cacdd18d3babfad7c910803bea0a19ba1` | blob | 2314 | `PORT_TEST` | tests/** |
| 598 | `tests/integration/test_picobench_runtime_track_e2e.py` | `807509bd011105aee1ecd9fca852a77e3627e59d` | blob | 1081 | `PORT_TEST` | tests/** |
| 599 | `tests/integration/test_session_continuity_e2e.py` | `8343a94045c53d820880197c07eaf6b5ef9aa733` | blob | 2240 | `PORT_TEST` | tests/** |
| 600 | `tests/integration/test_tui_cancel_inflight_e2e.py` | `c8921471645456e0e7370c11eaaf9c0e917cb7c0` | blob | 6833 | `PORT_TEST` | tests/** |
| 601 | `tests/integration/test_tui_exit_e2e.py` | `17e5120b7b121eab7109ecdb6e37857e95a1e0ba` | blob | 3104 | `PORT_TEST` | tests/** |
| 602 | `tests/integration/test_tui_rpc_production_smoke.py` | `574542efed0297341592acdca2b71c322cfcdf40` | blob | 3041 | `PORT_TEST` | tests/** |
| 603 | `tests/test_ag1_backend_dispatch.py` | `73d525e745db82ca7143a0f54e899335af286d8f` | blob | 9152 | `PORT_TEST` | tests/** |
| 604 | `tests/test_agent_hook_contract.py` | `85998a4fe34429444070c2a7c642090ea44e0df0` | blob | 17628 | `PORT_TEST` | tests/** |
| 605 | `tests/test_agent_loop_context_overflow.py` | `11986cbc3d408334b91ddcfe2292af7e2d76032a` | blob | 4113 | `PORT_TEST` | tests/** |
| 606 | `tests/test_agent_loop_empty_recovery.py` | `abba6fcab52d40afe7bacba56a4494dd2f9288a2` | blob | 10050 | `PORT_TEST` | tests/** |
| 607 | `tests/test_agent_loop_injected_skill_ids.py` | `a08e83070e8c2540f6323d767459530f4289e1f8` | blob | 3656 | `PORT_TEST` | tests/** |
| 608 | `tests/test_agent_loop_max_iter_synthesis.py` | `c303202619abd0513a45eb9f7298a5465d28fa8b` | blob | 7679 | `PORT_TEST` | tests/** |
| 609 | `tests/test_agent_loop_memory_pipeline.py` | `13bb28241b4d966798e9fbd127a27bdf18217bf4` | blob | 4530 | `PORT_TEST` | tests/** |
| 610 | `tests/test_agent_loop_run_emit.py` | `77e121cf5d00adb2755ee12bf6a3db5b2516cd0e` | blob | 27191 | `PORT_TEST` | tests/** |
| 611 | `tests/test_agent_loop_session_stamps.py` | `aea147f3feb4f50e649b75dbc049e59bbe9ee106` | blob | 4451 | `PORT_TEST` | tests/** |
| 612 | `tests/test_agent_loop_stream.py` | `ca5cdec3237d045f38f1598eb5b07d897ea6cbd5` | blob | 7637 | `PORT_TEST` | tests/** |
| 613 | `tests/test_agent_loop_tool_loop_break.py` | `086a07c83372ace593ce4160756c0043aa6faed6` | blob | 3663 | `PORT_TEST` | tests/** |
| 614 | `tests/test_agent_loop_tool_search.py` | `bedbbd4b8ca4b536c8b53f2630dffbe4d42d65c6` | blob | 3845 | `PORT_TEST` | tests/** |
| 615 | `tests/test_agent_loop_usage_sink.py` | `db320c45cedcdf53f0b9b177b7827d9410a9c6ab` | blob | 9282 | `PORT_TEST` | tests/** |
| 616 | `tests/test_appworld_precheck.py` | `da53ffe857ea835b5187380166a59d68755fd95d` | blob | 7064 | `PORT_TEST` | tests/** |
| 617 | `tests/test_appworld_sandbox.py` | `df5747771c589bcc76adbaac30f3ca2340ce44a0` | blob | 5306 | `PORT_TEST` | tests/** |
| 618 | `tests/test_atomic_io.py` | `66d2cff235407b17413fe31e999dd100d2c27103` | blob | 7505 | `PORT_TEST` | tests/** |
| 619 | `tests/test_auth_allowlist.py` | `735ffcc7be9dfb06b4e3d4cc9ac9117057819cba` | blob | 6934 | `PORT_TEST` | tests/** |
| 620 | `tests/test_bedrock_stub.py` | `531ca29bcad173f623735e9da95028406ee14a2f` | blob | 1950 | `PORT_TEST` | tests/** |
| 621 | `tests/test_bm25.py` | `79d77239231cd2c2952d8605b26a642182e5fbb5` | blob | 1812 | `PORT_TEST` | tests/** |
| 622 | `tests/test_call_efficiency_replay.py` | `ec78507878537db2e81093e04c058276b4795aa5` | blob | 6865 | `PORT_TEST` | tests/** |
| 623 | `tests/test_call_efficiency.py` | `189bb38f849d07ecb32af22d8c4365aa4e538e2e` | blob | 41906 | `PORT_TEST` | tests/** |
| 624 | `tests/test_channels_base.py` | `0381d28ec02d770c565b977c3ee2e2d408c4f8f4` | blob | 2381 | `PORT_TEST` | tests/** |
| 625 | `tests/test_channels_contract.py` | `f86d9cdd83c784ca552c61a085485cbf974385e9` | blob | 3049 | `PORT_TEST` | tests/** |
| 626 | `tests/test_channels_errors.py` | `e7da45fc75557c35e2c3ad58f4b7823da5ed39fd` | blob | 1288 | `PORT_TEST` | tests/** |
| 627 | `tests/test_channels_feishu.py` | `43bbd7c857301b87e21471b509e85d91ef464a2b` | blob | 14739 | `PORT_TEST` | tests/** |
| 628 | `tests/test_channels_intake.py` | `e33fab992b200d1248cec6ac8869be6143a35b0b` | blob | 5594 | `PORT_TEST` | tests/** |
| 629 | `tests/test_channels_manager.py` | `421363724cd1ba9dd2a7ae13d63b4b4dc11d3e19` | blob | 14926 | `PORT_TEST` | tests/** |
| 630 | `tests/test_channels_media.py` | `2c25479e3b1ac6cb7fccfd01464a3f1f5da02f14` | blob | 1337 | `PORT_TEST` | tests/** |
| 631 | `tests/test_channels_outlet.py` | `473be6019a51e0f74603f44f019628c3f7d7614f` | blob | 2311 | `PORT_TEST` | tests/** |
| 632 | `tests/test_channels_qq.py` | `fa8d49d9bb6570a08666f4f5a4b813493eb425f1` | blob | 13366 | `PORT_TEST` | tests/** |
| 633 | `tests/test_channels_registry.py` | `cd07eedc64fa2102e793282531ebdcaf1ce259f5` | blob | 1621 | `PORT_TEST` | tests/** |
| 634 | `tests/test_channels_required_marker.py` | `125abd4d65c416906f06afb08665f45247696866` | blob | 1033 | `PORT_TEST` | tests/** |
| 635 | `tests/test_channels_wecom.py` | `1b16eada21d02a9a05857977b80c5c1fbc870d5c` | blob | 13631 | `PORT_TEST` | tests/** |
| 636 | `tests/test_check_commit_messages.py` | `b32365027428ccd0486818317f54b0e210594645` | blob | 1617 | `PORT_TEST` | tests/** |
| 637 | `tests/test_cl1_plugin_stack.py` | `a3d03648c1e75bc2e1689b680b69ed7dd2959f42` | blob | 5548 | `PORT_TEST` | tests/** |
| 638 | `tests/test_cli_agent_commands.py` | `4bfd2e625539947c0133a34d2e737eef7d8f7c93` | blob | 21306 | `PORT_TEST` | tests/** |
| 639 | `tests/test_cli_channel_commands.py` | `dc1b646325c8cc331ce0b5445089366620bd55de` | blob | 7462 | `PORT_TEST` | tests/** |
| 640 | `tests/test_cli_config_precedence.py` | `59810cc8b2abfbd03f6aac93257a4a89af5ba3ef` | blob | 7501 | `PORT_TEST` | tests/** |
| 641 | `tests/test_cli_cron_commands.py` | `91fdd973027dd558a2b2c4d584e9143d9c7a606a` | blob | 27108 | `PORT_TEST` | tests/** |
| 642 | `tests/test_cli_cron_handler.py` | `93c852f45e5cb4457189911639a269b8befb87e7` | blob | 21150 | `PORT_TEST` | tests/** |
| 643 | `tests/test_cli_doctor_commands.py` | `76cad386b7394320b00540a86e94ad77a8034d9c` | blob | 10543 | `PORT_TEST` | tests/** |
| 644 | `tests/test_cli_evolve_commands.py` | `3c180ac1ffe8c02fac440c7627bada6457479f60` | blob | 1555 | `PORT_TEST` | tests/** |
| 645 | `tests/test_cli_gateway_commands.py` | `ef8628fd2d1b8b646f5290a0c15809242fd724e8` | blob | 17800 | `PORT_TEST` | tests/** |
| 646 | `tests/test_cli_gateway_health.py` | `0e4e1d0aaa3a5aa862a8c5af789e813bea531934` | blob | 905 | `PORT_TEST` | tests/** |
| 647 | `tests/test_cli_gateway_lock.py` | `ad0356ab9aa99eb2f0065665f4a42ac0048f998b` | blob | 3229 | `PORT_TEST` | tests/** |
| 648 | `tests/test_cli_gateway_spine.py` | `969082e607d1c30058544d4b06a1e85a04c3f77f` | blob | 14374 | `PORT_TEST` | tests/** |
| 649 | `tests/test_cli_helpers.py` | `f0420d609221a2577390c56957b7cca6d9070bef` | blob | 6676 | `PORT_TEST` | tests/** |
| 650 | `tests/test_cli_log_file.py` | `14027a213392e2628ad164b91f2a91d8c644540a` | blob | 10591 | `PORT_TEST` | tests/** |
| 651 | `tests/test_cli_onboard_commands.py` | `e9b2c66e6efa9692cfa519dd9c6db05e3f2aed4a` | blob | 47108 | `PORT_TEST` | tests/** |
| 652 | `tests/test_cli_provider_commands.py` | `7fdcc328026a7000285bd6e8dae4f306df8ba589` | blob | 12561 | `PORT_TEST` | tests/** |
| 653 | `tests/test_cli_repl_spine.py` | `e52e16e934175b6ef12375ec8f4ec21f4a62b449` | blob | 11218 | `PORT_TEST` | tests/** |
| 654 | `tests/test_cli_runtime_assembly.py` | `adbe5e879057699d8cdf41900656b64696848627` | blob | 24707 | `PORT_TEST` | tests/** |
| 655 | `tests/test_cli_session_commands.py` | `cb89233235637bc409914d88fe0610dcd62b2e77` | blob | 13824 | `PORT_TEST` | tests/** |
| 656 | `tests/test_cli_skill_commands.py` | `7afe1f08ea6df30e30388ea1b592694634eac285` | blob | 5335 | `PORT_TEST` | tests/** |
| 657 | `tests/test_cli_smoke.py` | `91a8bdc32dd587c0d5d97f330fdfcfddbdd92a3b` | blob | 6453 | `PORT_TEST` | tests/** |
| 658 | `tests/test_cli_stacks.py` | `3e8b5cc194fc592438154cfbe757b7c56dc43d5b` | blob | 5463 | `PORT_TEST` | tests/** |
| 659 | `tests/test_cli_status_commands.py` | `9d14f4531ee617df815b8bb08794ca28e8cac166` | blob | 2955 | `PORT_TEST` | tests/** |
| 660 | `tests/test_cli_tracing_commands.py` | `ae11f41d5089cc0e1c8d2c3708c5ec4781eb9214` | blob | 3529 | `PORT_TEST` | tests/** |
| 661 | `tests/test_cli_tui_bootstrap.py` | `ff04055d8d5840c7e3ced2b3213424c3990a7f41` | blob | 15569 | `PORT_TEST` | tests/** |
| 662 | `tests/test_cli_tui_commands.py` | `d742f8b733bed4a8a4757a20142dda6475ab8cfc` | blob | 29433 | `PORT_TEST` | tests/** |
| 663 | `tests/test_cli_tui_fork.py` | `9b655e4fd0128317925b2bddc3b1ac7d1fee7c35` | blob | 7898 | `PORT_TEST` | tests/** |
| 664 | `tests/test_cli_tui_logging_isolation.py` | `fd36bce1611a6bc61f4c9d48c8bdb29a5f6a7fc6` | blob | 5144 | `PORT_TEST` | tests/** |
| 665 | `tests/test_commit_lint.py` | `3629e31e0057d2533d3c7d3f3caf16ab12042bd2` | blob | 3530 | `PORT_TEST` | tests/** |
| 666 | `tests/test_config_cfg1.py` | `4069fbe162a1a96fa138f7bdff6a324cd8551283` | blob | 7998 | `PORT_TEST` | tests/** |
| 667 | `tests/test_config_loader.py` | `fa36cc844aaf68ababa45d7a00f24b64809bc49c` | blob | 7651 | `PORT_TEST` | tests/** |
| 668 | `tests/test_config_pico_loader.py` | `b97f9e864e8caef1b4d729fab28bf4fb49fd3c62` | blob | 6952 | `PORT_TEST` | tests/** |
| 669 | `tests/test_config_routing.py` | `8c4548859941fc026b0bd5ac7cbcf6933e00f684` | blob | 2055 | `PORT_TEST` | tests/** |
| 670 | `tests/test_config_update_channels.py` | `efec8c58b8c13e8a58e9959a99bf35f5499809a4` | blob | 8125 | `PORT_TEST` | tests/** |
| 671 | `tests/test_config_update_providers.py` | `9644ef11d112306713e78af5306276419242c85d` | blob | 17234 | `PORT_TEST` | tests/** |
| 672 | `tests/test_config_update.py` | `7a7f6fbf1897cb3278ef5795101cb3a903774f13` | blob | 9710 | `PORT_TEST` | tests/** |
| 673 | `tests/test_consolidator_split.py` | `04d0e9209810e6fe261852b4b90d8768dd640568` | blob | 17191 | `PORT_TEST` | tests/** |
| 674 | `tests/test_context_invariants.py` | `ccf324f496924d108378d2892a21543429087864` | blob | 8149 | `PORT_TEST` | tests/** |
| 675 | `tests/test_cron_delivery.py` | `b102ca9fd13a2ff915a0689723b9c4236b0b4229` | blob | 11339 | `PORT_TEST` | tests/** |
| 676 | `tests/test_cron_service_claim.py` | `3b0a13d509bd0ed404760f31f444e282d20fd5b5` | blob | 4211 | `PORT_TEST` | tests/** |
| 677 | `tests/test_cron_service_dedup.py` | `9c5c0c289bff53dbcccdc4fcfe2cf4a54a3ad8af` | blob | 5205 | `PORT_TEST` | tests/** |
| 678 | `tests/test_cron_service_outcomes.py` | `3ad188677ac660a6f46cccfc389adbbe5736aa5a` | blob | 10116 | `PORT_TEST` | tests/** |
| 679 | `tests/test_cron_service_reload.py` | `b8237e54c896572020b4930c908a19b568d87d38` | blob | 1516 | `PORT_TEST` | tests/** |
| 680 | `tests/test_cron_service_validation.py` | `51b2f5f495e3ac5b4b7668168ea3d99129912bb7` | blob | 3670 | `PORT_TEST` | tests/** |
| 681 | `tests/test_cron_tool.py` | `d0d072f78a8259708c7eaa16d03dae0088c7b2c7` | blob | 3424 | `PORT_TEST` | tests/** |
| 682 | `tests/test_curator_context_engine.py` | `bb2ef274c4696e94c60155710de710c5d496d9f4` | blob | 15456 | `PORT_TEST` | tests/** |
| 683 | `tests/test_default_context_engine.py` | `18a49a85ef79ebb0fa811fe499fe91cae9896cd5` | blob | 15277 | `PORT_TEST` | tests/** |
| 684 | `tests/test_error_classification.py` | `805faa4019c637e83dd804d3faaeef065b4eeb0d` | blob | 3238 | `PORT_TEST` | tests/** |
| 685 | `tests/test_eval_engine.py` | `0a302c02e0ba5c084ca80f76e732c8c584604499` | blob | 15354 | `PORT_TEST` | tests/** |
| 686 | `tests/test_evolver_activation_artifacts.py` | `66140e7bccd92bfeb405d4ac7a4f4bbe33640d9e` | blob | 41724 | `PORT_TEST` | tests/** |
| 687 | `tests/test_evolver_candidate_evidence.py` | `88532d3582cd5686ecebb0c82d376d18f896024c` | blob | 7685 | `PORT_TEST` | tests/** |
| 688 | `tests/test_evolver_candidate_manifest.py` | `bd00cef41c7eba6534bf9f00bae661ee780a319d` | blob | 16104 | `PORT_TEST` | tests/** |
| 689 | `tests/test_evolver_candidate_pipeline.py` | `216d98cbb01483d9a7aed65f1b79fd6b229e30c7` | blob | 7521 | `PORT_TEST` | tests/** |
| 690 | `tests/test_evolver_claude_cli.py` | `895bea1b23625e31908e1bb7b7d7bfa51da09aa4` | blob | 4253 | `PORT_TEST` | tests/** |
| 691 | `tests/test_evolver_compressor.py` | `d615c82271d7034086678da9f7ddb64cb6e27b12` | blob | 1954 | `PORT_TEST` | tests/** |
| 692 | `tests/test_evolver_gates.py` | `1d74bb9c712422d17b998c8e02f53364490deb7e` | blob | 20721 | `PORT_TEST` | tests/** |
| 693 | `tests/test_evolver_git_ops.py` | `556298066f00700b7ff8b62872b4125ea033e9e3` | blob | 6644 | `PORT_TEST` | tests/** |
| 694 | `tests/test_evolver_launch_e2e.py` | `398959e2367e05a147c79874e3929705fe27622c` | blob | 16039 | `PORT_TEST` | tests/** |
| 695 | `tests/test_evolver_launch.py` | `ac085ac7c2522c3772fe84f0142f25a911787fb3` | blob | 27666 | `PORT_TEST` | tests/** |
| 696 | `tests/test_evolver_scoring.py` | `3ae568f9964ad6ae13a4749ffd36c33cea440eff` | blob | 12171 | `PORT_TEST` | tests/** |
| 697 | `tests/test_evolver_small_real_bench.py` | `3540ce39589744a625c8e92639bf4a19e2b5fe4f` | blob | 19724 | `PORT_TEST` | tests/** |
| 698 | `tests/test_evolver_surface_contract.py` | `cb5974a63b599a9ca518f4cacd509dec64abd7a8` | blob | 2175 | `PORT_TEST` | tests/** |
| 699 | `tests/test_evolver_termination.py` | `99ba98cd76ce3efbd79f93e8ecbe17e1bf3c5b2c` | blob | 2959 | `PORT_TEST` | tests/** |
| 700 | `tests/test_file_search_traversal_guard.py` | `0d4fad0c90cc6c29459ea7762d51429dae70fae5` | blob | 1792 | `PORT_TEST` | tests/** |
| 701 | `tests/test_foresight_persistence.py` | `5e5760626c52be325adf7bea75e6c34edf2248ea` | blob | 13301 | `PORT_TEST` | tests/** |
| 702 | `tests/test_guards.py` | `c7e71dce09972449aa6e90f1baa6d54d88e1fae1` | blob | 8239 | `PORT_TEST` | tests/** |
| 703 | `tests/test_history_trimmer.py` | `6c2c5d546101952314ee50975c76ffd699cb4a5f` | blob | 3371 | `PORT_TEST` | tests/** |
| 704 | `tests/test_install_scripts.py` | `0a50c0894a7c29cf3f882b8286f002fbd56a2ef6` | blob | 2023 | `PORT_TEST` | tests/** |
| 705 | `tests/test_knn_router.py` | `2fe785af69660a8f575c3044b3ada3fbad0c83c5` | blob | 7289 | `PORT_TEST` | tests/** |
| 706 | `tests/test_large_file_check.py` | `333e630c08f658f8e08069f1d92a99afa57da0a6` | blob | 4284 | `PORT_TEST` | tests/** |
| 707 | `tests/test_lazy_provider.py` | `a69257ed8c0ba99ce3efb284874854099411eb0f` | blob | 2736 | `PORT_TEST` | tests/** |
| 708 | `tests/test_litellm_provider_attribution.py` | `8ec89f794f7ea5958407d2cc3cf2e696fee2a5df` | blob | 2897 | `PORT_TEST` | tests/** |
| 709 | `tests/test_litellm_provider_response.py` | `8faed6223209cd56fa23af3fa989a4a9b077c808` | blob | 5072 | `PORT_TEST` | tests/** |
| 710 | `tests/test_litellm_provider_stream.py` | `5e1edf22dca2a9268b1068d69480960851d867d4` | blob | 11185 | `PORT_TEST` | tests/** |
| 711 | `tests/test_litellm_setup.py` | `47d9428da8294896ce1044d3bfeeb6f663c189ae` | blob | 875 | `PORT_TEST` | tests/** |
| 712 | `tests/test_mcp_tools.py` | `6f8c73b9e96ddc63befb2d463255990c780a3bcd` | blob | 1225 | `PORT_TEST` | tests/** |
| 713 | `tests/test_memory_backend_contract.py` | `8ee49c5b048cb9bc62a7d052c1ea7c7fd82f695c` | blob | 2544 | `PORT_TEST` | tests/** |
| 714 | `tests/test_memory_backend_protocol.py` | `f8fc09b04e4b5d980a5612f34aaf813e6002650c` | blob | 4408 | `PORT_TEST` | tests/** |
| 715 | `tests/test_memory_locking.py` | `445f0ed2a40f23c5031930e9b6c772d656c88cb3` | blob | 3080 | `PORT_TEST` | tests/** |
| 716 | `tests/test_memory_store_lt_additions.py` | `a7b1a6a02556c3aa6411f4643f6f90005bc0e60c` | blob | 7109 | `PORT_TEST` | tests/** |
| 717 | `tests/test_message_tool_turn_local.py` | `08027de1eefc4f4186bef18a774a06a375f0d6fd` | blob | 1105 | `PORT_TEST` | tests/** |
| 718 | `tests/test_no_otel_tracing.py` | `223b6d1370597fc2233531786e791af71fa80193` | blob | 762 | `PORT_TEST` | tests/** |
| 719 | `tests/test_openai_codex_provider.py` | `5e59780fb0df9c479e13fecb80807b89dd57c87b` | blob | 1299 | `PORT_TEST` | tests/** |
| 720 | `tests/test_per_model_provider.py` | `7cdad654b82991960b82fd1e8152ee498cdc26fd` | blob | 3523 | `PORT_TEST` | tests/** |
| 721 | `tests/test_phase_a_default_engine.py` | `43481b40b7be0beeb7986658e467fef461662a23` | blob | 11685 | `PORT_TEST` | tests/** |
| 722 | `tests/test_picobench_budget.py` | `aa2a70d1966ed84090c2a1b654c48262b046115d` | blob | 17645 | `PORT_TEST` | tests/** |
| 723 | `tests/test_picobench_campaign.py` | `492f7125470636bafd66252a871ff16af9282081` | blob | 75869 | `PORT_TEST` | tests/** |
| 724 | `tests/test_picobench_context_track.py` | `d2e2ead5571a34c6c666a2c2b4a38108f97ee79e` | blob | 26833 | `PORT_TEST` | tests/** |
| 725 | `tests/test_picobench_contract.py` | `d32f59f6c5830048627ebcf5b93870969a23956b` | blob | 18962 | `PORT_TEST` | tests/** |
| 726 | `tests/test_picobench_environment.py` | `56c76ac8b0e191029e614637fae1a056b5114f39` | blob | 5348 | `PORT_TEST` | tests/** |
| 727 | `tests/test_picobench_memory_skill_track.py` | `78ba551ad18ed692ae8641f7f19e042345a50c69` | blob | 53839 | `PORT_TEST` | tests/** |
| 728 | `tests/test_picobench_reporting.py` | `2b477270a7e0c05ae724acb9220b4d592b2b78ee` | blob | 39839 | `PORT_TEST` | tests/** |
| 729 | `tests/test_picobench_reproduce.py` | `6745550bea7110a35b75d8b88b7e6f1ad64abd3b` | blob | 13102 | `PORT_TEST` | tests/** |
| 730 | `tests/test_picobench_runtime_experiments.py` | `9a93df53bfc053a6283851f0881ada4c43542805` | blob | 1278 | `PORT_TEST` | tests/** |
| 731 | `tests/test_picobench_runtime_live_experiment.py` | `c24c7718428fb9b307b97a2d6e362a3265572fb0` | blob | 5314 | `PORT_TEST` | tests/** |
| 732 | `tests/test_picobench_runtime_track.py` | `f072237fc165d7ca26427e84b067b103d8683d20` | blob | 1366 | `PORT_TEST` | tests/** |
| 733 | `tests/test_picobench_scorecard_campaign.py` | `cc66f17346b579b025a49a9dc398739d5c7285b1` | blob | 2531 | `PORT_TEST` | tests/** |
| 734 | `tests/test_picobench_scorecard.py` | `5379f67f8d1e840e863c8bfe2785aca85f1dbe48` | blob | 5526 | `PORT_TEST` | tests/** |
| 735 | `tests/test_picobench_semantic_campaign.py` | `861a9b61f11c8a42774ea62f7f60563c8c1337ec` | blob | 22055 | `PORT_TEST` | tests/** |
| 736 | `tests/test_picobench_semantic_memory_effect.py` | `445becea7e88cd19a1cfd72617d0d1e7951b6f85` | blob | 20864 | `PORT_TEST` | tests/** |
| 737 | `tests/test_picobench_semantic_v2.py` | `13edafefd6c4f3d95a9ff644bd63b43d95c340fe` | blob | 5441 | `PORT_TEST` | tests/** |
| 738 | `tests/test_picobench_tokenwise_cost_campaign.py` | `419437572ebdae838c81070a501764341c62e821` | blob | 15579 | `PORT_TEST` | tests/** |
| 739 | `tests/test_picobench_tokenwise_cost.py` | `0a6127805adfc1ffc29c34acb45af92f1f46858c` | blob | 6408 | `PORT_TEST` | tests/** |
| 740 | `tests/test_picobench_tool_execution_experiments.py` | `884e7060c7dcb5304cd4ce61c0705ab583143901` | blob | 856 | `PORT_TEST` | tests/** |
| 741 | `tests/test_picobench_tool_mcp_track.py` | `bb59c2d56701f6a260952bc90ddee01c7f9bdbaf` | blob | 21581 | `PORT_TEST` | tests/** |
| 742 | `tests/test_picobench_tracing_overhead.py` | `d88189eac961a8b62d480a1c00332a247bb550e5` | blob | 1611 | `PORT_TEST` | tests/** |
| 743 | `tests/test_picobench_trial_host.py` | `f7e1611130fec78f503044930f067f513fef71b8` | blob | 22455 | `PORT_TEST` | tests/** |
| 744 | `tests/test_plugin_bootstrap.py` | `6ad21a803a81a2c21fa6c4daef058769ff467b21` | blob | 11308 | `PORT_TEST` | tests/** |
| 745 | `tests/test_plugin_command.py` | `afc2dd4533554e6228349a8080bb16229222faf9` | blob | 4184 | `PORT_TEST` | tests/** |
| 746 | `tests/test_plugin_context.py` | `80a2e0f26357f0a492ddf699c56372fa7bc9a38f` | blob | 1887 | `PORT_TEST` | tests/** |
| 747 | `tests/test_plugin_discover.py` | `92c2298898df3d85612d8aa0c1979eec54f403e8` | blob | 8803 | `PORT_TEST` | tests/** |
| 748 | `tests/test_plugin_manifest.py` | `5a56467a6ab9e1a45db64fdf80f8d46076729f71` | blob | 7391 | `PORT_TEST` | tests/** |
| 749 | `tests/test_plugin_registry.py` | `aef455dc9a59c975d081d176af11f90c9be83bce` | blob | 9903 | `PORT_TEST` | tests/** |
| 750 | `tests/test_plugin_tools.py` | `3c359c14a64b65584ae59899f4f6a01319e7db6e` | blob | 9637 | `PORT_TEST` | tests/** |
| 751 | `tests/test_plugin_trust_boundary.py` | `feaccc536b302ed365ebc34f3b667d86f762f94d` | blob | 5925 | `PORT_TEST` | tests/** |
| 752 | `tests/test_product_identity.py` | `ce962e717f22a87215bec0a215eee117f53960b7` | blob | 9859 | `PORT_TEST` | tests/** |
| 753 | `tests/test_provider_catalog.py` | `45930c89064aa2e05c8ee0b496dad66f24dc9dc1` | blob | 3152 | `PORT_TEST` | tests/** |
| 754 | `tests/test_provider_fallback_chain.py` | `7ebc5bba2bf8546079dc6bf458051f162f418b62` | blob | 7116 | `PORT_TEST` | tests/** |
| 755 | `tests/test_provider_stream_fallback.py` | `0cf104d71a2ac55aed13fae757a4c91ce0183583` | blob | 2714 | `PORT_TEST` | tests/** |
| 756 | `tests/test_public_release_tree.py` | `1fea87949a5a91454ebc8ec324b259a0e38bc6b2` | blob | 3109 | `PORT_TEST` | tests/** |
| 757 | `tests/test_question_broker.py` | `eb0494f5479baef98a9d2866be9610dc2f59a6d8` | blob | 6257 | `PORT_TEST` | tests/** |
| 758 | `tests/test_recent_project_tags.py` | `3297ca66ddba3b220abbc4a2171fcc11c97816bf` | blob | 2409 | `PORT_TEST` | tests/** |
| 759 | `tests/test_retained_gate.py` | `395dda7719f6e5988389f59ce2841d2d5bb61094` | blob | 2179 | `PORT_TEST` | tests/** |
| 760 | `tests/test_routing_fallback_chain.py` | `f3df5bf7a9f34d11d4fe4b3ac02a391f99567277` | blob | 2679 | `PORT_TEST` | tests/** |
| 761 | `tests/test_rpc_schema_match.py` | `14953c4b77e2e5778f6ae83cecebcd40727b7f3b` | blob | 17123 | `PORT_TEST` | tests/** |
| 762 | `tests/test_runtime_checkpoint_bug2_deep.py` | `c0b7f8229d80d43deb6c7c47ce1be384fbfa26ed` | blob | 27449 | `PORT_TEST` | tests/** |
| 763 | `tests/test_runtime_checkpoint_bug2.py` | `59cfa9c36c3a8770f296bf353e264bd85154011c` | blob | 13787 | `PORT_TEST` | tests/** |
| 764 | `tests/test_runtime_host_contracts.py` | `6373a10f2ce0235df041b59a60c09f5585dfb27d` | blob | 13181 | `PORT_TEST` | tests/** |
| 765 | `tests/test_sandbox_cli_integration.py` | `4bd68f6407090591aff8acc7bf2deda577c9c76d` | blob | 10601 | `PORT_TEST` | tests/** |
| 766 | `tests/test_sandbox_cli.py` | `03e4572696aad1b68313399f9021a5c4bd485349` | blob | 16483 | `PORT_TEST` | tests/** |
| 767 | `tests/test_sandbox_debug_server.py` | `8454964e137df0c20faeb4fcf7f102a466afab23` | blob | 43412 | `PORT_TEST` | tests/** |
| 768 | `tests/test_sandbox_integration.py` | `50b9fe454b944a9223c27226eba0cc53af77f21e` | blob | 4621 | `PORT_TEST` | tests/** |
| 769 | `tests/test_sandbox_unit.py` | `9c5d814ed80b1c35bfaa08bc435e024947f3dbac` | blob | 42738 | `PORT_TEST` | tests/** |
| 770 | `tests/test_search_tools.py` | `b5e36fde5194a6f090eb962f8babb52fa592cf7b` | blob | 5675 | `PORT_TEST` | tests/** |
| 771 | `tests/test_section_aware_read.py` | `9f20204d06e4f0da0f1da0fc5c6855c40362ab20` | blob | 4920 | `PORT_TEST` | tests/** |
| 772 | `tests/test_security_network.py` | `c7d8e8ab8bb1c69a6af4e9e979f2ea1456c87a2a` | blob | 4197 | `PORT_TEST` | tests/** |
| 773 | `tests/test_security_trust.py` | `c9a5af5289bd85779dac975e3a4ee5a9ec5908d3` | blob | 2019 | `PORT_TEST` | tests/** |
| 774 | `tests/test_security_untrusted_context.py` | `e237936fc8e0ab84242fe94df891b7f5cb0fc271` | blob | 3502 | `PORT_TEST` | tests/** |
| 775 | `tests/test_security_web_ssrf.py` | `eb14946a21b32d831b9fe1f3f9124afc83c81716` | blob | 6089 | `PORT_TEST` | tests/** |
| 776 | `tests/test_segments.py` | `694cdbd98a9d48a6884bb2cd450589210631fa3f` | blob | 5101 | `PORT_TEST` | tests/** |
| 777 | `tests/test_session_export.py` | `8e7f813e1e15c30939210a5a0dbea18f93b3c8bd` | blob | 4978 | `PORT_TEST` | tests/** |
| 778 | `tests/test_session_manager.py` | `0ece111eeeb5acea4e08b566c327adcc7ddb1bb9` | blob | 57113 | `PORT_TEST` | tests/** |
| 779 | `tests/test_skill_forge_gate.py` | `b673bc05327c1c30230021bc1468b2a0d4dfbedc` | blob | 5010 | `PORT_TEST` | tests/** |
| 780 | `tests/test_skill_forge_local_pool.py` | `d6ee9b963e7b574842c999ba18cda851b13e18e0` | blob | 7533 | `PORT_TEST` | tests/** |
| 781 | `tests/test_skill_forge_phase_a.py` | `8cde324808c85c164a3ea2503ce554a77fe04ed7` | blob | 21038 | `PORT_TEST` | tests/** |
| 782 | `tests/test_skill_forge_refs.py` | `f4320b498c566e7a7591a9d44ffc0b240addb6ca` | blob | 3783 | `PORT_TEST` | tests/** |
| 783 | `tests/test_skill_forge_rewriter.py` | `281124dc3994491c236ed86aecd4d94ec00c518a` | blob | 3114 | `PORT_TEST` | tests/** |
| 784 | `tests/test_skill_ref_resolution.py` | `88edb3afe8f4fe8d059b139861eca5d9f5d99135` | blob | 7716 | `PORT_TEST` | tests/** |
| 785 | `tests/test_skill_router_sr1.py` | `48f685af19c49ac520c3bb27b7bcf336a4ae4bdb` | blob | 9137 | `PORT_TEST` | tests/** |
| 786 | `tests/test_skill_router_sr2.py` | `7c59cbabdc09cdbb1b77987d9f50562e783c2f79` | blob | 7721 | `PORT_TEST` | tests/** |
| 787 | `tests/test_skill_segment_builder.py` | `67bd95ae6bd0aedd3e484a81c5f345b2a8d77f7c` | blob | 6092 | `PORT_TEST` | tests/** |
| 788 | `tests/test_spine_delivery.py` | `7a1ad01050a0496f555cb3ed45f5ca1ea0925c32` | blob | 30077 | `PORT_TEST` | tests/** |
| 789 | `tests/test_spine_events.py` | `a3a667312f78e76159fa4abe0ff8101fd50c0286` | blob | 5792 | `PORT_TEST` | tests/** |
| 790 | `tests/test_spine_message.py` | `7b36b071d5b10df448e18c9fa1b615d35ef734bf` | blob | 1983 | `PORT_TEST` | tests/** |
| 791 | `tests/test_spine_runner.py` | `337c2b28f5e60482cec8ccacdfbfafad4181c3bd` | blob | 3055 | `PORT_TEST` | tests/** |
| 792 | `tests/test_spine_scheduler_lane.py` | `1c11e680a097fc578aa8b2998bd6512568562399` | blob | 16237 | `PORT_TEST` | tests/** |
| 793 | `tests/test_spine_scheduler_pools.py` | `f346acdaeaf76f62596ac30e4af9c7ea4541a5cd` | blob | 2041 | `PORT_TEST` | tests/** |
| 794 | `tests/test_spine_scheduler.py` | `1e4631f0dfe5b8f3a48b7bad31e49057fa38f9aa` | blob | 25416 | `PORT_TEST` | tests/** |
| 795 | `tests/test_spine_turn.py` | `0a03e0454ff39a264ae206d55e5e2edf1f663961` | blob | 2116 | `PORT_TEST` | tests/** |
| 796 | `tests/test_subagent_manager.py` | `9738dcb0a7d172ac33ba45a4ba165bcefbffb3f6` | blob | 17028 | `PORT_TEST` | tests/** |
| 797 | `tests/test_subscription_emitter.py` | `94c10507b76a404a726cff3465b77dd71575a577` | blob | 8615 | `PORT_TEST` | tests/** |
| 798 | `tests/test_token_estimation.py` | `2cd04bbd622e3a8e378fddf5cc765091c525c683` | blob | 5703 | `PORT_TEST` | tests/** |
| 799 | `tests/test_token_wise_agentloop_experiment.py` | `6f16be59bf7693f3509b21ac150c165d0c2735f5` | blob | 19370 | `PORT_TEST` | tests/** |
| 800 | `tests/test_token_wise_cache_optimizer.py` | `0983a50a19468ca80ebedd172d80fb5147a4f44b` | blob | 6852 | `PORT_TEST` | tests/** |
| 801 | `tests/test_token_wise_cache_strategies.py` | `85fa4e5af219d920478bd6e2a042ba6fe7be8142` | blob | 22481 | `PORT_TEST` | tests/** |
| 802 | `tests/test_token_wise_pricing.py` | `5efaf542e24793fa3dcd68245d88b520e84d9fd4` | blob | 15710 | `PORT_TEST` | tests/** |
| 803 | `tests/test_token_wise_registry.py` | `32aff534e416ba150cfd62a71aab95e401d2efcf` | blob | 4660 | `PORT_TEST` | tests/** |
| 804 | `tests/test_token_wise_usage_tracker.py` | `c05daee3c496732a136cb38f38d127f68bea66c1` | blob | 6835 | `PORT_TEST` | tests/** |
| 805 | `tests/test_token_wise_workload_scenarios.py` | `4efddf0c45b65aebf04368cf178292267abb9404` | blob | 24530 | `PORT_TEST` | tests/** |
| 806 | `tests/test_tool_registry_execution.py` | `f306217a0b37b482e5131cfd8c2c9fef0ce295b8` | blob | 6889 | `PORT_TEST` | tests/** |
| 807 | `tests/test_tool_registry_timeout.py` | `d94e01d559cd95ac6185ef424598b68e5ee02dcf` | blob | 4090 | `PORT_TEST` | tests/** |
| 808 | `tests/test_tool_search.py` | `d4e10ec10faa92b6d37528342bd269cffaf42efc` | blob | 14405 | `PORT_TEST` | tests/** |
| 809 | `tests/test_tracing_api.py` | `07ef977ea13519f19e986fddda3091d57ada2e60` | blob | 16697 | `PORT_TEST` | tests/** |
| 810 | `tests/test_tracing_viewer.py` | `59c79ad8f4fe83d8b0e061487aaaaf5f6ee02788` | blob | 7554 | `PORT_TEST` | tests/** |
| 811 | `tests/test_tui_commands_error_codes.py` | `3e853c83bcbacbf0f71d922a84c96374398f5169` | blob | 4489 | `PORT_TEST` | tests/** |
| 812 | `tests/test_tui_cron_delivered_event.py` | `a43d7f6c7bc4a63cd4872dc955e862cc5253bd87` | blob | 5505 | `PORT_TEST` | tests/** |
| 813 | `tests/test_tui_cron_tool_wired.py` | `8f770615c24f46f7f44ca3506df3dd1e2c0af2bc` | blob | 5421 | `PORT_TEST` | tests/** |
| 814 | `tests/test_tui_rpc_config.py` | `83ea023c109af8de0e352d1fb54df020a8da7e79` | blob | 11524 | `PORT_TEST` | tests/** |
| 815 | `tests/test_tui_rpc_confirm.py` | `77330aa0dbbb72857ecbb9f1e3f43e3cc4f1cad1` | blob | 5232 | `PORT_TEST` | tests/** |
| 816 | `tests/test_tui_rpc_image_attach.py` | `d4d8c325f266ea6c58de4f0e117f1741eaf43fd6` | blob | 8307 | `PORT_TEST` | tests/** |
| 817 | `tests/test_tui_rpc_message_tool_route.py` | `239a5885b44900a2b3bb1971ec9cc39cce8cce3c` | blob | 8986 | `PORT_TEST` | tests/** |
| 818 | `tests/test_tui_rpc_model.py` | `d33075e18d178d27fdd35c64dc51d711ebcb4766` | blob | 12217 | `PORT_TEST` | tests/** |
| 819 | `tests/test_tui_rpc_reasoning_render.py` | `e5a52e6e20e4cf6c76ac7eb36739b312bb4d8581` | blob | 4968 | `PORT_TEST` | tests/** |
| 820 | `tests/test_tui_rpc_server_socket.py` | `e3c5f60031290edb912767fceae892aaf3f04d1e` | blob | 9550 | `PORT_TEST` | tests/** |
| 821 | `tests/test_tui_rpc_session_init_bundle.py` | `29d5377e7c5f1a7035e467ff61cc793de8467e9a` | blob | 11678 | `PORT_TEST` | tests/** |
| 822 | `tests/test_tui_rpc_session.py` | `f2433d6656d26ea80293ad503f2a1a6b0bb5cfc8` | blob | 69338 | `PORT_TEST` | tests/** |
| 823 | `tests/test_tui_rpc_setup.py` | `018a02dd462a68848e3a81f375b615bc45e671b0` | blob | 3013 | `PORT_TEST` | tests/** |
| 824 | `tests/test_tui_rpc_spine.py` | `c75f21aada659f1f8f77f1ff9186eff07402c834` | blob | 28024 | `PORT_TEST` | tests/** |
| 825 | `tests/test_tui_rpc_system.py` | `92efb1d1b5fe07bbd88151e0d77839523db03f91` | blob | 5167 | `PORT_TEST` | tests/** |
| 826 | `tests/test_tui_rpc_terminal.py` | `33c7fdbfd4bf97b53a0b8c0043c85423ef9b209f` | blob | 2523 | `PORT_TEST` | tests/** |
| 827 | `tests/test_tui_rpc_tool_events.py` | `3570bfe3d7b75c72caa6090c66afa95119dcd287` | blob | 6922 | `PORT_TEST` | tests/** |
| 828 | `tests/test_tui_rpc_turn_cancel.py` | `ad4f6b71cfe43728aeaad4398399be391b01f3e1` | blob | 6755 | `PORT_TEST` | tests/** |
| 829 | `tests/test_tui_rpc_turn_send.py` | `301b48e1e58a43b9adfcbf82f2e3d6da581a4948` | blob | 11294 | `PORT_TEST` | tests/** |
| 830 | `tests/test_tui_rpc_turn_subscribe.py` | `fbad44f786132f767ad05f5eacf59f4b132f4fe2` | blob | 5015 | `PORT_TEST` | tests/** |
| 831 | `tests/test_tui_turn_logging.py` | `193b0dfac6b834b979622fe0f2942a7a7994af7d` | blob | 5853 | `PORT_TEST` | tests/** |
| 832 | `tests/test_turn_evidence_correlation.py` | `0950276d91a805fcfe4e6c6ddfdcd14363f98a8a` | blob | 11947 | `PORT_TEST` | tests/** |
| 833 | `tests/test_turn_evidence_scenario.py` | `ecd30f3cc502001be3576496a55add358cf747d2` | blob | 9008 | `PORT_TEST` | tests/** |
| 834 | `tests/test_turn_wire_shape_conformance.py` | `4ec3abb449e2feece3a55c1f21589fdfa6d78c19` | blob | 7969 | `PORT_TEST` | tests/** |
| 835 | `tests/test_verify_channels.py` | `0895ec141b4b3f77b7270d478a3e2d67a3e426d6` | blob | 3085 | `PORT_TEST` | tests/** |
| 836 | `tests/test_verify_distribution.py` | `680b98e54aed5f43e5feae2befdfb2a643603682` | blob | 45949 | `PORT_TEST` | tests/** |
| 837 | `tests/test_verify_turn_evidence.py` | `d90b924a444dd0c03c8e04b185e5ace0a1c14788` | blob | 18382 | `PORT_TEST` | tests/** |
| 838 | `tests/tui/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_TEST` | tests/** |
| 839 | `tests/tui/autotest/__init__.py` | `94b0d11f215cc96d23b83894bc5ce1600ac1d2ab` | blob | 51 | `PORT_TEST` | tests/** |
| 840 | `tests/tui/autotest/__main__.py` | `dbdd066172160ef2d47b29f0caa00e27c62ebc20` | blob | 83 | `PORT_TEST` | tests/** |
| 841 | `tests/tui/autotest/cli.py` | `47ee0fc0a2087a4a066b1dc957e2a8bc752d8a4d` | blob | 5255 | `PORT_TEST` | tests/** |
| 842 | `tests/tui/autotest/runner.py` | `ebb70609bc93f283fbcf7fd224250f3a03d70890` | blob | 8142 | `PORT_TEST` | tests/** |
| 843 | `tests/tui/autotest/tests/__init__.py` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | blob | 0 | `PORT_TEST` | tests/** |
| 844 | `tests/tui/autotest/tests/conftest.py` | `dee91f4a016ba05c66057664148ae178d0276a27` | blob | 839 | `PORT_TEST` | tests/** |
| 845 | `tests/tui/autotest/tests/test_cli_smoke.py` | `087ead04925c7794ed183265f6cfca1ab0d3f964` | blob | 1994 | `PORT_TEST` | tests/** |
| 846 | `tests/tui/autotest/tests/test_dogfood_whitelist.py` | `230233b3622f99925c6ab24d13f6b5f6e7f6396a` | blob | 1469 | `PORT_TEST` | tests/** |
| 847 | `tests/tui/autotest/tests/test_e2e_cheap_subprocess.py` | `1ab9853af1e280ded3cfb0517c702b8c293483d5` | blob | 535 | `PORT_TEST` | tests/** |
| 848 | `tests/tui/autotest/tests/test_e2e_ctrl_c.py` | `2eb2a6a0abb190df99b4831b4a0d6166b293c851` | blob | 1265 | `PORT_TEST` | tests/** |
| 849 | `tests/tui/autotest/tests/test_e2e_pico_tui_chat.py` | `1c6d6c8cde3ad7c92bc4c428fd42aabfedab525f` | blob | 3405 | `PORT_TEST` | tests/** |
| 850 | `tests/tui/autotest/tests/test_e2e_pico_tui_check.py` | `2f58967cfeaee98c4435b8b1212ebff0c64c296a` | blob | 483 | `PORT_TEST` | tests/** |
| 851 | `tests/tui/autotest/tests/test_e2e_streaming_no_log_overlay.py` | `ee84b03761d7474f42acb5322527bebe2a706ce3` | blob | 2750 | `PORT_TEST` | tests/** |
| 852 | `tests/tui/autotest/tests/test_e2e_tui_status_slash.py` | `dd50b4db25d24f3c4206f2c5eeeb859c4df0a973` | blob | 1504 | `PORT_TEST` | tests/** |
| 853 | `tests/tui/autotest/tests/test_harness_api_unit.py` | `d55bce0825e4d7dec89717351b88ed029ce79240` | blob | 10529 | `PORT_TEST` | tests/** |
| 854 | `ui-tui/.gitignore` | `9b578a6abeaf3a56967b4a60a51f3162206f30f5` | blob | 146 | `PORT_UI` | ui-tui/** |
| 855 | `ui-tui/.prettierignore` | `f8c575c43ad3463581ca1361f65ddced77056d9a` | blob | 59 | `PORT_UI` | ui-tui/** |
| 856 | `ui-tui/babel.compiler.config.cjs` | `18f2a7aaa424f900356db511a945a8e8e8a2f299` | blob | 281 | `PORT_UI` | ui-tui/** |
| 857 | `ui-tui/eslint.config.js` | `976a33e8a71f66fac9574b5c5122f8f3522f92fe` | blob | 1273 | `PORT_UI` | ui-tui/** |
| 858 | `ui-tui/package-lock.json` | `c94003ce96b3e55eefd99556b2c035ccae283abf` | blob | 286536 | `PORT_UI` | ui-tui/** |
| 859 | `ui-tui/package.json` | `118937985a2b1dfc6476bcf69283d9f4273e8912` | blob | 2228 | `PORT_UI` | ui-tui/** |
| 860 | `ui-tui/packages/hermes-ink/ambient.d.ts` | `943ff76bc0176976b2ef952b09509dfd68ec9cf9` | blob | 2705 | `PORT_UI` | ui-tui/** |
| 861 | `ui-tui/packages/hermes-ink/index.d.ts` | `5fc0206bf54af476d2603306761a49bf7ddb6c70` | blob | 2877 | `PORT_UI` | ui-tui/** |
| 862 | `ui-tui/packages/hermes-ink/index.js` | `8c0fa9c5b500faaae5e07a13db88dcb88d1e1066` | blob | 40 | `PORT_UI` | ui-tui/** |
| 863 | `ui-tui/packages/hermes-ink/package-lock.json` | `fce9c322c61538951991f877e5fae8a805506cd2` | blob | 41443 | `PORT_UI` | ui-tui/** |
| 864 | `ui-tui/packages/hermes-ink/package.json` | `8df3c02a4a501a350acafdbd1189dd89b244cc8e` | blob | 1356 | `PORT_UI` | ui-tui/** |
| 865 | `ui-tui/packages/hermes-ink/src/bootstrap/state.ts` | `dcbae499fc3a083e42cd4ebb18264bc8e6bfe7c1` | blob | 255 | `PORT_UI` | ui-tui/** |
| 866 | `ui-tui/packages/hermes-ink/src/entry-exports.ts` | `3b502cacc177957e4cd5f262f8c4c83f8ea69528` | blob | 2068 | `PORT_UI` | ui-tui/** |
| 867 | `ui-tui/packages/hermes-ink/src/hooks/use-stderr.ts` | `0aa7e1f20a2ec9d9921d4abd0975b67f6da2645c` | blob | 310 | `PORT_UI` | ui-tui/** |
| 868 | `ui-tui/packages/hermes-ink/src/hooks/use-stdout.ts` | `fde397af2b1b964aaf797c7e806936820f03eeeb` | blob | 310 | `PORT_UI` | ui-tui/** |
| 869 | `ui-tui/packages/hermes-ink/src/ink/Ansi.tsx` | `ea8f3946208352caf9d25f7df482a56343ba4003` | blob | 34397 | `PORT_UI` | ui-tui/** |
| 870 | `ui-tui/packages/hermes-ink/src/ink/bidi.ts` | `d70113d3f2688a36e19fff3f8f2043d369f97c74` | blob | 4589 | `PORT_UI` | ui-tui/** |
| 871 | `ui-tui/packages/hermes-ink/src/ink/cache-eviction.ts` | `f0155eb9b0d2c4d282dbf4d76f874aa11eba30b3` | blob | 1386 | `PORT_UI` | ui-tui/** |
| 872 | `ui-tui/packages/hermes-ink/src/ink/clearTerminal.ts` | `83614b58d339b899d48144d59514c8eed82418f5` | blob | 2173 | `PORT_UI` | ui-tui/** |
| 873 | `ui-tui/packages/hermes-ink/src/ink/colorize.test.ts` | `ef645c3b044a2ee42de10b3b5fc910f12257c489` | blob | 2547 | `PORT_UI` | ui-tui/** |
| 874 | `ui-tui/packages/hermes-ink/src/ink/colorize.ts` | `4cb1f72f343ca58880bfa1bdb5d4a915ec18d766` | blob | 9870 | `PORT_UI` | ui-tui/** |
| 875 | `ui-tui/packages/hermes-ink/src/ink/components/AlternateScreen.tsx` | `783cb2d9d265c84ab02485922779a0f34552a4ae` | blob | 10855 | `PORT_UI` | ui-tui/** |
| 876 | `ui-tui/packages/hermes-ink/src/ink/components/App.tsx` | `f219fde2b2a76f999f9b2dd2bfcbfd0e69e1b9a7` | blob | 103156 | `PORT_UI` | ui-tui/** |
| 877 | `ui-tui/packages/hermes-ink/src/ink/components/AppContext.ts` | `3d13e779ccadb20773ed428db9e1079bfae76141` | blob | 391 | `PORT_UI` | ui-tui/** |
| 878 | `ui-tui/packages/hermes-ink/src/ink/components/Box.tsx` | `7a61aeb75d70fd9affeaf7e2317ed3481085ebf1` | blob | 22832 | `PORT_UI` | ui-tui/** |
| 879 | `ui-tui/packages/hermes-ink/src/ink/components/Button.tsx` | `0b93cf13dbc3f928772afe7f5b99912d3a98b4da` | blob | 16645 | `PORT_UI` | ui-tui/** |
| 880 | `ui-tui/packages/hermes-ink/src/ink/components/ClockContext.tsx` | `bf8006d38bc053b0905f3119084905305db78384` | blob | 12383 | `PORT_UI` | ui-tui/** |
| 881 | `ui-tui/packages/hermes-ink/src/ink/components/CursorDeclarationContext.ts` | `37356afa170a83327bc426d1a4f19aa98fb69949` | blob | 1108 | `PORT_UI` | ui-tui/** |
| 882 | `ui-tui/packages/hermes-ink/src/ink/components/ErrorOverview.tsx` | `22ef3b0660e7cb69d9cdabeca945a1abd9852ccd` | blob | 15681 | `PORT_UI` | ui-tui/** |
| 883 | `ui-tui/packages/hermes-ink/src/ink/components/Link.tsx` | `26b9bf341f899851e983d458abe4dbe190db362f` | blob | 3867 | `PORT_UI` | ui-tui/** |
| 884 | `ui-tui/packages/hermes-ink/src/ink/components/Newline.tsx` | `4010dc9ffd3c36254997624a3010a18d9e311ccd` | blob | 2346 | `PORT_UI` | ui-tui/** |
| 885 | `ui-tui/packages/hermes-ink/src/ink/components/NoSelect.tsx` | `cdab4bc626c0ea20ad31f7f651f0601a471b727e` | blob | 6161 | `PORT_UI` | ui-tui/** |
| 886 | `ui-tui/packages/hermes-ink/src/ink/components/RawAnsi.tsx` | `28ce69a346635cfb135bbf302fbf3b00c0d1493c` | blob | 5435 | `PORT_UI` | ui-tui/** |
| 887 | `ui-tui/packages/hermes-ink/src/ink/components/ScrollBox.tsx` | `1a6d8a3f53f755cdee5e89041c9e72033db62937` | blob | 32525 | `PORT_UI` | ui-tui/** |
| 888 | `ui-tui/packages/hermes-ink/src/ink/components/Spacer.tsx` | `3ed7609b84c1225bb0ec9228938cbdbba890eaf1` | blob | 1558 | `PORT_UI` | ui-tui/** |
| 889 | `ui-tui/packages/hermes-ink/src/ink/components/StdinContext.ts` | `c6e9334dfa28e3f8a927f84e01b42b306431ffef` | blob | 678 | `PORT_UI` | ui-tui/** |
| 890 | `ui-tui/packages/hermes-ink/src/ink/components/TerminalFocusContext.tsx` | `e46c6322918f31ddabc28709dd84d5ce1e994d1a` | blob | 6207 | `PORT_UI` | ui-tui/** |
| 891 | `ui-tui/packages/hermes-ink/src/ink/components/TerminalSizeContext.tsx` | `ec743b3a0ecf538b69d0eb542b39203888467707` | blob | 979 | `PORT_UI` | ui-tui/** |
| 892 | `ui-tui/packages/hermes-ink/src/ink/components/Text.test.ts` | `50628d5380dc90cba6a69975b8fc563f757727d5` | blob | 1697 | `PORT_UI` | ui-tui/** |
| 893 | `ui-tui/packages/hermes-ink/src/ink/components/Text.tsx` | `19f4b6a778aba05b06bf4385f4ff2312b24934ed` | blob | 18305 | `PORT_UI` | ui-tui/** |
| 894 | `ui-tui/packages/hermes-ink/src/ink/constants.ts` | `1846997c0cb0507f542c4ebebf3a3638cb540548` | blob | 311 | `PORT_UI` | ui-tui/** |
| 895 | `ui-tui/packages/hermes-ink/src/ink/cursor.ts` | `fd3781671251c741b163b638cee69601d6f31c8f` | blob | 68 | `PORT_UI` | ui-tui/** |
| 896 | `ui-tui/packages/hermes-ink/src/ink/devtools.ts` | `73b0c9448d471173a1c08d9d7aa474f06f92698c` | blob | 70 | `PORT_UI` | ui-tui/** |
| 897 | `ui-tui/packages/hermes-ink/src/ink/dom.ts` | `6602167bca6f7561d12780b5637c3a594ecfae32` | blob | 15510 | `PORT_UI` | ui-tui/** |
| 898 | `ui-tui/packages/hermes-ink/src/ink/events/click-event.ts` | `1f58659a89bb7c5d7e8e24f875426ca959edc550` | blob | 1332 | `PORT_UI` | ui-tui/** |
| 899 | `ui-tui/packages/hermes-ink/src/ink/events/cmd-shortcuts.test.ts` | `3527e0a7e67cea4410423f604a844d6570052cf8` | blob | 2478 | `PORT_UI` | ui-tui/** |
| 900 | `ui-tui/packages/hermes-ink/src/ink/events/dispatcher.ts` | `13b278e3c45d8868c9cca27581a5b66424f68294` | blob | 6281 | `PORT_UI` | ui-tui/** |
| 901 | `ui-tui/packages/hermes-ink/src/ink/events/emitter.ts` | `d00c4d9e3c9df75f308011e54cffae288488549d` | blob | 1126 | `PORT_UI` | ui-tui/** |
| 902 | `ui-tui/packages/hermes-ink/src/ink/events/event-handlers.ts` | `9bdf51cf4fe74d1ac8096714fad332bedd06c2ca` | blob | 2863 | `PORT_UI` | ui-tui/** |
| 903 | `ui-tui/packages/hermes-ink/src/ink/events/event.ts` | `61874002ebbdb476ffe9a2a0db8001ec6aefb178` | blob | 250 | `PORT_UI` | ui-tui/** |
| 904 | `ui-tui/packages/hermes-ink/src/ink/events/focus-event.ts` | `527fd26d22a40d9a5a259cd9ed1daa414bdf723f` | blob | 674 | `PORT_UI` | ui-tui/** |
| 905 | `ui-tui/packages/hermes-ink/src/ink/events/input-event.ts` | `eae8bd745225bc85b7ef0a1ab37a6c86403c9cc4` | blob | 7264 | `PORT_UI` | ui-tui/** |
| 906 | `ui-tui/packages/hermes-ink/src/ink/events/keyboard-event.ts` | `d77eca0efea37c00f434173df876c49286ee570a` | blob | 2085 | `PORT_UI` | ui-tui/** |
| 907 | `ui-tui/packages/hermes-ink/src/ink/events/mouse-event.ts` | `d42839b5fb59897d4b95db087f1d7cd8c58b35b5` | blob | 407 | `PORT_UI` | ui-tui/** |
| 908 | `ui-tui/packages/hermes-ink/src/ink/events/paste-event.ts` | `38a88f3171f081dd81658f93e40af9264f060ab0` | blob | 239 | `PORT_UI` | ui-tui/** |
| 909 | `ui-tui/packages/hermes-ink/src/ink/events/resize-event.ts` | `b2627bb290f7201bd085c07ae0b5108c19575fce` | blob | 312 | `PORT_UI` | ui-tui/** |
| 910 | `ui-tui/packages/hermes-ink/src/ink/events/terminal-event.ts` | `6bb374320bf469472689156dfd88484cd3a2515a` | blob | 2820 | `PORT_UI` | ui-tui/** |
| 911 | `ui-tui/packages/hermes-ink/src/ink/events/terminal-focus-event.ts` | `6d0303fdb48c824d9ca7b104d0180ec7f9a5b0e8` | blob | 512 | `PORT_UI` | ui-tui/** |
| 912 | `ui-tui/packages/hermes-ink/src/ink/focus.ts` | `155e67f8b7758257d7afcfc448e8c8cda2789ddb` | blob | 5586 | `PORT_UI` | ui-tui/** |
| 913 | `ui-tui/packages/hermes-ink/src/ink/frame.ts` | `66808c256604a83bae0f215f2d31d8038a4a0f3f` | blob | 4812 | `PORT_UI` | ui-tui/** |
| 914 | `ui-tui/packages/hermes-ink/src/ink/get-max-width.ts` | `e079463748afb8e44f053e3e8a1d80f1a8a88089` | blob | 1149 | `PORT_UI` | ui-tui/** |
| 915 | `ui-tui/packages/hermes-ink/src/ink/global.d.ts` | `336ce12bb9106afdf843063ee67c0c1970f70d37` | blob | 10 | `PORT_UI` | ui-tui/** |
| 916 | `ui-tui/packages/hermes-ink/src/ink/hit-test.ts` | `0ac820f05bb971e94107f3650a99d9a768a95652` | blob | 5572 | `PORT_UI` | ui-tui/** |
| 917 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-animation-frame.ts` | `0a86106b7ecc61183790574aaed33caf492de637` | blob | 2243 | `PORT_UI` | ui-tui/** |
| 918 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-app.ts` | `9c06032448d46c072804a65deca8560f436e3b6a` | blob | 252 | `PORT_UI` | ui-tui/** |
| 919 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-declared-cursor.ts` | `51a13652e18d22602ab91f30f961b24b3d754d20` | blob | 3291 | `PORT_UI` | ui-tui/** |
| 920 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-external-process.ts` | `c895edeb218144a477c46280f65070e6a1423c2e` | blob | 572 | `PORT_UI` | ui-tui/** |
| 921 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-input.ts` | `2e4a99fb0e4ec4a54341da4bf03097ff33bf2205` | blob | 3350 | `PORT_UI` | ui-tui/** |
| 922 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-interval.ts` | `2d0cc2d664db7d2f9d25ceadd97c29303af5986a` | blob | 2114 | `PORT_UI` | ui-tui/** |
| 923 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-search-highlight.ts` | `34d3fb4e4572107e75c2a8504492f102ce7ab630` | blob | 2452 | `PORT_UI` | ui-tui/** |
| 924 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-selection.ts` | `747279abb9a95cf392f9c287178126b57e692277` | blob | 4864 | `PORT_UI` | ui-tui/** |
| 925 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-stdin.ts` | `58cf746f5774c40c7f2feb4cecafa35ccbe2e5ab` | blob | 233 | `PORT_UI` | ui-tui/** |
| 926 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-tab-status.ts` | `43b372df0bcdb447fb30f68ca03db7407c2a1387` | blob | 2468 | `PORT_UI` | ui-tui/** |
| 927 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-terminal-focus.ts` | `230d87a39f4d115aca1f3197a709f6aa45d9cbbf` | blob | 558 | `PORT_UI` | ui-tui/** |
| 928 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-terminal-title.ts` | `6b5b28f5c3e9e453e71810eb1c0f109591cc4123` | blob | 1035 | `PORT_UI` | ui-tui/** |
| 929 | `ui-tui/packages/hermes-ink/src/ink/hooks/use-terminal-viewport.ts` | `9097422d5d8b34e0c48a1e8b694762a7fdaa3f6e` | blob | 4287 | `PORT_UI` | ui-tui/** |
| 930 | `ui-tui/packages/hermes-ink/src/ink/ink.tsx` | `55ce9be73a91899a0c985581f595b3d0cedfe53b` | blob | 262460 | `PORT_UI` | ui-tui/** |
| 931 | `ui-tui/packages/hermes-ink/src/ink/instances.ts` | `389384a8d47ce1c15b22bf3e9afa534c61fe8a1c` | blob | 410 | `PORT_UI` | ui-tui/** |
| 932 | `ui-tui/packages/hermes-ink/src/ink/layout/engine.ts` | `38f6dcb0fb5614d423f9a59cedb31d696ddeeef6` | blob | 177 | `PORT_UI` | ui-tui/** |
| 933 | `ui-tui/packages/hermes-ink/src/ink/layout/geometry.ts` | `fbca14c88000619e6198a7d5a5cf493c009666f7` | blob | 2756 | `PORT_UI` | ui-tui/** |
| 934 | `ui-tui/packages/hermes-ink/src/ink/layout/node.ts` | `b98af729210bbdb5d40bf36d715af442aed61fb0` | blob | 4615 | `PORT_UI` | ui-tui/** |
| 935 | `ui-tui/packages/hermes-ink/src/ink/layout/yoga.ts` | `0912e09400230bd2530238ae089cb6f8baa99452` | blob | 7670 | `PORT_UI` | ui-tui/** |
| 936 | `ui-tui/packages/hermes-ink/src/ink/line-width-cache.ts` | `71b02b62268fd2081112bff15ff21479eaa37171` | blob | 874 | `PORT_UI` | ui-tui/** |
| 937 | `ui-tui/packages/hermes-ink/src/ink/log-update.test.ts` | `172d01efbe3a05282cedc889556fdfd8a7d06dc2` | blob | 5711 | `PORT_UI` | ui-tui/** |
| 938 | `ui-tui/packages/hermes-ink/src/ink/log-update.ts` | `4f5599ba5b1832f1f9d35a742506284a21e793da` | blob | 27265 | `PORT_UI` | ui-tui/** |
| 939 | `ui-tui/packages/hermes-ink/src/ink/lru.ts` | `cd119b5f00340f2e75a0d03de7e6b69221457752` | blob | 463 | `PORT_UI` | ui-tui/** |
| 940 | `ui-tui/packages/hermes-ink/src/ink/measure-element.ts` | `64124d6ec21ffadb861813e2027d9b802f86f070` | blob | 418 | `PORT_UI` | ui-tui/** |
| 941 | `ui-tui/packages/hermes-ink/src/ink/measure-text.ts` | `ea160b2e0518fdbf9bb8a7ba26bdd8358dd0f24a` | blob | 1446 | `PORT_UI` | ui-tui/** |
| 942 | `ui-tui/packages/hermes-ink/src/ink/node-cache.ts` | `42bb63638b879765d76a4ce9a3cc90d0eafac8bd` | blob | 1942 | `PORT_UI` | ui-tui/** |
| 943 | `ui-tui/packages/hermes-ink/src/ink/optimizer.ts` | `09ab05fc02fdf0b7683093f5a31b64470c31d32a` | blob | 2907 | `PORT_UI` | ui-tui/** |
| 944 | `ui-tui/packages/hermes-ink/src/ink/output.ts` | `b717c45872875921a10ef42db054737c9a92a982` | blob | 27085 | `PORT_UI` | ui-tui/** |
| 945 | `ui-tui/packages/hermes-ink/src/ink/parse-keypress.test.ts` | `7291eab22eb5def03ff4a4218227abcac7c4afd4` | blob | 9856 | `PORT_UI` | ui-tui/** |
| 946 | `ui-tui/packages/hermes-ink/src/ink/parse-keypress.ts` | `003a64573667d022ad8411b6a94bc4bd3c2dd61d` | blob | 25632 | `PORT_UI` | ui-tui/** |
| 947 | `ui-tui/packages/hermes-ink/src/ink/reconciler.ts` | `11e8306cb58eb6c7fdd90570775b4d6bb5768035` | blob | 10345 | `PORT_UI` | ui-tui/** |
| 948 | `ui-tui/packages/hermes-ink/src/ink/render-border.ts` | `c492f72f9dbe959223b9ba3129987e3ca1ce6293` | blob | 6731 | `PORT_UI` | ui-tui/** |
| 949 | `ui-tui/packages/hermes-ink/src/ink/render-node-to-output.ts` | `2c57e73621678b4ffc6b5f6f055021b7fb68e23a` | blob | 63960 | `PORT_UI` | ui-tui/** |
| 950 | `ui-tui/packages/hermes-ink/src/ink/render-to-screen.ts` | `55ee56d026da06d3115bb161139005f27b077c3b` | blob | 8485 | `PORT_UI` | ui-tui/** |
| 951 | `ui-tui/packages/hermes-ink/src/ink/renderer.ts` | `ab6c2d65c3aa6d10939d95eccaab681def4cde5c` | blob | 7884 | `PORT_UI` | ui-tui/** |
| 952 | `ui-tui/packages/hermes-ink/src/ink/root.ts` | `918a4c8f1e8fe3e84dbbe2dbd6eb04873872fa55` | blob | 5058 | `PORT_UI` | ui-tui/** |
| 953 | `ui-tui/packages/hermes-ink/src/ink/screen.ts` | `376bccdded4b5fda02bba2ad04efd014222e64f0` | blob | 51503 | `PORT_UI` | ui-tui/** |
| 954 | `ui-tui/packages/hermes-ink/src/ink/searchHighlight.ts` | `229417243aa54671b200967ab4e24a9402139f0d` | blob | 3587 | `PORT_UI` | ui-tui/** |
| 955 | `ui-tui/packages/hermes-ink/src/ink/selection.test.ts` | `5554ceb68481d9762dcccd14d50f502d52d424b5` | blob | 3335 | `PORT_UI` | ui-tui/** |
| 956 | `ui-tui/packages/hermes-ink/src/ink/selection.ts` | `744f7b21009e81e22a68bafdf21e03edce26e4ca` | blob | 37584 | `PORT_UI` | ui-tui/** |
| 957 | `ui-tui/packages/hermes-ink/src/ink/squash-text-nodes.ts` | `8d3d455a4942e3b0671e1b17595f3991f621382c` | blob | 2459 | `PORT_UI` | ui-tui/** |
| 958 | `ui-tui/packages/hermes-ink/src/ink/stringWidth.ts` | `b18eebec1553f432084ce2e6bf7fb90894c08d69` | blob | 9287 | `PORT_UI` | ui-tui/** |
| 959 | `ui-tui/packages/hermes-ink/src/ink/styles.ts` | `d2d00ce0080ae09e8b5f4c187dbdb637f6fca54c` | blob | 21056 | `PORT_UI` | ui-tui/** |
| 960 | `ui-tui/packages/hermes-ink/src/ink/supports-hyperlinks.ts` | `7853e5f913f35e5b6066f52fcde3de7b031f01b3` | blob | 1870 | `PORT_UI` | ui-tui/** |
| 961 | `ui-tui/packages/hermes-ink/src/ink/tabstops.ts` | `9b6007b101d252da0a4c23e5477fd3a992f1a9e3` | blob | 1107 | `PORT_UI` | ui-tui/** |
| 962 | `ui-tui/packages/hermes-ink/src/ink/terminal-focus-state.ts` | `188ba80d47366bbd0a035eabc670b6faac18ee9c` | blob | 1604 | `PORT_UI` | ui-tui/** |
| 963 | `ui-tui/packages/hermes-ink/src/ink/terminal-querier.test.ts` | `f65f83cd5142d5227625f81a0c3de6e49753a837` | blob | 1585 | `PORT_UI` | ui-tui/** |
| 964 | `ui-tui/packages/hermes-ink/src/ink/terminal-querier.ts` | `7b8ac33b16e94925600c2abb3328dbbf3a68edd0` | blob | 9269 | `PORT_UI` | ui-tui/** |
| 965 | `ui-tui/packages/hermes-ink/src/ink/terminal.test.ts` | `172dc3f654636bc2d38f76fdac014227732849f1` | blob | 2910 | `PORT_UI` | ui-tui/** |
| 966 | `ui-tui/packages/hermes-ink/src/ink/terminal.ts` | `bd8c33d2db9a3f209ec7a4093499f1a52bbce70f` | blob | 10784 | `PORT_UI` | ui-tui/** |
| 967 | `ui-tui/packages/hermes-ink/src/ink/termio.ts` | `e14db928cbf3494db5e56906bd734ebbb247fbcd` | blob | 1035 | `PORT_UI` | ui-tui/** |
| 968 | `ui-tui/packages/hermes-ink/src/ink/termio/ansi.ts` | `c3f8aa919e64f9b5cb51780431b327c0dea54923` | blob | 1782 | `PORT_UI` | ui-tui/** |
| 969 | `ui-tui/packages/hermes-ink/src/ink/termio/csi.ts` | `3c8f11261f9ba4af29ea569ad07ca6f6b9ebf1f2` | blob | 8999 | `PORT_UI` | ui-tui/** |
| 970 | `ui-tui/packages/hermes-ink/src/ink/termio/dec.ts` | `628fe89298141c82563b23c5ae896af3cac4f9c9` | blob | 2216 | `PORT_UI` | ui-tui/** |
| 971 | `ui-tui/packages/hermes-ink/src/ink/termio/esc.ts` | `951f6c250bde07b1c7393599e0b1364a9d9c330f` | blob | 1746 | `PORT_UI` | ui-tui/** |
| 972 | `ui-tui/packages/hermes-ink/src/ink/termio/osc.test.ts` | `7cb3d4f9e758e9403f9f42f1d2d894dd4763e98a` | blob | 10353 | `PORT_UI` | ui-tui/** |
| 973 | `ui-tui/packages/hermes-ink/src/ink/termio/osc.ts` | `0949ab75ccdd700a01fe0ebbc94a5786eba0013d` | blob | 25478 | `PORT_UI` | ui-tui/** |
| 974 | `ui-tui/packages/hermes-ink/src/ink/termio/parser.ts` | `72f31a056f8aaaa47cb0554d6838734223bb88c0` | blob | 12013 | `PORT_UI` | ui-tui/** |
| 975 | `ui-tui/packages/hermes-ink/src/ink/termio/sgr.ts` | `70cc4046ef98089ffb2be213380864fd3453bf7b` | blob | 6647 | `PORT_UI` | ui-tui/** |
| 976 | `ui-tui/packages/hermes-ink/src/ink/termio/tokenize.ts` | `998dfa428c338f1f71f0450c1c90cc03b028ee16` | blob | 9455 | `PORT_UI` | ui-tui/** |
| 977 | `ui-tui/packages/hermes-ink/src/ink/termio/types.ts` | `dc6514789feb8638147db192932cf237e8b47043` | blob | 7329 | `PORT_UI` | ui-tui/** |
| 978 | `ui-tui/packages/hermes-ink/src/ink/useTerminalNotification.ts` | `0b97877d0076ef594a36560ee85d52ca29eb2bf8` | blob | 3842 | `PORT_UI` | ui-tui/** |
| 979 | `ui-tui/packages/hermes-ink/src/ink/warn.ts` | `016b4ecd2b47eb360eedb84bb6473add3ed65018` | blob | 316 | `PORT_UI` | ui-tui/** |
| 980 | `ui-tui/packages/hermes-ink/src/ink/widest-line.ts` | `ac78cb6d5ac77360dbf05d6d73d2bab8c5be638b` | blob | 444 | `PORT_UI` | ui-tui/** |
| 981 | `ui-tui/packages/hermes-ink/src/ink/wrap-text.test.ts` | `8ccc31d9c9615636444620ee0f71f4f8c09f23ce` | blob | 548 | `PORT_UI` | ui-tui/** |
| 982 | `ui-tui/packages/hermes-ink/src/ink/wrap-text.ts` | `835492041ec1dfe6b7aaa53039aedc3f245ecc9f` | blob | 4459 | `PORT_UI` | ui-tui/** |
| 983 | `ui-tui/packages/hermes-ink/src/ink/wrapAnsi.ts` | `61b56dbf3f130bdec17bd066b9572445d4cb7a43` | blob | 364 | `PORT_UI` | ui-tui/** |
| 984 | `ui-tui/packages/hermes-ink/src/native-ts/yoga-layout/enums.ts` | `07d40179728e38fdfabcacfe752cb2d313dcfe99` | blob | 2887 | `PORT_UI` | ui-tui/** |
| 985 | `ui-tui/packages/hermes-ink/src/native-ts/yoga-layout/index.ts` | `f0550f87e2af1df2a589878a3d51cc3d03c12793` | blob | 60138 | `PORT_UI` | ui-tui/** |
| 986 | `ui-tui/packages/hermes-ink/src/utils/debug.ts` | `285a07ac1b72b04278f68387000211a01ad1e6a0` | blob | 106 | `PORT_UI` | ui-tui/** |
| 987 | `ui-tui/packages/hermes-ink/src/utils/earlyInput.ts` | `448f63290bb8bd4a293872f665db367ee467207c` | blob | 2738 | `PORT_UI` | ui-tui/** |
| 988 | `ui-tui/packages/hermes-ink/src/utils/env.ts` | `5662a138b7c38b49a8b7953a730086fa6680670e` | blob | 2486 | `PORT_UI` | ui-tui/** |
| 989 | `ui-tui/packages/hermes-ink/src/utils/envUtils.ts` | `f3286197b53957a6207a013f25a701fe66c128d9` | blob | 267 | `PORT_UI` | ui-tui/** |
| 990 | `ui-tui/packages/hermes-ink/src/utils/execFileNoThrow.ts` | `8f97008ac7592aff601e9db2ea6ee089ad0e22e5` | blob | 1613 | `PORT_UI` | ui-tui/** |
| 991 | `ui-tui/packages/hermes-ink/src/utils/fullscreen.ts` | `523a43102b5a4e58d18b16a9635283929e36559a` | blob | 161 | `PORT_UI` | ui-tui/** |
| 992 | `ui-tui/packages/hermes-ink/src/utils/intl.ts` | `2d038d6131545ac76cb20f340ad0774c7c6add87` | blob | 2266 | `PORT_UI` | ui-tui/** |
| 993 | `ui-tui/packages/hermes-ink/src/utils/log.ts` | `369763eee0a714b6ee0ae0047184b70de045ad31` | blob | 136 | `PORT_UI` | ui-tui/** |
| 994 | `ui-tui/packages/hermes-ink/src/utils/semver.ts` | `1a83edeaac66cfbc5cd6b4ec6ab72b3803a31aa4` | blob | 1688 | `PORT_UI` | ui-tui/** |
| 995 | `ui-tui/packages/hermes-ink/src/utils/sliceAnsi.ts` | `228698df32650d3a7d2a3a65e92c8f8ba61ece3d` | blob | 3073 | `PORT_UI` | ui-tui/** |
| 996 | `ui-tui/packages/hermes-ink/text-input.d.ts` | `f9f5df1c8d80e80733b804b64a4efa2e0e644d07` | blob | 108 | `PORT_UI` | ui-tui/** |
| 997 | `ui-tui/packages/hermes-ink/text-input.js` | `8cb79c0ccb5df6abf3cc9f2e9e5e9e205a428563` | blob | 64 | `PORT_UI` | ui-tui/** |
| 998 | `ui-tui/rpc-schema/openrpc.json` | `8987d0db7884279ab4c370854ea62a81a30c180d` | blob | 45283 | `PORT_UI` | ui-tui/** |
| 999 | `ui-tui/scripts/build.mjs` | `d697c26aca3437467d033d5e0397b0a89009efda` | blob | 2191 | `PORT_UI` | ui-tui/** |
| 1000 | `ui-tui/scripts/check-rpc-surface.mjs` | `9630a3fd8bcadef72ff84cfc3d44b503b875391a` | blob | 2543 | `PORT_UI` | ui-tui/** |
| 1001 | `ui-tui/scripts/gen-color-palettes.mjs` | `5a37c78d16ed849979d095c19de3146e02d13925` | blob | 5244 | `PORT_UI` | ui-tui/** |
| 1002 | `ui-tui/scripts/gen-rpc-types.mjs` | `af18c042dc01dcbc80a7ef3e53ef92c3270ee6c9` | blob | 13563 | `PORT_UI` | ui-tui/** |
| 1003 | `ui-tui/src/__tests__/branding.test.tsx` | `660ed734150b2c845ba6de79ccb426057dbd735a` | blob | 2832 | `PORT_UI` | ui-tui/** |
| 1004 | `ui-tui/src/__tests__/chatStream.test.ts` | `4ddd83253b162d842da204215102f486ba014e16` | blob | 43130 | `PORT_UI` | ui-tui/** |
| 1005 | `ui-tui/src/__tests__/clipboard.test.ts` | `fc451af410a59c65d248b17d286926b708c05675` | blob | 28711 | `PORT_UI` | ui-tui/** |
| 1006 | `ui-tui/src/__tests__/colorTier.test.ts` | `5e04ae4653f347d64aea94073f1a7a4d3cedba50` | blob | 2605 | `PORT_UI` | ui-tui/** |
| 1007 | `ui-tui/src/__tests__/confirmRoundTrip.test.ts` | `4bf997d6d3c74f9b92f1ce5afec996e00533bd72` | blob | 8689 | `PORT_UI` | ui-tui/** |
| 1008 | `ui-tui/src/__tests__/constants.test.ts` | `cdb894cb76dfe805a1b3b1a29544dbb1ecafc4dd` | blob | 2026 | `PORT_UI` | ui-tui/** |
| 1009 | `ui-tui/src/__tests__/createGatewayEventHandler.test.ts` | `6fb8c16406895f6ac2bda8d1abbc22f8b4faecea` | blob | 26405 | `PORT_UI` | ui-tui/** |
| 1010 | `ui-tui/src/__tests__/createSlashHandler.test.ts` | `87b041c9e6673fe8aa8b55bb4bbbd8506faa0bc7` | blob | 9370 | `PORT_UI` | ui-tui/** |
| 1011 | `ui-tui/src/__tests__/details.test.ts` | `e15eb040740d85030b88fc5f26f2fd940948f3e9` | blob | 4763 | `PORT_UI` | ui-tui/** |
| 1012 | `ui-tui/src/__tests__/emoji.test.ts` | `4be66357fd7f02f39dbb4bf21773a5eb74e41c45` | blob | 2719 | `PORT_UI` | ui-tui/** |
| 1013 | `ui-tui/src/__tests__/externalLink.test.ts` | `7a4963a536decd2c66a9e884a1124470b2ab6132` | blob | 5536 | `PORT_UI` | ui-tui/** |
| 1014 | `ui-tui/src/__tests__/inputHistory.test.ts` | `5054e316dcfe9349ecc67769e5d9757f61557fba` | blob | 2774 | `PORT_UI` | ui-tui/** |
| 1015 | `ui-tui/src/__tests__/markdown.test.ts` | `c5faf8cabeedb2b4f3819847cdaec65e794a7000` | blob | 11829 | `PORT_UI` | ui-tui/** |
| 1016 | `ui-tui/src/__tests__/mathUnicode.test.ts` | `ab5c7a88de84e56532b49a02a3ba7127101579d2` | blob | 11932 | `PORT_UI` | ui-tui/** |
| 1017 | `ui-tui/src/__tests__/messages.test.ts` | `7397b5177f93458df8b190e587e50cbcf94604a9` | blob | 3021 | `PORT_UI` | ui-tui/** |
| 1018 | `ui-tui/src/__tests__/modelPicker.test.tsx` | `724427a0d1c856e19ed932ff0bd4be059461e1d9` | blob | 7277 | `PORT_UI` | ui-tui/** |
| 1019 | `ui-tui/src/__tests__/osc52.test.ts` | `c3fe2ecafac887b5811bfce7210853a03d879712` | blob | 2749 | `PORT_UI` | ui-tui/** |
| 1020 | `ui-tui/src/__tests__/paths.test.ts` | `5a4eec2a89e8da2278e96606f160bbe49b8c87ae` | blob | 2968 | `PORT_UI` | ui-tui/** |
| 1021 | `ui-tui/src/__tests__/platform.test.ts` | `dabb2125c365c135698c00c3156f5214a964496a` | blob | 1773 | `PORT_UI` | ui-tui/** |
| 1022 | `ui-tui/src/__tests__/precisionWheel.test.ts` | `13567521799c09359a96da7f34894e94402286f2` | blob | 1460 | `PORT_UI` | ui-tui/** |
| 1023 | `ui-tui/src/__tests__/productPaths.test.ts` | `2c49d18fedea9b3ae582c877f69385968020d49e` | blob | 667 | `PORT_UI` | ui-tui/** |
| 1024 | `ui-tui/src/__tests__/providers.test.ts` | `733ccf8a057982f5d7f679b9f967e94846e19425` | blob | 1996 | `PORT_UI` | ui-tui/** |
| 1025 | `ui-tui/src/__tests__/reasoning.test.ts` | `2618d8833b1258fc4b7211dbbbe46022736c7b5f` | blob | 2439 | `PORT_UI` | ui-tui/** |
| 1026 | `ui-tui/src/__tests__/rpc.test.ts` | `7980093a9eea7d610f1c532c9239e837705d3c41` | blob | 827 | `PORT_UI` | ui-tui/** |
| 1027 | `ui-tui/src/__tests__/scroll.test.ts` | `243ab46455c86a40cd66942d3a8100a7c5458a55` | blob | 3095 | `PORT_UI` | ui-tui/** |
| 1028 | `ui-tui/src/__tests__/sessionManagement.test.ts` | `4007725e8a94704d313db31eb6ab1c1875c12716` | blob | 18198 | `PORT_UI` | ui-tui/** |
| 1029 | `ui-tui/src/__tests__/slashParity.test.ts` | `69ed21ad106429a1cc7b852b3d72f37ac4cc1332` | blob | 1058 | `PORT_UI` | ui-tui/** |
| 1030 | `ui-tui/src/__tests__/stateIsolation.test.ts` | `b3fdbb40712454cd89dd1692633239e93b369a4e` | blob | 1431 | `PORT_UI` | ui-tui/** |
| 1031 | `ui-tui/src/__tests__/statusBarOverlay.test.tsx` | `78f0601e3ec39491d2c396164f7e669e8172fd87` | blob | 5765 | `PORT_UI` | ui-tui/** |
| 1032 | `ui-tui/src/__tests__/statusBarTicker.test.ts` | `4f3369bfa337bb3677e5536d68c659a802c554ab` | blob | 511 | `PORT_UI` | ui-tui/** |
| 1033 | `ui-tui/src/__tests__/streamingMarkdown.test.ts` | `acce3c4214e7e3af5ab030dcbf4b0c7cdb4bb173` | blob | 4684 | `PORT_UI` | ui-tui/** |
| 1034 | `ui-tui/src/__tests__/subagentTree.test.ts` | `c1b26b169a54cbb319e2c4bb7b00ff4b8bea6446` | blob | 12272 | `PORT_UI` | ui-tui/** |
| 1035 | `ui-tui/src/__tests__/syntax.test.ts` | `5a13d447bb3d0efd872d7ef7bcace7b2a6dc1600` | blob | 1498 | `PORT_UI` | ui-tui/** |
| 1036 | `ui-tui/src/__tests__/terminalModes.test.ts` | `784a9e04cd65df678e1eb6a160e82fdcccf32e6c` | blob | 1812 | `PORT_UI` | ui-tui/** |
| 1037 | `ui-tui/src/__tests__/terminalParity.test.ts` | `1ef85cbac10496e61af7a730837676a9d74509ad` | blob | 2704 | `PORT_UI` | ui-tui/** |
| 1038 | `ui-tui/src/__tests__/terminalSetup.test.ts` | `dc354808eabe97aba42a8059fb7fb517afbaeb7f` | blob | 14541 | `PORT_UI` | ui-tui/** |
| 1039 | `ui-tui/src/__tests__/text.test.ts` | `00b1f3225cb13c5ce7e722434c3d20f905ed846f` | blob | 5611 | `PORT_UI` | ui-tui/** |
| 1040 | `ui-tui/src/__tests__/textInputIsLfReturn.test.ts` | `b06127233c9264b0f459867d02e00a77ee53bcb7` | blob | 1968 | `PORT_UI` | ui-tui/** |
| 1041 | `ui-tui/src/__tests__/textInputLineNav.test.ts` | `30b609f756142041c64e9a90794b34d5db71d0bb` | blob | 1977 | `PORT_UI` | ui-tui/** |
| 1042 | `ui-tui/src/__tests__/textInputPassThrough.test.ts` | `e6526e2522dd44eab8b27973876e9653e1ee39be` | blob | 1091 | `PORT_UI` | ui-tui/** |
| 1043 | `ui-tui/src/__tests__/textInputRightClick.test.ts` | `bf37b41223600dc019268b9d350893582ac4edca` | blob | 1479 | `PORT_UI` | ui-tui/** |
| 1044 | `ui-tui/src/__tests__/textInputWrap.test.ts` | `6cb19e9426d6920093703fbebea4c56f85871c30` | blob | 4225 | `PORT_UI` | ui-tui/** |
| 1045 | `ui-tui/src/__tests__/theme.test.ts` | `43c1f78aba57e52e48cfe20816292dd75ad7d61f` | blob | 18236 | `PORT_UI` | ui-tui/** |
| 1046 | `ui-tui/src/__tests__/todoPanel.test.tsx` | `72e5aa8d4fb0014e34f75d448d270adfefb0a0e4` | blob | 3178 | `PORT_UI` | ui-tui/** |
| 1047 | `ui-tui/src/__tests__/tuiRpcClient.test.ts` | `8dddce4f307a095a430277ba017660b2883b112e` | blob | 8810 | `PORT_UI` | ui-tui/** |
| 1048 | `ui-tui/src/__tests__/turn-subscribe.test.ts` | `14bf888a6e060e25d71ffd2f8546fb9be0e1ecf3` | blob | 12162 | `PORT_UI` | ui-tui/** |
| 1049 | `ui-tui/src/__tests__/turnStore.test.ts` | `bf926c78fa8f7ffed70092dc6c0736a4ce056bc6` | blob | 2141 | `PORT_UI` | ui-tui/** |
| 1050 | `ui-tui/src/__tests__/useCompletion.test.ts` | `15448a92587b68ff90d8924ef65a0579f6b66338` | blob | 2550 | `PORT_UI` | ui-tui/** |
| 1051 | `ui-tui/src/__tests__/useComposerState.test.ts` | `046e846bf3bde5433b35fcaf8f1c6d81c77e22f9` | blob | 2683 | `PORT_UI` | ui-tui/** |
| 1052 | `ui-tui/src/__tests__/useQueue.test.ts` | `a3f029b370f22f29ac3dc5b29de273bd4ee98e17` | blob | 1420 | `PORT_UI` | ui-tui/** |
| 1053 | `ui-tui/src/__tests__/useSessionLifecycle.test.ts` | `9243d2ade8caf2da46926e26140af68ad1b25f1e` | blob | 10141 | `PORT_UI` | ui-tui/** |
| 1054 | `ui-tui/src/__tests__/useVirtualHistoryHeights.test.ts` | `ae5658f83ebe42118f0f95fd169773a6404c72d5` | blob | 1425 | `PORT_UI` | ui-tui/** |
| 1055 | `ui-tui/src/__tests__/viewport.test.ts` | `bb3c0106bd3ce1b794e5612218d3127c815a46c8` | blob | 2283 | `PORT_UI` | ui-tui/** |
| 1056 | `ui-tui/src/__tests__/viewportStore.test.ts` | `c25f0839f01263f34a6ccb04009e0ce79142e269` | blob | 2473 | `PORT_UI` | ui-tui/** |
| 1057 | `ui-tui/src/__tests__/virtualHeights.test.ts` | `dfbb5d5cf2856693aa9bdd095c6a62905e97c53e` | blob | 1867 | `PORT_UI` | ui-tui/** |
| 1058 | `ui-tui/src/__tests__/virtualHistoryClamp.test.ts` | `d14f308d8f6265846d4a541eee92eb0b1e880808` | blob | 730 | `PORT_UI` | ui-tui/** |
| 1059 | `ui-tui/src/__tests__/virtualHistoryOffsetCache.test.ts` | `aab7e616488b85e52e2a6cf1a498f17fb19e7181` | blob | 5435 | `PORT_UI` | ui-tui/** |
| 1060 | `ui-tui/src/__tests__/wheelAccel.test.ts` | `96cd19976933dea879ad536dc83886dd9cb913a2` | blob | 3671 | `PORT_UI` | ui-tui/** |
| 1061 | `ui-tui/src/app.tsx` | `b5fa9a8772a60bca301b989cd4b0676d9282105c` | blob | 3438 | `PORT_UI` | ui-tui/** |
| 1062 | `ui-tui/src/app/chatStream.ts` | `b66ac43cb1e65399c39a5868980f3b0bf8603149` | blob | 19306 | `PORT_UI` | ui-tui/** |
| 1063 | `ui-tui/src/app/confirmResponse.ts` | `f16f0fc48a13c09ec0840cbbde1e23a5d4196330` | blob | 1294 | `PORT_UI` | ui-tui/** |
| 1064 | `ui-tui/src/app/createGatewayEventHandler.ts` | `c3c43754b50c5297e9b2db36bc627229956784b4` | blob | 14728 | `PORT_UI` | ui-tui/** |
| 1065 | `ui-tui/src/app/createSlashHandler.ts` | `7df2ba251f17f94f8435cf3ea8f47595adb2e912` | blob | 1501 | `PORT_UI` | ui-tui/** |
| 1066 | `ui-tui/src/app/delegationStore.ts` | `0ace1f6fb0a7116c6506ac90bbd9aad32fa635c6` | blob | 1767 | `PORT_UI` | ui-tui/** |
| 1067 | `ui-tui/src/app/gatewayContext.tsx` | `9187f15a3ad804c8802d8ca299c2f0e22c30f106` | blob | 521 | `PORT_UI` | ui-tui/** |
| 1068 | `ui-tui/src/app/inputSelectionStore.ts` | `c01e11861fcdfd1f1afac353be35c71b68bfbede` | blob | 386 | `PORT_UI` | ui-tui/** |
| 1069 | `ui-tui/src/app/interfaces.ts` | `3512c3ac56fac90395b6c655c41c57bf9679e38c` | blob | 11244 | `PORT_UI` | ui-tui/** |
| 1070 | `ui-tui/src/app/overlayStore.ts` | `7cf8d62f8a5f3993dda05daa3438f7286c6eab73` | blob | 1862 | `PORT_UI` | ui-tui/** |
| 1071 | `ui-tui/src/app/scroll.ts` | `ed9b26457d3b469b51d5d7140fd3ca7d7229b0af` | blob | 2311 | `PORT_UI` | ui-tui/** |
| 1072 | `ui-tui/src/app/setupHandoff.ts` | `4069123ae0d384f5928f9006758ec5d3266d4519` | blob | 1704 | `PORT_UI` | ui-tui/** |
| 1073 | `ui-tui/src/app/slash/commands/core.ts` | `a3ce56e028e7e0d78d4f39c23da48799de54a35c` | blob | 10624 | `PORT_UI` | ui-tui/** |
| 1074 | `ui-tui/src/app/slash/commands/session.ts` | `f04c0ad00113aa9f8c0856d5660b933a86d42ded` | blob | 7594 | `PORT_UI` | ui-tui/** |
| 1075 | `ui-tui/src/app/slash/registry.ts` | `637a42f535d2743a33eaa71bc5af2ce88e48fbfc` | blob | 472 | `PORT_UI` | ui-tui/** |
| 1076 | `ui-tui/src/app/slash/types.ts` | `bbd187a23b3f015eee4149a18e01fd06b5d1e2ae` | blob | 555 | `PORT_UI` | ui-tui/** |
| 1077 | `ui-tui/src/app/spawnHistoryStore.ts` | `28dccd0473c56099529bb79057c67a1d32528eb8` | blob | 2398 | `PORT_UI` | ui-tui/** |
| 1078 | `ui-tui/src/app/turnController.ts` | `814edf9326e659f55a75a963267b86e185f28d9b` | blob | 25676 | `PORT_UI` | ui-tui/** |
| 1079 | `ui-tui/src/app/turnStore.ts` | `6d47b036bdca8309a2da11b22b80d5a8fb517d60` | blob | 2416 | `PORT_UI` | ui-tui/** |
| 1080 | `ui-tui/src/app/uiStore.ts` | `e32a9834f276b6cb8846945addfd26be0dfae1c3` | blob | 2619 | `PORT_UI` | ui-tui/** |
| 1081 | `ui-tui/src/app/useComposerState.ts` | `65897f87c521dc09e0c0b91ae894c9e8e713f98a` | blob | 10837 | `PORT_UI` | ui-tui/** |
| 1082 | `ui-tui/src/app/useInputHandlers.ts` | `dbced62993310130454f4171f5bbd797faf98e2a` | blob | 13592 | `PORT_UI` | ui-tui/** |
| 1083 | `ui-tui/src/app/useLongRunToolCharms.ts` | `02c3e95af041f441a2c467537614eade85761290` | blob | 1907 | `PORT_UI` | ui-tui/** |
| 1084 | `ui-tui/src/app/useMainApp.ts` | `51766a92091b38a64ca8d93fa03757efea96d215` | blob | 29319 | `PORT_UI` | ui-tui/** |
| 1085 | `ui-tui/src/app/useSessionLifecycle.ts` | `6fd4bab9605d2a1862f5a1be7d5a4d9815bb0060` | blob | 16666 | `PORT_UI` | ui-tui/** |
| 1086 | `ui-tui/src/app/useSubmission.ts` | `8ee66230d679935aec4a71a637206cde110841b4` | blob | 15264 | `PORT_UI` | ui-tui/** |
| 1087 | `ui-tui/src/banner.ts` | `c7d67c473092cac4895ae200f7b5928632f8a1df` | blob | 5101 | `PORT_UI` | ui-tui/** |
| 1088 | `ui-tui/src/components/agentsOverlay.tsx` | `2a3c307f0be965d1b2cd18a233f8d6c329109ec6` | blob | 33973 | `PORT_UI` | ui-tui/** |
| 1089 | `ui-tui/src/components/appChrome.tsx` | `fc7f22f2b06ed988036e49eaa1a1b26d97d7f195` | blob | 14250 | `PORT_UI` | ui-tui/** |
| 1090 | `ui-tui/src/components/appLayout.tsx` | `bbbfe41a25d47689ca99dab2bea68a30e90bcf04` | blob | 16692 | `PORT_UI` | ui-tui/** |
| 1091 | `ui-tui/src/components/appOverlays.tsx` | `1442e33a350069ba048d093f2e19de2067c4db8f` | blob | 7025 | `PORT_UI` | ui-tui/** |
| 1092 | `ui-tui/src/components/branding.tsx` | `d7350fbea524d36dfe49eaf8cde164c02a71dee7` | blob | 12607 | `PORT_UI` | ui-tui/** |
| 1093 | `ui-tui/src/components/fpsOverlay.tsx` | `ca9fa13f4b06b54f1395538b82ebe8b0bd806a64` | blob | 892 | `PORT_UI` | ui-tui/** |
| 1094 | `ui-tui/src/components/helpHint.tsx` | `ad115b54b82a1a775112e377ae07cab1c110a351` | blob | 2186 | `PORT_UI` | ui-tui/** |
| 1095 | `ui-tui/src/components/markdown.tsx` | `377a521d7b02cde91f07f3448e7b4cbe43181015` | blob | 25014 | `PORT_UI` | ui-tui/** |
| 1096 | `ui-tui/src/components/messageLine.tsx` | `0e332593f06041c94b78fca83736211695b57aeb` | blob | 7654 | `PORT_UI` | ui-tui/** |
| 1097 | `ui-tui/src/components/modelPicker.tsx` | `262afda70832db4d5b63450565570183911471eb` | blob | 22215 | `PORT_UI` | ui-tui/** |
| 1098 | `ui-tui/src/components/overlayControls.tsx` | `f1b4066b024755fa93c1e6cf85e44c54463e6311` | blob | 1283 | `PORT_UI` | ui-tui/** |
| 1099 | `ui-tui/src/components/prompts.tsx` | `7a076dc6d96381e0c5a035912d6783ce74a66d17` | blob | 6227 | `PORT_UI` | ui-tui/** |
| 1100 | `ui-tui/src/components/queuedMessages.tsx` | `e2b41646234c6b90082dc2387a684ed293964df4` | blob | 1950 | `PORT_UI` | ui-tui/** |
| 1101 | `ui-tui/src/components/sessionPicker.tsx` | `7ccd4f41b0034a4951449836285d6f7e9910106a` | blob | 6462 | `PORT_UI` | ui-tui/** |
| 1102 | `ui-tui/src/components/streamingAssistant.tsx` | `bfe007187712caea78b965eac4c3df5205c5fe6b` | blob | 3600 | `PORT_UI` | ui-tui/** |
| 1103 | `ui-tui/src/components/streamingMarkdown.tsx` | `b3d15e4b7d3e5f0f46eccc2c02536122c832e837` | blob | 5860 | `PORT_UI` | ui-tui/** |
| 1104 | `ui-tui/src/components/textInput.tsx` | `9d639f01d64eef7aa3aff1d011bfae4c3abc9cdf` | blob | 29702 | `PORT_UI` | ui-tui/** |
| 1105 | `ui-tui/src/components/themed.tsx` | `b9cc50972585cebe287aac590170d92643472a4a` | blob | 880 | `PORT_UI` | ui-tui/** |
| 1106 | `ui-tui/src/components/thinking.tsx` | `77cfc0769ae1b74434b598897433032711ea5b11` | blob | 30702 | `PORT_UI` | ui-tui/** |
| 1107 | `ui-tui/src/components/todoPanel.tsx` | `f87735d0eba0056351c380b9cb092d67febdbda7` | blob | 2823 | `PORT_UI` | ui-tui/** |
| 1108 | `ui-tui/src/config/env.ts` | `0a11c31e1eead5957c5e461b441d752ce3ab4b8e` | blob | 889 | `PORT_UI` | ui-tui/** |
| 1109 | `ui-tui/src/config/limits.ts` | `2ea45f68cfa326d2c8791c7182fd6bb6b8affd95` | blob | 1026 | `PORT_UI` | ui-tui/** |
| 1110 | `ui-tui/src/config/paths.ts` | `773c25e7b6f17a0e53aeba744fbeea49eba26fa2` | blob | 297 | `PORT_UI` | ui-tui/** |
| 1111 | `ui-tui/src/config/timing.ts` | `e1811e830dc57f96ee7a0e8b1fac182ce4ea1271` | blob | 227 | `PORT_UI` | ui-tui/** |
| 1112 | `ui-tui/src/content/charms.ts` | `546e44dd09d97c53881f483feeaa20b98da6a481` | blob | 103 | `PORT_UI` | ui-tui/** |
| 1113 | `ui-tui/src/content/faces.ts` | `1bb64debb2b6a1c3dfc2f9cb02880a13e961768b` | blob | 304 | `PORT_UI` | ui-tui/** |
| 1114 | `ui-tui/src/content/fortunes.ts` | `87943f9f4271062db35b447615826ddd1449f8d8` | blob | 1193 | `PORT_UI` | ui-tui/** |
| 1115 | `ui-tui/src/content/hotkeys.ts` | `5a7175572e4982a027923012cd0a8e134be6b964` | blob | 1582 | `PORT_UI` | ui-tui/** |
| 1116 | `ui-tui/src/content/placeholders.ts` | `3d97eecac0e0bcb74bef6397c821ccf22ba5a48e` | blob | 346 | `PORT_UI` | ui-tui/** |
| 1117 | `ui-tui/src/content/setup.ts` | `712c3c5bfbcb0c69614f33f503ce664930b4f586` | blob | 485 | `PORT_UI` | ui-tui/** |
| 1118 | `ui-tui/src/content/verbs.ts` | `f12e95e2c8c1ac97eafa74e356c4289100a53444` | blob | 759 | `PORT_UI` | ui-tui/** |
| 1119 | `ui-tui/src/demo/gallery.tsx` | `12189a2f8ba579c45b50372a73b84af858afbc61` | blob | 8420 | `PORT_UI` | ui-tui/** |
| 1120 | `ui-tui/src/domain/details.ts` | `337de7e83b88c39497df5e3c10e6f69ef56a1265` | blob | 3410 | `PORT_UI` | ui-tui/** |
| 1121 | `ui-tui/src/domain/messages.ts` | `4624c2b10432cd1a84f5a4ce805d987d26ce5c61` | blob | 2537 | `PORT_UI` | ui-tui/** |
| 1122 | `ui-tui/src/domain/paths.ts` | `bd56d3880e850fdadd1cfd309dc0eb7dd18da807` | blob | 674 | `PORT_UI` | ui-tui/** |
| 1123 | `ui-tui/src/domain/providers.ts` | `83ac016ff19b4d8c34beca5e6c55d7de705a9c16` | blob | 374 | `PORT_UI` | ui-tui/** |
| 1124 | `ui-tui/src/domain/roles.ts` | `fba451ed5ec43f51dbe01dfbed7052dbb4010d33` | blob | 500 | `PORT_UI` | ui-tui/** |
| 1125 | `ui-tui/src/domain/session.ts` | `33a8fa77110c5db8b7c514984bd713facb29f268` | blob | 197 | `PORT_UI` | ui-tui/** |
| 1126 | `ui-tui/src/domain/slash.ts` | `1fc8082ba5c427709c8cfbfc0a3f66bf4b1cc79c` | blob | 264 | `PORT_UI` | ui-tui/** |
| 1127 | `ui-tui/src/domain/usage.ts` | `c8f568136d6f38abf4d2a9682696390ea4d3b71d` | blob | 346 | `PORT_UI` | ui-tui/** |
| 1128 | `ui-tui/src/domain/viewport.ts` | `336a0709dacb3f03fc8a9ec418e4894a7100bee6` | blob | 1396 | `PORT_UI` | ui-tui/** |
| 1129 | `ui-tui/src/entry.tsx` | `e52eb2d87a3456bd501e757b8ebd5fe227aaebf4` | blob | 5724 | `PORT_UI` | ui-tui/** |
| 1130 | `ui-tui/src/gatewayTypes.ts` | `7bd228c71092f27cb0463919eb8cd9659c487d7e` | blob | 7507 | `PORT_UI` | ui-tui/** |
| 1131 | `ui-tui/src/hooks/useCompletion.ts` | `27852d3962e8076fa7be155a3f4b5fa0ef81087b` | blob | 2435 | `PORT_UI` | ui-tui/** |
| 1132 | `ui-tui/src/hooks/useGitBranch.ts` | `d586e6a0db31d219aafea79dcb1f6cf445f865dd` | blob | 1817 | `PORT_UI` | ui-tui/** |
| 1133 | `ui-tui/src/hooks/useInputHistory.ts` | `8192b86c8f27e983fab4469c1ae17a523817a1c6` | blob | 398 | `PORT_UI` | ui-tui/** |
| 1134 | `ui-tui/src/hooks/useQueue.ts` | `3cf6c8bcb9bb1b1e36f8d90f66f16b4a4f940117` | blob | 4746 | `PORT_UI` | ui-tui/** |
| 1135 | `ui-tui/src/hooks/useVirtualHistory.ts` | `13513e0eae701f3ca4685d9e8d9771072dab769f` | blob | 18605 | `PORT_UI` | ui-tui/** |
| 1136 | `ui-tui/src/lib/circularBuffer.ts` | `31502fc227902a6c1396e0fc8a0db6021b619af7` | blob | 994 | `PORT_UI` | ui-tui/** |
| 1137 | `ui-tui/src/lib/clipboard.ts` | `c5305653159cecdee659f9ffc4f15d5642d72289` | blob | 15319 | `PORT_UI` | ui-tui/** |
| 1138 | `ui-tui/src/lib/colorTier.ts` | `4510e35a08ec249c20b86cf6af201fdd0336d3dd` | blob | 2760 | `PORT_UI` | ui-tui/** |
| 1139 | `ui-tui/src/lib/confirmCountdown.ts` | `dc73d43bbf3fced742c7d78036651d574074554a` | blob | 799 | `PORT_UI` | ui-tui/** |
| 1140 | `ui-tui/src/lib/editor.test.ts` | `d2af2bea1b61f87c5b02991ab1c211a718574ae6` | blob | 2400 | `PORT_UI` | ui-tui/** |
| 1141 | `ui-tui/src/lib/editor.ts` | `bcf25f3033f9bebadffbbd459ae8b59c629e1d00` | blob | 1303 | `PORT_UI` | ui-tui/** |
| 1142 | `ui-tui/src/lib/emoji.ts` | `4bded51f28f4fe62291da7cb7a70cac483026076` | blob | 2976 | `PORT_UI` | ui-tui/** |
| 1143 | `ui-tui/src/lib/externalCli.ts` | `757680afb58e3531f3eccfa90ea239b787a29677` | blob | 488 | `PORT_UI` | ui-tui/** |
| 1144 | `ui-tui/src/lib/externalLink.ts` | `c54659996b867be05b7211345e91c2bba7dec98b` | blob | 10473 | `PORT_UI` | ui-tui/** |
| 1145 | `ui-tui/src/lib/fpsStore.ts` | `8baf9f24932a22a20a10fde03143c8fd5e8e764a` | blob | 1574 | `PORT_UI` | ui-tui/** |
| 1146 | `ui-tui/src/lib/gracefulExit.ts` | `2896fd126514d14e5d8d1719923fae2b2dd74947` | blob | 1209 | `PORT_UI` | ui-tui/** |
| 1147 | `ui-tui/src/lib/history.ts` | `cd81ef50159f37962c60e55468e78effc1e0b00c` | blob | 1695 | `PORT_UI` | ui-tui/** |
| 1148 | `ui-tui/src/lib/inputMetrics.ts` | `92f12e7d7c1de2b42080ae9a16e4a7e72a509bb3` | blob | 5143 | `PORT_UI` | ui-tui/** |
| 1149 | `ui-tui/src/lib/liveProgress.test.ts` | `2476c4ecf104cf421b78d414e7bf5065661742f8` | blob | 4487 | `PORT_UI` | ui-tui/** |
| 1150 | `ui-tui/src/lib/liveProgress.ts` | `d5a1fb2f56a941b48ab3c82051bd0ce9f34a9e0d` | blob | 2320 | `PORT_UI` | ui-tui/** |
| 1151 | `ui-tui/src/lib/mathUnicode.ts` | `e6ccce664ccba1e9183a38cd88f3cb944096407d` | blob | 19935 | `PORT_UI` | ui-tui/** |
| 1152 | `ui-tui/src/lib/memory.ts` | `20ee5dad8800d10f5c5203a7107b5f79dd660820` | blob | 6628 | `PORT_UI` | ui-tui/** |
| 1153 | `ui-tui/src/lib/memoryMonitor.ts` | `07dc3f626c69b148023315f3ff708b764aa98966` | blob | 3752 | `PORT_UI` | ui-tui/** |
| 1154 | `ui-tui/src/lib/messages.test.ts` | `422ddb1af90402dbe39ef95fd6b3a2be36aec795` | blob | 1056 | `PORT_UI` | ui-tui/** |
| 1155 | `ui-tui/src/lib/messages.ts` | `b8e89421e5a73824b0f7037724e659e0b88a7191` | blob | 384 | `PORT_UI` | ui-tui/** |
| 1156 | `ui-tui/src/lib/osc52.ts` | `d11e56281e8f91cd769065f1c0e63c782e431a7f` | blob | 2331 | `PORT_UI` | ui-tui/** |
| 1157 | `ui-tui/src/lib/perfPane.tsx` | `7326b5582be45264d44e3d1c34819a968f1f3147` | blob | 3577 | `PORT_UI` | ui-tui/** |
| 1158 | `ui-tui/src/lib/platform.ts` | `5fba34b5e51b6b0def237bea4973211894171797` | blob | 1302 | `PORT_UI` | ui-tui/** |
| 1159 | `ui-tui/src/lib/precisionWheel.ts` | `4ddb447abf03dde6a70426b79cf9f028935bd563` | blob | 1074 | `PORT_UI` | ui-tui/** |
| 1160 | `ui-tui/src/lib/printColors.ts` | `f3e1ed7c74a9b6e0aa5b6627ef1d96c8496aae00` | blob | 4776 | `PORT_UI` | ui-tui/** |
| 1161 | `ui-tui/src/lib/reasoning.ts` | `f384285e91570110cb9b3afad81a4b649fab0e2f` | blob | 1256 | `PORT_UI` | ui-tui/** |
| 1162 | `ui-tui/src/lib/rpc.ts` | `bcddad70cd6091ff8f7a9c8ac38a5528614f7c52` | blob | 387 | `PORT_UI` | ui-tui/** |
| 1163 | `ui-tui/src/lib/subagentTree.ts` | `73043146d1fbb9ae1f48ea6268522d64bbc95fb7` | blob | 9937 | `PORT_UI` | ui-tui/** |
| 1164 | `ui-tui/src/lib/syntax.ts` | `7e5a5a78367789b20fd0062fa74c6f7e491f7872` | blob | 3652 | `PORT_UI` | ui-tui/** |
| 1165 | `ui-tui/src/lib/terminalModes.ts` | `9d9aa16aab131d1fc1dbdb48c8ac8e1cc9451b66` | blob | 1716 | `PORT_UI` | ui-tui/** |
| 1166 | `ui-tui/src/lib/terminalParity.ts` | `7f2beb20f7ed7a36b20ab44d73715514c9c8adc5` | blob | 2318 | `PORT_UI` | ui-tui/** |
| 1167 | `ui-tui/src/lib/terminalSetup.ts` | `a590cd77053a404f9b83eed92c610e890398500b` | blob | 11789 | `PORT_UI` | ui-tui/** |
| 1168 | `ui-tui/src/lib/text.test.ts` | `1a3800ec7606ef9fd151e85ed95006ab8b43cc14` | blob | 613 | `PORT_UI` | ui-tui/** |
| 1169 | `ui-tui/src/lib/text.ts` | `5d4611b27ffb9d419c032a1cb842001f7223b4ee` | blob | 8910 | `PORT_UI` | ui-tui/** |
| 1170 | `ui-tui/src/lib/todo.test.ts` | `bf8befa2c6ed9e63f366ab44683fb2f429e90fa7` | blob | 716 | `PORT_UI` | ui-tui/** |
| 1171 | `ui-tui/src/lib/todo.ts` | `1846d02fe631c92a423b7e4bad39bf42723a2dd7` | blob | 406 | `PORT_UI` | ui-tui/** |
| 1172 | `ui-tui/src/lib/viewportStore.ts` | `11bba0feb2a2a7ef04de69783f5ce94a739a2b65` | blob | 3719 | `PORT_UI` | ui-tui/** |
| 1173 | `ui-tui/src/lib/virtualHeights.ts` | `5e71976cd96502a555a40320d9d88e92efa4f750` | blob | 2752 | `PORT_UI` | ui-tui/** |
| 1174 | `ui-tui/src/lib/wheelAccel.ts` | `abdb264a4e2b347dd8f875b3298339448a915712` | blob | 6747 | `PORT_UI` | ui-tui/** |
| 1175 | `ui-tui/src/protocol/interpolation.ts` | `804cf1cf040934440dd506a02bd9ff8d05e0ea93` | blob | 113 | `PORT_UI` | ui-tui/** |
| 1176 | `ui-tui/src/protocol/paste.ts` | `9eae137cea455d3414c37390ee53153d5ef24418` | blob | 51 | `PORT_UI` | ui-tui/** |
| 1177 | `ui-tui/src/rpc/__tests__/client.test.ts` | `b89c9e9b90867d9fecaf7c0632ed865156f5989e` | blob | 8425 | `PORT_UI` | ui-tui/** |
| 1178 | `ui-tui/src/rpc/__tests__/subscriptions.test.ts` | `ff008d482204154a1e7935a588ba7365d4e4ebae` | blob | 8744 | `PORT_UI` | ui-tui/** |
| 1179 | `ui-tui/src/rpc/client.ts` | `4469e474ff356966cb8a9c9d98dbf2e2a8f82154` | blob | 10480 | `PORT_UI` | ui-tui/** |
| 1180 | `ui-tui/src/rpc/errors.ts` | `cce7de83ce49b6efe2c6130d14d5dee337f14b8a` | blob | 4049 | `PORT_UI` | ui-tui/** |
| 1181 | `ui-tui/src/rpc/generated.ts` | `caf8b3e6fe1c17ba00538622b959e65e3596a506` | blob | 21531 | `PORT_UI` | ui-tui/** |
| 1182 | `ui-tui/src/rpc/index.ts` | `96e3838612ad2d5b7313c37fb3567251c561d0a2` | blob | 815 | `PORT_UI` | ui-tui/** |
| 1183 | `ui-tui/src/rpc/subscriptions.ts` | `73f4c79160e397431a9fbe88f0deb6fb09950a46` | blob | 2109 | `PORT_UI` | ui-tui/** |
| 1184 | `ui-tui/src/theme.ts` | `46bd1b4b4d64aaf937ad85d1a9927963f6dd1b67` | blob | 25203 | `PORT_UI` | ui-tui/** |
| 1185 | `ui-tui/src/tuiRpcClient.ts` | `676d33204f8b2adb0c8b86037aad04302a907933` | blob | 4280 | `PORT_UI` | ui-tui/** |
| 1186 | `ui-tui/src/types.ts` | `4142dc1a4fb337a71200583afa908bcd5209fb75` | blob | 4210 | `PORT_UI` | ui-tui/** |
| 1187 | `ui-tui/src/types/hermes-ink.d.ts` | `69b6f37cd153432015e241894fb2a96f0c274325` | blob | 6792 | `PORT_UI` | ui-tui/** |
| 1188 | `ui-tui/tsconfig.build.json` | `c4e75895e63c4c6212efe5a2e9da9bc7f1998c56` | blob | 132 | `PORT_UI` | ui-tui/** |
| 1189 | `ui-tui/tsconfig.json` | `8e81d9ebc4d18af134c6d69725e11ef472559533` | blob | 535 | `PORT_UI` | ui-tui/** |
| 1190 | `ui-tui/vitest.config.ts` | `b3efa48af91f52242e3b0103e4e8da3fcce51794` | blob | 137 | `PORT_UI` | ui-tui/** |
| 1191 | `uv.lock` | `f3908d64b9133e9a70f5084c7d34945dc3ecb03b` | blob | 269936 | `MERGE_BUILD` | uv.lock |

## 最终验收记录

- [x] 固定上游提交并读取完整 Git tree
- [x] 核对上游 tree 总数为 1191 个 blob
- [x] 核对 `pico` 355 个文件、`ui-tui` 337 个文件、`tests` 269 个文件
- [x] 核对上游实际存在的 Channels、Media、Transcription、BoxLite、Evolver、TUI RPC、TUI、Installer 和 Token-wise 文件
- [x] 核对上游树中没有通用 OIDC、tenant、marketplace、signature、OTEL collector 或 leader-election 产品路径
- [x] 逐文件完成工作区映射；测试路径按约定重定位到 `tests/pico_upstream/`
- [x] 完成 API/行为兼容审查，并通过根 Python、上游 Python、TUI、Desktop、构建和发布树验收
- [x] 形成最终新增、修改、包装、保留不动文件清单，详见 `PICO_ABSORPTION_REPORT.md`
- [x] 在任何现有文件修改前创建 `E:\codex_backup\<timestamp>-<description>\` 备份

## 最终结论

固定提交 `d6c7a648fd7ee63e472c0d438f1c8299d9b8f871` 的 1191 个 blob 均已在当前工作区找到，缺失数为 0。平台限制、未执行的真实外部 E2E、BoxLite Windows wheel 限制和全仓非门禁 Ruff 告警均已记录在 `PICO_ABSORPTION_REPORT.md`。

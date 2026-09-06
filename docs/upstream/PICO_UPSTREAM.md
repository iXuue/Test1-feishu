# Pico Harness provenance

本仓库已从上游 Pico Harness 固定提交导入产品源码、TUI、基准/验证脚本和隔离测试；
CodeCub 原有 `codecub/**` 运行时代码仍保留。该文档记录来源，逐文件处理动作见
`docs/upstream/PICO_ABSORPTION_MANIFEST.md`。

| 字段 | 值 |
| --- | --- |
| 上游仓库 | https://gitee.com/htxoffical/pico-harness |
| 审计分支 | `main` |
| 固定提交 | `d6c7a648fd7ee63e472c0d438f1c8299d9b8f871` |
| 发布标签上下文 | `v0.1.7`（peeled commit `c2524dbf507b2dc31ba8eb24790444bfb9acb563`） |
| 许可证 | Apache-2.0；随仓库保留 `LICENSE`、`LICENSES/`、`NOTICES.md` |
| 导入产品源码 | `pico/**`（355 个文件）、`ui-tui/**`（337 个文件） |
| 导入验证内容 | `benchmarks/**`、`scripts/**`、`tests/pico_upstream/**`、`tests/tui/**` |
| 本地适配 | 构建/依赖配置、Pico distribution 版本回退、Windows 锁兼容、TUI 跨平台路径/测试传输、混合仓库测试路径和 CodeCub 本地安装探测 |
| 详细清单 | `docs/upstream/PICO_ABSORPTION_MANIFEST.md` |

## 归属与修改边界

- `pico/**` 和 `ui-tui/**` 保留上游包路径，便于 API、协议和来源审计。
- `codecub/**` 保留 CodeCub 既有运行时；后续桥接只能复用同一 session、spine、tool executor
  和持久化状态，不能为同一次调用创建第二套状态机。
- 上游固定树之外的 OIDC/tenant、Marketplace、远程 OTEL collector 和泛化 leader election
  不因本次吸收新增。
- 本地适配应在报告中逐条列出，并保留上游语义、测试契约和许可证声明。

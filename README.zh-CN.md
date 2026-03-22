<!-- language-switch:start -->
[English](./README.md) | [中文](./README.zh-CN.md)
<!-- language-switch:end -->

# aro-审计-langchain-回执

用于 [aro-audit](https://github.com/joy7758/aro-audit) 的薄适配器和集成表面。

## 角色

该仓库封装了一个小型的面向 LangChain 的回执发射器，该发射器位于运行时执行的下游。它的存在是为了展示紧凑的运行后回执的集成粘合剂，而不是取代规范的 ARO 审计控制平面。

## 规范主页

规范审计实现位于 `aro-audit` 中，特别是：

- `aro-audit/aro_audit/`
- `aro-audit/docs/boundaries.md`
- `aro-audit/docs/receipts-vs-events.md`
- `aro-audit/examples/receipts/`

## 不是这个仓库

- 不是规范的审计实施
- 不是证据捕获基质
- 不是架构总仓
- 不是基准套件

## 最少使用量

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
pytest
```

```python
import json
from pathlib import Path

from aro_audit_langchain_receipt.receipt import build_receipt

run_state = json.loads(Path("examples/inputs/run-state.example.json").read_text())
policy_signals = json.loads(Path("examples/inputs/policy-signals.example.json").read_text())
print(build_receipt(run_state, policy_signals))
```

对于有界审查、回执语义和验证工作流程，请从 `aro-audit` 开始。

## 地位

- 薄型适配器
- 规范主页是 `aro-audit`
- 保留为最小的 LangChain 回执示例

## 笔记

- 这个 repo 故意使适配器表面变窄。
- 审计验证、一致性和控制平面逻辑应首先在 `aro-audit` 中发展。

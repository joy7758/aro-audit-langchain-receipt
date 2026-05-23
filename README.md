> **Maintenance notice**
>
> This repository is no longer the primary maintenance entry for the Agent Evidence / Operation Accountability Profile（智能体执行证据与操作问责配置文件）mainline. It is retained for migration review or historical reference. This change does not delete or archive the repository. See `MIGRATED_TO.md` for the current migration target and review status.

<!-- language-switch:start -->
[English](./README.md) | [中文](./README.zh-CN.md)
<!-- language-switch:end -->

# aro-audit-langchain-receipt

Thin adapter and integration surface for [aro-audit](https://github.com/joy7758/aro-audit).

## Role

This repo packages a small LangChain-oriented receipt emitter that sits downstream of runtime execution. It exists to show integration glue for compact post-run receipts, not to replace the canonical ARO Audit control plane.

## Canonical home

The canonical audit implementation lives in `aro-audit`, especially:

- `aro-audit/aro_audit/`
- `aro-audit/docs/boundaries.md`
- `aro-audit/docs/receipts-vs-events.md`
- `aro-audit/examples/receipts/`

## Not this repo

- not the canonical audit implementation
- not the evidence capture substrate
- not the architecture hub
- not the benchmark suite

## Minimal usage

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

For bounded review, receipt semantics, and verification workflows, start from `aro-audit`.

## Status

- thin adapter
- canonical home is `aro-audit`
- kept as a minimal LangChain receipt example

## Notes

- This repo keeps the adapter surface narrow on purpose.
- Audit verification, conformance, and control-plane logic should evolve in `aro-audit` first.

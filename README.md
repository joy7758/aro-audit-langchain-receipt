# ARO Audit LangChain Receipt

Compact post-run execution receipts for LangChain agents on LangGraph.

Part of the Agent Runtime Safety Kit.  
This repo shows a thin adapter pattern for emitting a compact execution receipt after a LangChain agent run.

## What this is

- A docs-first and minimal runnable adapter repo.
- A compact receipt builder for local run-state dictionaries.
- A thin adapter that emits a post-run receipt after agent execution.
- A small example that composes with budget-window and trust-gate adapters.

## What this is not

- Not a full observability platform.
- Not an official LangChain or LangGraph extension.
- Not a complete compliance system.
- Not a claim that receipts alone provide full governance coverage.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[test]"

python - <<'PY'
import json
from pathlib import Path
from aro_audit_langchain_receipt.receipt import build_receipt

run_state = json.loads(Path("examples/inputs/run-state.example.json").read_text())
policy_signals = json.loads(Path("examples/inputs/policy-signals.example.json").read_text())
print(build_receipt(run_state, policy_signals))
PY

pytest
```

## Demo Assets

- [Demo](docs/demo.md)
- [Integration Pattern](docs/integration-pattern.md)
- [Run State Example](examples/inputs/run-state.example.json)
- [Policy Signals Example](examples/inputs/policy-signals.example.json)
- [Receipt Example](examples/results/receipt.example.json)

## Receipt Shape

- `build_receipt(run_state, policy_signals)` emits a compact receipt dictionary.
- Missing fields fall back to safe defaults.
- The adapter layer simply wraps the builder and returns the same receipt shape.

This is a thin adapter example, not an official LangChain extension.

## Related Projects

- [ARO Audit](https://github.com/joy7758/aro-audit)
- [Token Governor](https://github.com/joy7758/token-governor)
- [God Spear](https://github.com/joy7758/god-spear)
- [Token Governor LangChain Middleware](https://github.com/joy7758/token-governor-langchain-middleware)
- [God Spear MCP Gate](https://github.com/joy7758/god-spear-mcp-gate)

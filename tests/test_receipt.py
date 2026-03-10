from __future__ import annotations

import json
from pathlib import Path

from aro_audit_langchain_receipt.receipt import build_receipt


ROOT = Path(__file__).resolve().parents[1]


def test_minimal_run_state_outputs_receipt() -> None:
    receipt = build_receipt({"run_id": "run_minimal_001"})

    assert receipt["run_id"] == "run_minimal_001"
    assert receipt["actor"] == "unknown"
    assert receipt["model"] == "unknown"
    assert receipt["tools"] == []
    assert receipt["outcome"] == "unknown"
    assert "created_at" in receipt


def test_policy_signals_are_merged_into_receipt() -> None:
    run_state = json.loads((ROOT / "examples" / "inputs" / "run-state.example.json").read_text())
    policy_signals = json.loads(
        (ROOT / "examples" / "inputs" / "policy-signals.example.json").read_text()
    )

    receipt = build_receipt(run_state, policy_signals)

    assert receipt["run_id"] == "run_receipt_adapter_001"
    assert receipt["policy_signals"]["budget_decision"] == "allow"
    assert receipt["policy_signals"]["trust_gate_decision"] == "allow"

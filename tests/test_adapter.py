from __future__ import annotations

from aro_audit_langchain_receipt.adapter import LangChainReceiptEmitter


def test_emitter_can_emit_receipt_dict() -> None:
    emitter = LangChainReceiptEmitter()

    receipt = emitter.emit(
        {
            "run_id": "run_adapter_001",
            "actor": "ops-review-agent",
            "model": "small-general-model",
            "outcome": "completed",
        }
    )

    assert isinstance(receipt, dict)
    assert receipt["run_id"] == "run_adapter_001"
    assert receipt["outcome"] == "completed"

"""Thin adapter layer for emitting compact execution receipts."""

from __future__ import annotations

from typing import Any

from .receipt import build_receipt


class LangChainReceiptEmitter:
    """Emit a compact post-run receipt from local run state.

    This is a thin adapter example, not an official LangChain extension.
    """

    def emit(
        self, run_state: dict[str, Any], policy_signals: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        return build_receipt(run_state, policy_signals)

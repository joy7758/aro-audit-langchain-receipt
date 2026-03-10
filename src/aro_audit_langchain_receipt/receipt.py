"""Compact receipt builder helpers."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def _utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def _as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return []


def _as_dict(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    return {}


def build_receipt(
    run_state: dict[str, Any], policy_signals: dict[str, Any] | None = None
) -> dict[str, Any]:
    signals = _as_dict(policy_signals) or _as_dict(run_state.get("policy_signals"))
    input_summary = run_state.get("input_summary", "not_provided")
    output_summary = run_state.get("output_summary", "not_provided")

    if "cost_summary" in run_state and isinstance(run_state["cost_summary"], dict):
        cost_summary = {
            "currency": run_state["cost_summary"].get("currency", "USD"),
            "estimated_cost": run_state["cost_summary"].get("estimated_cost", 0.0),
            "token_usage": _as_dict(run_state["cost_summary"].get("token_usage")),
        }
    else:
        cost_summary = {
            "currency": "USD",
            "estimated_cost": run_state.get("estimated_cost", 0.0),
            "token_usage": _as_dict(run_state.get("token_usage")),
        }

    return {
        "run_id": run_state.get("run_id", "unknown"),
        "created_at": run_state.get("created_at", _utc_now()),
        "actor": run_state.get("actor", "unknown"),
        "model": run_state.get("model", "unknown"),
        "tools": _as_list(run_state.get("tools")),
        "input_summary": input_summary,
        "output_summary": output_summary,
        "policy_signals": signals,
        "cost_summary": cost_summary,
        "outcome": run_state.get("outcome", "unknown"),
    }

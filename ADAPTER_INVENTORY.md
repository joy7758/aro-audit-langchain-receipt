# Adapter Inventory

## Repo role

Minimal receipt emitter adapter for LangChain-style runs.

## Current retained surfaces

- package code under `src/aro_audit_langchain_receipt/`
- examples under `examples/`
- tests under `tests/`
- docs under `docs/`

## Canonical overlap

- canonical audit control plane lives in `aro-audit/aro_audit/`
- canonical receipt semantics and examples live in `aro-audit/docs/receipts-vs-events.md` and `aro-audit/examples/receipts/`

## Boundary decision

Keep this repo as a thin adapter example, with canonical audit behavior anchored in `aro-audit`.

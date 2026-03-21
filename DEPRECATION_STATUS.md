# Deprecation Status

## Recommended use

Use `aro-audit` for canonical receipt semantics, verification, and control-plane workflows. Use this repo only when a lightweight standalone adapter example is useful.

## Canonical parent repo

- `aro-audit`

## Current posture

- thin adapter
- standalone wrapper still acceptable for examples and compatibility

## Future direction

This repo can remain as a small adapter surface as long as it does not duplicate the audit control plane. If the parent repo grows a first-class LangChain receipt adapter, this repo should be downgraded further.

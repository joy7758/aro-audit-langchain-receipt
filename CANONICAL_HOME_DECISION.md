# Canonical Home Decision

## Decision

Canonical home: `aro-audit`

## Why

- receipt verification and control-plane semantics belong in the audit repo
- this standalone repo is useful only as a narrow integration example
- keeping the canonical home explicit prevents the adapter from competing with the audit layer

## Posture

- thin adapter, not the source of truth
- parent repo remains the authoritative home for receipts, verification, and conformance

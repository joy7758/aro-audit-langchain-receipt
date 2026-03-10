# Demo

## Scenario

This demo shows a compact receipt emitted after a LangChain agent run. The goal is to keep the post-run artifact small, readable, and easy to pass into later review flows.

## Run State

The run-state example contains a small summary of actor, model, tool usage, input/output summaries, and cost information.

- [run-state.example.json](../examples/inputs/run-state.example.json)

## Policy Signals

The policy-signals example carries a small summary of earlier runtime decisions such as budget and trust-gate outcomes.

- [policy-signals.example.json](../examples/inputs/policy-signals.example.json)

## Example Receipt

The receipt combines the run state and policy signals into a compact post-run record.

- [receipt.example.json](../examples/results/receipt.example.json)

## Why this matters

This is a compact receipt after the run, not a full observability suite. It is designed to be composable with budget-window and trust-gate adapters so teams can carry a small review artifact across the runtime control chain.

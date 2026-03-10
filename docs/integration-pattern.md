# Integration Pattern

This repository shows an adapter pattern, not an official LangChain or LangGraph extension.

```text
request
  -> optional trust gate
  -> optional budget middleware
  -> model/tool execution
  -> receipt emitter
```

In the smallest integration, a request may first pass through a trust gate and a budget check, then execute the model or tools, and finally emit a compact receipt for later review. The receipt emitter stays thin and focuses only on post-run receipt construction.

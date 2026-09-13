# `agent/` — Role 1: AI Agent Developer

This package contains the **agentic orchestration controller** for SatQuery AI.
It is the decision-making "brain" that sits between the user-facing GUI/API and
the specialist remote-sensing models.

```
User query + image(s)
        │
        ▼
┌────────────────────────┐
│ controller.py           │   ← entry point, wires everything together
└───────────┬────────────┘
            │
   ┌────────┼─────────────────────┬──────────────────┬───────────────────┐
   ▼        ▼                     ▼                  ▼                   ▼
task_      input_                model_             workflow_           tool_
classifier validator             registry           planner             executor
   │        │                     │                  │                   │
   └────────┴─────────────────────┴──────────────────┴───────────┬───────┘
                                                                 ▼
                                                          output_integrator
                                                                 │
                                                     ┌───────────┴──────────┐
                                                     ▼                      ▼
                                                 confidence               audit
```

## File map

| File | Responsibility |
|---|---|
| `__init__.py` | Package docstring & exports. |
| `controller.py` | **Main orchestration loop** — the top-level `Agent` class that receives a query + images and drives the full pipeline. |
| `task_classifier.py` | Classifies the user's natural-language query into one or more task types (VQA, captioning, grounding, change-VQA, cross-modal fusion, etc.) and extracts entities (locations, dates, target objects). |
| `input_validator.py` | Validates uploaded images: count, modality (optical/SAR/both), format (GeoTIFF/TIFF/PNG/JPEG), metadata, CRS, co-registration, temporal pairing compatibility. |
| `model_registry.py` | Registry of available specialist models/tools (name, task type, modality support, input schema, parameters, endpoint). Used by the planner to discover callable tools. |
| `workflow_planner.py` | Plans a multi-step execution DAG/sequence based on the classified task and validated inputs (e.g., grounding → crop → caption, or change-detect → describe). |
| `tool_executor.py` | Dispatches calls to specialist models (via API / in-process) with only permitted parameters, enforces timeouts, and collects raw outputs. |
| `output_integrator.py` | Merges textual answers with spatial outputs (bounding boxes, change masks, heatmaps) into a single response object ready for the frontend. |
| `confidence.py` | Aggregates per-tool scores / uncertainties into a calibrated response-level confidence estimate. |
| `audit.py` | Builds the auditable execution trace: selected task(s), tool names, parameters used, intermediate outputs, confidence, and timestamps. |

## Sub-packages

| Directory | Purpose |
|---|---|
| `prompts/` | Prompt templates used by the LLM-driven parts of the agent (task classification, planner reasoning, response synthesis). |
| `schemas/` | Typed schemas (Pydantic / dataclasses) for agent inputs, outputs, tool definitions, task types, audit records, etc. |
| `utils/` | Shared helpers: logging, config loading, serialisation, geo helpers (thin wrappers only — real GIS work lives in `geo/`). |
| `tests/` | Unit and integration tests for the agent modules. |

## Status

> 🚧 **Skeleton only.** Files are empty placeholders. Implementation will be
> added iteratively as we agree on the design.

## Typical invocation (future)

```python
from agent.controller import SatQueryAgent

agent = SatQueryAgent.from_config("configs/agent.yaml")
result = agent.run(
    query="What changed between these two dates, and where?",
    images=[image_t1, image_t2],   # bi-temporal pair
)
print(result.answer)        # natural-language answer
print(result.visuals)       # change mask / overlays
print(result.confidence)    # confidence score
print(result.audit_trace)   # auditable execution log
```

"""
SatQuery AI — Agentic Controller Package (Role 1: AI Agent Developer)

This package implements the agentic orchestration layer of SatQuery AI.
It is responsible for:

    • interpreting the user's natural-language query and classifying the task,
    • validating the number, modality, format, metadata, and compatibility of
      the input remote-sensing images,
    • selecting specialist models/tools from the model registry,
    • planning and sequencing multi-step workflows,
    • executing tools with permitted parameters,
    • integrating textual + spatial outputs and estimating confidence,
    • producing an auditable execution trace (audit log).

Modules
-------
controller          : main orchestration loop (entry point for the agent).
task_classifier     : maps natural-language queries → task types + entities.
input_validator     : validates image count, modality, format, co-registration.
model_registry      : registry of available specialist models / tools.
workflow_planner    : composes and sequences multi-step pipelines.
tool_executor       : invokes selected tools with permitted parameters.
output_integrator   : fuses textual + spatial outputs into a unified response.
confidence          : estimates and calibrates response-level confidence.
audit               : builds the observable execution trace / audit log.
prompts/            : prompt templates for the LLM-driven agent steps.
schemas/            : Pydantic/dataclass schemas for tasks, tools, inputs, outputs.
utils/              : shared helper utilities (logging, serialisation, etc.).
tests/              : unit and integration tests for the agent package.

NOTE: This package is a skeleton at the moment. Implementation will be
      filled in incrementally as the project evolves.
"""

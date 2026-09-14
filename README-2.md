# SatQuery AI

<div align="center">

**An Interactive Vision-Language Assistant for Multimodal Remote Sensing Image Analysis through Text Queries**

*An agentic, query-driven framework that intelligently routes natural-language requests over satellite imagery to specialized remote-sensing models — supporting single-image understanding, bi-temporal change analysis, and cross-modal optical–SAR fusion.*

![Organization: ISRO](https://img.shields.io/badge/Organization-ISRO-blue)
![Department](https://img.shields.io/badge/Department-Dept.%20of%20Space%2FISRO-darkblue)
![Category](https://img.shields.io/badge/Category-Software-green)
![Theme](https://img.shields.io/badge/Theme-Space%20Technology-purple)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

</div>

---

## Table of Contents

- [Overview](#overview)
- [The Problem](#the-problem)
- [Why SatQuery AI](#why-satquery-ai)
- [Key Features](#key-features)
- [Supported Inputs](#supported-inputs)
- [Representative Queries](#representative-queries)
- [System Architecture](#system-architecture)
- [Agentic Orchestration](#agentic-orchestration)
- [Specialist Model Suite](#specialist-model-suite)
- [Technology Stack](#technology-stack)
- [Datasets](#datasets)
- [Evaluation & Judging Criteria](#evaluation--judging-criteria)
- [Project Structure](#project-structure)
- [Team Roles](#team-roles)
- [Development Roadmap](#development-roadmap)
- [Installation](#installation)
- [Usage](#usage)
- [Deliverables](#deliverables)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Overview

**SatQuery AI** is an interactive, agentic vision-language assistant for analyzing single and paired remote-sensing images through natural-language queries. It is built under the **Indian Space Research Organisation (ISRO) / Department of Space** as a software solution themed around Space Technology.

Unlike monolithic vision-language models, SatQuery AI uses a **controller + specialist-tools** architecture: an intelligent agent interprets the user's intent, validates inputs, routes the request to the appropriate remote-sensing specialist model(s), handles uncertainty through confidence gates and bounded fallbacks, and returns an **evidence-grounded, auditable response** complete with visual overlays and a downloadable execution report.

The system supports three core input configurations:

1. **Single optical, multispectral, or SAR image** — for VQA, captioning, and text-guided region grounding.
2. **Co-registered optical–SAR pair** — for cross-modal fusion and joint analysis.
3. **Bi-temporal image pair** — for change detection, change description, and change-based VQA.

---

## The Problem

### Background

Remote-sensing imagery powers a wide range of critical applications:

| Domain | Applications |
|---|---|
| **Agriculture** | Crop-health monitoring, yield estimation, irrigation planning |
| **Disaster Management** | Flood mapping, damage assessment, post-event response |
| **Urban Planning** | Sprawl analysis, infrastructure mapping, growth modelling |
| **Forest Monitoring** | Deforestation detection, canopy cover, biomass mapping |
| **Water Resources** | Reservoir monitoring, wetland delineation, flood risk |
| **Environmental Analysis** | Land-cover classification, habitat mapping, pollution tracking |

### Gaps in Existing Tools

Most existing remote-sensing AI solutions are **single-task silos** — built for one predefined job (land-cover classification, object detection, VQA, or change detection). Using them typically requires:

- Knowledge of satellite sensor characteristics (optical, multispectral, SAR).
- Familiarity with GIS workflows and coordinate-reference systems.
- Manual model selection and parameter tuning.
- Manual stitching of outputs across modalities and time steps.

This makes it difficult for **non-expert users** to extract meaningful insights through simple natural-language queries.

### The Multimodal Reality

Operational remote-sensing questions rarely have reliable answers from a single optical image:

- **Optical/multispectral imagery** captures rich spectral and contextual information but is blocked by cloud cover and darkness.
- **Synthetic Aperture Radar (SAR)** penetrates clouds, operates day/night, and carries complementary structural information.
- **Bi-temporal pairs** are required to detect, localize, and interpret changes over time.
- **Co-registered optical–SAR pairs** together provide more complete and reliable information than either modality alone.

### Why Generic VLMs Are Not Enough

Off-the-shelf LLMs and VLMs are not reliable for remote-sensing tasks without **domain adaptation** to sensor physics, geospatial terminology, and RS-specific reasoning patterns. SatQuery AI addresses this with remote-sensing fine-tuning and a multi-specialist architecture rather than a single generic model.

---

## Why SatQuery AI

SatQuery AI is designed from the ground up to be:

- 🧠 **Agentic** — interprets intent, routes to specialists, self-corrects on low confidence.
- 🛰️ **Multimodal** — handles optical, multispectral, and SAR in single, paired, and bi-temporal configurations.
- 🌍 **Domain-adapted** — vision-language components are fine-tuned on remote-sensing data (BigEarthNet).
- 🔍 **Evidence-grounded** — every answer is paired with visual evidence (bounding boxes, masks, change maps).
- 📝 **Auditable** — produces a complete execution trace: task, tools used, parameters, timings, confidence, outputs.
- 🔁 **Stateful** — remembers active image context across multi-turn follow-up queries.
- 🧪 **Resilient** — confidence-gated fallback and retry logic; deterministic mock/demo path for reliability.
- 🖥️ **Interactive** — ships with a web GUI supporting upload, querying, visualization, and report export.

---

## Key Features

### Mandatory Capabilities

- [x] **Remote-sensing adaptation** — visual / vision-language component(s) fine-tuned on BigEarthNet and other open RS datasets.
- [x] **Single-image VQA** (baseline, mandatory).
- [x] **Single-image captioning or text-guided region grounding** (one additional single-image task).
- [x] **Bi-temporal change analysis** — change description / change-based VQA, with spatial change maps where masks are available.
- [x] **Cross-modal (optical–SAR) pair analysis** — joint information extraction from co-registered pairs.
- [x] **Agentic orchestration** — automatic task routing, model selection, sequencing, and parameter governance.

### Additional Capabilities

- Multi-turn conversational memory (session-scoped, no re-upload needed for follow-ups).
- Confidence scoring with bounded fallback/retry on low-confidence outputs.
- Structured, auditable execution traces exportable as JSON / HTML / PDF.
- Visual overlays (bounding boxes, segmentation masks, change heatmaps).
- Downloadable per-session reports.
- Deterministic demo / mock mode for environments without GPU or model access.

---

## Supported Inputs

| Input Type | Description | Supported Tasks |
|---|---|---|
| **Single Image** | One optical/multispectral **or** SAR image | VQA, captioning, text-guided region grounding |
| **Cross-Modal Pair** | Co-registered optical/multispectral + SAR image of the same geographic area | Joint information extraction, cross-modal analysis, fusion-based classification |
| **Bi-Temporal Pair** | Two spatially corresponding images acquired at different times | Change detection, change description, change-based VQA, change mapping |

### Formats

- **GeoTIFF / TIFF** — primary geospatial format for production.
- **PNG / JPEG** — accepted for public benchmark datasets (VRSBench, RSVQA, CDVQA).

---

## Representative Queries

> *"Describe the land-cover and major objects visible in this image."*
> — Single-image captioning / scene understanding

> *"Highlight the water body referred to in the query."*
> — Text-guided region grounding

> *"What changed between these two dates, and where did the change occur?"*
> — Bi-temporal change description + localization

> *"Use the optical and SAR images together to identify built-up and water-covered regions."*
> — Cross-modal (optical–SAR) fusion

> *"Has the built-up area increased, decreased, or remained unchanged?"*
> — Bi-temporal change VQA with trend answer

---

## System Architecture

SatQuery AI is composed of four layers:

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND (Web GUI)                       │
│   Upload • Query box • Map view • Result panel • Reports    │
└───────────────────────────┬─────────────────────────────────┘
                            │  (REST / WebSocket)
┌───────────────────────────▼─────────────────────────────────┐
│               AGENTIC CONTROLLER (Role 1)                   │
│  Intent classification → Input validation → Routing → DAG   │
│  → Tool execution → Confidence/Fallback → Integration       │
│  → Audit trace → Response                                   │
│  + Multi-turn session memory (LangGraph Checkpointer)       │
└───────────────────────────┬─────────────────────────────────┘
                            │  (tool contracts, Pydantic I/O)
┌───────────────────────────▼─────────────────────────────────┐
│              SPECIALIST MODEL SUITE (Roles 4 & 6)           │
│  RS-VQA • Captioning • Grounding • Change-VQA •             │
│  Optical–SAR Fusion                                         │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│        BACKEND, DATA & GEOSPATIAL SERVICES (Roles 2 & 3)    │
│  Ingestion • Preprocessing • Model serving • GIS/CRS        │
│  • Co-registration checks • SAR/optical processing          │
└─────────────────────────────────────────────────────────────┘
```

---

## Agentic Orchestration

The agentic controller is the decision-making brain of SatQuery AI. It is **Role 1 (AI Agent Developer)**'s responsibility.

### Execution Pipeline

```
User Query + Image(s)
        │
        ▼
INTENT CLASSIFICATION            classify query into SINGLE_VQA,
                                 REGION_GROUNDING, BI_TEMPORAL_CHANGE,
                                 CROSS_MODAL_OPTICAL_SAR
        │
        ▼
INPUT / CONTEXT VALIDATION       check count, modality, format,
                                 metadata, co-registration, pairing
        │
        ▼
TOOL + PARAMETER ROUTING         select specialist contracts from
                                 registry; build structured params
        │
        ▼
DYNAMIC WORKFLOW / TASK DAG      compose multi-step pipelines
        │
        ├──────────────────────► SPECIALIST TOOL CALL(S)
        │                               │
        └──────────────────────► SESSION STATE / MEMORY
                                        │
                                        ▼
                              OUTPUT + CONFIDENCE CHECK
                                   │        │
                                ≥ 0.65     < 0.65
                                   │        │
                                   ▼        ▼
                              INTEGRATE   FALLBACK / RETRY
                              RESULT      (adjust params, switch
                                          backup model, re-prompt;
                                          bounded retries)
                                        │
                                        ▼
                              EVIDENCE + TRACE + RESPONSE
```

### Tool Contracts

Each specialist capability is exposed behind a **stable Pydantic contract**, so the router depends on interfaces, not implementations:

| Tool | Inputs | Expected Output |
|---|---|---|
| `single_image_vqa` | `image_path`, `query` | Text answer / visual interpretation |
| `region_grounding` | `image_path`, `target_object` | Bounding boxes / grounded regions |
| `bitemporal_change_analysis` | `img_t1`, `img_t2`, `query` | Change mask + text description |
| `cross_modal_fusion` | `optical_img`, `sar_img`, `query` | Joint analysis text (+ optional masks) |

### Stateful Multi-turn Memory

The agent preserves active visual context across follow-up turns (e.g., "describe this image" → "now highlight water bodies" without re-upload). State is keyed by `session_id` and persisted via **LangGraph Checkpointers** (in-memory `MemorySaver` for development; Postgres-backed for production).

Binary image data is **not** stored in the graph state — only stable identifiers and metadata.

### Confidence, Fallback & Self-Correction

- Model outputs below a configurable confidence threshold (default **0.65**) trigger a fallback loop rather than a terminal failure.
- Fallback actions: adjust parameters, switch to a backup model/VLM, re-prompt with contextual hints.
- Bounded retries with a clear terminal response when all paths fail.
- Failure taxonomy: input validation failure, metadata/context issue, model timeout, low confidence, dependency failure, unexpected exception.
- Every retry/switch is recorded in the trace for observability.
- Deterministic **mock/demo path** guarantees the agent can run end-to-end even when models are unavailable.

### Auditable Execution Trace

Every run produces a trace containing:

| Field | Purpose |
|---|---|
| `request_id` | Reconstruct one execution end-to-end |
| `session_id` | Tie multiple turns to one conversation |
| `selected_workflow` | Explain why a specialist path was chosen |
| `tool / model name` | Identify the capability invoked |
| `input IDs / parameters` | Record what the tool received |
| `duration + status` | Measure execution and locate failures |
| `confidence` | Make acceptance/fallback inspectable |
| `output references` | Point to masks, evidence, reports |
| `fallback reason` | Explain self-correction behaviour |

---

## Specialist Model Suite

| Specialist | Purpose | Adaptation / Training |
|---|---|---|
| **RS-VQA Model** | Single-image visual question answering | Fine-tuned on BigEarthNet, RSVQA |
| **Captioning Model** | Scene description, land-cover narration | Fine-tuned on RS captioning datasets |
| **Grounding Model** | Text-guided region localisation (boxes/masks) | Adapted for RS entities (water, built-up, roads, vegetation) |
| **Change-VQA / Change-Understanding Model** | Bi-temporal change description + VQA | Evaluated on CDVQA |
| **Optical–SAR Fusion Model** | Cross-modal joint information extraction | Trained on BigEarthNet co-registered Sentinel-1/Sentinel-2 pairs |

A generic off-the-shelf VLM without remote-sensing adaptation does **not** satisfy project requirements.

---

## Technology Stack

| Area | Technology |
|---|---|
| **Agent framework** | LangGraph (stateful DAG orchestration) + async Python |
| **Tool contracts** | Pydantic v2 (strict input/output schemas) |
| **LLM/VLM routing** | OpenAI / Gemini API / local vLLM instance (configurable) |
| **State persistence** | LangGraph Checkpointers (MemorySaver dev, Postgres prod) |
| **Backend** | FastAPI (REST/WebSocket), Uvicorn |
| **Computer Vision** | PyTorch, torchvision, OpenCV, detectron2 / mmdet (as applicable) |
| **Geospatial** | GDAL, rasterio, geopandas, shapely, pyproj |
| **Frontend** | React / Next.js, MapLibre GL / Leaflet for geospatial overlays, TailwindCSS |
| **Model serving** | TorchServe / Triton Inference Server (production), FastAPI wrappers (dev) |
| **Trace & reporting** | JSON Schema + WeasyPrint / ReportLab for PDF reports |
| **Data & experiment tracking** | HuggingFace Datasets, Weights & Biases (optional) |
| **Containerization** | Docker, docker-compose |

---

## Datasets

### Training / Fine-Tuning

| Dataset | Purpose | Link |
|---|---|---|
| **BigEarthNet** | Primary dataset for remote-sensing adaptation of image-text representations using co-registered **Sentinel-1 SAR** + **Sentinel-2 multispectral** imagery with text annotations. | [arXiv:2603.29630](https://arxiv.org/abs/2603.29630) |

All training datasets are open-source.

### Public Evaluation Benchmarks

| Benchmark | Evaluates |
|---|---|
| **VRSBench** | Single-image captioning, grounding, VQA |
| **RSVQA** | Single-image remote-sensing VQA |
| **CDVQA** | Multitemporal change-based VQA |

### ISRO/SAC Evaluation Set (Final Judging)

- Pre-georeferenced, co-registered **Cartosat-2S optical** and **RISAT SAR** image pairs.
- Task-specific reference answers, labels, bounding boxes, or masks.
- Evaluation annotations are **not disclosed** to participating teams.

---

## Evaluation & Judging Criteria

Final evaluation uses public benchmark test splits and the ISRO/SAC evaluation dataset. Scores are normalized before being combined across metrics.

| Criterion | Weight | Description |
|---|---|---|
| **Single-Image VQA Accuracy** | High | Correctness and relevance of answers on VRSBench / RSVQA. |
| **Captioning / Grounding Quality** | Medium | Caption relevance (BLEU/CIDEr/meteor); grounding IoU / localisation accuracy. |
| **Change Understanding** | High | Change-VQA accuracy, change-description relevance, change-map quality (CDVQA + ISRO set). |
| **Cross-Modal (Optical–SAR) Analysis** | High | Accuracy of fused extraction (built-up, water, etc.) on co-registered pairs. |
| **Agentic Orchestration** | High | Correctness of task routing, model selection, parameter governance, audit-trail completeness. |
| **Evidence Grounding & Confidence** | Medium | Quality of visual evidence; calibration of confidence scores. |
| **GUI / UX Quality** | Medium | Usability, input validation, visualization clarity, report export. |
| **Remote-Sensing Adaptation** | Required (threshold) | Demonstrated domain adaptation — generic VLMs without RS adaptation do not qualify. |

---

## Project Structure

```
satquery-ai/
├── README.md                          ← You are here
├── agent/                             ← ROLE 1 — AI Agent Developer
│   ├── README.md
│   ├── __init__.py
│   ├── agent_engine.py                ← LangGraph state graph / main loop
│   ├── controller.py                  ← (alias) high-level entry point
│   ├── router.py                      ← Intent classifier / route selection
│   ├── task_classifier.py             ← Query → task type mapping
│   ├── validators.py                  ← Input + contract validation
│   ├── input_validator.py
│   ├── state.py                       ← Session + visual-context state
│   ├── confidence.py                  ← Confidence aggregation / gates
│   ├── fallback.py                    ← Retry + backup-model routing
│   ├── tracer.py                      ← Auditable trace generator
│   ├── audit.py
│   ├── reports.py                     ← JSON/HTML/PDF evidence output
│   ├── model_registry.py              ← Specialist-tool registry
│   ├── workflow_planner.py            ← DAG planner
│   ├── tool_executor.py               ← Tool dispatch
│   ├── output_integrator.py           ← Fuse textual + spatial results
│   ├── tools/                         ← Tool wrappers (one per contract)
│   │   ├── single_image_vqa.py
│   │   ├── region_grounding.py
│   │   ├── bitemporal_change.py
│   │   └── cross_modal_fusion.py
│   ├── prompts/
│   ├── schemas/                       ← Pydantic contracts
│   ├── utils/
│   └── tests/
│       ├── test_contracts.py
│       ├── test_routing.py
│       ├── test_memory.py
│       ├── test_fallback.py
│       └── test_trace.py
│
├── backend/                           ← ROLE 2 — Data Engineer
│   ├── api/                           ← FastAPI routes & schemas
│   ├── preprocessing/                 ← Image ingestion, format conversion
│   ├── serving/                       ← Model-serving layer
│   └── storage/                       ← Session & result storage
│
├── geo/                               ← ROLE 3 — Remote Sensing & GIS
│   ├── gis_utils.py                   ← CRS, co-registration, metadata
│   ├── sar_preprocess.py              ← SAR-specific preprocessing
│   ├── optical_preprocess.py          ← Optical/multispectral preprocessing
│   └── metrics/                       ← RS-specific evaluation metrics
│
├── cv/                                ← ROLE 4 — Computer Vision
│   ├── grounding.py                   ← Text-guided region localisation
│   ├── change_detection.py            ← Bi-temporal change masks
│   ├── segmentation.py                ← Land-cover / built-up / water
│   ├── visualisation.py               ← Overlay rendering
│   └── utils/
│
├── frontend/                          ← ROLE 5 — Frontend Developer
│   ├── public/
│   └── src/
│       ├── components/                ← Uploader, QueryBox, ResultPanel, Map
│       ├── pages/
│       └── App.*
│
├── models/                            ← ROLE 6 — AI/ML & VLM
│   ├── rs_vqa/
│   ├── captioning/
│   ├── grounding/
│   ├── change_vqa/
│   ├── optical_sar_fusion/
│   ├── adapters/                      ← PEFT / LoRA RS adapters
│   └── training/                      ← Fine-tuning scripts (BigEarthNet, etc.)
│
├── data/                              ← Dataset loaders & samples
│   ├── bigearthnet/
│   ├── vrsbench/
│   ├── rsvqa/
│   └── cdvqa/
│
├── configs/                           ← YAML/JSON configs
├── notebooks/                         ← Exploration & demos
├── tests/                             ← End-to-end / integration tests
├── scripts/                           ← Utility & deployment scripts
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── environment.yml
└── pyproject.toml
```

---

## Team Roles

| # | Role | Primary Responsibilities |
|---|---|---|
| 1 | **AI Agent Developer** | Agentic controller, LangGraph DAG, intent classification, input validation, tool registry, workflow planning, confidence gating, fallback/self-correction, multi-turn memory, audit trace, reports, output integration. |
| 2 | **Data Engineer (Backend)** | Data pipelines, image ingestion/preprocessing, format conversion, model-serving infrastructure, REST/WebSocket APIs, storage, containerization. |
| 3 | **Remote Sensing & GIS Developer** | Sensor-characteristic handling, CRS/georeferencing, co-registration verification, SAR/optical preprocessing, domain feature engineering, RS-specific metrics. |
| 4 | **Computer Vision Developer** | Grounding, change-detection, segmentation models; spatial-output rendering (boxes, masks, heatmaps); post-processing. |
| 5 | **Frontend Developer** | Interactive web GUI, geospatial map visualisation with overlays, query interface, result panels, confidence indicators, report-export UI. |
| 6 | **AI/ML & VLM Developer** | VLM selection, remote-sensing fine-tuning on BigEarthNet, RS-VQA / captioning / grounding / change-VQA models, optical–SAR fusion, adapters. |

---

## Development Roadmap

Build order is deliberately **mock-first and contract-first** to de-risk integration:

### Phase 1 — Core Fundamentals (Days 1–7)
- Learn state machines, tool registration, Pydantic schemas, structured outputs, fallback loops.
- Build a minimal agent that selects between toy tools (e.g., Weather, Math) and writes an auditable trace.

### Phase 2 — Intermediate Integration (Days 8–15)
- Design Pydantic contracts for the four core RS workflows.
- Implement the model router with **mock model functions** returning dummy spatial coordinates and text summaries to prove end-to-end routing.

### Phase 3 — Advanced Agentic Features (Days 16–25)
- Add multi-turn memory via LangGraph Checkpointers.
- Add confidence-gated fallback and self-correction.
- Generate JSON / HTML / PDF execution traces.
- Add structured tool contracts and contract tests.

### Phase 4 — Real Model Integration (Days 26+)
- Swap mocks for real specialist implementations as they become available.
- Integrate frontend visualization and report download.
- End-to-end evaluation on VRSBench / RSVQA / CDVQA.
- Hardening, golden-demo case, demo readiness.

### Definition of Done (D0 → D7)

| Stage | Definition |
|---|---|
| **D0 — Contracted** | Schemas exist for tools, state, confidence, errors, traces. |
| **D1 — Vertical Slice** | One image + one query completes end-to-end with mock inference. |
| **D2 — Spatially Aware** | Relevant image context and spatial references preserved through the workflow. |
| **D3 — Stateful** | A follow-up turn reuses active image context without re-upload. |
| **D4 — Resilient** | Low-confidence results trigger a bounded fallback/retry path and remain observable. |
| **D5 — Tool-Complete** | All four core workflows are registered behind stable contracts. |
| **D6 — Auditable** | Trace contains route, tools, parameters, timings, confidence, status, outputs. |
| **D7 — Demo Ready** | Real model or deterministic fallback path + trace generation work together. |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/ramrounakmukherjee-blip/demo-prototype-satquery-ai.git
cd demo-prototype-satquery-ai

# Set up environment
conda env create -f environment.yml
conda activate satquery-ai

# Install dependencies
pip install -r requirements.txt
```

### Prerequisites

- Python 3.10+
- Node.js 18+ (for frontend)
- PyTorch 2.x (with CUDA for GPU acceleration)
- GDAL / rasterio for GeoTIFF handling
- Docker & docker-compose (optional, for deployment)

---

## Usage

### High-Level User Flow

1. **Upload** one or more images (single optical/SAR, co-registered optical–SAR pair, or bi-temporal pair) in GeoTIFF/TIFF (or PNG/JPEG for benchmarks).
2. **Type** a natural-language query.
3. The **agentic controller** automatically classifies the task, validates inputs, selects and runs the appropriate specialist model(s), and combines results with confidence scores.
4. **View** the answer with visual evidence (bounding boxes, change masks, highlighted regions) and an auditable execution summary.
5. **Download** a report (JSON/HTML/PDF) including the query, answer, visuals, confidence, and full execution trace.

### Example (Python, mock path)

```python
from agent import SatQueryAgent

agent = SatQueryAgent.from_config("configs/agent.yaml", mock_mode=True)
result = agent.run(
    query="What changed between these two dates, and where?",
    images=[image_t1, image_t2],
)
print(result.answer)      # natural-language answer
print(result.visuals)     # change mask / overlays
print(result.confidence)  # confidence score
print(result.trace)       # auditable execution log
```

---

## Deliverables

- [ ] **Interactive web GUI** with an agentic remote-sensing AI backend.
- [ ] **Source code** for all six role packages (agent, backend, geo, cv, frontend, models).
- [ ] **Remote-sensing adapted models** with fine-tuning scripts and checkpoints.
- [ ] **Test suite** (contract, routing, memory, fallback, trace, integration, e2e).
- [ ] **Demo script and golden-demo case**.
- [ ] **Documentation** — this README, API docs, agent-module docs, demo walkthrough.
- [ ] **Downloadable execution reports** (JSON/HTML/PDF).

---

## Acknowledgments

- **Indian Space Research Organisation (ISRO)** and the **Department of Space** for framing the problem and providing the evaluation framework.
- Authors of the open datasets and benchmarks used in this project: BigEarthNet, VRSBench, RSVQA, and CDVQA.
- The open-source communities behind LangGraph, Pydantic, PyTorch, GDAL/rasterio, FastAPI, React, and the other projects that make this work possible.

---

## Organization

| Field | Detail |
|---|---|
| **Organization** | [Indian Space Research Organisation (ISRO)](https://www.isro.gov.in/) |
| **Department** | Dept. of Space / ISRO |
| **Category** | Software |
| **Theme** | Space Technology |

---

## License

*To be added.*

---

<div align="center">

**SatQuery AI — Making satellite imagery understandable to everyone, one natural-language query at a time.** 🌍🛰️

</div>

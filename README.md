# SatQuery AI

<div align="center">

**An Interactive Vision-Language Assistant for Multimodal Remote Sensing Image Analysis through Text Queries**

*An agentic, query-driven framework that intelligently selects, orchestrates, and composes remote-sensing specialist models to answer natural-language questions about satellite imagery — from single-image understanding to cross-modal optical–SAR fusion and bi-temporal change detection.*

![Organization: ISRO](https://img.shields.io/badge/Organization-ISRO-blue)
![Department](https://img.shields.io/badge/Department-Dept.%20of%20Space%2FISRO-darkblue)
![Category](https://img.shields.io/badge/Category-Software-green)
![Theme](https://img.shields.io/badge/Theme-Space%20Technology-purple)

</div>

---

## Table of Contents

- [The Problem](#the-problem)
- [The Solution: SatQuery AI](#the-solution-satquery-ai)
- [Key Innovation — Agentic Orchestration](#key-innovation--agentic-orchestration)
- [Input Scope](#input-scope)
- [Functional Capabilities](#functional-capabilities)
- [Representative Queries](#representative-queries)
- [System Architecture](#system-architecture)
- [Datasets](#datasets)
- [Evaluation & Judging Criteria](#evaluation--judging-criteria)
- [Tech Stack & Team Roles](#tech-stack--team-roles)
- [Repository Structure](#repository-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Deliverables](#deliverables)
- [Contributing](#contributing)
- [License](#license)

---

## The Problem

### Background

Remote-sensing imagery underpins a vast range of societal and scientific applications:

| Domain | Example Applications |
|---|---|
| **Agriculture** | Crop-health monitoring, yield estimation, irrigation planning |
| **Disaster Management** | Flood mapping, damage assessment, post-event response |
| **Urban Planning** | Sprawl analysis, infrastructure mapping, growth modelling |
| **Forest Monitoring** | Deforestation detection, canopy-cover estimation, biomass mapping |
| **Water Resources** | Reservoir monitoring, wetland delineation, flood-risk assessment |
| **Environmental Analysis** | Land-cover classification, habitat mapping, pollution tracking |

### Why Existing Solutions Fall Short

Most contemporary remote-sensing AI tools are **siloed, single-task applications** — built for one predefined job such as:

- Land-cover classification
- Object detection
- Visual question answering (VQA)
- Change detection

These systems place a heavy burden on users, who must:

1. Understand satellite sensor characteristics (optical, multispectral, SAR)
2. Navigate GIS workflows and coordinate-reference systems
3. Select the right model for each task
4. Tune task-specific parameters and thresholds
5. Manually integrate outputs across modalities and time steps

As a result, **non-expert users struggle to extract meaningful information from satellite imagery** using simple natural-language queries.

### The Multimodal Challenge

Operational remote-sensing questions *cannot reliably be answered from a single optical image*. Relevant information is often distributed across:

- **Multiple observations** acquired at different times (bi-temporal / multitemporal).
- **Different sensors** — optical/multispectral imagery provides rich spectral and contextual cues, while **Synthetic Aperture Radar (SAR)** offers complementary structural information and penetrates cloud cover for day/night acquisition.
- **Co-registered optical–SAR pairs** that together yield more complete and reliable information than either modality alone.
- **Bi-temporal pairs** required to detect, localise, and interpret changes over time.

### Why Generic VLMs Are Not Enough

Off-the-shelf Large Language Models (LLMs) and Vision-Language Models (VLMs) cannot perform these specialised tasks reliably without **adaptation to remote-sensing imagery, sensor physics, and domain-specific terminology**. SatQuery AI addresses this gap through remote-sensing fine-tuning, domain adaptation, and a multi-specialist architecture rather than relying on a single generic model.

---

## The Solution: SatQuery AI

SatQuery AI is a **software-based, agentic vision-language assistant** that analyses single and paired remote-sensing images through natural-language queries.

- **Single-image understanding** is provided as a mandatory baseline (VQA + captioning or grounding).
- The **principal focus** is *joint reasoning over paired cross-modal (optical + SAR) and bi-temporal imagery*.

Instead of applying one monolithic VLM, SatQuery AI uses an **agentic controller** that:

1. Interprets the user's natural-language query.
2. Validates the inputs (number, modality, format, geospatial compatibility).
3. Selects and sequences the appropriate specialist models from a registry.
4. Executes the workflow with permitted parameters.
5. Combines textual and spatial outputs, estimates confidence, and returns **evidence-grounded results** (with visual overlays, bounding boxes, change masks, or heatmaps).
6. Produces an **auditable execution summary** for transparency and reproducibility.

---

## Key Innovation — Agentic Orchestration

The novelty of SatQuery AI lies in its **agentic, query-driven orchestration layer** — the focus of the AI Agent Development role on this project.

Rather than requiring users to manually chain models, the controller acts as an intelligent routing layer:

```
User Query + Image(s)
        │
        ▼
┌─────────────────────────┐
│   Query Interpreter      │  ← Classify task type, extract entities
│   (Task Classifier)      │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   Input Validator        │  ← Check count, modality, format, metadata,
│                          │    co-registration, compatibility
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   Model Registry /       │  ← Look up candidate specialists:
│   Tool Selector          │    • RS-VQA / Captioning
│                          │    • Grounding model
│                          │    • Change-VQA / Change detection
│                          │    • Optical–SAR fusion / extraction
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   Workflow Planner       │  ← Sequence & compose tools (e.g., detect →
│                          │    caption → fuse → answer)
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   Tool Executor          │  ← Run each specialist with permitted params
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   Output Integrator      │  ← Merge textual + spatial outputs,
│   & Confidence Estimator │    estimate confidence, attach visual evidence
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│   Response Builder       │  ← Return natural-language answer + visuals
│   + Audit Trail          │    + downloadable report + execution trace
└─────────────────────────┘
```

### Observable Execution Trace

While internal planning is opaque by design, the system exposes a **fully auditable execution trace** containing:

- Identified task type(s)
- Selected models / tools (by name)
- Key parameters used
- Intermediate outputs and confidence scores
- Final textual response with visual evidence

This trace is what gets evaluated and is what builds user trust.

---

## Input Scope

SatQuery AI accepts three input configurations:

| Input Type | Description | Supported Tasks |
|---|---|---|
| **Single Image** | One optical/multispectral **or** SAR image | Captioning, VQA, text-guided region grounding |
| **Cross-Modal Pair** | Co-registered optical/multispectral + SAR image of the same geographic area | Joint information extraction, cross-modal analysis, fusion-based classification |
| **Bi-Temporal Pair** | Two spatially corresponding images of the same area acquired at different times | Change detection, change description, change-based VQA, spatial change mapping |

### Supported Formats

- **GeoTIFF / TIFF** — primary geospatial imagery format (preferred for production use).
- **PNG / JPEG** — accepted only for prescribed public benchmark datasets (VRSBench, RSVQA, CDVQA).

---

## Functional Capabilities

### Mandatory Functional Scope

| Capability | Details |
|---|---|
| **Remote-Sensing Adaptation** | At least one visual / vision-language component is fine-tuned or domain-adapted using BigEarthNet or equivalent open-source remote-sensing data. |
| **Single-Image Baseline** | **Visual Question Answering (VQA) is mandatory**, plus at least one of: (a) captioning / scene description, or (b) text-guided region grounding. |
| **Multi-Image Change Analysis** | Change description **or** change-based VQA from a bi-temporal pair is mandatory. A spatial change map is generated where reference masks are available. |
| **Cross-Modal Pair Analysis** | The system extracts complementary information from co-registered optical/multispectral + SAR pairs (e.g., joint built-up / water-body detection). |
| **Agentic Orchestration** | The controller automatically selects, sequences, and executes appropriate specialist models based on the query and input configuration. |

---

## Representative Queries

SatQuery AI is designed to answer questions like:

> *"Describe the land-cover and major objects visible in this image."*
> — Single-image captioning / scene understanding

> *"Highlight the water body referred to in the query."*
> — Text-guided region grounding

> *"What changed between these two dates, and where did the change occur?"*
> — Bi-temporal change description + change localisation

> *"Use the optical and SAR images together to identify built-up and water-covered regions."*
> — Cross-modal (optical–SAR) fusion / extraction

> *"Has the built-up area increased, decreased, or remained unchanged?"*
> — Bi-temporal change VQA with qualitative trend

---

## System Architecture

SatQuery AI is composed of the following components:

### 1. Agentic Controller (AI Agent Developer — this role)
The "brain" of the system. Responsibilities:
- **Query parsing & task classification** — NLU over natural-language input to map to one or more task types (captioning, VQA, grounding, change-VQA, cross-modal fusion).
- **Input validation** — verify image count, modality, geospatial co-registration, format, and metadata compatibility.
- **Model registry & tool selection** — maintain a registry of available specialist models and select the best fit per task and input configuration.
- **Workflow planning & sequencing** — compose multi-step pipelines (e.g., grounding → crop → caption for a "highlight X and describe it" query).
- **Parameter governance** — ensure only permitted, safe parameters are passed to downstream models.
- **Confidence estimation** — aggregate per-model confidences into a calibrated response-level score.
- **Execution trace generation** — produce an auditable log of the entire pipeline.
- **Output integration** — fuse textual answers with spatial outputs (bounding boxes, masks, change maps) into a unified response.

### 2. Specialist Model Suite

| Specialist | Purpose | Adaptation |
|---|---|---|
| **RS-VQA Model** | Single-image visual question answering | Fine-tuned / adapted on BigEarthNet, RSVQA |
| **Captioning Model** | Scene description, land-cover narration | Fine-tuned on remote-sensing captions |
| **Grounding Model** | Text-guided region localisation (bounding box / mask) | Adapted for RS entities (water, built-up, roads, etc.) |
| **Change-VQA / Change-Understanding Model** | Bi-temporal change description, change VQA | Evaluated on CDVQA |
| **Optical–SAR Fusion Model** | Cross-modal joint information extraction | Trained on BigEarthNet co-registered Sentinel-1/Sentinel-2 pairs |

### 3. Frontend GUI / Web Application
- Interactive image upload (with drag-and-drop)
- Natural-language query input
- Visual overlay of results (bounding boxes, change masks, heatmaps)
- Confidence indicators
- Execution-summary panel
- Downloadable PDF/JSON reports

### 4. Backend Services
- Image ingestion, format conversion, and preprocessing
- Model serving (REST/gRPC endpoints)
- Geospatial metadata parsing and co-registration checks
- Result storage and session management

---

## Datasets

### Training / Fine-Tuning

| Dataset | Purpose | Link |
|---|---|---|
| **BigEarthNet** | Primary dataset for remote-sensing adaptation of image–text representations using co-registered **Sentinel-1 SAR** and **Sentinel-2 multispectral** imagery with diverse text annotations. | [arXiv:2603.29630](https://arxiv.org/abs/2603.29630) |

All training datasets are open-source and publicly available.

### Public Evaluation Benchmarks

| Benchmark | Evaluates |
|---|---|
| **VRSBench** | Single-image captioning, grounding, and visual question answering |
| **RSVQA** | Single-image remote-sensing VQA |
| **CDVQA** | Multitemporal change-based visual question answering |

### ISRO/SAC Evaluation Set (Final Judging)

- Pre-georeferenced and co-registered **Cartosat-2S optical** and **RISAT SAR** image pairs.
- Task-specific reference answers, labels, bounding boxes, or masks (as applicable).
- Evaluation annotations are **not disclosed** to participating teams.

---

## Evaluation & Judging Criteria

Final evaluation uses prescribed public benchmark test subsets and the ISRO/SAC evaluation dataset. Scores are normalised before combining across different metrics.

| Criterion | Weight | Description |
|---|---|---|
| **Single-Image VQA Accuracy** | High | Correctness and relevance of answers on VRSBench / RSVQA splits. |
| **Captioning / Grounding Quality** | Medium | BLEU/CIDEr/meteor for captions; IoU / localisation accuracy for grounding. |
| **Change-Understanding Performance** | High | Change-VQA accuracy, change-description relevance, change-map quality (CDVQA + ISRO set). |
| **Cross-Modal (Optical–SAR) Analysis** | High | Accuracy of fused extraction (built-up, water, etc.) on co-registered pairs. |
| **Agentic Orchestration** | High | Correctness of task routing, model selection, parameter governance, and audit-trail completeness. |
| **Evidence Grounding & Confidence** | Medium | Quality of visual evidence, calibration of confidence scores. |
| **GUI / UX Quality** | Medium | Usability, input validation, visualisation clarity, report export. |
| **Remote-Sensing Adaptation** | Required (threshold) | Demonstrated domain adaptation (no generic off-the-shelf VLM accepted). |

> **Note:** A generic LLM or VLM used without remote-sensing adaptation will **not** satisfy the requirements.

---

## Tech Stack & Team Roles

SatQuery AI is a cross-disciplinary effort spanning six roles:

| # | Role | Primary Responsibilities |
|---|---|---|
| 1 | **AI Agent Developer** *(this role — my focus)* | Agentic controller, task classification, workflow planning, model registry, tool orchestration, confidence estimation, execution trace, output integration. |
| 2 | **Data Engineer (Backend Developer)** | Data pipelines, image ingestion/preprocessing, geospatial format handling, model serving infrastructure, APIs, databases. |
| 3 | **Remote Sensing & GIS Developer** | Sensor characteristics, georeferencing/co-registration checks, domain-specific feature engineering, SAR/optical preprocessing, evaluation-metric implementation. |
| 4 | **Computer Vision Developer** | Change-detection models, grounding models, image-processing pipelines, spatial-output rendering (masks, bounding boxes, heatmaps). |
| 5 | **Frontend Developer** | Interactive web GUI, image visualisation with overlays, query interface, result panels, report export. |
| 6 | **AI/ML & VLM Developer** | VLM selection, remote-sensing fine-tuning on BigEarthNet, captioning/VQA/change-VQA models, optical–SAR fusion models. |

---

## Repository Structure

```
demo-prototype-satquery-ai/
├── README.md                          ← You are here
├── agent/                             ← ROLE 1 — AI Agent Developer (active ✅)
│   ├── README.md                      ← Agent-module documentation
│   ├── __init__.py                    ← Package docstring & exports
│   ├── controller.py                  ← Main agentic orchestration loop
│   ├── task_classifier.py             ← Query → task type mapping
│   ├── input_validator.py             ← Image count / modality / format checks
│   ├── model_registry.py              ← Registry of specialist models & tools
│   ├── workflow_planner.py            ← Multi-step pipeline composition
│   ├── tool_executor.py               ← Tool dispatch & parameter governance
│   ├── output_integrator.py           ← Fusion of textual + spatial results
│   ├── confidence.py                  ← Confidence estimation & calibration
│   ├── audit.py                       ← Execution-trace / audit-log generation
│   ├── prompts/                       ← LLM prompt templates
│   │   └── __init__.py
│   ├── schemas/                       ← Typed schemas (Pydantic / dataclasses)
│   │   └── __init__.py
│   ├── utils/                         ← Shared helpers (logging, config, etc.)
│   │   └── __init__.py
│   └── tests/                         ← Agent unit & integration tests
│       ├── __init__.py
│       ├── test_controller.py
│       ├── test_task_classifier.py
│       ├── test_input_validator.py
│       └── test_workflow_planner.py
│
├── backend/                           ← Data Engineer (role 2)
│   ├── api/                           ← REST/gRPC service endpoints
│   ├── preprocessing/                 ← Image ingestion, format conversion
│   ├── serving/                       ← Model-serving layer
│   └── storage/                       ← Session & result storage
│
├── geo/                               ← Remote Sensing & GIS (role 3)
│   ├── gis_utils.py                   ← CRS, co-registration, metadata parsing
│   ├── sar_preprocess.py              ← SAR-specific preprocessing
│   ├── optical_preprocess.py          ← Optical/multispectral preprocessing
│   └── metrics/                       ← RS-specific evaluation metrics
│
├── cv/                                ← Computer Vision (role 4)
│   ├── grounding.py                   ← Text-guided region localisation
│   ├── change_detection.py            ← Bi-temporal change masks
│   ├── visualisation.py               ← Overlay rendering (boxes, masks, heatmaps)
│   └── utils/
│
├── frontend/                          ← Frontend Developer (role 5)
│   ├── src/
│   │   ├── components/                ← Uploader, QueryBox, ResultPanel, Map
│   │   ├── pages/
│   │   └── App.*
│   └── public/
│
├── models/                            ← AI/ML & VLM (role 6)
│   ├── rs_vqa/                        ← Remote-sensing VQA model
│   ├── captioning/                    ← Scene-captioning model
│   ├── change_vqa/                    ← Change-VQA / change-understanding model
│   ├── optical_sar_fusion/            ← Cross-modal fusion model
│   ├── adapters/                      ← PEFT / LoRA adapters for RS adaptation
│   └── training/                      ← Fine-tuning scripts (BigEarthNet, etc.)
│
├── data/                              ← Dataset loaders & sample data
│   ├── bigearthnet/
│   ├── vrsbench/
│   ├── rsvqa/
│   └── cdvqa/
│
├── configs/                           ← YAML/JSON configs for models & pipelines
├── notebooks/                         ← Exploration & demo notebooks
├── tests/                             ← End-to-end & integration tests
├── scripts/                           ← Utility & deployment scripts
├── requirements.txt
├── environment.yml
└── pyproject.toml
```

> **Note:** The `agent/` package (Role 1) is currently scaffolded on disk. The remaining directories are planned and will be scaffolded as the respective team members begin work.


---

## Installation & Setup

*(Coming soon — will be populated as components are built.)*

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
- PyTorch 2.x (with CUDA for GPU acceleration)
- GDAL / rasterio for GeoTIFF handling
- Node.js 18+ (for frontend)
- Access to open-source remote-sensing datasets (BigEarthNet, VRSBench, RSVQA, CDVQA)

---

## Usage

*(Coming soon — workflow will be updated as the agentic controller and specialist models are integrated.)*

### High-Level User Flow

1. **Upload** one or more images (single optical/SAR, co-registered optical–SAR pair, or bi-temporal pair) in GeoTIFF/TIFF (or PNG/JPEG for benchmarks).
2. **Type** a natural-language query (e.g., *"What changed in this area between the two dates?"*).
3. SatQuery AI's **agentic controller** automatically:
   - Classifies the task,
   - Validates inputs,
   - Selects and runs the appropriate specialist model(s),
   - Combines results with confidence scores.
4. **View** the answer with visual evidence (bounding boxes, change masks, highlighted regions) and an auditable execution summary.
5. **Download** a report (PDF/JSON) including the query, answer, visuals, confidence, and execution trace.

---

## Deliverables

- [x] **Interactive GUI / Web Application** with an agentic remote-sensing AI backend.
- [ ] **Source code** for all components (agent, backend, CV, geo, frontend, models).
- [ ] **Fine-tuned / adapted models** for remote-sensing tasks (with checkpoints).
- [ ] **Test suite** and demonstration scripts.
- [ ] **Documentation** including this README, API docs, and a demo walkthrough.

---

## Contributing

This is a team project with six defined roles. Contributions should be made via pull requests to the `arena/01a0999a-demo-prototype-satquery-ai` branch.

| Branch | Purpose |
|---|---|
| `main` | Stable releases |
| `arena/01a0999a-demo-prototype-satquery-ai` | Active development (this branch) |

---

## Organization

| Field | Detail |
|---|---|
| **Organization** | [ISRO](https://www.isro.gov.in/) — Indian Space Research Organisation |
| **Department** | Dept. of Space / ISRO |
| **Category** | Software |
| **Theme** | Space Technology |

---

## License

*(License to be added.)*

---

<div align="center">

**SatQuery AI — Making satellite imagery understandable to everyone, one natural-language query at a time.** 🌍🛰️

</div>

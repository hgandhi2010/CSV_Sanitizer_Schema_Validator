# Enterprise CSV Sanitizer & Schema Validator

A production-grade command-line interface (CLI) data engineering utility built to stream, scrub, and validate high-volume unstructured enterprise sheets and application logs cleanly without memory leaks or unhandled script execution crashes.

---

## 🎯 Core Project Overview (STAR Metrics)

* **Situation:** Helpdesk systems and standard application roles regularly deal with corrupted data pipelines, downstream import rejections, and crashing analytics engines due to malformed, unescaped, and corrupt manual CSV exports from legacy corporate platforms.

* **Task:** Build a resilient, automated command-line sanitation workflow capable of operating completely isolated from system-level environment risks. It must stream arbitrary file volumes, standardize dynamic mixed date formats, isolate corrupt multi-column breaks, and strip invisible anomalies without processing loop disruptions.

* **Action:** Implemented a strict modular Python streaming engine. Wrapped processing iterations within isolated `try-except` data boundaries, enforced `python-dotenv` masking configurations to eliminate raw environment path leaks, integrated `python-dateutil` for automated timeline parsing, and diverted structural edge cases into isolated fault logs.

* **Result:** Achieved 100% crash-resilient streaming loops over highly asymmetric rows. Converts messy runtime string configurations into clean ISO 8601 formatting, intercepts operating system level directory faults safely, and scales gracefully across large data sheets with a flat horizontal memory allocation signature.

---

## ⚙️ Environment Setup & Installation

1. Initialize the Virtual Workspace
Isolate the project dependency layout from your global system environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Dependency Ingestion
Install the concrete engine components into your active virtual bubble:
python -m pip install python-dotenv python-dateutil pytest

3. Environment Context
Create an .env file in the root workspace directory to configure engine file streams dynamically:
TARGET_INPUT_DIR=./data/Input
CLEAN_OUTPUT_DIR=./data/Output
ERROR_LOG_PATH=./data/Output/malformed_rows.log

🚀 Execution & Verification Pipelines
Core Pipeline Execution
To ingest, sanitize, and execute the core cleaning loops against your raw data targets:
python .\Src\main.py

Test Suite Validation
Execute full system assertion validations via the explicit Python module path layer:
python -m pytest -v


📊 Pipeline Architecture
The following data flow map demonstrates how data transitions through our validation layers cleanly:

```mermaid
graph TD
    %% Base Color Layout Schemes
    classDef input fill:#0d47a1,stroke:#1565c0,stroke-width:2px,color:#ffffff;
    classDef process fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#f8fafc;
    classDef decision fill:#311b92,stroke:#673ab7,stroke-width:2px,color:#ffffff;
    classDef success fill:#1b5e20,stroke:#2e7d32,stroke-width:2px,color:#ffffff;
    classDef failure fill:#b71c1c,stroke:#c62828,stroke-width:2px,color:#ffffff;

    %% Data Pipeline Node Tree Map
    A([📥 Raw Dirty CSV Input Target]) --> B[⚙️ Load Environment Config via python-dotenv]
    B --> C{🔍 Is Directory Valid?}
    
    C -- Path Fault --> D[❌ Abort Loop & Log Configuration Fault]
    C -- Valid Path --> E[🔄 Stream Row-by-Row Active Iterator]
    
    E --> F{📐 Check Column Schema Dimensions}
    
    F -- Size Mismatch --> G[⚠️ Route Malformed Row to Fault Log]
    F -- Uniform Schema --> H[🪥 Clean Whitespace & Strip Hidden Bytes]
    
    H --> I[📅 Standardize Mixed Timestamps to ISO 8601]
    I --> J[📤 Commit Sanitized Payload to Stream Buffer]
    J --> K([✨ Complete Production CSV File Pipeline])

    %% Dynamic Class Injections
    class A input;
    class C,F decision;
    class B,E,H,I,J process;
    class D,G failure;
    class K success;

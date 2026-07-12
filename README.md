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
graph TD
    %% Define Node Styles & Themes
    classDef input fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px,color:#0D47A1;
    classDef process fill:#FFF3E0,stroke:#FB8C00,stroke-width:2px,color:#E65100;
    classDef decision fill:#EDE7F6,stroke:#5E35B1,stroke-width:2px,color:#4A148C;
    classDef success fill:#E8F5E9,stroke:#43A047,stroke-width:2px,color:#1B5E20;
    classDef failure fill:#FFEBEE,stroke:#E53935,stroke-width:2px,color:#B71C1C;

    %% Workflow Nodes
    A([📥 Raw Dirty CSV Input]) --> B[⚙️ Load Environment Context via python-dotenv]
    
    B --> C{🔍 Is Directory Path Valid?}
    class C decision;

    C -- No --> D[❌ Graceful Safety Exit & Log Configuration Fault]
    class D failure;

    C -- Yes --> E[🔄 Initialize Row-by-Row Data Streaming Loop]
    class E process;

    F -- Column Mismatch --> G[⚠️ Isolate Malformed Row to Error Log]
    class G failure;

    F -- Valid Dimensions --> H[🪥 Clean Whitespace & Strip Hidden Bytes]
    class H process;

    H --> I[📅 Standardize Dynamic Dates to ISO 8601]
    class I process;

    I --> J[📤 Write Sanitized Row to Output Stream]
    class J process;

    J --> K([✨ Clean Standardized CSV File Completed])

    %% Apply Classes
    class A input;
    class K success;





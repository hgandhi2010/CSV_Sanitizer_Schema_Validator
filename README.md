# Enterprise CSV Sanitizer & Schema Validator

A production-grade command-line interface (CLI) data engineering utility built to stream, scrub, and validate high-volume unstructured enterprise sheets and application logs cleanly without memory leaks or unhandled script execution crashes.

---

## 🎯 Core Project Overview (STAR Metrics)

* **Situation:** Helpdesk systems and standard application roles regularly deal with corrupted data pipelines, downstream import rejections, and crashing analytics engines due to malformed, unescaped, and corrupt manual CSV exports from legacy corporate platforms.
* **Task:** Build a resilient, automated command-line sanitation workflow capable of operating completely isolated from system-level environment risks. It must stream arbitrary file volumes, standardize dynamic mixed date formats, isolate corrupt multi-column breaks, and strip invisible anomalies without processing loop disruptions.
* **Action:** Implemented a strict modular Python streaming engine. Wrapped processing iterations within isolated `try-except` data boundaries, enforced `python-dotenv` masking configurations to eliminate raw environment path leaks, integrated `python-dateutil` for automated timeline parsing, and diverted structural edge cases into isolated fault logs.
* **Result:** Achieved 100% crash-resilient streaming loops over highly asymmetric rows. Converts messy runtime string configurations into clean ISO 8601 formatting, intercepts operating system level directory faults safely, and scales gracefully across large data sheets with a flat horizontal memory allocation signature.

---

## 📊 Pipeline Architecture

The following data flow map demonstrates how data transitions through our validation layers cleanly:

```mermaid
graph TD
    A[Dirty CSV Input Path] --> B[python-dotenv Directory Check]
    B --> C{Is Directory Secure?}
    C -- No --> D[Graceful Safety Exit]
    C -- Yes --> E[Stream Row-by-Row Iterator]
    E --> F{Validate Column Dimensions}
    F -- Misaligned Columns --> G[Isolate Malformed Row to Error Log]
    F -- Structural Match --> H[Strip Hidden Bytes / Whitespace]
    H --> I[Parse and Convert Date to ISO 8601]
    I --> J[Write Clean Output Stream File]

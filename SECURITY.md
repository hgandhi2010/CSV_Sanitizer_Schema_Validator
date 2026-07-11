# Security Policy

## Supported Versions

We actively monitor and patch the core components of the CSV Sanitizer pipeline. Please ensure you are running the latest version to prevent unhandled script execution bugs.

| Version | Supported          |
| ------- | ------------------ |
| v1.0.x  | ✅ Supported       |
| < v1.0  | ❌ Not Supported   |

## Reporting a Vulnerability

We take the security and integrity of data processing pipelines seriously. If you discover a security vulnerability (such as an environment path traversal risk, data leakage exploit, or memory exhaustion vector), please do not open a public GitHub issue. 

Instead, please report it through the following process:

1. **Email the Maintainer:** Send a detailed report to your-email@example.com (replace with your actual email).
2. **Include Details:** Provide a brief description of the vulnerability, a proof of concept (PoC), and an example of a malformed or malicious CSV row that triggers the exploit.
3. **Response Timeline:** You will receive an acknowledgment of your report within 48 hours, along with a timeline for a coordinated security patch release.

## Core Security Safeguards in This Project

This utility enforces a strict data isolation architecture to ensure enterprise compliance:

* **No Environment Path Leaks:** System-level paths and directory configurations are completely abstracted out of the codebase using localized `.env` configuration masks via `python-dotenv`.
* **Zero-Leak Memory Limits:** High-volume files are handled exclusively using row-by-row iterable streaming chunks. Large datasets never flood the system RAM, preventing Denial of Service (DoS) memory exhaustion crashes.
* **Malicious Row Isolation:** Any structurally compromised, misaligned, or unescaped rows are instantly diverted out of the primary runtime execution bubble into an isolated, local error log folder (`/data/Output/malformed_rows.log`) to keep downstream production servers safe.

# Privacy Model

The public repository is generic and contains no real patient data. Private medical data belongs outside version control.

A local workspace is useful for file organization and for avoiding accidental publication, but it does **not** mean the workflow is private once the user sends medical records, MRI/DICOM-derived images, reports, symptom logs, or Q&A content to an LLM, vision model, hosted agent runtime, cloud workspace, or storage provider.

Users should assume that any medical data submitted to an external AI/cloud service is disclosed to that service and processed according to that provider's terms, retention rules, training policies, logging practices, and security controls.

Cloud export should be optional, provider-agnostic, and user-directed. Local-only workflows require a genuinely local model/runtime and local storage; using a hosted LLM or hosted agent is not local-only.

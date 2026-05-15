# Quickstart

1. Clone this repository or download it from GitHub as a ZIP file.
2. Copy templates into a private workspace outside the public repo.
3. Configure your chosen AI-agent runtime. If using Claude Code / Claude Cowork, follow `docs/claude-code.md` first.
4. Keep real patient data outside version control.
5. Start with `templates/USER.md`, `templates/SpineHarmony_Journal.md`, `templates/qa-log.md`, and `templates/symptom-tracker.md`.
6. Use symptom/pain tracking to record daily facts before asking the agent for trend summaries. See `docs/symptom-pain-tracking.md`.
7. Use Q&A to clarify source material and prepare clinician questions, not to make medical decisions.
8. If using imaging workflows, read `docs/imaging-workflow.md` before converting or analyzing MRI/DICOM files.

For the safest beginner setup, use two folders:

```text
Documents/
├── spine-harmony-agent/     # public repo and templates
└── spine-harmony-private/   # real private notes; do not upload to GitHub
```

Read `DISCLAIMER.md` before use.

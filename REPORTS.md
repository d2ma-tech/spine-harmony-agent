# Report Guidelines

Reports should be patient-facing, source-grounded, visually clean, and suitable for review with qualified clinicians.

Spine Harmony reports are not fixed medical forms. Each user will have different history, imaging, procedures, and questions. The report generator should therefore use a **modular structure**: start from a consistent spine-health report skeleton, then rename, omit, add, or merge sections based on the user's actual source material.

## Required caveats

Every report should:

- state what sources were reviewed;
- flag transcription, OCR, translation, imaging-export, or model-vision uncertainty;
- separate source facts from interpretation;
- avoid diagnostic certainty;
- state that LLM/vision-model observations are not radiology interpretation, diagnosis, validated measurement, clinical decision support, or treatment planning;
- recommend clinician verification;
- include red-flag / urgent-care caveats where appropriate.

## Recommended report structure

Use user-specific headings, but prefer a structure similar to this when enough source material exists:

1. **Executive Summary** — concise answer: what the report is about, why it matters, and what decisions/questions it supports.
2. **Patient Profile** — age range or relevant context only; avoid unnecessary identifiers in shareable versions.
3. **Longitudinal Timeline** — timeline length should match the user, e.g. “6-Month Timeline”, “3-Year Timeline”, or “14-Year Timeline”.
4. **Symptom & Pain Tracking Summary** — user-reported pain scores, daily check-ins, trend table, triggers, relieving factors, medication/activity context, sleep, function limits, flares/spasms, new symptoms, and post-procedure recovery notes where relevant. Keep raw facts separate from cautious interpretation.
5. **Lumbar / Cervical / Thoracic Imaging Findings** — rename by region and source availability.
6. **Official Radiology Report** — quote/summarize official report separately from AI interpretation.
7. **Clinical Report Audit** — inconsistencies, missing details, unclear wording, or items to verify.
8. **Treatment Research** — only source-grounded, non-prescriptive background research.
9. **Procedure-Specific Analysis** — e.g. spine injections, radiofrequency procedures, surgery, physiotherapy, regenerative-medicine discussions, or other clinician-directed options; include only if relevant.
10. **Ergonomics / Activity / Rehab Considerations** — include only where source data supports it.
11. **Discussion Points for Your Doctor** — prioritized questions for the clinician.
12. **Prioritized Action Plan** — framed as “items to discuss/verify”, not instructions to self-treat.
13. **Sources** — files, reports, images, conversations, transcripts, and caveats.

## Section adaptation rules

- Rename sections to match the user’s actual condition and materials.
- Do not include empty sections just to match the template.
- Keep official clinician/radiology statements separate from agent interpretation.
- If symptom/pain tracking is used, include a compact trend table and state the tracking period, frequency, missing entries, and whether the pattern is stable, mixed, improving, or worsening without claiming diagnosis or treatment success.
- If imaging files are used, include both the official radiology-report section and an AI/vision-model caveat section.
- If the user has multiple anatomical regions, use region-specific headings.
- If the report is short, collapse the structure into fewer sections while preserving the same logic: summary → evidence → interpretation → clinician questions → sources.

## HTML style standard

Reports should use a restrained, professional HTML design system, not ad-hoc styling.

Preferred style: **clean Vercel/Linear/Apple-inspired clinical report**. Use the 🦴 symbol sparingly as a brand marker in the report heading/cover area, not as decorative clutter throughout the report:

- white background;
- near-black text;
- generous whitespace;
- strong typographic hierarchy;
- card-based sections;
- subtle shadow/border treatment;
- compact metric/status cards where useful;
- clear source/caveat callouts;
- print-aware A4 layout;
- no decorative clutter, gradients, emoji-heavy headings, or amateur medical-dashboard styling; the 🦴 symbol should appear in the main heading/brand line only unless there is a strong reason.

Minimum HTML requirements:

- standalone HTML file with embedded CSS;
- responsive screen layout;
- print stylesheet using A4-friendly margins;
- table of contents for long reports;
- clear disclaimer/caveat callout near the top;
- distinct visual treatment for source facts, interpretation, and action/discussion items;
- sources section at the end;
- footer with generation date, “not medical advice” note, and attribution to D2MA Limited linking to https://d2ma.com.

Use [`templates/report.html`](templates/report.html) as the baseline HTML structure and [`docs/report-generation.md`](docs/report-generation.md) for detailed generation rules.

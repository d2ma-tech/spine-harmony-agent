# Report Generation

Spine Harmony reports should be modular, user-specific, and visually clean. They should resemble a professional patient-facing briefing pack rather than a raw chat transcript or generic markdown summary.

## Core principle

Use a consistent report architecture, but adapt the headings to the user’s actual history, anatomy, source material, and clinical questions.

A real report might include sections such as:

1. Executive Summary
2. Patient Profile
3. 14-Year Longitudinal Timeline
4. Symptom Profile & Pain Generator Mapping
5. Lumbar Imaging Findings
6. Cervical Foraminal Findings
7. Official Radiology Report
8. Clinical Report Audit
9. Treatment Research
10. Radiofrequency Ablation — Full Analysis
11. Spine Injection — Revised Assessment
12. Ergonomic Chair Recommendation
13. Discussion Points for Your Doctor
14. Prioritized Action Plan
15. Sources

Do **not** hardcode those exact headings for every user. Instead, use them as a pattern for report completeness and adapt them:

- “14-Year Longitudinal Timeline” might become “8-Week Symptom Timeline” or “3-Year Treatment Timeline”.
- “Lumbar Imaging Findings” might become “Cervical Imaging Findings”, “Thoracic Imaging Findings”, or “Imaging Findings by Region”.
- Procedure sections should match the user’s actual treatments.
- Ergonomic/activity sections should appear only when relevant.
- Region-specific sections should appear only when supported by source material.

## Recommended section architecture

### 1. Executive Summary

A concise, high-signal overview of:

- why the report was generated;
- the main pattern in the source material;
- the most important uncertainties;
- the key clinician discussion points.

### 2. Patient Profile

Include only relevant context. Avoid unnecessary identifiers in shareable versions.

Examples:

- age range instead of full date of birth;
- broad activity/work context if clinically relevant;
- major constraints affecting treatment decisions.

### 3. Longitudinal Timeline

Summarize the relevant time horizon. Use a title that matches the evidence:

- “6-Week Post-Injection Timeline”;
- “18-Month Symptom Timeline”;
- “Multi-Year Spine History”.

### 4. Symptom Profile & Pain Generator Mapping

Organize:

- pain location and quality;
- triggers and relieving factors;
- functional limitations;
- neurological symptoms if reported;
- plausible source-to-symptom mapping.

Keep this explicitly caveated. It is not diagnosis.

### 5. Imaging Findings by Region

Use region-specific headings when applicable:

- Lumbar Imaging Findings;
- Cervical Imaging Findings;
- Thoracic Imaging Findings;
- Foraminal / canal / disc / facet findings where relevant.

Separate:

- official radiology statements;
- user-provided image observations;
- LLM/vision-model observations;
- agent interpretation.

### 6. Official Radiology Report

Keep official radiology text or summary separate from AI interpretation. If quoting, preserve meaning and flag any OCR/transcription uncertainty.

### 7. Clinical Report Audit

Highlight:

- inconsistencies between symptoms and imaging;
- missing details;
- unclear terminology;
- items that should be verified with the clinician/radiologist.

### 8. Treatment Research

Source-grounded, non-prescriptive background only. Do not recommend treatment independently.

### 9. Procedure-Specific Analysis

Only include sections for relevant treatments or options, e.g.:

- Spine Injection — Assessment;
- Radiofrequency Ablation — Analysis;
- Regenerative-Medicine Option — Questions and Evidence Summary;
- Artificial Disc Replacement — Consultation Questions;
- Fusion — Discussion Points;
- Physiotherapy / Rehab — Summary.

### 10. Ergonomics / Activity / Rehab Considerations

Include if the source material contains relevant work, chair, activity, swimming, lifting, sleep, or rehab issues.

### 11. Discussion Points for Your Doctor

Prioritized questions grouped by urgency and decision relevance.

### 12. Prioritized Action Plan

Frame as:

- “items to verify”;
- “questions to ask”;
- “records to obtain”;
- “symptoms to monitor”.

Do not frame as self-directed medical instructions.

### 13. Sources

List:

- documents reviewed;
- imaging files or converted image sets;
- reports;
- transcripts/meeting notes;
- user-provided symptom logs;
- relevant caveats.

## Required caveats

Reports should include:

- source list;
- imaging-source caveats when MRI/DICOM-derived images or model observations are used;
- reliability caveats;
- timeline summary;
- key Q&A themes where relevant;
- key questions for clinicians;
- user-facing interpretation;
- clinician-verification note;
- red-flag disclaimer.

Q&A-derived reports should state that the content came from interactive user-agent discussion and must be verified against original source documents and qualified clinical advice.

## Clean HTML style standard

Use [`templates/report.html`](../templates/report.html) as the baseline for report HTML.

The visual style should be restrained and professional:

- Vercel/Linear/Apple-inspired minimalism;
- white page background;
- near-black text;
- clear hierarchy;
- subtle card borders/shadows;
- metric/status cards for key facts;
- small monospace labels for source/caveat tags;
- table of contents for long reports;
- A4 print-aware CSS;
- no decorative clutter.

Every generated HTML report should be standalone, with embedded CSS and no remote assets required.

## Symptom and pain tracking in reports

When a user maintains a symptom or pain diary, reports should include a concise tracking section before interpretation-heavy sections. The goal is to show the clinician the raw pattern clearly.

Include where available:

- tracking window and check-in frequency;
- pain-score range and latest score;
- trend table by date/day or relative period;
- sleep, medication, activity/function, sitting/standing/walking tolerance, therapy/exercise, and comfort measures;
- flares, spasms, acute episodes, new symptoms, and missing data;
- cautious trend language such as stable, mixed, improving, worsening, or too early to interpret;
- specific clinician questions raised by the pattern.

Do not state that a treatment has succeeded, failed, or identified the pain generator unless that conclusion comes from a qualified clinician. Phrase the report as: “the diary shows user-reported improvement with one flare,” not “the injection worked.”

## Visual section types

Use these consistent section treatments:

- **Hero / cover block:** report title with the 🦴 Spine Harmony brand marker, patient-safe subtitle, generation date, caveat.
- **Metric cards:** timeline length, source count, key anatomical regions, main decision question.
- **Caveat callout:** not medical advice; AI/vision-model limitations; privacy/source limitations.
- **Evidence cards:** source facts and timeline entries.
- **Interpretation cards:** clearly labelled agent synthesis.
- **Doctor questions:** prioritized list with high/medium/low labels.
- **Sources:** compact final audit list.
- **Footer attribution:** “Generated by Spine Harmony — © D2MA Limited” with a link to https://d2ma.com.

## Verification before sharing

Before sending or publishing a generated report:

1. Confirm all sections are supported by source material.
2. Confirm no unsupported diagnosis or treatment instruction appears.
3. Confirm official radiology/clinician statements are separated from agent interpretation.
4. Confirm privacy-sensitive identifiers are appropriate for the intended recipient.
5. Open the HTML in a browser and check readability.
6. Check print layout if the report may be sent to a doctor.

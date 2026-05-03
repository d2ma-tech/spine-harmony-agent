# Usage

Common workflows:

- Ask structured Q&A about user-provided spine-health notes and source documents.
- Maintain structured symptom and pain diaries from daily or scheduled check-ins.
- Convert and organize user-owned MRI/DICOM files into high-resolution review images when imaging tools are configured.
- Use LLM-assisted imaging observations to generate better clinician questions, not to replace clinical interpretation.
- Build a spine-health timeline.
- Record symptom notes, pain scores, medications, sleep, activity, flares/spasms, and post-procedure recovery observations.
- Prepare questions for appointments.
- Compare information across clinician visits, imaging summaries, and symptom logs.
- Summarize user-provided records.
- Draft patient-facing reports for clinician review.

## Q&A workflow

The Q&A workflow is intended to help users think clearly about their own materials, not to make clinical decisions. A good answer should:

1. restate the user's question;
2. identify which source facts are available;
3. flag uncertainty or missing data;
4. separate source facts from interpretation;
5. produce better follow-up questions for qualified clinicians;
6. avoid diagnosis, treatment recommendations, and emergency triage.

Every workflow should preserve source uncertainty and end with clinician verification where medical decisions are involved.


## Symptom and pain tracking workflow

Spine Harmony can turn short check-ins into a useful longitudinal symptom record. This is especially useful around flares, medication changes, physiotherapy blocks, injections, procedures, or the run-up to a clinician appointment.

A structured entry should capture:

1. date/time or relative day label;
2. pain score on a 0–10 scale;
3. location and character of symptoms where the user reports them;
4. sleep quality;
5. medication used, if reported;
6. activity and function: sitting, standing, walking, work, therapy, exercise, swimming, lifting, travel;
7. flares, spasms, acute episodes, new symptoms, or neurological symptoms;
8. comfort measures such as heat, ice, rest, position changes, or bracing;
9. comparison with the prior entry: better, same, worse, or mixed;
10. clinician questions raised by the trend.

The diary should preserve raw user facts and use cautious trend language. It should not declare that a treatment succeeded or failed without clinician confirmation and adequate follow-up duration.

Use [`docs/symptom-pain-tracking.md`](symptom-pain-tracking.md) for detailed guidance, [`templates/symptom-tracker.md`](../templates/symptom-tracker.md) for the private diary format, and [`examples/anonymized-symptom-tracking.md`](../examples/anonymized-symptom-tracking.md) for a synthetic example.

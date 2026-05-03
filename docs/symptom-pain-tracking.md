# Symptom and Pain Tracking

Spine Harmony can maintain a structured private symptom diary from short check-ins. This is one of the core agent workflows: it preserves daily facts, creates trend summaries, and turns messy symptom history into clinician-ready context.

This workflow is useful for:

- baseline spine-pain tracking;
- flare tracking;
- therapy or rehab blocks;
- medication-change observation;
- post-procedure recovery tracking after clinician-directed interventions;
- preparing a concise update before follow-up appointments.

## What to track

A good check-in captures the facts a clinician is likely to ask for:

| Field | Examples |
| --- | --- |
| Pain score | 0–10 now, on waking, worst today, best today |
| Location/quality | back, leg, neck, arm; sharp/dull/burning/tight if the user reports it |
| Sleep | quality, waking, position issues |
| Medication | type/amount only if the user chooses to record it |
| Activity/function | sitting, standing, walking, work, therapy, exercise, travel, lifting |
| Flares/acute episodes | spasm-like events, sudden worsening, triggers, duration, recovery |
| New symptoms | especially neurological changes or other red-line symptoms |
| Comfort measures | heat, ice, rest, walking, position changes, bracing |
| Comparison | better, same, worse, mixed, or too early to say |
| Clinician questions | questions raised by the trend |

## Check-in cadence

Cadence should match the user's situation. Examples:

- once daily evening check-in for stable recovery or low-burden tracking;
- morning and evening during a flare or medication/procedure observation window;
- activity-triggered entries after sitting, walking, therapy, travel, or exercise;
- pre-appointment summary in the final few days before a clinician review.

Avoid unnecessary prompting. The goal is useful continuity, not anxiety or obsessive tracking.

## Agent behavior

When the user provides a short check-in, the agent should:

1. preserve the raw facts;
2. add or update the correct diary entry;
3. update the trend table or current-status summary;
4. identify missing fields only when they matter;
5. use cautious trend language;
6. generate clinician questions if the pattern raises them;
7. avoid diagnosis, treatment decisions, or overclaiming response.

Good wording:

> The last three entries show user-reported pain staying in the 1–2/10 range, with no new symptoms reported. This is encouraging but still needs clinician interpretation and longer follow-up to understand durability.

Bad wording:

> The procedure worked and the pain generator is confirmed.

## Post-procedure recovery tracking

For clinician-directed procedures or interventions, track response durability and side effects without making clinical conclusions. Useful fields include:

- day number or relative time since intervention;
- current pain score;
- best/worst pain since prior check-in;
- medication use;
- activity level and tolerance;
- flare/spasm recurrence;
- new or worsening symptoms;
- comparison with the prior day;
- questions for the follow-up clinician.

The agent may summarize patterns such as “stable low pain,” “mixed response,” “temporary flare,” or “worsening trend,” but should not decide whether the intervention succeeded or failed.

## Privacy

Symptom diaries can contain sensitive health information. Keep real trackers in a private workspace, outside version control. If symptom logs are pasted into hosted LLMs, cloud agents, chat products, or cloud storage, treat that as disclosure of medical information to that provider.

## Templates and examples

- [`templates/symptom-tracker.md`](../templates/symptom-tracker.md)
- [`examples/anonymized-symptom-tracking.md`](../examples/anonymized-symptom-tracking.md)

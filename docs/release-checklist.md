# Public Release Checklist

Before publishing Spine Harmony publicly:

- [ ] Confirm this is a fresh repository with no private history.
- [ ] Review all synthetic examples manually.
- [ ] Run PII and secrets scans on the working tree.
- [ ] Confirm no real patient data is present.
- [ ] Confirm no real doctor, clinic, hospital, appointment, transcript, imaging, converted image, metadata dump, or medication details are present unless intentionally generic.
- [ ] Confirm imaging documentation clearly states that MRI/DICOM export and LLM-assisted image review are not radiology interpretation, diagnosis, validated measurement, or treatment guidance.
- [ ] Confirm no API keys, access tokens, local IPs, private paths, or credentials are present.
- [ ] Confirm `LICENSE`, `DISCLAIMER.md`, `PRIVACY.md`, `SECURITY.md`, `TRADEMARKS.md`, `NOTICE`, and `CITATION.cff` are present.
- [ ] Confirm cloud export wording is provider-agnostic and user-directed.
- [ ] Confirm README and docs state that Spine Harmony is not medical advice, diagnosis, treatment guidance, radiology interpretation, clinical decision support, emergency triage, or a medical device.
- [ ] Confirm README top warning is visible in the first screenful and links to `DISCLAIMER.md` and `TERMS.md`.
- [ ] Confirm no wording claims the project is safe, validated, clinically reliable, regulator-approved, or suitable for unsupervised medical use.
- [ ] Confirm hosted deployment warnings say public/clinical/patient-facing use requires legal, privacy, regulatory, clinical safety, and security review.
- [ ] Confirm `CONTRIBUTING.md` tells contributors their contributions are not medical advice and do not create clinical responsibility.
- [ ] Confirm `TERMS.md` is present and includes no-clinician-relationship, no clinical reliance, emergency warning, hosted deployment warning, warranty/liability limitation, and governing-law language.
- [ ] Create a clean initial commit only after review.
- [ ] Publish only after maintainer approval.

## Verification commands

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

Run the DICOM export tests before publishing changes to the imaging workflow.


## Symptom/pain tracking review

- Confirm README presents symptom and pain tracking as a core feature.
- Confirm only synthetic tracking examples are included.
- Confirm no real pain diary, medication log, procedure response log, appointment date, or private user timeline is committed.
- Confirm tracking language preserves raw facts and avoids diagnosis or treatment-response conclusions.

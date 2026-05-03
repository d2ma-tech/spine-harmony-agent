# Privacy Model

Spine Harmony's public repository contains only generic instructions, templates, and synthetic examples. It does not contain real patient data.

A user-controlled workspace can help keep private files out of version control, but it does not guarantee that medical data remains local or private once the user sends records, images, reports, or Q&A content to an LLM, vision model, hosted agent runtime, cloud workspace, or storage provider.

## Plain-English warning

If you send your spine-health records, MRI/DICOM files, converted images, reports, notes, symptom/pain diaries, check-in logs, or Q&A text to a hosted LLM, hosted vision model, cloud agent, chat product, cloud IDE, or cloud storage service, that information is leaving your local machine. It should be treated as a disclosure of medical information to that provider. Spine Harmony cannot control what that provider logs, retains, reviews, trains on, or shares under its own policies.

## User responsibility

Users are responsible for deciding where their medical data is stored and which AI/runtime providers process it. If you upload or paste medical records, MRI/DICOM-derived images, radiology reports, clinician letters, symptom logs, or generated reports into an external LLM, vision model, hosted agent, chat service, cloud IDE, or cloud storage workflow, you should assume that information is being disclosed to that service and processed under that service's terms, retention rules, training policies, logging practices, and security controls.

Do not provide sensitive personal or medical data to any system unless you understand and accept that system's privacy, retention, and security practices.

## Recommended data boundaries

Keep real patient data outside the public repository and outside version control. Store private files in a local workspace or user-selected secure storage location, but treat any file or content sent to an external AI/cloud service as no longer purely local.

Never commit:

- medical records;
- diagnostic imaging;
- clinic letters;
- appointment notes containing personal identifiers;
- raw transcripts;
- exported reports containing real patient data;
- API credentials or access tokens.

## Imaging privacy

MRI/DICOM files frequently contain embedded personal information in metadata, including personal identifiers, study dates, institution names, study/reference numbers, device information, and other fields. Some images may also contain burned-in annotations.

Converted review images, contact sheets, screenshots, metadata summaries, and LLM-generated imaging notes should be treated as sensitive medical data. If they are uploaded to a hosted LLM/vision model or cloud service, they should be assumed to have been disclosed to that provider. Do not commit them to public repositories or share them without explicit review and de-identification.

## Cloud-storage agnostic exports

Spine Harmony does not require any specific cloud provider. If cloud storage is configured and the user explicitly requests it, reports may be saved or archived to the chosen storage provider. Otherwise, save locally only.


## Related terms

See [TERMS.md](TERMS.md) for additional no-reliance, no-clinical-use, hosted-deployment, warranty, liability, and governing-law terms.

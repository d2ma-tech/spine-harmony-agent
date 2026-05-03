# DICOM Export Tool

Convert user-owned DICOM/MRI files into high-resolution PNG review images and optional contact sheets.

## Install dependencies

```bash
python -m pip install pydicom pillow numpy
```

## Basic conversion

```bash
python tools/dicom-export/dicom_export.py /path/to/DICOM_FOLDER /path/to/output-folder
```

The tool recursively scans the input folder, reads DICOM files, applies DICOM rescale/windowing where available, and writes PNG files grouped by series.

## Create a contact sheet

```bash
python tools/dicom-export/dicom_export.py /path/to/DICOM_FOLDER /path/to/output-folder --contact-sheet
```

Outputs:

```text
output-folder/
├── series-001_.../
│   ├── series-001_instance-0001_....png
│   └── ...
├── export_manifest.csv
└── contact_sheet.jpg
```

## What this tool does

- Reads DICOM files using `pydicom`.
- Applies rescale slope/intercept.
- Uses DICOM window center/width when available.
- Falls back to robust percentile scaling when window fields are missing.
- Handles MONOCHROME1 inversion.
- Exports high-resolution PNG images without downsampling.
- Optionally creates a JPEG contact sheet for quick review.

## What this tool does not do

- It does not diagnose.
- It does not interpret MRI findings.
- It does not validate measurements.
- It does not segment anatomy.
- It does not remove all possible identifiers from source DICOM files.
- It does not make outputs safe to publish.

Treat raw DICOM files, exported PNGs, contact sheets, and manifests as sensitive medical data.

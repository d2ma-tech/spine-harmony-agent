#!/usr/bin/env python3
"""Export DICOM/MRI files to high-resolution PNG review images.

Scope: file conversion and organization only. This tool does not diagnose,
interpret imaging, validate measurements, or provide treatment guidance.

Typical use:
    python tools/dicom-export/dicom_export.py /path/to/dicom-folder /path/to/output --contact-sheet
"""

from __future__ import annotations

import argparse
import csv
import math
import re
from pathlib import Path
from typing import Iterable, Optional

import numpy as np
from PIL import Image, ImageOps, ImageDraw

try:
    import pydicom
    from pydicom.errors import InvalidDicomError
except Exception:  # pragma: no cover - handled by CLI dependency error
    pydicom = None
    InvalidDicomError = Exception


def safe_filename(value: object, fallback: str = "unnamed") -> str:
    """Return a filesystem-safe filename component."""
    text = str(value or fallback).strip()
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("._-")
    return text or fallback


def first_value(value: object) -> Optional[float]:
    """Return the first numeric value from a DICOM scalar/list-like field."""
    if value is None:
        return None
    if isinstance(value, (list, tuple)):
        value = value[0] if value else None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def get_pixels(ds) -> np.ndarray:
    """Return DICOM pixel data with rescale slope/intercept applied."""
    arr = ds.pixel_array.astype(np.float32)
    slope = float(getattr(ds, "RescaleSlope", 1) or 1)
    intercept = float(getattr(ds, "RescaleIntercept", 0) or 0)
    return arr * slope + intercept


def window_pixels(
    pixels: np.ndarray,
    window_center: Optional[float] = None,
    window_width: Optional[float] = None,
    invert: bool = False,
) -> np.ndarray:
    """Scale image pixels to uint8 using DICOM window or robust min/max."""
    arr = pixels.astype(np.float32)

    if window_center is not None and window_width and window_width > 0:
        low = window_center - window_width / 2
        high = window_center + window_width / 2
    else:
        finite = arr[np.isfinite(arr)]
        if finite.size == 0:
            return np.zeros(arr.shape, dtype=np.uint8)
        low, high = np.percentile(finite, [1, 99])
        if high <= low:
            low, high = float(finite.min()), float(finite.max())
        if high <= low:
            high = low + 1

    arr = np.clip(arr, low, high)
    arr = (arr - low) / (high - low)
    arr = (arr * 255).round().astype(np.uint8)
    if invert:
        arr = 255 - arr
    return arr


def build_output_name(ds) -> str:
    """Build stable output filename from series/instance metadata."""
    series_no = int(getattr(ds, "SeriesNumber", 0) or 0)
    instance_no = int(getattr(ds, "InstanceNumber", 0) or 0)
    desc = safe_filename(getattr(ds, "SeriesDescription", "series"), "series")
    return f"series-{series_no:03d}_instance-{instance_no:04d}_{desc}.png"


def iter_input_files(input_path: Path) -> Iterable[Path]:
    if input_path.is_file():
        yield input_path
        return
    for path in sorted(input_path.rglob("*")):
        if path.is_file() and not path.name.startswith("."):
            yield path


def read_dicom(path: Path):
    if pydicom is None:
        raise RuntimeError("pydicom is required. Install with: python -m pip install pydicom pillow numpy")
    try:
        return pydicom.dcmread(str(path), force=False)
    except InvalidDicomError:
        return None
    except Exception:
        return None


def export_dicom_file(path: Path, output_dir: Path, preserve_series_dirs: bool = True) -> Optional[dict]:
    ds = read_dicom(path)
    if ds is None or not hasattr(ds, "PixelData"):
        return None

    pixels = get_pixels(ds)
    center = first_value(getattr(ds, "WindowCenter", None))
    width = first_value(getattr(ds, "WindowWidth", None))
    invert = str(getattr(ds, "PhotometricInterpretation", "")).upper() == "MONOCHROME1"
    image_arr = window_pixels(pixels, center, width, invert=invert)

    image = Image.fromarray(image_arr)
    image = ImageOps.exif_transpose(image)

    series_desc = safe_filename(getattr(ds, "SeriesDescription", "series"), "series")
    series_no = int(getattr(ds, "SeriesNumber", 0) or 0)
    target_dir = output_dir / f"series-{series_no:03d}_{series_desc}" if preserve_series_dirs else output_dir
    target_dir.mkdir(parents=True, exist_ok=True)
    out_path = target_dir / build_output_name(ds)
    image.save(out_path, optimize=True)

    return {
        "source_file": str(path),
        "output_file": str(out_path),
        "series_number": series_no,
        "series_description": str(getattr(ds, "SeriesDescription", "")),
        "instance_number": int(getattr(ds, "InstanceNumber", 0) or 0),
        "rows": int(getattr(ds, "Rows", image_arr.shape[0])),
        "columns": int(getattr(ds, "Columns", image_arr.shape[1])),
        "window_center": center,
        "window_width": width,
        "photometric_interpretation": str(getattr(ds, "PhotometricInterpretation", "")),
    }


def write_manifest(rows: list[dict], output_dir: Path) -> None:
    if not rows:
        return
    manifest = output_dir / "export_manifest.csv"
    keys = [
        "output_file",
        "series_number",
        "series_description",
        "instance_number",
        "rows",
        "columns",
        "window_center",
        "window_width",
        "photometric_interpretation",
        "source_file",
    ]
    with manifest.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def create_contact_sheet(rows: list[dict], output_dir: Path, thumb_size: int = 220) -> Optional[Path]:
    if not rows:
        return None
    image_paths = [Path(r["output_file"]) for r in rows if Path(r["output_file"]).exists()]
    if not image_paths:
        return None
    cols = min(5, max(1, math.ceil(math.sqrt(len(image_paths)))))
    rows_count = math.ceil(len(image_paths) / cols)
    label_height = 32
    sheet = Image.new("RGB", (cols * thumb_size, rows_count * (thumb_size + label_height)), "white")
    draw = ImageDraw.Draw(sheet)
    for idx, path in enumerate(image_paths):
        img = Image.open(path).convert("L")
        img.thumbnail((thumb_size, thumb_size), Image.Resampling.LANCZOS)
        x = (idx % cols) * thumb_size + (thumb_size - img.width) // 2
        y = (idx // cols) * (thumb_size + label_height)
        sheet.paste(img.convert("RGB"), (x, y))
        draw.text(((idx % cols) * thumb_size + 8, y + thumb_size + 4), path.stem[:32], fill="black")
    out = output_dir / "contact_sheet.jpg"
    sheet.save(out, quality=92, optimize=True)
    return out


def run(input_path: Path, output_dir: Path, contact_sheet: bool = False) -> list[dict]:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in iter_input_files(input_path):
        row = export_dicom_file(path, output_dir)
        if row:
            rows.append(row)
    rows.sort(key=lambda r: (r["series_number"], r["instance_number"], r["output_file"]))
    write_manifest(rows, output_dir)
    if contact_sheet:
        create_contact_sheet(rows, output_dir)
    return rows


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Export DICOM/MRI files to high-resolution PNG review images.")
    parser.add_argument("input", type=Path, help="Input DICOM file or folder")
    parser.add_argument("output", type=Path, help="Output folder for PNG exports")
    parser.add_argument("--contact-sheet", action="store_true", help="Create contact_sheet.jpg")
    args = parser.parse_args(argv)

    rows = run(args.input, args.output, contact_sheet=args.contact_sheet)
    print(f"Exported {len(rows)} DICOM image(s) to {args.output}")
    if rows:
        print(f"Manifest: {args.output / 'export_manifest.csv'}")
        if args.contact_sheet:
            print(f"Contact sheet: {args.output / 'contact_sheet.jpg'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import importlib.util
import unittest
from pathlib import Path

import numpy as np

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "dicom-export" / "dicom_export.py"
spec = importlib.util.spec_from_file_location("dicom_export", MODULE_PATH)
dicom_export = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dicom_export)


class DicomExportTests(unittest.TestCase):
    def test_window_pixels_scales_to_uint8_with_given_window(self):
        arr = np.array([[0, 50], [100, 150]], dtype=np.float32)

        out = dicom_export.window_pixels(arr, window_center=75, window_width=150)

        self.assertEqual(out.dtype, np.uint8)
        self.assertEqual(out.shape, arr.shape)
        self.assertEqual(int(out[0, 0]), 0)
        self.assertEqual(int(out[-1, -1]), 255)

    def test_safe_filename_removes_unsafe_characters(self):
        self.assertEqual(dicom_export.safe_filename("Series: 1 / T2 SAG"), "Series_1_T2_SAG")

    def test_build_output_name_uses_series_and_instance_numbers(self):
        class DS:
            SeriesNumber = 4
            InstanceNumber = 12
            SeriesDescription = "T2 SAG"

        self.assertEqual(dicom_export.build_output_name(DS()), "series-004_instance-0012_T2_SAG.png")


if __name__ == "__main__":
    unittest.main()

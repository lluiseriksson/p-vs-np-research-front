from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ExperimentReproductionTests(unittest.TestCase):
    def test_literal_subcube_search_artifact(self) -> None:
        script_path = ROOT / "experiments" / "search_literal_subcube.py"
        spec = importlib.util.spec_from_file_location("literal_subcube", script_path)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        expected = json.loads(
            (ROOT / "artifacts" / "literal-subcube-search-31.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(module.search(31), expected)


if __name__ == "__main__":
    unittest.main()

"""Regression certificates for the corrected finite gap reduction."""

from __future__ import annotations

import unittest

from gap_reduction import unsafe_bound_gap_counterexample


class GapReductionTests(unittest.TestCase):
    def test_bound_plus_residue_reduction_can_destroy_nonoverlap(self) -> None:
        large_gap, reduced_gap = unsafe_bound_gap_counterexample()
        self.assertIn(3, large_gap)
        self.assertNotIn(3, reduced_gap)


if __name__ == "__main__":
    unittest.main()

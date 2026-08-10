"""Regression checks for the phase-sensitive SAT-specific gap parameters."""

from __future__ import annotations

import unittest

from phase_gap_reduction import (
    phase_gap_caps,
    reduce_phase_gaps,
    reduced_type_counts,
    zero_overhangs,
)
from quartet_type_audit import LENGTH68_REPAIR_IDENTIFIERS
from quartet_type_audit_fast import QuartetAuditor


class PhaseGapReductionTests(unittest.TestCase):
    def test_length68_alphabet_overhangs_are_exact(self) -> None:
        self.assertEqual(
            zero_overhangs(LENGTH68_REPAIR_IDENTIFIERS),
            ((68, 67, 66, 65), (64, 65, 66, 67)),
        )

    def test_phase_caps_and_domain_count(self) -> None:
        caps = phase_gap_caps(LENGTH68_REPAIR_IDENTIFIERS)
        self.assertEqual(caps, (135, 134, 133, 132))
        counts = reduced_type_counts(caps)
        self.assertEqual(counts, (2405635, 2387748, 2369994, 2352372))
        self.assertEqual(sum(counts), 9515749)

    def test_exact_oracle_agrees_across_large_gap_normalizations(self) -> None:
        caps = phase_gap_caps(LENGTH68_REPAIR_IDENTIFIERS)
        auditor = QuartetAuditor(LENGTH68_REPAIR_IDENTIFIERS, 600)
        for residue in range(4):
            for large_index in range(3):
                for excess in range(1, 5):
                    gaps = [9, 10, 11]
                    source = residue
                    for index in range(large_index):
                        source = (source + gaps[index]) % 4
                    gaps[large_index] = caps[source] + excess
                    reduced = reduce_phase_gaps(residue, tuple(gaps), caps)
                    first = 68 + residue
                    original_positions = [first]
                    reduced_positions = [first]
                    for original_gap, reduced_gap in zip(gaps, reduced):
                        original_positions.append(
                            original_positions[-1] + original_gap
                        )
                        reduced_positions.append(
                            reduced_positions[-1] + reduced_gap
                        )
                    self.assertEqual(
                        auditor.reached_masks_positions(
                            tuple(original_positions), 3
                        ),
                        auditor.reached_masks_positions(tuple(reduced_positions), 3),
                    )


if __name__ == "__main__":
    unittest.main()

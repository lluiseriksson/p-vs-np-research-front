"""Exact local component certificates for the large-gap quartet theorem."""

from __future__ import annotations

from quartet_type_audit import BASE_IDENTIFIERS
from quartet_type_audit_fast import QuartetAuditor


def single_zero_pair_failures() -> tuple[
    tuple[tuple[int, int], tuple[int, ...]], ...
]:
    """Check one-block realization of either singleton zero on every pair."""
    auditor = QuartetAuditor(BASE_IDENTIFIERS, 164)
    failures = []
    for residue in range(4):
        first = 36 + residue
        for gap in range(1, 40):
            pair = (first, first + gap)
            reached = auditor.reached_masks_positions(pair, 1)
            missing = tuple(
                mask for mask in (1, 2) if not (reached >> mask) & 1
            )
            if missing:
                failures.append((pair, missing))
    return tuple(failures)


def full_zero_triple_failures() -> tuple[tuple[int, int, int], ...]:
    """Check three-block realization of 000 on the safe triple domain."""
    auditor = QuartetAuditor(BASE_IDENTIFIERS, 260)
    failures = []
    for residue in range(4):
        first = 36 + residue
        for gap_1 in range(1, 76):
            for gap_2 in range(1, 76):
                triple = (first, first + gap_1, first + gap_1 + gap_2)
                reached = auditor.reached_masks_positions(
                    triple, 3, include_full_mask=True
                )
                if not (reached >> 7) & 1:
                    failures.append(triple)
    return tuple(failures)

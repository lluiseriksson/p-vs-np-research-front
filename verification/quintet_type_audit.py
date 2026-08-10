"""Residue-partitioned local audit for GATE-004AF quintet types."""

from __future__ import annotations

import argparse
import json

from quartet_type_audit import (
    LENGTH68_BOUND,
    WIDTH5_INITIAL_IDENTIFIERS,
    WIDTH5_REPAIR_IDENTIFIERS,
    WIDTH5_REPRESENTATIVE_LENGTH,
)
from quartet_type_audit_fast import QuartetAuditor
from covering_basis import strength_five_identifier_basis


def audit_residue(
    residue: int, gap_cap: int, *, initial: bool = False, covering: bool = False
) -> dict[str, object]:
    if residue not in range(4):
        raise ValueError("residue must be 0, 1, 2, or 3")
    if gap_cap < 1 or gap_cap > LENGTH68_BOUND + 3:
        raise ValueError("gap cap must lie between 1 and 71")
    if initial and covering:
        raise ValueError("choose at most one alphabet mode")
    if covering:
        identifiers = tuple(
            dict.fromkeys(
                WIDTH5_REPAIR_IDENTIFIERS + strength_five_identifier_basis()
            )
        )
    else:
        identifiers = (
            WIDTH5_INITIAL_IDENTIFIERS if initial else WIDTH5_REPAIR_IDENTIFIERS
        )
    auditor = QuartetAuditor(identifiers, WIDTH5_REPRESENTATIVE_LENGTH)
    first = LENGTH68_BOUND + residue
    failures = []
    checked = 0
    for gap_1 in range(1, gap_cap + 1):
        for gap_2 in range(1, gap_cap + 1):
            for gap_3 in range(1, gap_cap + 1):
                for gap_4 in range(1, gap_cap + 1):
                    positions = (
                        first,
                        first + gap_1,
                        first + gap_1 + gap_2,
                        first + gap_1 + gap_2 + gap_3,
                        first + gap_1 + gap_2 + gap_3 + gap_4,
                    )
                    reached = auditor.reached_masks_positions(positions, 4)
                    missing = tuple(
                        mask
                        for mask in range(1, 31)
                        if not (reached >> mask) & 1
                    )
                    if missing:
                        failures.append((positions, missing))
                    checked += 1
    return {
        "residue": residue,
        "gap_cap": gap_cap,
        "identifiers": identifiers,
        "checked": checked,
        "failure_count": len(failures),
        "first_failures": failures[:10],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("residue", type=int)
    parser.add_argument("--gap-cap", type=int, default=20)
    parser.add_argument("--initial", action="store_true")
    parser.add_argument("--covering", action="store_true")
    arguments = parser.parse_args()
    print(
        json.dumps(
            audit_residue(
                arguments.residue,
                arguments.gap_cap,
                initial=arguments.initial,
                covering=arguments.covering,
            ),
            sort_keys=True,
        )
    )

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
from symbolic_identifier_audit import CompleteIdentifierAuditor


def audit_residue(
    residue: int,
    gap_cap: int,
    *,
    initial: bool = False,
    covering: bool = False,
    length76_repair: bool = False,
    symbolic76: bool = False,
) -> dict[str, object]:
    if residue not in range(4):
        raise ValueError("residue must be 0, 1, 2, or 3")
    bound = 76 if length76_repair or symbolic76 else LENGTH68_BOUND
    if gap_cap < 1 or gap_cap > bound + 3:
        raise ValueError(f"gap cap must lie between 1 and {bound + 3}")
    if sum((initial, covering, length76_repair, symbolic76)) > 1:
        raise ValueError("choose at most one alphabet mode")
    if symbolic76:
        identifiers: tuple[int, ...] | str = "all identifiers 1 through 131071"
    elif covering or length76_repair:
        identifiers = tuple(
            dict.fromkeys(
                WIDTH5_REPAIR_IDENTIFIERS + strength_five_identifier_basis()
                + ((98370,) if length76_repair else ())
            )
        )
    else:
        identifiers = (
            WIDTH5_INITIAL_IDENTIFIERS if initial else WIDTH5_REPAIR_IDENTIFIERS
        )
    representative_length = (
        500 if symbolic76 else 460 if length76_repair else WIDTH5_REPRESENTATIVE_LENGTH
    )
    auditor = (
        CompleteIdentifierAuditor(16, representative_length)
        if symbolic76
        else QuartetAuditor(identifiers, representative_length)
    )
    first = bound + residue
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
        "bound": bound,
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
    parser.add_argument("--length76-repair", action="store_true")
    parser.add_argument("--symbolic76", action="store_true")
    arguments = parser.parse_args()
    print(
        json.dumps(
            audit_residue(
                arguments.residue,
                arguments.gap_cap,
                initial=arguments.initial,
                covering=arguments.covering,
                length76_repair=arguments.length76_repair,
                symbolic76=arguments.symbolic76,
            ),
            sort_keys=True,
        )
    )

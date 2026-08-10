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
    symbolic80: bool = False,
    symbolic84: bool = False,
    symbolic88: bool = False,
    symbolic100: bool = False,
    symbolic104: bool = False,
    symbolic112: bool = False,
    symbolic116: bool = False,
) -> dict[str, object]:
    if residue not in range(4):
        raise ValueError("residue must be 0, 1, 2, or 3")
    bound = (
        116 if symbolic116 else
        112 if symbolic112 else
        104 if symbolic104 else
        100 if symbolic100 else
        88 if symbolic88 else
        84 if symbolic84 else
        80 if symbolic80 else
        76 if length76_repair or symbolic76 else
        LENGTH68_BOUND
    )
    if gap_cap < 1 or gap_cap > bound + 3:
        raise ValueError(f"gap cap must lie between 1 and {bound + 3}")
    if sum(
        (
            initial, covering, length76_repair, symbolic76,
            symbolic80, symbolic84, symbolic88, symbolic100, symbolic104,
            symbolic112, symbolic116,
        )
    ) > 1:
        raise ValueError("choose at most one alphabet mode")
    if symbolic116:
        identifiers: tuple[int, ...] | str = "all identifiers 1 through 134217727"
    elif symbolic112:
        identifiers = "all identifiers 1 through 67108863"
    elif symbolic104:
        identifiers: tuple[int, ...] | str = "all identifiers 1 through 16777215"
    elif symbolic100:
        identifiers: tuple[int, ...] | str = "all identifiers 1 through 8388607"
    elif symbolic88:
        identifiers: tuple[int, ...] | str = "all identifiers 1 through 1048575"
    elif symbolic84:
        identifiers: tuple[int, ...] | str = "all identifiers 1 through 524287"
    elif symbolic80:
        identifiers = "all identifiers 1 through 262143"
    elif symbolic76:
        identifiers = "all identifiers 1 through 131071"
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
        860 if symbolic116 else
        820 if symbolic112 else
        760 if symbolic104 else
        720 if symbolic100 else
        580 if symbolic88 else
        540 if symbolic80 or symbolic84 else
        500 if symbolic76 else
        460 if length76_repair else
        WIDTH5_REPRESENTATIVE_LENGTH
    )
    auditor = (
        CompleteIdentifierAuditor(
            26 if symbolic116 else
            25 if symbolic112 else
            23 if symbolic104 else
            22 if symbolic100 else
            19 if symbolic88 else
            18 if symbolic84 else
            17 if symbolic80 else
            16,
            representative_length,
        )
        if (
            symbolic76 or symbolic80 or symbolic84 or symbolic88
            or symbolic100 or symbolic104 or symbolic112 or symbolic116
        )
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
    parser.add_argument("--symbolic80", action="store_true")
    parser.add_argument("--symbolic84", action="store_true")
    parser.add_argument("--symbolic88", action="store_true")
    parser.add_argument("--symbolic100", action="store_true")
    parser.add_argument("--symbolic104", action="store_true")
    parser.add_argument("--symbolic112", action="store_true")
    parser.add_argument("--symbolic116", action="store_true")
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
                symbolic80=arguments.symbolic80,
                symbolic84=arguments.symbolic84,
                symbolic88=arguments.symbolic88,
                symbolic100=arguments.symbolic100,
                symbolic104=arguments.symbolic104,
                symbolic112=arguments.symbolic112,
                symbolic116=arguments.symbolic116,
            ),
            sort_keys=True,
        )
    )

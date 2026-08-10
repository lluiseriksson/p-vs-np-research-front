"""Exhaustive residue-partitioned audit for GATE-004AD quartet types."""

from __future__ import annotations

import argparse
import json
from bisect import bisect_right
from functools import lru_cache

from sat_encoding import contradiction, tautology


BOUND = 36
REPRESENTATIVE_LENGTH = 164
BASE_IDENTIFIERS = tuple(range(1, 69))
ENRICHED_IDENTIFIERS = BASE_IDENTIFIERS + (69, 80, 98, 130, 260, 324, 529)
ENRICHED_BOUND = 48
ENRICHED_REPRESENTATIVE_LENGTH = 256
LENGTH68_INITIAL_IDENTIFIERS = ENRICHED_IDENTIFIERS + (
    102,
    1013,
    1028,
    1042,
    1058,
    1284,
    4130,
    4162,
    4164,
    4228,
    16450,
)
LENGTH68_REPAIR_IDENTIFIERS = LENGTH68_INITIAL_IDENTIFIERS + (
    1044,
    1060,
    1092,
    1156,
    16452,
    16516,
)
LENGTH68_BOUND = 68
LENGTH68_REPRESENTATIVE_LENGTH = 360


@lru_cache(maxsize=None)
def _extend(mask_set: int, mask: int) -> int:
    result = 0
    while mask_set:
        lowest = mask_set & -mask_set
        value = lowest.bit_length() - 1
        result |= 1 << (value | mask)
        mask_set -= lowest
    return result


@lru_cache(maxsize=None)
def _placements(
    identifiers: tuple[int, ...] = BASE_IDENTIFIERS,
    representative_length: int = REPRESENTATIVE_LENGTH,
) -> tuple[tuple[int, int, frozenset[int]], ...]:
    blocks = {
        block
        for identifier in identifiers
        for block in (
            "01" + tautology(identifier),
            "10" + contradiction(identifier),
        )
    }
    return tuple(
        (start, start + len(block), frozenset(
            start + offset for offset, bit in enumerate(block) if bit == "0"
        ))
        for block in blocks
        for start in range(0, representative_length - len(block) + 1, 4)
    )


def reached_masks(
    quartet: tuple[int, int, int, int],
    identifiers: tuple[int, ...] = BASE_IDENTIFIERS,
    representative_length: int = REPRESENTATIVE_LENGTH,
) -> int:
    """Return zero masks realized by up to three selected identifier blocks."""
    placements = _placements(identifiers, representative_length)
    indices = {
        index
        for index, (_, _, zeros) in enumerate(placements)
        if any(position in zeros for position in quartet)
    }
    candidates = set()
    for index in indices:
        start, end, zeros = placements[index]
        mask = sum(
            1 << bit
            for bit, position in enumerate(quartet)
            if position in zeros
        )
        if mask:
            candidates.add((end, start, mask))
    ordered = sorted(candidates)
    ends = [candidate[0] for candidate in ordered]
    count = len(ordered)
    dynamic = [[0] * (count + 1) for _ in range(4)]
    dynamic[0] = [1] * (count + 1)
    for position, (_, start, mask) in enumerate(ordered, 1):
        previous = bisect_right(ends, start, 0, position - 1)
        for block_count in range(1, 4):
            dynamic[block_count][position] = (
                dynamic[block_count][position - 1]
                | _extend(dynamic[block_count - 1][previous], mask)
            )
    return dynamic[1][count] | dynamic[2][count] | dynamic[3][count]


def reached_masks_direct(
    quartet: tuple[int, int, int, int],
    identifiers: tuple[int, ...],
    representative_length: int,
) -> int:
    """Audit one quartet without materializing every global placement."""
    candidates = set()
    for identifier in identifiers:
        for block in (
            "01" + tautology(identifier),
            "10" + contradiction(identifier),
        ):
            for start in range(0, representative_length - len(block) + 1, 4):
                mask = sum(
                    1 << bit
                    for bit, position in enumerate(quartet)
                    if start <= position < start + len(block)
                    and block[position - start] == "0"
                )
                if mask:
                    candidates.add((start + len(block), start, mask))
    ordered = sorted(candidates)
    ends = [candidate[0] for candidate in ordered]
    count = len(ordered)
    dynamic = [[0] * (count + 1) for _ in range(4)]
    dynamic[0] = [1] * (count + 1)
    for position, (_, start, mask) in enumerate(ordered, 1):
        previous = bisect_right(ends, start, 0, position - 1)
        for block_count in range(1, 4):
            dynamic[block_count][position] = (
                dynamic[block_count][position - 1]
                | _extend(dynamic[block_count - 1][previous], mask)
            )
    return dynamic[1][count] | dynamic[2][count] | dynamic[3][count]


def audit_residue(
    residue: int,
    identifiers: tuple[int, ...] = BASE_IDENTIFIERS,
    bound: int = BOUND,
    representative_length: int = REPRESENTATIVE_LENGTH,
) -> dict[str, object]:
    if residue not in range(4):
        raise ValueError("residue must be 0, 1, 2, or 3")
    placements = _placements(identifiers, representative_length)
    by_zero: list[list[int]] = [[] for _ in range(representative_length)]
    for index, (_, _, zeros) in enumerate(placements):
        for position in zeros:
            by_zero[position].append(index)

    failures = []
    checked = 0
    first = bound + residue
    for gap_1 in range(1, bound + 4):
        for gap_2 in range(1, bound + 4):
            for gap_3 in range(1, bound + 4):
                quartet = (
                    first,
                    first + gap_1,
                    first + gap_1 + gap_2,
                    first + gap_1 + gap_2 + gap_3,
                )
                indices: set[int] = set()
                for position in quartet:
                    indices.update(by_zero[position])
                candidates = set()
                for index in indices:
                    start, end, zeros = placements[index]
                    mask = sum(
                        1 << bit
                        for bit, position in enumerate(quartet)
                        if position in zeros
                    )
                    if mask:
                        candidates.add((end, start, mask))
                ordered = sorted(candidates)
                ends = [candidate[0] for candidate in ordered]
                count = len(ordered)
                dynamic = [[0] * (count + 1) for _ in range(4)]
                dynamic[0] = [1] * (count + 1)
                for position, (_, start, mask) in enumerate(ordered, 1):
                    previous = bisect_right(ends, start, 0, position - 1)
                    for block_count in range(1, 4):
                        dynamic[block_count][position] = (
                            dynamic[block_count][position - 1]
                            | _extend(dynamic[block_count - 1][previous], mask)
                        )
                reached = (
                    dynamic[1][count] | dynamic[2][count] | dynamic[3][count]
                )
                missing = tuple(
                    mask for mask in range(1, 15) if not (reached >> mask) & 1
                )
                if missing:
                    failures.append((quartet, missing))
                checked += 1
    return {
        "residue": residue,
        "checked": checked,
        "identifiers": identifiers,
        "bound": bound,
        "failures": failures,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("residue", type=int)
    parser.add_argument("--enriched", action="store_true")
    parser.add_argument("--length68", action="store_true")
    parser.add_argument("--summary", action="store_true")
    arguments = parser.parse_args()
    if arguments.enriched and arguments.length68:
        parser.error("choose at most one alphabet mode")
    if arguments.length68:
        result = audit_residue(
            arguments.residue,
            LENGTH68_REPAIR_IDENTIFIERS,
            LENGTH68_BOUND,
            LENGTH68_REPRESENTATIVE_LENGTH,
        )
    elif arguments.enriched:
        result = audit_residue(
            arguments.residue,
            ENRICHED_IDENTIFIERS,
            ENRICHED_BOUND,
            ENRICHED_REPRESENTATIVE_LENGTH,
        )
    else:
        result = audit_residue(arguments.residue)
    if arguments.summary:
        result = {
            **{key: value for key, value in result.items() if key != "failures"},
            "failure_count": len(result["failures"]),
            "first_failures": result["failures"][:10],
        }
    print(json.dumps(result, sort_keys=True))

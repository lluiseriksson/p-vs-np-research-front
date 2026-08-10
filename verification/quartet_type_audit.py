"""Exhaustive residue-partitioned audit for GATE-004AD quartet types."""

from __future__ import annotations

import argparse
import json
from bisect import bisect_right
from functools import lru_cache

from sat_encoding import contradiction, tautology


BOUND = 36
REPRESENTATIVE_LENGTH = 164


@lru_cache(maxsize=None)
def _extend(mask_set: int, mask: int) -> int:
    result = 0
    while mask_set:
        lowest = mask_set & -mask_set
        value = lowest.bit_length() - 1
        result |= 1 << (value | mask)
        mask_set -= lowest
    return result


def _placements() -> tuple[tuple[int, int, frozenset[int]], ...]:
    blocks = {
        block
        for identifier in range(1, 69)
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
        for start in range(0, REPRESENTATIVE_LENGTH - len(block) + 1, 4)
    )


def reached_masks(quartet: tuple[int, int, int, int]) -> int:
    """Return zero masks realized by up to three identifier-1..68 blocks."""
    placements = _placements()
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


def audit_residue(residue: int) -> dict[str, object]:
    if residue not in range(4):
        raise ValueError("residue must be 0, 1, 2, or 3")
    placements = _placements()
    by_zero: list[list[int]] = [[] for _ in range(REPRESENTATIVE_LENGTH)]
    for index, (_, _, zeros) in enumerate(placements):
        for position in zeros:
            by_zero[position].append(index)

    failures = []
    checked = 0
    first = BOUND + residue
    for gap_1 in range(1, BOUND + 4):
        for gap_2 in range(1, BOUND + 4):
            for gap_3 in range(1, BOUND + 4):
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
    return {"residue": residue, "checked": checked, "failures": failures}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("residue", type=int)
    arguments = parser.parse_args()
    print(json.dumps(audit_residue(arguments.residue), sort_keys=True))

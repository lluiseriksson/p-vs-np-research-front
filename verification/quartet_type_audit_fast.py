"""Bitset-compressed exhaustive verifier for three-block quartet universality."""

from __future__ import annotations

import argparse
import json

from quartet_type_audit import (
    BASE_IDENTIFIERS,
    BOUND,
    LENGTH68_BOUND,
    LENGTH68_INITIAL_IDENTIFIERS,
    LENGTH68_REPAIR_IDENTIFIERS,
    LENGTH68_REPRESENTATIVE_LENGTH,
    REPRESENTATIVE_LENGTH,
)
from sat_encoding import contradiction, tautology


class QuartetAuditor:
    """Compress placement identities into position-indexed Python bitsets."""

    def __init__(self, identifiers: tuple[int, ...], length: int) -> None:
        blocks = {
            block
            for identifier in identifiers
            for block in (
                "01" + tautology(identifier),
                "10" + contradiction(identifier),
            )
        }
        placements = set()
        for block in blocks:
            for start in range(0, length - len(block) + 1, 4):
                zeros = sum(
                    1 << (start + offset)
                    for offset, bit in enumerate(block)
                    if bit == "0"
                )
                placements.add((start + len(block), start, zeros))
        self.placements = tuple(sorted(placements))
        self.length = length
        self.universe = (1 << len(self.placements)) - 1
        self.ends = tuple(end for end, _, _ in self.placements)

        zero_at = [0] * length
        starts = [0] * (length + 1)
        for index, (_, start, zeros) in enumerate(self.placements):
            placement_bit = 1 << index
            starts[start] |= placement_bit
            remaining = zeros
            while remaining:
                lowest = remaining & -remaining
                zero_at[lowest.bit_length() - 1] |= placement_bit
                remaining -= lowest
        self.zero_at = tuple(zero_at)

        start_ge = [0] * (length + 1)
        running = 0
        for threshold in range(length, -1, -1):
            running |= starts[threshold]
            start_ge[threshold] = running
        self.start_ge = tuple(start_ge)

    def reached_masks(self, quartet: tuple[int, int, int, int]) -> int:
        if not (0 <= quartet[0] < quartet[1] < quartet[2] < quartet[3] < self.length):
            raise ValueError("quartet must be strictly increasing and interior")
        coordinate_sets = tuple(self.zero_at[position] for position in quartet)
        exact: dict[int, int] = {}
        for mask in range(1, 15):
            placements = self.universe
            for bit, zero_set in enumerate(coordinate_sets):
                placements &= (
                    zero_set if (mask >> bit) & 1 else self.universe ^ zero_set
                )
            if placements:
                exact[mask] = placements

        reached = 1
        frontier = {0: 0}
        for _ in range(3):
            following: dict[int, int] = {}
            for accumulated, previous_end in frontier.items():
                eligible = self.start_ge[previous_end]
                for mask, placement_set in exact.items():
                    combined = accumulated | mask
                    if combined == 15:
                        continue
                    feasible = placement_set & eligible
                    if not feasible:
                        continue
                    lowest = feasible & -feasible
                    end = self.ends[lowest.bit_length() - 1]
                    if end < following.get(combined, self.length + 1):
                        following[combined] = end
                    reached |= 1 << combined
            frontier = following
            if not frontier or reached & 0x7FFE == 0x7FFE:
                break
        return reached


def audit_residue(
    residue: int,
    identifiers: tuple[int, ...],
    bound: int,
    representative_length: int,
) -> dict[str, object]:
    if residue not in range(4):
        raise ValueError("residue must be 0, 1, 2, or 3")
    auditor = QuartetAuditor(identifiers, representative_length)
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
                reached = auditor.reached_masks(quartet)
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
        "failure_count": len(failures),
        "first_failures": failures[:10],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("residue", type=int)
    parser.add_argument("--length68", action="store_true")
    parser.add_argument("--length68-initial", action="store_true")
    arguments = parser.parse_args()
    if arguments.length68 and arguments.length68_initial:
        parser.error("choose at most one alphabet mode")
    if arguments.length68_initial:
        result = audit_residue(
            arguments.residue,
            LENGTH68_INITIAL_IDENTIFIERS,
            LENGTH68_BOUND,
            LENGTH68_REPRESENTATIVE_LENGTH,
        )
    elif arguments.length68:
        result = audit_residue(
            arguments.residue,
            LENGTH68_REPAIR_IDENTIFIERS,
            LENGTH68_BOUND,
            LENGTH68_REPRESENTATIVE_LENGTH,
        )
    else:
        result = audit_residue(
            arguments.residue,
            BASE_IDENTIFIERS,
            BOUND,
            REPRESENTATIVE_LENGTH,
        )
    print(json.dumps(result, sort_keys=True))

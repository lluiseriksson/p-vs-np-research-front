#!/usr/bin/env python3
"""NUMERICAL: exhaustive bounded search for one-bit literal polarity gadgets."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict


Semantics = tuple[int, int]


def enumerate_formulas(max_length: int) -> dict[int, dict[Semantics, set[str]]]:
    """Enumerate all formulas using only variable identifier 1."""
    by_length: dict[int, dict[Semantics, set[str]]] = defaultdict(
        lambda: defaultdict(set)
    )
    by_length[3][(0, 1)].add("001")

    for length in range(4, max_length + 1):
        if length - 2 in by_length:
            for semantics, formulas in by_length[length - 2].items():
                negated = (1 - semantics[0], 1 - semantics[1])
                by_length[length][negated].update("11" + f for f in formulas)

        for left_length in range(3, length - 4 + 1):
            right_length = length - 2 - left_length
            if right_length < 3:
                continue
            for left_semantics, left_formulas in by_length[left_length].items():
                for right_semantics, right_formulas in by_length[
                    right_length
                ].items():
                    and_semantics = (
                        left_semantics[0] & right_semantics[0],
                        left_semantics[1] & right_semantics[1],
                    )
                    or_semantics = (
                        left_semantics[0] | right_semantics[0],
                        left_semantics[1] | right_semantics[1],
                    )
                    by_length[length][and_semantics].update(
                        "01" + left + right
                        for left in left_formulas
                        for right in right_formulas
                    )
                    by_length[length][or_semantics].update(
                        "10" + left + right
                        for left in left_formulas
                        for right in right_formulas
                    )
    return by_length


def flipped(bits: str, positions: tuple[int, ...]) -> str:
    result = list(bits)
    for position in positions:
        result[position] = "1" if result[position] == "0" else "0"
    return "".join(result)


def search(max_length: int) -> dict[str, object]:
    by_length = enumerate_formulas(max_length)
    first_distance_one = None
    first_distance_two = None
    counts = []

    for length in range(3, max_length + 1):
        positive = by_length[length][(0, 1)]
        negative = by_length[length][(1, 0)]
        counts.append(
            {
                "length": length,
                "positive_literal_formulas": len(positive),
                "negative_literal_formulas": len(negative),
            }
        )

        if first_distance_one is None and positive and negative:
            for formula in sorted(positive):
                for position in range(length):
                    neighbor = flipped(formula, (position,))
                    if neighbor in negative:
                        first_distance_one = {
                            "length": length,
                            "positive": formula,
                            "negative": neighbor,
                            "flipped_positions_zero_based": [position],
                        }
                        break
                if first_distance_one is not None:
                    break

        if first_distance_two is None and positive and negative:
            for formula in sorted(positive):
                for positions in itertools.combinations(range(length), 2):
                    neighbor = flipped(formula, positions)
                    if neighbor in negative:
                        first_distance_two = {
                            "length": length,
                            "positive": formula,
                            "negative": neighbor,
                            "flipped_positions_zero_based": list(positions),
                        }
                        break
                if first_distance_two is not None:
                    break

    return {
        "label": "NUMERICAL",
        "experiment": "bounded one-variable literal polarity gadget search",
        "variable_identifier": 1,
        "maximum_formula_length": max_length,
        "first_hamming_distance_one_pair": first_distance_one,
        "first_hamming_distance_two_pair": first_distance_two,
        "counts": counts,
        "scope_warning": (
            "Finite exhaustive search only; absence through the bound is not an "
            "asymptotic impossibility theorem."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=31)
    args = parser.parse_args()
    if args.max_length < 3:
        raise SystemExit("--max-length must be at least 3")
    print(json.dumps(search(args.max_length), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

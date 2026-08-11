#!/usr/bin/env python3
"""Finite regression for the cycle-184 oriented residual loss caps."""

from itertools import combinations, product


def main() -> None:
    universe = range(8)
    pairs = [set(p) for p in combinations(universe, 2)]
    carrier = {0, 1}
    max_and_or = 0
    max_or_and = 0
    for other in pairs:
        max_and_or = max(max_and_or, len((carrier | carrier | other) - carrier))
    for left, right in product(pairs, repeat=2):
        max_or_and = max(max_or_and, len((left | right | carrier) - carrier))
    assert max_and_or == 2
    assert max_or_and == 4
    print("oriented loss-budget audit passed: residual maxima AND->OR 2; OR->AND 4")


if __name__ == "__main__":
    main()

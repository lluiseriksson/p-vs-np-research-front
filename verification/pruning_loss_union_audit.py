#!/usr/bin/env python3
"""Finite audit of the cycle-182 three-two-set union cap."""

from itertools import combinations, product


def main() -> None:
    pairs = list(combinations(range(6), 2))
    maximum = 0
    equality_count = 0
    for triple in product(pairs, repeat=3):
        sets = [set(pair) for pair in triple]
        union_size = len(set().union(*sets))
        maximum = max(maximum, union_size)
        pairwise_disjoint = all(not (sets[i] & sets[j]) for i, j in combinations(range(3), 2))
        assert (union_size == 6) == pairwise_disjoint
        equality_count += int(union_size == 6)
    assert maximum == 6
    print(
        "pruning-loss union audit passed: 3375 ordered triples; maximum union 6; "
        f"{equality_count} pairwise-disjoint equality cases"
    )


if __name__ == "__main__":
    main()

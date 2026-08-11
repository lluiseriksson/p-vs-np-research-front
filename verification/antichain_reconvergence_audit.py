#!/usr/bin/env python3
"""Finite diagnostics for LEMMA-241/242 and NG-175."""

from __future__ import annotations

from itertools import product


def term(bits: tuple[int, ...], index: int) -> int:
    return bits[2 * index] & bits[2 * index + 1]


def comb_values(bits: tuple[int, ...], k: int) -> tuple[list[int], list[int]]:
    terms = [term(bits, index) for index in range(k)]
    merges = [terms[0] | terms[1]]
    for index in range(2, k):
        merges.append(merges[-1] | terms[index])
    return terms, merges


def audit_member(k: int) -> None:
    arity = 2 * k
    term_tables = [[] for _ in range(k)]
    merge_tables = [[] for _ in range(k - 1)]
    for bits in product((0, 1), repeat=arity):
        terms, merges = comb_values(bits, k)
        for index, value in enumerate(terms):
            term_tables[index].append(value)
        for index, value in enumerate(merges):
            merge_tables[index].append(value)

    assert len({tuple(values) for values in term_tables}) == k
    assert len({tuple(values) for values in merge_tables}) == k - 1
    assert len(merge_tables) == k - 1

    for j in range(2, k + 1):
        earlier_only = [0] * k
        earlier_only[0] = 1
        new_only = [0] * k
        new_only[j - 1] = 1

        def original_output(values: list[int]) -> int:
            return int(any(values))

        def replace_merge_by_left(values: list[int]) -> int:
            # r_j becomes r_{j-1}; p_j is lost, while later terms remain.
            return int(any(values[: j - 1]) or any(values[j:]))

        def replace_merge_by_right(values: list[int]) -> int:
            # r_j becomes p_j; earlier terms are lost, while later remain.
            return int(values[j - 1] or any(values[j:]))

        assert original_output(earlier_only) == 1
        assert replace_merge_by_right(earlier_only) == 0
        assert original_output(new_only) == 1
        assert replace_merge_by_left(new_only) == 0


def main() -> None:
    for k in range(2, 8):
        audit_member(k)
    print("antichain reconvergence diagnostics passed for k=2..7")
    print("each comb has exactly k-1 distinct merge functions")
    print("general mathematical certification: structural proofs in LEMMA-241/242")


if __name__ == "__main__":
    main()

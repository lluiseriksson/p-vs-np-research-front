#!/usr/bin/env python3
"""Finite diagnostics for LEMMA-243/244 and NG-176."""

from __future__ import annotations

from itertools import combinations, product


def comb_paths(k: int) -> tuple[list[str], dict[str, list[str]]]:
    leaves = [f"p{i}" for i in range(1, k + 1)]
    paths: dict[str, list[str]] = {}
    for i, leaf in enumerate(leaves, start=1):
        first_merge = 2 if i <= 2 else i
        paths[leaf] = [leaf] + [f"r{j}" for j in range(first_merge, k + 1)]
    return leaves, paths


def comparable(left: str, right: str, paths: dict[str, list[str]]) -> bool:
    return any(
        left in path and right in path
        for path in paths.values()
    )


def audit_irredundant_comb_cuts(k: int) -> int:
    leaves, paths = comb_paths(k)
    vertices = leaves + [f"r{j}" for j in range(2, k + 1)]
    checked = 0
    for size in range(1, len(vertices) + 1):
        for subset_tuple in combinations(vertices, size):
            subset = set(subset_tuple)
            if not all(subset.intersection(path) for path in paths.values()):
                continue
            if any(
                all((subset - {vertex}).intersection(path) for path in paths.values())
                for vertex in subset
            ):
                continue
            assert all(
                not comparable(left, right, paths)
                or not comparable(right, left, paths)
                for left, right in combinations(subset, 2)
            )
            blocks = {
                vertex: {
                    leaf for leaf, path in paths.items() if vertex in path
                }
                for vertex in subset
            }
            assert all(blocks.values())
            assert set().union(*blocks.values()) == set(leaves)
            assert sum(len(block) for block in blocks.values()) == k
            checked += 1
    return checked


def prefix_value(order: list[int], length: int, terms: tuple[int, ...]) -> int:
    return int(any(terms[index] for index in order[:length]))


def audit_cyclic_pair(k: int) -> None:
    old_order = list(range(k))
    new_order = list(range(1, k)) + [0]
    for terms in product((0, 1), repeat=k):
        for length in range(2, k):
            old = prefix_value(old_order, length, terms)
            new = prefix_value(new_order, length, terms)
            if terms == (1,) + (0,) * (k - 1):
                assert old == 1 and new == 0
        assert prefix_value(old_order, k, terms) == prefix_value(
            new_order, k, terms
        )


def main() -> None:
    cut_count = sum(audit_irredundant_comb_cuts(k) for k in range(2, 7))
    for k in range(3, 9):
        audit_cyclic_pair(k)
    print(f"tree-cut partition diagnostics passed on {cut_count} comb cuts")
    print("cyclic one-seal diagnostics passed for k=3..8")
    print("general mathematical certification: structural proofs in LEMMA-243/244")


if __name__ == "__main__":
    main()

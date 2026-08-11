#!/usr/bin/env python3
"""Finite diagnostics for LEMMA-238/239/240 and NG-174."""

from __future__ import annotations

from itertools import combinations, product


def table(arity: int, function) -> tuple[int, ...]:
    return tuple(function(bits) for bits in product((0, 1), repeat=arity))


def nested_coordinate(bits: tuple[int, ...], index: int) -> int:
    # bits=(a,z_1,...,z_m), while index is zero-based for p_{index+1}.
    return int(all(bits[position] for position in range(index + 2)))


def essential_variables(arity: int, function) -> set[int]:
    answer: set[int] = set()
    for bits in product((0, 1), repeat=arity):
        for variable in range(arity):
            flipped = list(bits)
            flipped[variable] ^= 1
            if function(bits) != function(tuple(flipped)):
                answer.add(variable)
    return answer


def audit_nested_member(m: int) -> None:
    arity = m + 1
    coordinates = [
        table(arity, lambda bits, i=i: nested_coordinate(bits, i))
        for i in range(m)
    ]
    inputs = {
        table(arity, lambda bits, variable=variable: bits[variable])
        for variable in range(arity)
    }
    assert len(set(coordinates)) == m
    assert all(coordinate not in inputs for coordinate in coordinates)
    for i in range(m):
        assert essential_variables(
            arity, lambda bits, i=i: nested_coordinate(bits, i)
        ) == set(range(i + 2))


def reachability(n: int, edges: set[tuple[int, int]]) -> list[list[bool]]:
    reach = [[False] * n for _ in range(n)]
    for left, right in edges:
        reach[left][right] = True
    for middle in range(n):
        for left in range(n):
            for right in range(n):
                reach[left][right] |= reach[left][middle] and reach[middle][right]
    return reach


def height(n: int, edges: set[tuple[int, int]]) -> int:
    longest = [1] * n
    for right in range(n):
        predecessors = [left for left in range(right) if (left, right) in edges]
        if predecessors:
            longest[right] = 1 + max(longest[left] for left in predecessors)
    return max(longest, default=0)


def width(n: int, reach: list[list[bool]]) -> int:
    answer = 0
    for size in range(n + 1):
        for subset in combinations(range(n), size):
            if all(
                not reach[left][right] and not reach[right][left]
                for left, right in combinations(subset, 2)
            ):
                answer = max(answer, size)
    return answer


def audit_ordered_dags(n: int) -> int:
    candidates = [(left, right) for left in range(n) for right in range(left + 1, n)]
    checked = 0
    for mask in range(1 << len(candidates)):
        edges = {
            edge for bit, edge in enumerate(candidates) if mask & (1 << bit)
        }
        reach = reachability(n, edges)
        h = height(n, edges)
        w = width(n, reach)
        assert n <= h * w
        checked += 1
    return checked


def main() -> None:
    for m in range(1, 9):
        audit_nested_member(m)
    dag_count = sum(audit_ordered_dags(n) for n in range(1, 6))
    print("zero-overhead nested-vector diagnostics passed for m=1..8")
    print(f"height-width inequality passed on {dag_count} ordered DAGs through n=5")
    print("general mathematical certification: structural proofs in LEMMA-238/239/240")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite truth-table diagnostics for LEMMA-236/237 and NG-173.

The general lower bounds are proved structurally in the lemma files.  This
script checks the claimed coordinate distinction, essential-variable sets,
and input-signal exclusions on small members of the diagonal family.
"""

from __future__ import annotations

from itertools import product


def raw_coordinate(bits: tuple[int, ...], index: int) -> int:
    x, y, *zs = bits
    return x & y & zs[index]


def supplied_coordinate(bits: tuple[int, ...], index: int) -> int:
    a, *zs = bits
    return a & zs[index]


def table(arity: int, function) -> tuple[int, ...]:
    return tuple(function(bits) for bits in product((0, 1), repeat=arity))


def essential_variables(arity: int, function) -> set[int]:
    essential: set[int] = set()
    for bits in product((0, 1), repeat=arity):
        for variable in range(arity):
            flipped = list(bits)
            flipped[variable] ^= 1
            if function(bits) != function(tuple(flipped)):
                essential.add(variable)
    return essential


def projection_table(arity: int, variable: int) -> tuple[int, ...]:
    return table(arity, lambda bits: bits[variable])


def audit_member(m: int) -> None:
    raw_arity = m + 2
    raw_tables = [
        table(raw_arity, lambda bits, i=i: raw_coordinate(bits, i))
        for i in range(m)
    ]
    assert len(set(raw_tables)) == m
    raw_inputs = {projection_table(raw_arity, variable) for variable in range(raw_arity)}
    assert all(coordinate not in raw_inputs for coordinate in raw_tables)
    for i in range(m):
        essential = essential_variables(
            raw_arity, lambda bits, i=i: raw_coordinate(bits, i)
        )
        assert essential == {0, 1, i + 2}

    supplied_arity = m + 1
    supplied_tables = [
        table(
            supplied_arity,
            lambda bits, i=i: supplied_coordinate(bits, i),
        )
        for i in range(m)
    ]
    assert len(set(supplied_tables)) == m
    supplied_inputs = {
        projection_table(supplied_arity, variable)
        for variable in range(supplied_arity)
    }
    assert all(coordinate not in supplied_inputs for coordinate in supplied_tables)
    for i in range(m):
        essential = essential_variables(
            supplied_arity, lambda bits, i=i: supplied_coordinate(bits, i)
        )
        assert essential == {0, i + 1}


def main() -> None:
    for m in range(1, 9):
        audit_member(m)
    print("diagonal joint-port diagnostics passed for m=1..8")
    print("raw exact construction count: m+1; supplied-signal count: m")
    print("mathematical minimality certification: structural proof in LEMMA-236/237")


if __name__ == "__main__":
    main()

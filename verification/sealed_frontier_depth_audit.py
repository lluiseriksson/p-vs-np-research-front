#!/usr/bin/env python3
"""Regression audit for the cycle-186 arbitrary sealing-depth family."""

from itertools import product


def trace(v: int, x: int, zs: tuple[int, ...], y: int, replace: bool) -> list[int]:
    e = x if replace else (v | x)
    chain = []
    current = e
    for z in zs:
        current &= z
        chain.append(current)
    neg = 1 - current
    seal = current | neg
    parent = y & seal
    return [e, *chain, neg, seal, parent]


def main() -> None:
    for m in range(1, 9):
        for bits in product((0, 1), repeat=m + 3):
            v, x = bits[:2]
            zs = bits[2 : 2 + m]
            y = bits[-1]
            old = trace(v, x, zs, y, False)
            new = trace(v, x, zs, y, True)
            assert old[-2:] == new[-2:] == [1, y]
        witness_old = trace(1, 0, (1,) * m, 1, False)
        witness_new = trace(1, 0, (1,) * m, 1, True)
        assert witness_old[1 : m + 2] != witness_new[1 : m + 2]
        assert witness_old[-2:] == witness_new[-2:]
    print("sealed-frontier depth audit passed: m=1..8; arbitrary changed chain; first seal and parent exact")


if __name__ == "__main__":
    main()

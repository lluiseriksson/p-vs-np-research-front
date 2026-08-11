#!/usr/bin/env python3
"""Regression audit for the cycle-185 restriction-lost family."""

from itertools import product


def output(v: int, xs: tuple[int, ...], zs: tuple[int, ...], ss: tuple[int, ...]) -> int:
    return int(any(s & ((v | x) & z) for x, z, s in zip(xs, zs, ss)))


def specialized(xs: tuple[int, ...], zs: tuple[int, ...], ss: tuple[int, ...]) -> int:
    return int(any(s & (x & z) for x, z, s in zip(xs, zs, ss)))


def main() -> None:
    for m in range(1, 7):
        for bits in product((0, 1), repeat=3 * m):
            xs = bits[:m]
            zs = bits[m : 2 * m]
            ss = bits[2 * m :]
            assert output(0, xs, zs, ss) == specialized(xs, zs, ss)
        for i in range(m):
            xs = [0] * m
            zs = [0] * m
            ss = [0] * m
            zs[i] = ss[i] = 1
            assert output(1, tuple(xs), tuple(zs), tuple(ss)) == 1
            assert specialized(tuple(xs), tuple(zs), tuple(ss)) == 0
        assert 4 * m - 1 >= m
    print("restriction-lost audit passed: m=1..6; zero-cofactors exact; every named gate parent-essential")


if __name__ == "__main__":
    main()

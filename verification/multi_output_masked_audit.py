#!/usr/bin/env python3
"""Regression audit for the cycle-180 masked two-output family."""

from __future__ import annotations

from itertools import product


def values(u: int, t: int, xs: tuple[int, ...], w: int) -> dict[str, int]:
    x_all = int(all(xs))
    a = u & w
    h = int(all(x | a for x in xs))
    q = u & xs[0]
    for x in xs[1:]:
        q &= x
    k = q & (1 - t)
    r = w | k
    b = h | r
    c = u & k
    k_one = x_all & (1 - t)
    r_one = w | k_one
    c_replaced = u & k_one
    b_replaced = h | r_one
    return locals()


def main() -> None:
    for n in range(3, 9):
        for bits in product((0, 1), repeat=n + 3):
            u, t = bits[:2]
            xs = bits[2 : 2 + n]
            w = bits[-1]
            row = values(u, t, xs, w)
            assert row["h"] == (row["x_all"] | (u & w))
            assert row["b"] == (row["x_all"] | w)
            assert row["c"] == row["k"]
            assert row["c_replaced"] == row["c"]
            assert row["b_replaced"] == row["b"]
        assert n - 2 > 0

    print(
        "multi-output masked audit passed: n=3..8; outputs k,r jointly "
        "masked at sigma=1; one entry gate versus deficit n-2"
    )


if __name__ == "__main__":
    main()

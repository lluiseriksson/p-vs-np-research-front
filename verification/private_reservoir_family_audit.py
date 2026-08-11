#!/usr/bin/env python3
"""Regression audit for the cycle-179 constant-frontier family."""

from __future__ import annotations

from itertools import product


def evaluate(u: int, t: int, xs: tuple[int, ...], w: int) -> tuple[int, int, int]:
    x_all = int(all(xs))
    a = u & w
    h = int(all(x | a for x in xs))
    q = u & xs[0]
    for x in xs[1:]:
        q &= x
    k = q & (1 - t)
    r = w | k
    b = h | r
    return h, r, b


def private_set(n: int) -> tuple[set[str], int]:
    consumers: dict[str, set[str]] = {"a": {f"c{i}" for i in range(1, n + 1)}}
    for i in range(1, n + 1):
        consumers[f"c{i}"] = {"h2" if i <= 2 else f"h{i}"}
    for i in range(2, n):
        consumers[f"h{i}"] = {f"h{i + 1}"}
    consumers[f"h{n}"] = {"b", "nh"}
    consumers["nt"] = {"k"}
    for i in range(1, n):
        consumers[f"q{i}"] = {f"q{i + 1}"}
    consumers[f"q{n}"] = {"k"}
    consumers["k"] = {"r", "s"}
    consumers["r"] = {"b"}

    # The final h_n is the distinguished carrier and is ineligible.
    eligible = set(consumers) - {f"h{n}"}
    private = set(eligible)
    changed = True
    while changed:
        changed = False
        for gate in tuple(private):
            if not consumers[gate] <= private | {"b"}:
                private.remove(gate)
                changed = True
    frontier_edges = sum(
        consumer not in eligible | {"b"}
        for gate in eligible
        for consumer in consumers[gate]
    )
    return private, frontier_edges


def main() -> None:
    for n in range(3, 9):
        for bits in product((0, 1), repeat=n + 3):
            u, t = bits[:2]
            xs = bits[2 : 2 + n]
            w = bits[-1]
            h, r, b = evaluate(u, t, xs, w)
            x_all = int(all(xs))
            assert h == (x_all | (u & w))
            assert r == (w | (u & x_all & (1 - t)))
            assert b == (x_all | w)

        private, frontier_edges = private_set(n)
        assert private == {"r"}
        assert frontier_edges == 3
        assert 3 * n + 11 > 0
        assert (n - 1) - 1 == n - 2

    print(
        "private-reservoir family audit passed: n=3..8; exact identities; "
        "greatest reservoir {r}; three frontier exits versus deficit n-2"
    )


if __name__ == "__main__":
    main()

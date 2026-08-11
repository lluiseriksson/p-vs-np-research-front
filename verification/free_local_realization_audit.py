#!/usr/bin/env python3
"""Regression audit for the cycle-176 free-local-realization witness."""

from __future__ import annotations

from itertools import product


def values(u: int, t: int, x: int, y: int, z: int) -> dict[str, int]:
    nt = 1 - t
    a = u & z
    c = x | a
    d = y | a
    h = c & d
    e = u & x
    f = e & y
    j = f & nt
    r = z | j
    b = h | r
    return {
        "x": x,
        "y": y,
        "z": z,
        "t": t,
        "nt": nt,
        "a": a,
        "c": c,
        "d": d,
        "h": h,
        "e": e,
        "f": f,
        "j": j,
        "r": r,
        "b": b,
    }


def truth(name: str) -> tuple[int, ...]:
    return tuple(values(*bits)[name] for bits in product((0, 1), repeat=5))


def main() -> None:
    rows = list(product((0, 1), repeat=5))
    for u, t, x, y, z in rows:
        row = values(u, t, x, y, z)
        assert row["h"] == ((x & y) | (u & z))
        assert row["r"] == (z | (u & x & y & (1 - t)))
        assert row["b"] == ((x & y) | z)

    for x, y, z in product((0, 1), repeat=3):
        assert values(0, 0, x, y, z)["r"] == z
        assert values(1, 0, x, y, z)["r"] == (z | (x & y))
        assert values(0, 1, x, y, z)["r"] == z
        assert values(1, 1, x, y, z)["r"] == z

    names = ["x", "y", "z", "t", "nt", "a", "c", "d", "h", "e", "f", "j", "r"]
    independent = []
    for name in names:
        is_independent = all(
            values(0, t, x, y, z)[name] == values(1, t, x, y, z)[name]
            for t, x, y, z in product((0, 1), repeat=4)
        )
        if is_independent:
            independent.append(name)
    assert independent == ["x", "y", "z", "t", "nt"]

    target = truth("b")
    pool = {name: truth(name) for name in independent}
    candidates = set(pool.values())
    candidates.update(tuple(1 - bit for bit in table) for table in pool.values())
    for left in pool.values():
        for right in pool.values():
            candidates.add(tuple(a & b for a, b in zip(left, right)))
            candidates.add(tuple(a | b for a, b in zip(left, right)))
    assert target not in candidates

    print("free-local-realization audit passed: 32 assignments; 5 independent predecessors; basis radius one excluded")


if __name__ == "__main__":
    main()

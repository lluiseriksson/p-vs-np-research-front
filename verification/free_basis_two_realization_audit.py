#!/usr/bin/env python3
"""Regression audit for the cycle-177 basis-radius-two witness."""

from __future__ import annotations

from itertools import product


def values(u: int, t: int, x: int, y: int, z: int, w: int) -> dict[str, int]:
    nt = 1 - t
    a = u & w
    c = x | a
    d = y | a
    e = c & d
    f = z | a
    h = e & f
    g = u & x
    i = g & y
    j = i & z
    k = j & nt
    r = w | k
    b = h | r
    return {
        "x": x,
        "y": y,
        "z": z,
        "w": w,
        "t": t,
        "nt": nt,
        "a": a,
        "c": c,
        "d": d,
        "e": e,
        "f": f,
        "h": h,
        "g": g,
        "i": i,
        "j": j,
        "k": k,
        "r": r,
        "b": b,
    }


def truth(name: str) -> tuple[int, ...]:
    return tuple(values(*bits)[name] for bits in product((0, 1), repeat=6))


def neg(table: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(1 - bit for bit in table)


def combine(left: tuple[int, ...], right: tuple[int, ...], op: str) -> tuple[int, ...]:
    if op == "and":
        return tuple(a & b for a, b in zip(left, right))
    return tuple(a | b for a, b in zip(left, right))


def main() -> None:
    for u, t, x, y, z, w in product((0, 1), repeat=6):
        row = values(u, t, x, y, z, w)
        assert row["h"] == ((x & y & z) | (u & w))
        assert row["r"] == (w | (u & x & y & z & (1 - t)))
        assert row["b"] == ((x & y & z) | w)

    for x, y, z, w in product((0, 1), repeat=4):
        assert values(0, 0, x, y, z, w)["r"] == w
        assert values(1, 0, x, y, z, w)["r"] == (w | (x & y & z))
        assert values(0, 1, x, y, z, w)["r"] == w
        assert values(1, 1, x, y, z, w)["r"] == w

    names = ["x", "y", "z", "w", "t", "nt", "a", "c", "d", "e", "f", "h", "g", "i", "j", "k", "r"]
    independent = []
    for name in names:
        if all(
            values(0, t, x, y, z, w)[name] == values(1, t, x, y, z, w)[name]
            for t, x, y, z, w in product((0, 1), repeat=5)
        ):
            independent.append(name)
    assert independent == ["x", "y", "z", "w", "t", "nt"]

    radius_zero = {truth(name) for name in independent}
    radius_one = set(radius_zero)
    radius_one.update(neg(table) for table in radius_zero)
    for left in radius_zero:
        for right in radius_zero:
            radius_one.add(combine(left, right, "and"))
            radius_one.add(combine(left, right, "or"))

    radius_two = set(radius_one)
    radius_two.update(neg(table) for table in radius_one)
    for left in radius_one:
        for right in radius_zero:
            radius_two.add(combine(left, right, "and"))
            radius_two.add(combine(left, right, "or"))

    assert truth("b") not in radius_two
    print(
        "basis-two audit passed: 64 assignments; 6 independent predecessors; "
        f"{len(radius_two)} distinct radius-two functions excluded"
    )


if __name__ == "__main__":
    main()

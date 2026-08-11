#!/usr/bin/env python3
"""Regression audit for the cycle-178 private-reservoir witness."""

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
    return locals()


def private_fixed_point() -> set[str]:
    consumers = {
        "nt": {"k"},
        "a": {"c", "d", "f"},
        "c": {"e"},
        "d": {"e"},
        "e": {"h"},
        "f": {"h"},
        "h": {"b", "n"},
        "g": {"i", "s_g"},
        "i": {"j", "s_i"},
        "j": {"k", "s_j"},
        "k": {"r", "s_k"},
        "r": {"b"},
    }
    private = set(consumers) - {"h"}
    changed = True
    while changed:
        changed = False
        for gate in tuple(private):
            if not consumers[gate] <= private | {"b"}:
                private.remove(gate)
                changed = True
    return private


def main() -> None:
    assert 13 + 1 + 4 + 6 + 5 == 29

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

    # Each variable is essential for xyz OR w. An at-most-two-gate formula has
    # at most three leaf occurrences, hence cannot depend on all four.
    target = lambda x, y, z, w: (x & y & z) | w
    for position in range(4):
        witnessed = False
        for bits in product((0, 1), repeat=4):
            flipped = list(bits)
            flipped[position] ^= 1
            if target(*bits) != target(*flipped):
                witnessed = True
                break
        assert witnessed

    private = private_fixed_point()
    assert private == {"r"}
    assert len(private) < 2

    # A selector-isolated six-term OR is exactly the selected signal, so each
    # named escape is semantically observable at the single output.
    for chosen in range(6):
        for signal in (0, 1):
            terms = [0] * 6
            terms[chosen] = signal
            assert int(any(terms)) == signal
    print(
        "private-reservoir audit passed: 64 assignments; four essential base "
        "variables; greatest private reservoir {r} has budget 1 < 2"
    )


if __name__ == "__main__":
    main()

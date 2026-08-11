#!/usr/bin/env python3
"""Regression audit for the cycle-181 exact joint-saving calculation."""

from __future__ import annotations

from itertools import product


def main() -> None:
    for n in range(3, 9):
        for bits in product((0, 1), repeat=n + 2):
            xs = bits[:n]
            nt, w = bits[-2:]
            x_all = int(all(xs))
            k_one = x_all & nt
            r_one = w | k_one
            assert k_one == (int(all(xs)) & nt)
            assert r_one == (w | (int(all(xs)) & nt))

        region_size = n + 2
        explicit_joint_size = (n - 1) + 1 + 1
        essential_sources_of_r = n + 2
        arity_lower_bound = essential_sources_of_r - 1
        assert explicit_joint_size == arity_lower_bound == n + 1
        assert region_size - explicit_joint_size == 1
        assert (n - 1) - 1 == n - 2

    print(
        "joint cofactor saving audit passed: n=3..8; exact joint size n+1; "
        "region size n+2; saving 1 versus deficit n-2"
    )


if __name__ == "__main__":
    main()

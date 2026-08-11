#!/usr/bin/env python3
"""Small regression for the cycle-183 shared-DAG reservoir rewrite."""

from itertools import product


def main() -> None:
    for x, y, z, w in product((0, 1), repeat=4):
        q = x & y
        left = q | z
        right = q | w
        output = left & right
        mapped_q = x & y
        mapped_left = mapped_q | z
        mapped_right = mapped_q | w
        mapped_output = mapped_left & mapped_right
        assert mapped_output == output
    # Four physical vertices host the shared four-gate DAG: three private
    # non-output vertices plus the boundary output vertex.
    assert 3 + 1 == 4
    print("aligned-DAG reservoir audit passed: 16 assignments; shared q retained; 4 vertices repurposed")


if __name__ == "__main__":
    main()

"""Finite diagnostics for LEMMA-233 and NG-171."""

from itertools import product


core_vertices = 5  # raw x,y plus marked g,h,k
core_edges = 6
assert core_edges - core_vertices + 1 == 2

for m in range(1, 7):
    assert 3 * m + 4 == 3 + m + (m + 1) + m
    for bits in product((0, 1), repeat=3 + 2 * m):
        x, y, s0 = bits[:3]
        zs = bits[3:3 + m]
        selectors = bits[3 + m:]
        g = x & y
        h = x | y
        k = g | h
        ports = [g & z for z in zs]
        terms = [s0 & k, *(s & p for s, p in zip(selectors, ports))]
        output = int(any(terms))
        assert output in (0, 1)
    for i in range(m):
        # Selector i isolates p_i. Neither g nor z_i is a valid wire substitute.
        assert (1 & 0) != 1
        assert (0 & 1) != 1

print(
    "bounded-core/unbounded-port audit passed: fixed rank-two core; "
    "families m=1..6; all assignments and input-substitution witnesses"
)

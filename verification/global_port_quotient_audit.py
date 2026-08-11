"""Finite diagnostics for LEMMA-234/235 and NG-172."""

from itertools import product


for m in range(1, 11):
    tables = []
    assignments = list(product((0, 1), repeat=m + 1))
    for i in range(m):
        table = tuple(g & zs[i] for g, *zs in assignments)
        assert any(table) and not all(table)
        tables.append(table)
    assert len(set(tables)) == m

print(
    "global port-quotient audit passed: m=1..10; "
    "all named port functions nonconstant and pairwise distinct"
)

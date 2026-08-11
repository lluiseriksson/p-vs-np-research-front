"""Finite graph audit for LEMMA-230 and NG-169."""


edges = {f"e{i}" for i in range(6)}
contracted = {
    "00": {"e0", "e1"},
    "01": {"e2", "e3"},
    "11": {"e4", "e5"},
}

parent_vertices = 6
parent_edges = 6
parent_rank = parent_edges - parent_vertices + 1
assert parent_rank == 1

surviving_literal = []
for code, pair in contracted.items():
    minor_vertices = parent_vertices - len(pair)
    minor_edges = parent_edges - len(pair)
    assert minor_edges - minor_vertices + 1 == parent_rank
    remaining = edges - pair
    assert len(remaining) == 4
    surviving_literal.append(remaining)

common = set.intersection(*surviving_literal)
assert common == set()
assert set.union(*contracted.values()) == edges

print(
    "cycle-support contraction audit passed: rank 1 in parent and three minors; "
    "two contractions each; common literal edge set empty"
)

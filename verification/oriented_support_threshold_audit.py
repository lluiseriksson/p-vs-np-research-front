"""Set-system audit for LEMMA-231/232 and NG-170."""

from itertools import combinations


carrier = frozenset((0, 1))
universe = set(range(8))
pairs = [frozenset(pair) for pair in combinations(universe, 2)]

and_max = 0
for loss_11 in pairs:
    union = carrier | loss_11
    and_max = max(and_max, len(union))
assert and_max == 4

or_max = 0
for loss_00 in pairs:
    for loss_01 in pairs:
        union = carrier | loss_00 | loss_01
        or_max = max(or_max, len(union))
assert or_max == 6

and_witness = carrier | frozenset((2, 3))
or_witness = carrier | frozenset((2, 3)) | frozenset((4, 5))
assert len(and_witness) == 4
assert len(or_witness) == 6
assert not (set(range(5)) - and_witness) == set()
assert not (set(range(7)) - or_witness) == set()

print(
    "oriented support-threshold audit passed: AND-to-OR max union 4; "
    "OR-to-AND max union 6; threshold covers realized abstractly"
)

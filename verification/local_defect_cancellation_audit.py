"""Truth-table checks for LEMMA-224 and the NG-165 mask witness."""

from itertools import product


for a, b, alpha, beta in product((0, 1), repeat=4):
    anew = a ^ alpha
    bnew = b ^ beta
    not_defect = (1 - a) ^ (1 - anew)
    and_defect = (a & b) ^ (anew & bnew)
    or_defect = (a | b) ^ (anew | bnew)
    assert not_defect == alpha
    assert and_defect == ((a & beta) ^ (b & alpha) ^ (alpha & beta))
    assert or_defect == (
        alpha ^ beta ^ (a & beta) ^ (b & alpha) ^ (alpha & beta)
    )
    if beta == 0:
        assert and_defect == (alpha & b)
        assert or_defect == (alpha & (1 - b))


for u, t, x, y in product((0, 1), repeat=4):
    n = 1 - t
    q = u & n
    old_a = x | q
    new_a = x
    mask = 1 - x
    old_c = old_a | mask
    new_c = new_a | mask
    assert old_c == new_c == 1
    assert (y & old_c) == (y & new_c) == y
    assert (old_a ^ new_a) == (u & (1 - t) & (1 - x))

print("local defect-cancellation audit passed: 16 local states; NG-165 all 16 assignments")

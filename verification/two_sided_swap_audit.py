"""Finite checks for LEMMA-227 and the NG-167 crossbar."""

from itertools import product


for op_name, op in (("AND", lambda x, y: x & y), ("OR", lambda x, y: x | y)):
    for a, b, alpha, beta in product((0, 1), repeat=4):
        anew = a ^ alpha
        bnew = b ^ beta
        zero = op(a, b) == op(anew, bnew)
        if (alpha, beta) == (0, 0):
            expected = True
        elif op_name == "AND" and (alpha, beta) == (1, 0):
            expected = b == 0
        elif op_name == "AND" and (alpha, beta) == (0, 1):
            expected = a == 0
        elif op_name == "OR" and (alpha, beta) == (1, 0):
            expected = b == 1
        elif op_name == "OR" and (alpha, beta) == (0, 1):
            expected = a == 1
        else:
            expected = a != b
        assert zero == expected
        if alpha == beta == 1 and zero:
            assert (anew, bnew) == (b, a)


for u, t, x, y in product((0, 1), repeat=4):
    q = u & (1 - t)
    r = 1 - q
    a = (r & x) | (q & y)
    b = (r & y) | (q & x)
    assert (a, b) == ((y, x) if (u, t) == (1, 0) else (x, y))
    assert (a | b) == (x | y)
    assert (a & b) == (x & y)
    defect = q & (x ^ y)
    assert (a ^ x) == defect
    assert (b ^ y) == defect

for z, fresh in product((0, 1), repeat=2):
    double_not = 1 - (1 - z)
    reconvergent_identity = (z & fresh) | (z & (1 - fresh))
    assert double_not == z
    assert reconvergent_identity == z

print(
    "two-sided swap audit passed: 32 local operation states; "
    "crossbar all 16 assignments; both padding identities"
)

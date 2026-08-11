"""Finite checks for LEMMA-225/226 and NG-166."""

from itertools import product


def bit(table, u, t, x):
    return (table >> ((u << 2) | (t << 1) | x)) & 1


triples = 0
or_certificates = 0
and_certificates = 0
for a in range(256):
    for anew in range(256):
        if not all(bit(a, u, t, x) == bit(anew, u, t, x)
                   for u, t in ((0, 0), (0, 1), (1, 1))
                   for x in (0, 1)):
            continue
        for b in range(256):
            triples += 1
            d = tuple(bit(a, 1, 0, x) ^ bit(anew, 1, 0, x) for x in (0, 1))
            or_mask = all(not (d[x] and not bit(b, 1, 0, x)) for x in (0, 1))
            and_mask = all(not (d[x] and bit(b, 1, 0, x)) for x in (0, 1))
            or_equal = all((bit(a, u, t, x) | bit(b, u, t, x)) ==
                           (bit(anew, u, t, x) | bit(b, u, t, x))
                           for u, t, x in product((0, 1), repeat=3))
            and_equal = all((bit(a, u, t, x) & bit(b, u, t, x)) ==
                            (bit(anew, u, t, x) & bit(b, u, t, x))
                            for u, t, x in product((0, 1), repeat=3))
            assert or_mask == or_equal
            assert and_mask == and_equal
            or_certificates += or_mask
            and_certificates += and_mask

assert triples == 262144


for m in range(1, 6):
    for bits in product((0, 1), repeat=3 + 2 * m):
        u, t, w = bits[:3]
        xs = bits[3:3 + m]
        selectors = bits[3 + m:]
        q = u & (1 - t)
        mask = q | w
        old_c = [(x | q) | mask for x in xs]
        new_c = [x | mask for x in xs]
        assert old_c == new_c
        old_out = int(any(s & c for s, c in zip(selectors, old_c)))
        new_out = int(any(s & c for s, c in zip(selectors, new_c)))
        assert old_out == new_out
    for i in range(m):
        selectors = [int(j == i) for j in range(m)]
        # q=0, x_i=0, w=1: c_i=1 but a_i=0.
        xs = [0] * m
        mask = 1
        seals = [x | mask for x in xs]
        exact = int(any(s & c for s, c in zip(selectors, seals)))
        by_a = int(any(s & (xs[j] if j == i else seals[j])
                       for j, s in enumerate(selectors)))
        assert exact == 1 and by_a == 0
        # q=0, x_i=1, w=0: c_i=1 but b=0.
        xs[i] = 1
        mask = 0
        seals = [x | mask for x in xs]
        exact = int(any(s & c for s, c in zip(selectors, seals)))
        by_b = int(any(s & (mask if j == i else seals[j])
                       for j, s in enumerate(selectors)))
        assert exact == 1 and by_b == 0

print(
    "one-sided mask/payment audit passed: "
    f"{triples} triples; OR certs={or_certificates}; "
    f"AND certs={and_certificates}; family m=1..5"
)

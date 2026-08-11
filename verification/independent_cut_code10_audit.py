"""Finite truth-table audits for LEMMA-222/223 and NG-164."""

from itertools import product


def bit(table, u, t, x):
    return (table >> ((u << 2) | (t << 1) | x)) & 1


checked = 0
for a in range(256):
    for b in range(256):
        if all(bit(a, u, t, x) == bit(b, u, t, x)
               for u, t in ((0, 0), (0, 1), (1, 1))
               for x in (0, 1)):
            for u, t, x in product((0, 1), repeat=3):
                defect = bit(a, 1, 0, x) ^ bit(b, 1, 0, x)
                expected = u & (1 - t) & defect
                assert (bit(a, u, t, x) ^ bit(b, u, t, x)) == expected
            checked += 1


def witness_a(u, t, x):
    return x | (u & (1 - t))


def witness_b(u, t, x):
    return x


for u, t, x in product((0, 1), repeat=3):
    if (u, t) in ((0, 0), (0, 1), (1, 1)):
        assert witness_a(u, t, x) == witness_b(u, t, x)
assert witness_a(1, 0, 0) != witness_b(1, 0, 0)
assert checked == 1024

print(
    "independent-cut/code-10 audit passed: "
    "1024 three-code-equal function pairs; exact u&~t defect factorization"
)

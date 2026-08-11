"""Finite diagnostics for LEMMA-221's canonical difference frontier."""

from itertools import product


NAMES = ("v", "x", "z", "y")


def table(fn):
    return tuple(int(fn(**dict(zip(NAMES, bits)))) for bits in product((0, 1), repeat=4))


def circuit(rewrite, sealed):
    funcs = {}
    funcs["e"] = table(lambda v, x, z, y: x if rewrite else (v or x))
    funcs["c"] = table(lambda v, x, z, y: (x if rewrite else (v or x)) and z)
    if sealed:
        funcs["n"] = tuple(1 - bit for bit in funcs["c"])
        funcs["a"] = tuple(c or n for c, n in zip(funcs["c"], funcs["n"]))
        funcs["o"] = tuple(y and a for (*_, y), a in zip(product((0, 1), repeat=4), funcs["a"]))
        edges = {("e", "c"), ("c", "n"), ("c", "a"), ("n", "a"), ("a", "o")}
    else:
        funcs["o"] = tuple(c and y for (*_, y), c in zip(product((0, 1), repeat=4), funcs["c"]))
        edges = {("e", "c"), ("c", "o")}
    return funcs, edges


def audit(sealed):
    old, old_edges = circuit(False, sealed)
    new, new_edges = circuit(True, sealed)
    delta = {name for name in old if old[name] != new[name]}
    boundary = {
        target
        for source, target in old_edges | new_edges
        if source in delta and target not in delta
    }
    assert all(old[name] == new[name] for name in boundary)
    assert (("o" not in delta) == (old["o"] == new["o"]))
    return delta, boundary


sealed_delta, sealed_boundary = audit(True)
open_delta, open_boundary = audit(False)
assert sealed_delta == {"e", "c", "n"}
assert sealed_boundary == {"a"}
assert "o" in open_delta
assert open_boundary == set()

print(
    "canonical difference-frontier audit passed: "
    "sealed delta={e,c,n}, boundary={a}; unsealed output belongs to delta"
)

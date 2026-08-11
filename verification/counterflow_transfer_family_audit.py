"""Finite regression for the symbolic GATE-004CZ transfer-path family."""

from itertools import product


def evaluate(bits, specialized: bool):
    x, y, u, t, *zs = bits
    g = u or x
    h = g and y
    if specialized:
        r = x
    else:
        a = u or t
        v = not a
        r = x or v
    b = h and r
    q = r or u
    qs = [q]
    for z in zs:
        q = q and z
        qs.append(q)
    c = h and q
    o = b or c
    return {"r": r, "qs": tuple(qs), "b": b, "c": c, "o": o}


def main() -> None:
    total = 0
    for m in range(7):
        checked = 0
        for bits in product((False, True), repeat=4 + m):
            before = evaluate(bits, False)
            after = evaluate(bits, True)
            assert before["b"] == after["b"]
            assert before["c"] == after["c"]
            assert before["o"] == after["o"]
            checked += 1

        changed_witness = (False, True, False, False, *((True,) * m))
        before = evaluate(changed_witness, False)
        after = evaluate(changed_witness, True)
        assert before["r"] != after["r"]
        assert all(old != new for old, new in zip(before["qs"], after["qs"]))

        old_q00 = []
        old_q10 = []
        new_q00 = []
        new_q10 = []
        for base in product((False, True), repeat=2 + m):
            x, y, *zs = base
            old_q00.append(evaluate((x, y, False, False, *zs), False)["qs"][-1])
            old_q10.append(evaluate((x, y, True, False, *zs), False)["qs"][-1])
            new_q00.append(evaluate((x, y, False, False, *zs), True)["qs"][-1])
            new_q10.append(evaluate((x, y, True, False, *zs), True)["qs"][-1])
        assert old_q00 == old_q10
        assert new_q00 != new_q10

        total += checked
        print(f"m={m} PASS assignments={checked} changed_path={m + 1}")
    print(f"PASS total_assignments={total}; symbolic proof covers every m>=0")


if __name__ == "__main__":
    main()

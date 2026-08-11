"""Exact finite regression for GATE-004CY-TERMINAL-OUTPUT-ONLY."""

from itertools import product


def evaluate(x: bool, y: bool, u: bool, t: bool, specialized: bool):
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
    c = h and q
    o = b or c
    return {"r": r, "b": b, "q": q, "c": c, "o": o}


def cofactor_table(signal: str, u: bool, t: bool, specialized: bool):
    return tuple(
        evaluate(x, y, u, t, specialized)[signal]
        for x, y in product((False, True), repeat=2)
    )


def main() -> None:
    assignments = 0
    for x, y, u, t in product((False, True), repeat=4):
        before = evaluate(x, y, u, t, False)
        after = evaluate(x, y, u, t, True)
        assert before["b"] == after["b"]
        assert before["c"] == after["c"]
        assert before["o"] == after["o"]
        assignments += 1

    r00 = cofactor_table("r", False, False, False)
    r10 = cofactor_table("r", True, False, False)
    q00 = cofactor_table("q", False, False, False)
    q10 = cofactor_table("q", True, False, False)
    rp00 = cofactor_table("r", False, False, True)
    rp10 = cofactor_table("r", True, False, True)
    qp00 = cofactor_table("q", False, False, True)
    qp10 = cofactor_table("q", True, False, True)

    assert r00 != r10
    assert q00 == q10
    assert rp00 == rp10
    assert qp00 != qp10

    print(f"PASS assignments={assignments} preserved=b,c,o")
    print("R0 transfer verified: b leaves exactly when c enters")


if __name__ == "__main__":
    main()

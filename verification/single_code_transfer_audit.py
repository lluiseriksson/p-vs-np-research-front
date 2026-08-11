"""Exact regression for GATE-004DA-SATISFYING-EXTERIOR-ONLY."""

from itertools import product


def evaluate(x: bool, u: bool, t: bool, specialized: bool):
    p = u or x
    h = p or t
    if specialized:
        r = x or (not t)
    else:
        a = u or t
        v = not a
        r = x or v
    b = h or r
    w = not t
    d = u and w
    s = x or d
    q = r and s
    c = h or q
    o = b and c
    return {"r": r, "b": b, "q": q, "c": c, "o": o}


def cofactor(signal: str, u: bool, t: bool, specialized: bool):
    return tuple(evaluate(x, u, t, specialized)[signal] for x in (False, True))


def main() -> None:
    assignments = 0
    for x, u, t in product((False, True), repeat=3):
        before = evaluate(x, u, t, False)
        after = evaluate(x, u, t, True)
        assert before["b"] == after["b"]
        assert before["c"] == after["c"]
        assert before["o"] == after["o"]
        assignments += 1

    codes = ((False, False), (True, False), (False, True), (True, True))
    for signal in ("r", "q"):
        changed = [
            index
            for index, (u, t) in enumerate(codes)
            if cofactor(signal, u, t, False) != cofactor(signal, u, t, True)
        ]
        assert changed == [1]

    assert cofactor("r", False, False, False) != cofactor("r", True, False, False)
    assert cofactor("r", False, False, True) == cofactor("r", True, False, True)
    assert cofactor("q", False, False, False) == cofactor("q", True, False, False)
    assert cofactor("q", False, False, True) != cofactor("q", True, False, True)

    print(f"PASS assignments={assignments} preserved=b,c,o")
    print("PASS only code 10 changes; R0 transfer verified: b -> c")


if __name__ == "__main__":
    main()

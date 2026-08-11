# GATE-004AT — a minimum canonical circuit has a pure-base bottleneck

**Label: EXPLORATORY**

## Falsifiable theorem

For the canonical base-tail function `F=H AND W_m` in GATE-004AG, prove that
some minimum unrestricted circuit contains a gate satisfying conditions 1–3
of LEMMA-143: it depends only on base variables, every essential base-to-output
path passes through it, and its upstream cone meets the downstream cone only
at that gate.

If no minimum circuit has such a gate, the theorem is false. If proved,
LEMMA-143 gives exact `C(F)=K+6m` for `p=4`, makes the displayed circuit
minimum, and proves alternative 1 of GATE-004AG.

Disjoint variable supports alone do not prove this topology, as recorded by
GATE-004AT-DISJOINT-SUPPORT-ONLY. A successful proof must use the canonical
agreement rows or a circuit transformation that creates the separator without
increasing size.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for the canonical base conjoined with fresh disjoint one-negative clauses |
| Uniform/non-uniform | Uniform canonical instance; fully non-uniform minimum-circuit adversary |
| Circuit size | Separator would prove exact `K+6m` and the displayed `7m` tail quotient for `p=4` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed vertex separators and Boolean cofactors |
| Asymptotic quantifiers | Every sufficiently large compatible canonical instance and at least one of its minimum circuits |
| Regime | Exact canonical base-tail gate; not arbitrary direct sum, a SAT lower bound, or a terminal result |

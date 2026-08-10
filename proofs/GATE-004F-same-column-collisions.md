# GATE-004F — same-column internal collision count

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `A,B>0`, `0<=beta<1`, `delta>0`, and `n0`
such that for every `n>=n0` and every minimum circuit `C_n` computing
`SAT-gamma_n`, there are `k>=1` and `0<=l<=k` with `12k<=A n^beta` for which
at least

`B n^(beta+delta)+3`

original gates have residual functions under `P_{k,l}` that are constant,
equal to a free input, or equal to the residual function of an earlier gate in
a topological ordering, counting all but the earliest representative of each
nontrivial residual-function class.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for exact SAT-gamma slices; ENC-004 restrictions; exact internal residual functions |
| Uniform/non-uniform | Fully non-uniform circuit adversary, topological order, and prefix choice |
| Circuit size | At least `B n^(beta+delta)+3` directly mergeable/replacable gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | No verifier advice; restriction choice may depend non-uniformly on the circuit |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed constants; every sufficiently large `n`; every minimum circuit; exists `k,l` in the stated range |
| Regime | Worst-case exact total-language computation; malformed suffixes reject |

## Bridge

LEMMA-005 deletes every counted gate by semantic replacement or merging. At
most three gates restore constants in the original constant-free basis, so the
net loss is at least `B n^(beta+delta)`. Therefore GATE-004F implies GATE-004E
and the existing recurrence chain reaches GATE-004.

## Why this is the next brick

The theorem speaks only about collisions *within one restriction column*.
Equal outputs across columns, Hamming separation, prefix essentiality, and a
small recognizer for the neutral set do not establish it: LEMMA-008 realizes
all those features with an arbitrary core and only an `O(p)` shell. This failed
route is `GATE-004E-CROSS-TABLE — NO-GO`.

ENC-005 adds a tempting local comparison: a prefix two bits from the neutral
context has constant-zero residual. LEMMA-009 shows that this also fails
generically. The selector `s AND G` has adjacent hard and zero cofactors while
the hard restriction loses at most one gate. Hence
`GATE-004F-ANNIHILATOR — NO-GO` for any inference using only that cofactor
pair and selector essentiality.

The next attempt must identify a SAT-specific invariant of internal residual
gate functions that forces many same-column equivalence classes to merge. The
next audit will examine the full four-cofactor table of the two differing
operator bits; no derivative or sensitivity claim is assumed in advance.

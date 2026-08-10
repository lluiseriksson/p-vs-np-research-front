# GATE-004E — collision surplus in one neutral-prefix family

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `A,B>0`, `0<=beta<1`, `delta>0`, and `n0`
such that for every `n>=n0` and every minimum circuit `C_n` for
`SAT-gamma_n`, there is an integer `k>=1` with

`12k <= A n^beta`

and an index `0<=l<=k` such that the LEMMA-005 semantic quotient of `C_n`
under prefix `P_{k,l}` has at most

`|C_n|-B n^(beta+delta)`

gates after constant normalization. The quotient computes the exact
length-`n-12k` SAT-gamma slice.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for exact SAT-gamma slices; the explicit neutral-prefix family; semantic restriction quotient |
| Uniform/non-uniform | Fully non-uniform circuit adversary and per-circuit choice of `k,l` |
| Circuit size | Net quotient loss at least `B n^(beta+delta)` under length loss at most `A n^beta` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | No verifier advice; prefix choice may depend non-uniformly on the circuit |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed constants; every sufficiently large `n`; every minimum circuit; exists `k,l` in the stated range |
| Regime | Worst-case exact total-language computation; malformed suffixes reject |

## Bridge

LEMMA-006 proves that every permitted restriction computes
`SAT-gamma_{n-12k}`. Thus GATE-004E is a concrete sufficient subgate of
GATE-004D. LEMMA-002 then gives GATE-004 through the existing chain. The gate
does not supply downstream exponent amplification or a terminal proof.

## Attempt: parser-state multiplicity

For fixed `k`, the `k+1` prefixes are separated assignments of the same `12k`
coordinates and every one produces the same output residual. This makes an
averaging attempt explicit: compare the internal residual functions of each
gate across all `k+1` columns and seek a column with many constants,
collisions, or dead gates.

The output equality alone does not prove that conclusion. LEMMA-007 realizes
the same neutral-subcube pattern, with every prefix coordinate essential,
around an arbitrary shared core using only an `O(k^2)` decoder shell. Hence
parser-state multiplicity and input essentiality have no generic bridge to a
loss depending on core complexity. This failed lifting is
`GATE-004D-PARSER-LIFT — NO-GO`.

GATE-004E remains open only as a SAT-specific internal-gate statement. The
next attack is to analyze the cross-restriction table

`( residual function of gate v under P_{k,l} )_{v,l}`

and identify a property forced by exact SAT semantics but violated by the
LEMMA-007 shared-core construction. No such property is currently claimed.

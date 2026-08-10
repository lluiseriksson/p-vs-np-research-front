# LEMMA-010 — a complete one-hot cofactor square can retain the hard core

**Label: PROVED**

## Statement

Let `G(z)` be any nonzero Boolean function on at least one input and define

`F(q_1,q_2,z)=q_1 AND NOT(q_2) AND G(z)`.

The four cofactors of `(q_1,q_2)` consist of exactly one copy of `G`, at `10`,
and three constant-zero functions. Both selector coordinates are essential,
yet

`S(F)-S(G) <= 3`.

Consequently, even the complete one-hot cofactor table does not generically
force substantial gate loss when its hard column is selected.

## Model card

| Field | Value |
|---|---|
| Computational model | General acyclic Boolean circuits and all four restrictions of two selector bits |
| Uniform/non-uniform | Fully non-uniform circuit complexity |
| Circuit size | Exact minimum gate count; hard-cofactor gap at most three |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every positive-arity nonzero Boolean function `G` |
| Regime | Worst-case exact total Boolean functions; no promise or distribution |

## Proof

Append to a minimum circuit for `G` one NOT gate on `q_2` and two AND gates.
This proves `S(F)<=S(G)+3`. The cofactor table follows directly. Since `G` is
nonzero, fix a satisfying `z`; changing `q_1` while `q_2=0`, or changing
`q_2` while `q_1=1`, changes the output, so both selector bits are essential.

Restricting any minimum circuit for `F` by `(q_1,q_2)=(1,0)` produces a
circuit for `G` and therefore cannot remove more than
`S(F)-S(G)<=3` gates after normalization. QED.

## Scope

ENC-006 proves that the exact local SAT-gamma operator-bit square has this
one-hot output form. The lemma rules out conclusions based only on the four
output cofactors and selector essentiality. It does not constrain internal
gate residuals arising from longer, nonlocal SAT prefixes.

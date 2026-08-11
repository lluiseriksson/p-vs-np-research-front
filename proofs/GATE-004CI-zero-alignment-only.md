# GATE-004CI-ZERO-ALIGNMENT-ONLY — the active branch cannot normalize to `W=0`

**Label: NO-GO**

## Tempting inference

Assume or normalize to a common backbone with `W=0`, then use complete
satisfying-cofactor alignment to expose three deletion classes.

## Failure

LEMMA-189 proves `W>=1` for every pruning triple in the active switching
branch. The earliest mixed NOT survives all three satisfying minors and has
`n_01!=n_11`; it is an unavoidable misaligned common gate. Postulating `W=0`
therefore assumes away the branch whose exclusion is the goal.

This does not refute a same-size rewrite that would leave the switching branch
and thereby produce the desired contradiction. It closes only arguments that
treat zero alignment as a free normal form. A valid extremal proof must descend
toward the mandatory floor, analyze the unique mandatory misalignment if
`W=1` is reached, or derive the private/non-bridge contradiction earlier.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted switching-branch plateau parents and satisfying pruning triples |
| Uniform/non-uniform | Every individual finite non-uniform operational tuple |
| Circuit size | No new size bound; structural lower floor `W>=1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor inequality and finite survivor intersection |
| Asymptotic quantifiers | Every active GATE-004CI switching tuple |
| Regime | Structural no-go for zero-alignment-only normalization; not a plateau counterexample, SAT lower bound, or terminal result |

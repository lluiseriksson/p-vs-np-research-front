# LEMMA-012 — exact accounting for a joint two-restriction quotient

**Label: PROVED**

## Statement

Let `C` have `S` gates. For two restrictions, let `q_0,q_1` be the gate counts
of their individually normalized semantic quotients, let `q_J` be the count
after additionally merging semantically identical gates across the two
quotients, and define

`ell_b=S-q_b`,

`x=q_0+q_1-q_J`.

Then `x>=0` and

`q_J = 2S-ell_0-ell_1-x`.

Consequently, for every `L>=0`,

`q_J <= S-L`

if and only if

`ell_0+ell_1+x >= S+L`.

Thus a joint quotient smaller than the single parent by `L` requires at least
`S+L` total within-branch loss plus cross-branch sharing. The first `S` units
only cancel the duplication of the parent circuit; the additional `L` is the
actual lower-bound surplus.

## Model card

| Field | Value |
|---|---|
| Computational model | Two restricted copies of one acyclic Boolean circuit; normalized semantic quotients and cross-copy merging |
| Uniform/non-uniform | Fully non-uniform, exact semantic accounting |
| Circuit size | Exact finite gate-count identity |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one in the intended application |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Integer accounting only; no algebraic computation model |
| Asymptotic quantifiers | Every finite circuit, every pair of restrictions, and every real/integer target loss `L>=0` |
| Regime | Worst-case exact circuit computation; multi-output quotient |

## Proof

The disjoint union of the two individual quotients has `q_0+q_1` gates.
Cross-copy semantic merging and subsequent dead-gate deletion save exactly `x`
by definition, so `q_J=q_0+q_1-x` and `x>=0`. Substituting
`q_b=S-ell_b` gives the first identity. Rearranging

`2S-ell_0-ell_1-x <= S-L`

gives the stated equivalence. QED.

## Consequence for GATE-004G

Separate statements `ell_0>=L` and `ell_1>=L` yield only
`ell_0+ell_1>=2L`. When `S` is much larger than `L`, this does not pay the
mandatory duplication term `S`; without a proved cross-sharing contribution
or much larger within-branch losses, it gives no circuit for the OR of the
branches smaller than `C`.

This is an accounting guard, not a circuit lower bound. GATE-004G requires the
SAT-specific surplus `ell_0+ell_1+x-S >= B n^delta+1`.

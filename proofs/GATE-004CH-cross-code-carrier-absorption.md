# GATE-004CH — make carrier absorption incompatible across satisfying codes

**Label: EXPLORATORY**

For each satisfying code `s in {00,01,11}`, fix an arbitrary rank-neutral
two-binary-gate pruning map `pi_s` from the hypothetical plateau parent to a
minimum `K`-gate circuit for `A`. A canonical carrier region from LEMMA-187 is
**absorbed** by `pi_s` if its nonconstant image lies in surviving base
computation; it is **exposed** if its routes must meet a deleted binary
contraction class.

At code `11`, use the `10/11` carrier sourced by `t` and the two post-divergence
arms of the `01/11` carrier supplied by the earliest mixed NOT and its shared
exit. Track their corresponding images under `pi_00,pi_01,pi_11`.

## Falsifiable theorem

For every triple of rank-neutral minimum pruning maps, at least one satisfying
code exposes all three regions in three distinct binary elimination classes.
If two regions are absorbed by a common surviving base subcone across the
required codes, or are exposed through the same eliminated contraction class,
that cross-code alignment instead yields either

1. an admissible LEMMA-183 private realization certificate, or
2. deletion of a non-bridge edge of `gamma` in one satisfying minor.

Three distinctly exposed regions require at least three binary eliminations,
contradicting LEMMA-178. The two alignment outcomes contradict extremality or
LEMMA-185. Proving this theorem therefore establishes GATE-004CG.

The quantifier over every pruning triple is essential. Canonical carrier
regions can survive as base computation, so single-code carrier counting is
invalid by GATE-004CG-CARRIER-COVERAGE-ONLY.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted plateau DAG and three rank-neutral pruning maps to minimum base circuits |
| Uniform/non-uniform | Every individual non-uniform operational GATE-004CG parent; uniform fresh implication pair |
| Circuit size | One code with three exposed regions versus exactly two binary eliminations, or private/non-bridge contradiction |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Canonical Boolean-difference carriers and cycle minors over `F_2` |
| Asymptotic quantifiers | Every operational parent and every triple of minimum prunings for `00,01,11` |
| Regime | Exact worst-case cross-code absorption gate; not a SAT lower bound or terminal result |

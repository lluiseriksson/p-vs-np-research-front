# GATE-004BE — one neutral clause prunes one resource

**Label: PROVED**

Assume `sigma>=2`, `Delta_j=sigma-1`, and let `C` be a minimum pruned circuit
for `J_j`. LEMMA-153 gives `N(C)+r(C)=j+1`.

## Theorem

Some clause `i` has the following property: after the neutral
restriction

`(u_i,t_i)=(0,1)`,

constant propagation and pruning leave a circuit for `J_{j-1}` with

`N+r<=j`.

LEMMA-159 excludes rank zero under `sigma>=2`. GATE-004BF closes rank one,
and GATE-004BL closes every rank at least two. These cases exhaust the parent
cycle rank.

## Sufficiency for GATE-004BD

The restricted circuit gives `mu_{j-1}<=j`, hence LEMMA-153 gives

`Delta_{j-1}=sigma+j-1-mu_{j-1}>=sigma-1`.

Deficits are nondecreasing by LEMMA-152, so
`Delta_{j-1}<=Delta_j=sigma-1`; equality follows. Iterating the operation down
to `min(m,K+sigma-1)` proves GATE-004BD. Clause symmetry identifies the
surviving set with the canonical prefix.

LEMMA-158 supplies the complete satisfying-base count strata. The proof above
does not follow from those counts alone: LEMMA-164 supplies the required core
source and rank drop, while LEMMA-165 supplies the Boolean interface
dichotomy.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unrestricted implication circuits under neutral clause restrictions |
| Uniform/non-uniform | Every individual non-uniform one-excess minimum circuit; symmetric uniform clause family |
| Circuit size | Parent `N+r=j+1`; target restricted `N+r<=j` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2`, NOT gates, and Boolean restriction semantics |
| Asymptotic quantifiers | Every `j>=2` in every compatible near-maximal descent stratum with `sigma>=2` |
| Regime | Exact worst-case sufficient subgate proving GATE-004BD; not full GATE-004BA, a SAT lower bound, or a terminal result |

# LEMMA-169 — every at-most-one-excess tail descends

**Label: PROVED**

Let `Q` be any nonzero Boolean base on variables disjoint from `j>=2`
implication clauses. If the canonical function `Q W_j` has a circuit with

`N+r<=j+1`,

then `Q W_{j-1}` has a circuit with

`N+r<=j`.

## Proof

If `Q=1`, the standard formula for `W_{j-1}` has resource `j-1`. Assume
`Q` is nonconstant and use the notation `mu_i, sigma` of LEMMA-153.

If `mu_j<=j`, monotonicity `mu_{j-1}<=mu_j` gives the result. It remains to
consider `mu_j=j+1`.

If `sigma<=1`, the general upper bound gives

`mu_{j-1}<=sigma+j-1<=j`.

If `sigma>=2`, then

`Delta_j=sigma+j-mu_j=sigma-1`.

GATE-004BE applies to a minimum circuit at this one-excess stratum and gives a
neutral clause restriction with resource at most `j`. Clause symmetry
identifies its result with `Q W_{j-1}`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unrestricted canonical implication circuits and arbitrary witness circuits |
| Uniform/non-uniform | Every individual non-uniform base; uniform symmetric tail family |
| Circuit size | Premise `mu_j<=j+1`; conclusion `mu_{j-1}<=j` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2` and Boolean restrictions |
| Asymptotic quantifiers | Every nonzero finite base `Q` and every `j>=2` |
| Regime | Exact worst-case corollary of GATE-004BE; not a SAT lower bound or terminal result |

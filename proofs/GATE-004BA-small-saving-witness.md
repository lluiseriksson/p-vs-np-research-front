# GATE-004BA — every final saving has a small clause witness

**Label: EXPLORATORY**

Let `d=Delta_m` for the canonical implication sequence and put

`k_*=min(m,K+d)`.

## Falsifiable theorem

Prove

`Delta_{k_*}=d`.

Equivalently, using LEMMA-153, prove that some circuit for `J_{k_*}` has

`N+r<=sigma+k_*-d`.

A compatible canonical family whose final saving `d` first reaches its final
value after `K+d` clauses falsifies the theorem.

## Exact equivalence with GATE-004AZ

LEMMA-152 makes `Delta_j` nondecreasing. Therefore `Delta_{k_*}=Delta_m`
holds exactly when no positive increment occurs after `K+d` (with the case
`m<=K+d` automatic). This is precisely

`r<=Delta_m+K`,

the statement of GATE-004AZ. Thus GATE-004BA is neither a surrogate nor an
unstated strengthening: it is the small-witness form of the active sufficient
gate.

The resource formulation identifies the next proof obligation. Every one of
the `d` missing displayed `N+r` resources at size `m` must already be
witnessed on at most `K+d<=2K` clauses. A proof must use circuit topology or
Boolean semantics beyond the cardinality form of dependency-cone Hall;
GATE-004BA-HALL-INCIDENCE-ONLY gives an exact abstract obstruction to the
latter.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted canonical implication circuits and exact NOT-plus-cycle-rank resources |
| Uniform/non-uniform | Uniform symmetric clause family; fully non-uniform circuit minima |
| Circuit size | Final deficit `d`; target saturation by `k_*=min(m,K+d)` and resource upper `sigma+k_*-d` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Fundamental cycle rank over `F_2` and Boolean circuit semantics |
| Asymptotic quantifiers | Every sufficiently large compatible canonical instance |
| Regime | Exact equivalent small-witness form of GATE-004AZ; not a SAT lower bound or terminal result |

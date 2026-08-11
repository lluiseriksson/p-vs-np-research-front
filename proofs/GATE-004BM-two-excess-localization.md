# GATE-004BM — localize resource excess two

**Label: EXPLORATORY**

Use the notation of LEMMA-153 and assume

`sigma>=3` and `Delta_m=sigma-2`.

Put `k_2=min(m,K+sigma-2)`.

## Falsifiable theorem

Then `Delta_{k_2}=sigma-2`. Equivalently, `J_{k_2}` has a circuit with
`N+r<=k_2+2`.

A sufficient local operation would be: whenever a minimum circuit for `J_j`
has `N+r=j+2`, some neutral clause restriction leaves a circuit for `J_{j-1}`
with `N+r<=j+1`.

## First audited obstruction

The source-rank argument that proves GATE-004BL has one unit of slack here.
For a degree-two core source with no cut clause and residual rank `r-1`, the
LEMMA-119/139 accounting can meet `N+r=j+2` with equality. Thus the strict
contradiction used at resource excess one does not repeat automatically.
The next brick must classify this equality case or produce a second
independent interface/rank reduction. This observation is not a no-go theorem
and does not promote GATE-004BM.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unrestricted canonical implication circuits under neutral clause restrictions |
| Uniform/non-uniform | Uniform symmetric clause family; fully non-uniform endpoint and prefix minima |
| Circuit size | Premise `Delta_m=sigma-2`, equivalently `mu_m=m+2`; target prefix `N+r<=k_2+2` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2` and Boolean restriction semantics |
| Asymptotic quantifiers | Every sufficiently large compatible canonical instance with `sigma>=3` and `Delta_m=sigma-2` |
| Regime | Exact worst-case two-excess subgate of GATE-004BA; not a SAT lower bound or terminal result |

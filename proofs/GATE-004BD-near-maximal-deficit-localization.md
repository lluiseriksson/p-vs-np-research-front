# GATE-004BD — localize the near-maximal deficit

**Label: EXPLORATORY**

Use the notation of LEMMA-153 and assume

`sigma>=2` and `Delta_m=sigma-1`.

Put

`k_1=min(m,K+sigma-1)`.

## Falsifiable theorem

Prove

`Delta_{k_1}=sigma-1`.

Equivalently, prove that `J_{k_1}` has a circuit with

`N+r<=k_1+1`.

A compatible canonical instance whose deficit first reaches `sigma-1` after
`K+sigma-1` clauses falsifies the theorem.

## Why this is the next stratum

GATE-004BB and LEMMA-157 close the apparent maximal endpoint by proving it
collapses to `sigma=0`. The first unresolved resource excess is therefore

`mu_m=m+1`.

Unlike the maximal case, a satisfying-base restriction with resource budget
`m+1` need not be a formula with exactly `m` NOT gates: rank one, an extra
NOT, or a higher-rank equality case of LEMMA-139 remain possible. The next
attack must classify these one-excess topologies or prove a one-excess
restriction/exchange theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted canonical implication circuits with exact NOT-plus-cycle-rank resource excess one |
| Uniform/non-uniform | Uniform symmetric clause family; fully non-uniform endpoint and prefix minima |
| Circuit size | Premise `Delta_m=sigma-1`, equivalently `mu_m=m+1`; target prefix `N+r<=k_1+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2` and Boolean restriction semantics |
| Asymptotic quantifiers | Every sufficiently large compatible canonical instance with `sigma>=2` and `Delta_m=sigma-1` |
| Regime | Falsifiable worst-case near-maximal subgate of GATE-004BA; not a SAT lower bound or terminal result |

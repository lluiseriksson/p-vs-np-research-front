# LEMMA-158 — exact satisfying-base strata at resource excess one

**Label: PROVED**

Assume `sigma>=2` and `Delta_m=sigma-1`. Let `C` be any minimum pruned circuit
for `J_m`, with global NOT count `N` and cycle rank `r`. Then

`N+r=m+1`.

Fix any satisfying base assignment, propagate constants, and prune. If the
residual `W_m` circuit has `q` NOT gates and cycle rank `rho`, exactly one of
the following holds:

1. `q+rho=m`, necessarily `rho=0` and `q=m`;
2. `q+rho=m+1` and `rho=0,q=m+1`;
3. `q+rho=m+1` and `rho=1,q=m`; or
4. `q+rho=m+1`, `rho>=2`, and `q=m-rho+1`.

In the first case the residual is a variable-read-once formula with one
private NOT in every implication pair.

## Proof

LEMMA-153 gives

`mu_m=sigma+m-Delta_m=m+1`.

Every minimum circuit attains `mu_m`, so `N+r=m+1`. Restriction, constant
propagation, and pruning do not create NOT gates or increase cycle rank;
therefore

`q+rho<=m+1`.                                               (1)

LEMMA-139 gives `q>=m` for `rho=0,1` and

`q>=m-rho+1`

for `rho>=2`. Hence `q+rho>=m`; equality at `m` is possible only when
`rho=0,q=m`. Otherwise the integer bound (1) forces `q+rho=m+1`, and the
three displayed rank cases give exactly alternatives 2–4. In alternative 1,
the private-pair argument of LEMMA-157 applies with the base absent.

## Boundary

The theorem classifies resource counts after a satisfying-base restriction.
It does not locate the single excess resource in the parent circuit or prove
that any neutral clause restriction removes a NOT or a cycle coordinate.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unrestricted implication circuits, satisfying-base restrictions, NOT counts, and undirected cycle rank |
| Uniform/non-uniform | Every individual non-uniform endpoint minimum circuit; uniform tail function |
| Circuit size | Exact global `N+r=m+1`; exact four-way residual count/rank classification |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2` and Boolean restrictions |
| Asymptotic quantifiers | Every `m>=1`, every nonconstant base with `sigma>=2`, every endpoint satisfying `Delta_m=sigma-1`, and every satisfying base assignment |
| Regime | Exact worst-case one-excess classification; not resource localization, a SAT lower bound, or a terminal result |

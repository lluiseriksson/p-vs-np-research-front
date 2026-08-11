# LEMMA-147 — two rows cannot recognize a globally raw input

**Label: PROVED**

Let `rho_0,rho_1` be two assignments to base variables `X`, and suppose the
base cube contains an assignment different from both. For every collection of
fresh inputs `t_1,...,t_m`, there are `m` pairwise distinct Boolean functions
`g_i(X,t_i)` such that

1. `g_i` is globally different from the raw input `t_i`;
2. `g_i|rho_0=g_i|rho_1=t_i`; and
3. all the `g_i` can be computed from one shared base predicate using one
   additional binary gate per index.

## Proof

Choose a nonzero Boolean predicate `R(X)` with
`R(rho_0)=R(rho_1)=0`. The indicator of any third base assignment is one
explicit choice. Define

`g_i=t_i OR R`.

On either selected row, `R=0`, so the restricted function is exactly `t_i`.
At a base assignment where `R=1`, however, `g_i=1` for both values of `t_i`;
hence `g_i` is not globally the raw input. The functions are pairwise distinct
because `g_i` depends essentially on `t_i` and no `t_j` with `j!=i`. After
one circuit for `R` is available, the displayed family uses exactly `m`
additional OR gates.

The same construction works with `AND` and a predicate equal to one on both
rows. The point is semantic: equality with a raw input on two restrictions
does not certify that the parent gate was a raw-input gate, nor does it force a
row-specific quotient class.

## Scope boundary

This lemma does not assert that the `g_i` occur in a minimum circuit for the
canonical implication function. It proves only that the two selected
cofactors, global non-rawness, and linear-size realizability cannot by
themselves bound the collision count `b`. Any valid bound must use minimum
circuit structure, behavior on additional canonical rows, or a combined
surplus-versus-collision charge.

## Model card

| Field | Value |
|---|---|
| Computational model | Boolean functions represented by unrestricted AND/OR/NOT circuits and two fixed base restrictions |
| Uniform/non-uniform | Fully non-uniform finite construction |
| Circuit size | One shared circuit for `R` plus `m` binary OR gates |
| Circuit depth | Unrestricted; one extra layer after `R` suffices |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors only |
| Asymptotic quantifiers | Every `m>=1`, every two selected rows in a base cube containing a third assignment |
| Regime | Worst-case exact structural witness; not a minimum-circuit counterexample, SAT lower bound, or terminal result |

# LEMMA-155 — maximal deficit forces formula rigidity

**Label: PROVED**

Let `H` be nonconstant, depend essentially on `h` inputs, and have circuit
complexity `K`. For

`J_m=H AND AND_{i=1}^m(t_i OR NOT u_i)`, `sigma=K-h+1`,

suppose the final deficit is maximal:

`Delta_m=sigma`.

Then every minimum pruned circuit `C` for `J_m` has cycle rank zero and
exactly `m` NOT gates. Moreover, for every assignment `x*` satisfying
`H(x*)=1`, fixing `X=x*`, propagating constants, and pruning leaves a formula
for `W_m` with cycle rank zero and exactly the same `m` NOT gates. In
particular, no NOT gate of `C` disappears under any satisfying base
restriction.

## Proof

Write `N` and `r` for the NOT count and output-cone cycle rank of `C`.
LEMMA-153 gives

`mu_m=sigma+m-Delta_m=m`.

For every pruned circuit for `J_m`, its total size is the fixed essential-input
term `h+2m-1` plus `N+r`. Hence every minimum circuit attains `mu_m`, and

`N+r=m`.                                                    (1)

Fix any `x*` with `H(x*)=1`. The restricted function is `W_m`. Let the
constant-propagated, pruned residual circuit have `q` NOT gates and cycle rank
`rho`. Restriction deletes gates and wires; pruning deletes further subgraphs;
and suppressing a gate replaced by a wire is an edge contraction. These
operations do not increase cycle rank and create no NOT gate. Therefore

`q+rho<=N+r=m`.                                             (2)

Apply LEMMA-139 to the residual circuit. If `rho=0`, then `q>=m`. If
`rho=1`, then `q>=m`, so `q+rho>=m+1`. If `rho>=2`, then

`q>=m-rho+1`,

so again `q+rho>=m+1`. Comparison with (2) leaves only

`rho=0` and `q=m`.                                         (3)

Because restriction creates no NOT gates, `q<=N`. Equations (1) and (3)
give `N>=m` and `N+r=m`, whence `N=m` and `r=0`. Also `q=N`, so every original
NOT gate survives the restriction. Since `x*` was arbitrary, the conclusion
holds for every satisfying base assignment.

## Boundary

The theorem is an endpoint rigidity statement. It does not classify where
the `m` NOT gates occur in the formula, associate them canonically with the
`m` implication clauses, or prove that the maximal saving already occurs in a
short prefix. Those are the explicit obligations of GATE-004BB.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unrestricted AND/OR/NOT circuits, satisfying-base restrictions, and undirected output-cone cycle rank |
| Uniform/non-uniform | Every individual non-uniform minimum circuit for the uniform base–implication family |
| Circuit size | Under `Delta_m=sigma`, exact `N=m`, `r=0`; every satisfying-base residual has exact `q=m`, `rho=0` |
| Circuit depth | Unrestricted formula depth after the proved rank-zero conclusion |
| Fan-in | AND/OR two; NOT one; fanout unrestricted before the conclusion and formula fanout in the output cone after it |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle rank over `F_2`; Boolean restrictions and formula inversion lower bounds |
| Asymptotic quantifiers | Every `m>=1`, every nonconstant finite base `H`, every minimum pruned `J_m` circuit with `Delta_m=sigma`, and every satisfying assignment of `H` |
| Regime | Exact worst-case maximal-deficit stratum; not NOT localization, prefix saving, a SAT lower bound, or a terminal result |

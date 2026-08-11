# LEMMA-151 — implication tails admit selector mobility at fixed size

**Label: PROVED**

Let `H(X)` have circuit complexity `K`, and suppose two compatible row
restrictions give distinct nonconstant residuals `H_0,H_1`. On fresh inputs
put

`q_i=t_i OR NOT u_i`,

`J=H AND q_1 AND ... AND q_m`.

There are two circuits of the same size `K+3m` computing `J`:

1. an aggregated-tail circuit with at most `K+1` gates depending on the
   interpolating row selector `a`; and
2. an interleaved circuit with at least `m` selector-dependent gates, at least
   `4m` two-row quotient classes, and collision count `b=0`.

## Aggregated-tail architecture

Use a minimum `K`-gate circuit for `H`. Compute every `q_i` with one NOT and
one OR, combine all clauses with a binary AND tree of `m-1` gates, and use one
final AND with `H`. The size is

`K+2m+(m-1)+1=K+3m`.

Every clause and clause-aggregation gate is independent of the row selector.
At most the `K` base gates and the final AND depend on it, so

`D_a<=K+1`.

## Interleaved architecture

Use the same base and clause circuits, but set

`T_0=H`, `T_j=T_{j-1} AND q_j`

for `1<=j<=m`. This again uses exactly `K+2m+m=K+3m` gates.

Every `T_j` depends essentially on the row selector: after setting all
clauses true, its two selector cofactors reduce to the distinct functions
`H_0,H_1`. Hence `D_a>=m`.

The `m` functions `NOT u_i` and the `m` clause functions `q_i` are pairwise
distinct active row-independent classes. The `2m` functions

`H_e AND q_1 AND ... AND q_j`, `e in {0,1}`, `1<=j<=m`,

are pairwise distinct by the distinct nonconstant residuals and their
essential fresh clause supports. They cannot collide with the clause-local
classes because they retain essential base-residual dependence. Thus the
joint quotient has at least `4m` classes.

No gate cofactor equals raw `t_i`: base gates do not depend on fresh tail
variables, `NOT u_i` and `q_i` are not `t_i`, and every `T_j` retains an
essential base-residual variable on both rows. Therefore `b=0`.

## Consequence

Selector penetration is representation-dependent even at fixed circuit
size. If `C(J)=K+3m`, however, the interleaved circuit is itself minimum and
supplies the high-quotient minimum required by the zero-deficit case of
GATE-004AX.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit unrestricted circuits for a base conjoined with disjoint implication clauses |
| Uniform/non-uniform | Fully non-uniform minimum base circuit; uniform two equal-size tail architectures |
| Circuit size | Both architectures have exactly `K+3m` gates; selector counts at most `K+1` and at least `m` respectively |
| Circuit depth | Unrestricted; aggregate tree or interleaved chain |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean row cofactors and semantic selector dependence only |
| Asymptotic quantifiers | Every `m>=1`, every nonconstant finite `H`, and every pair of distinct nonconstant compatible row residuals |
| Regime | Exact worst-case displayed-circuit theorem; minimum-circuit conclusion only when the displayed upper bound is exact |

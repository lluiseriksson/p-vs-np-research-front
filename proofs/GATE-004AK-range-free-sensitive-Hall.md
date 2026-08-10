# GATE-004AK-RANGE-FREE-SENSITIVE-HALL — sensitivity alone gives Hall expansion

**Label: NO-GO**

The Hall claim is false if the unresolved low-N hypothesis is dropped.
Consider the De Morgan formula

`W_m = NOT OR_i (u_i AND AND_{j=1}^4 NOT v_{i,j})`.

It has `B=5m-1`, cycle rank `t=0`, and `N=4m+1`. Under the witness pair for
index `i`, exactly the input `u_i`, its violation-term path through the OR
tree, and the final NOT change. The four local `NOT v_{i,j}` gates remain one
on both assignments. Therefore every sensitive resource neighborhood is the
same singleton containing only the final NOT:

`A_i(T)={top NOT}`.

For any two distinct indices, the union has size one and violates Hall. This
is an explicit circuit-level counterexample, not only an abstract incidence
pattern.

The counterexample lies outside `N<=m-1`, so it does not refute GATE-004AK.
It proves that local sensitivity and odd-path parity alone cannot establish
the needed expansion; any successful proof must exploit the low negation
budget or another minimum-structure constraint. GATE-004AJ/AI/AH and all
larger gates remain open.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit fan-out-one De Morgan AND/OR/NOT formula and its assignment-sensitive subgraphs |
| Uniform/non-uniform | Uniform explicit circuit family; range-free method audit |
| Circuit size | `B=5m-1`, `N=4m+1`, `t=0`; all `m` neighborhoods equal one singleton |
| Circuit depth | Unrestricted; displayed balanced or unbalanced formula allowed |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean sensitivity incidence; no algebraic circuit model |
| Asymptotic quantifiers | Every `m>=2`; Hall fails on every index subset of size at least two |
| Regime | Explicit no-go outside the low-N target range; the restricted Hall gate remains open |

# LEMMA-121 — one-bit factorizations of `W_m` have only two clause partitions

**Label: PROVED**

Partition the variables of `W_m` into `X` and `Y`, and suppose

`W_m(X,Y)=F(z(X),Y)`

for a nonconstant Boolean bit `z`. Classify a clause as `X`-whole,
`Y`-whole, or cut according to where its variables lie. Exactly one of the
following holds:

1. no clause is cut; or
2. exactly one clause is cut and there is no `X`-whole clause.

In case 1, if `a` clauses are `X`-whole and `b=m-a` are `Y`-whole, then
`z` is `W_a` or its complement, and any formulas for `z` and `F` require at
least `a` and `b` NOT occurrences respectively. In case 2, fixing `z` to an
attained value restricts `F` to `W_{m-1}`, so every formula for `F` needs at
least `m-1` NOT occurrences.

## Cofactor classification

Because `z` is one bit, varying `X` produces at most two distinct residual
functions of `Y`.

For a cut clause, one assignment to its nonempty `X` part forces the clause
to one, while another leaves a nonconstant clause on its nonempty `Y` part.
The choices for disjoint clauses are independent. Two cut clauses would
therefore give four distinct nonzero `Y` residuals. One cut clause together
with an `X`-whole clause gives the zero residual plus two distinct nonzero
residuals. Both contradict the two-residual limit. This proves the dichotomy.

## Formula costs

In case 2, choose the `X` assignment that forces the cut clause to one. The
remaining `m-1` whole `Y` clauses give exactly `W_{m-1}`. Its associated
value of `z` is attained, so fixing that value in a formula for `F` proves the
`m-1` lower bound by LEMMA-119.

In case 1, varying `X` gives exactly the residuals zero and `W_b`. Therefore
`z` must distinguish precisely whether all `a` `X`-whole clauses are true;
it is `W_a` or `NOT W_a`. LEMMA-119 gives the upstream lower bound `a`.
Fixing `z` to the code for satisfied `X` clauses leaves `W_b`, giving the
downstream lower bound `b`. The conventions `W_0=1` and zero required NOTs
cover empty sides.

## Model card

| Field | Value |
|---|---|
| Computational model | One-bit functional factorizations and formula realizations of disjoint fixed-sign clause products |
| Uniform/non-uniform | Every variable partition and every nonconstant intermediary bit |
| Circuit size | Formula NOT lower `a+b=m` in the uncut case; downstream lower `m-1` in the sole-cut case |
| Circuit depth | Unrestricted formula depth |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and disjoint clause incidence only |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=2`, and every partition of the `(p+1)m` variables |
| Regime | Exact worst-case factorization dichotomy; not a general circuit lower bound or terminal result |

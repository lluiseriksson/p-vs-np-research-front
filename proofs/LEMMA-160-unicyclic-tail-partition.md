# LEMMA-160 — exact tail partition in a unicyclic parent

**Label: PROVED**

Let a nonconstant one-bit factorization

`J_j(X,Y)=F(z(X),Y)`

arise from LEMMA-120, so the upstream circuit `A(X)` computing `z` is a
formula with `p` NOT gates and the downstream formula for `F` has `j-p` NOT
occurrences. Classify each implication clause as `X`-whole, `Y`-whole, or cut.

Then exactly one of the following holds:

1. no tail clause is cut; or
2. exactly one tail clause is cut and there is no `X`-whole tail clause.

In case 1, if `a` clauses are `X`-whole and `b=j-a` are `Y`-whole, then

`p=a` and `j-p=b`.

In case 2,

`p<=1` and `j-p>=j-1`.

## Tail-cofactor dichotomy

Split the base variables according to `X,Y`. Choose the `X` part `alpha` of
any satisfying assignment of `H`. The residual base function
`H_alpha(Y_base)` is nonzero because it is one at the chosen `Y` part.

For a cut implication clause, one assignment to its nonempty `X` part forces
the clause to one and another leaves a nonconstant clause on its `Y` part.
The choices for disjoint tail clauses are independent. Two cut clauses would
therefore give four distinct nonzero residual functions of `Y`: fix the base
variables to a satisfying value and satisfy all other tail clauses to
separate the four products. One cut clause plus an `X`-whole clause gives the
zero residual and two distinct nonzero residuals. Both contradict the fact
that the one-bit `z` permits at most two residual functions. This proves the
dichotomy.

## Exact NOT split without a cut

Fix the `X`-base variables to `alpha`. When the `a` `X`-whole clauses are not
all true, the `Y` residual is zero; when they are all true, the residual is
the nonzero function `H_alpha W_b`. Hence the two values of `z` distinguish
exactly `W_a`, and the restricted upstream formula computes `W_a` or its
complement. LEMMA-119 gives `p>=a`.

Set `z` to its attained all-true code, fix the `Y`-base variables to a value
satisfying `H_alpha`, and neutralize no `Y`-whole clause. The downstream
formula restricts to `W_b`, so LEMMA-119 gives `j-p>=b`. Since `a+b=j`, both
inequalities are equalities.

## Sole-cut split

Choose the `X` assignment that forces the cut clause true while retaining a
nonzero base residual, and then fix the `Y`-base variables to a satisfying
value. At the attained `z` code, the downstream formula restricts to the
product of the `j-1` `Y`-whole clauses. LEMMA-119 gives `j-p>=j-1`, hence
`p<=1`.

## Boundary

The theorem counts NOT occurrences in the two formula regions. It does not
prove that those occurrences are syntactically private to tail clauses in the
unrestricted parent or that a neutral restriction deletes the unique cycle.

## Model card

| Field | Value |
|---|---|
| Computational model | One-bit factorizations induced by pruned unicyclic AND/OR/NOT circuits and formula cofactors |
| Uniform/non-uniform | Every individual non-uniform unicyclic factorization of the uniform implication tail |
| Circuit size | Parent exactly `j` NOTs; no-cut split exactly `(a,b)`; sole-cut upstream at most one NOT |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; downstream factor formula may contain two leaves labeled by `z` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors, residual-function counting, and formula inversion complexity |
| Asymptotic quantifiers | Every `j>=2`, every nonconstant satisfiable base, and every unicyclic factorization with `N=j` |
| Regime | Exact worst-case tail-partition and NOT-split theorem; not resource pruning, a SAT lower bound, or a terminal result |

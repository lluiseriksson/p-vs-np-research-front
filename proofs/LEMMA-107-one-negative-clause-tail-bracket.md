# LEMMA-107 — one-negative disjoint clause tails have a one-gate gap

**Label: PROVED**

Let `H(x)` be a nonconstant total Boolean function with exact unrestricted
circuit size `K`. For `1<=i<=m`, let all inputs below be fresh and pairwise
distinct, and put

`Q_i = NOT u_i OR v_{i,1} OR ... OR v_{i,p}`

for fixed `p>=1`. If `F=H AND Q_1 AND ... AND Q_m`, then

`K+(p+1)m <= C(F) <= K+(p+2)m`.

For `p=4`, this is `K+5m<=C(F)<=K+6m`.

## Upper bound and displayed quotient

Compute the positive `p`-literal disjunction with `p-1` OR gates, compute
`NOT u_i`, and join the two parts with one OR. This costs `p+1` gates per
clause. Conjoining the `m` clauses successively above a minimum circuit for
`H` costs another `m` gates, proving the upper bound.

If two designated row restrictions give distinct nonconstant residuals
`H_0,H_1`, the displayed circuit has at least `(p+3)m` active diagonal tail
classes: `(p-1)m` positive-OR prefixes, `m` negations, `m` clause outputs,
and `2m` row-dependent conjunction-tail functions. Essential-input supports
separate clause-local classes, and dependence on the base variables separates
the row tails from them. For `p=4`, the displayed count is `7m`. If this upper
circuit were minimum, its signed loss would be at most `K-m`.

## Lower bound

Restrict `u_i=1` successively. Before each restriction, `u_i` is essential:
choose an input with `H=1`, satisfy every other clause, and set all `p`
positive inputs of the current clause to zero. The current function is not a
raw input, so earliest-dependent-gate elimination removes at least one gate
per restriction.

After all `m` restrictions the residual is `H` conjoined with `m` disjoint
fresh positive width-`p` clauses. LEMMA-048 gives its exact size `K+pm`.
Restoring the `m` eliminated gates proves `C(F)>=K+(p+1)m`.

The certificates differ by exactly `m` gates. No minimum-circuit quotient
survival is inferred from the displayed representation.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits, disjoint one-negative width-`p+1` clauses, restrictions, and exact semantic diagonal quotients |
| Uniform/non-uniform | Fully non-uniform base and minimizing circuit; uniform clause family and restriction sequence |
| Circuit size | `K+(p+1)m<=C(F)<=K+(p+2)m`; displayed quotient at least `(p+3)m`, conditional loss at most `K-m` |
| Circuit depth | Base unrestricted; displayed OR and conjunction chains unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits only |
| Asymptotic quantifiers | Every finite nonconstant `H`, every `m,p>=1`, every qualifying disjoint fresh input family, and every pair of distinct nonconstant designated base residuals for quotient counting |
| Regime | Exact worst-case circuit-size bracket and displayed-representation theorem; not a circuit lower bound or terminal result |

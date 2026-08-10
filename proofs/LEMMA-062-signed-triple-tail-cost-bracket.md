# LEMMA-062 — disjoint signed-triple tails have a one-gate-per-clause gap

**Label: PROVED**

## Statement

Let `H(x)` be a nonconstant total Boolean function with exact unrestricted
circuit size `K`. For `1<=i<=m`, let the triples of fresh inputs be pairwise
disjoint and let each `Q_i` be one of

`NOT a_i OR b_i OR NOT c_i`

or

`NOT a_i OR NOT b_i OR c_i`.

Put `F=H AND Q_1 AND ... AND Q_m`. Then

`K+3m <= C(F) <= K+4m`.

For any two restrictions giving distinct nonconstant base residuals, the
factorized `K+4m` circuit from LEMMA-064 has at least `5m` active semantic
joint-quotient classes in its signed tail. If that circuit were proved
minimum, its loss would be at most `K-m`. The proved lower bound is short of
this minimality certificate by exactly `m` gates.

## Upper bound

Write each clause as

`Q_i=p_i OR NOT(u_i AND v_i)`.

It uses one AND, one NOT, and one OR gate. Conjoin the `m` clauses above `H`
with `m` further AND gates, for total cost `K+4m`. LEMMA-064 records the
factorization and its quotient count. The older literalwise construction
costs `K+5m` and is nonminimum for every `m>=1`.

## Lower bound

In each clause, successively set the two variables occurring negatively to
one. Before each restriction the variable is essential: choose a base input
with `H=1`, satisfy every other clause, and set the current clause's remaining
positive literal to zero. The earliest-dependent-gate argument deletes at
least one gate for each of the `2m` restrictions.

After all restrictions the residual is `H` conjoined with the one positive
fresh literal from each clause. LEMMA-037 gives exact size `K+m`. Therefore
the original circuit has size at least `K+2m+m=K+3m`.

## Displayed quotient count

Implement a clause as `p_i OR NOT(u_i AND v_i)`. Its AND, NOT, and OR
functions are distinct within the clause. Across clauses their disjoint
essential-input supports distinguish them, giving `3m` row-independent active
classes.

Under base row `e`, the `j`th conjunction-tail gate computes

`H_e AND Q_1 AND ... AND Q_j`.

The resulting `2m` functions are distinct across rows and prefix lengths:
all clauses can be set true to preserve `H_0!=H_1`, and the successive
essential clause supports distinguish different `j`. They depend on base
variables and cannot collide with a clause-internal function. The displayed
tail therefore supplies at least `5m` classes.

## Exact unresolved gap

Restriction proves only `K+3m`, while the factorized construction costs
`K+4m`, leaving exactly `m` gates between the certificates. Global
minimization may remove those gates and merge displayed semantic classes.
Neither exact size nor representation-independent quotient survival is
asserted.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits, pairwise-disjoint fresh signed width-three clauses, restrictions, and exact semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform base and minimizing circuit; uniform displayed extension and restriction sequence |
| Circuit size | `K+3m<=C(F)<=K+4m`; factorized displayed quotient at least `5m`; conditional displayed loss at most `K-m` |
| Circuit depth | Base unrestricted; displayed clause and conjunction chains unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits only |
| Asymptotic quantifiers | Every finite nonconstant `H`, every `m>=1`, every disjoint fresh triple family of the two stated sign types, and every pair of distinct nonconstant designated base residuals for quotient counting |
| Regime | Worst-case exact total-function bounds; the negative-loss conclusion and GATE-004X falsification are explicitly unproved |

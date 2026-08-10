# LEMMA-057 — disjoint implication tails have a one-gate-per-clause cost gap

**Label: PROVED**

## Statement

Let `H(x)` be a nonconstant total Boolean function with exact unrestricted
circuit size `K`. For pairwise distinct fresh inputs `a_i,b_i`, `1<=i<=m`,
put

`Q_i=a_i OR NOT b_i`,

`F=H AND Q_1 AND ... AND Q_m`.

Then

`K+2m <= C(F) <= K+3m`.

The displayed `K+3m` circuit has, under any two restrictions yielding
distinct nonconstant base residuals, at least `4m` active semantic joint-
quotient classes in its signed tail. If that displayed circuit were proved
minimum, its loss would be at most `K-m`. The present lower bound misses that
minimality certificate by exactly `m` gates.

## Upper bound

Use one NOT and one OR gate for each `Q_i`, then conjoin the `m` clauses above
a minimum circuit for `H` with `m` AND gates. This costs `K+3m`.

## Lower bound

In any circuit for `F`, successively set `b_i=1`. Before its restriction,
`b_i` is essential: choose an input with `H=1`, set every other clause true,
and set `a_i=0`. The earliest-`b_i`-dependent-gate argument removes at least
one gate. After all `m` restrictions the residual is

`H AND a_1 AND ... AND a_m`,

which has exact size `K+m` by LEMMA-037. Therefore the original circuit had
at least `K+2m` gates.

## Displayed quotient count

The `m` functions `NOT b_i` are distinct row-independent active classes. The
`m` clause functions `Q_i` are also distinct and cannot collide with them.
Under row `e`, the `j`th conjunction-tail gate computes

`H_e AND Q_1 AND ... AND Q_j`.

These `2m` functions are distinct across `e,j` by the distinct nonconstant
base residuals and their essential clause supports, and they cannot collide
with the row-independent clause gates. Hence the displayed circuit supplies
at least `4m` classes.

## Exact unresolved gap

The restriction proof certifies only `K+2m`, while the circuit carrying the
`4m` quotient classes has size `K+3m`. Removing up to `m` gates during global
minimization may also destroy or merge the displayed tail classes. Neither
the exact identity `C(F)=K+3m` nor a representation-independent `4m` quotient
lower bound is asserted.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits, disjoint fresh implication clauses, restrictions, and exact semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform base and minimum circuit; uniform displayed extension and restriction sequence |
| Circuit size | `K+2m <= C(F) <= K+3m`; displayed circuit quotient at least `4m`; conditional displayed loss at most `K-m` |
| Circuit depth | Base unrestricted; displayed clause and conjunction chains unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits only |
| Asymptotic quantifiers | Every finite nonconstant `H`, every `m>=1`, every disjoint fresh pair family, and every pair of distinct nonconstant designated row residuals for the quotient count |
| Regime | Worst-case exact total-function bounds; the negative-loss conclusion is explicitly unproved |

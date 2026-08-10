# LEMMA-063 — global De Morgan sharing compresses the signed-triple tail

**Label: PROVED**

## Statement

Let `Q_1,...,Q_m` be pairwise variable-disjoint three-clauses, each with
exactly one positive and two negative literals, and put `W=AND_i Q_i`. Then

`C(W)<=4m`.

For every nonconstant base `H` of exact unrestricted circuit size `K` on
disjoint inputs,

`C(H AND W)<=K+4m+1`.

Hence the clausewise circuit of cost `K+5m` from the first LEMMA-062 attempt
is not minimum whenever `m>=2`.

LEMMA-064 subsequently gives the sharper bounds `C(W)<=4m-1` and
`C(H AND W)<=K+4m` by factoring each clause locally. The global De Morgan
construction remains a proved alternative implementation and an
implementation-instability witness; it is not the best recorded upper bound.

Under two distinct nonconstant base residuals, the compressed displayed
circuit supplies at least `4m+2` active semantic joint-quotient classes in
its signed tail and final output. Its displayed loss is therefore at most
`K-1`, which does not grow negatively with `m`.

## Compression proof

Write the variables of clause `i` so that

`Q_i=NOT u_i OR p_i OR NOT v_i`.

Its unique falsifying condition is

`V_i=u_i AND NOT p_i AND v_i`.

Compute each `V_i` with one NOT and two binary AND gates, using `3m` gates.
An OR tree or chain for all violation terms uses `m-1` gates, and one final
NOT computes

`W=NOT(V_1 OR ... OR V_m)`.

The total is `3m+(m-1)+1=4m`. One additional AND above a minimum circuit for
`H` proves the base-extension bound. For `m>=2`,
`K+4m+1<K+5m`.

## Compressed quotient count

The `m` literal negations and `2m` within-term AND functions are distinct by
their essential-input supports. The `m-1` OR-prefix functions and final NOT
are also distinct and active, giving `4m` row-independent tail classes.
The final AND with `H_e` gives two more classes across distinct nonconstant
rows. They cannot collide with tail-only functions because they depend on
base inputs. Thus the displayed joint quotient contains at least `4m+2`
tail/output classes.

The circuit has size `K+4m+1`; subtracting these classes gives `K-1`. This is
only a calculation for the displayed circuit, not a minimum-circuit quotient
theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted Boolean circuits, disjoint signed three-clauses, global De Morgan sharing, and exact semantic joint quotients |
| Uniform/non-uniform | Uniform tail construction; fully non-uniform base circuit and later minimization |
| Circuit size | `C(W)<=4m`; `C(H AND W)<=K+4m+1`; clausewise `K+5m` circuit nonminimum for `m>=2`; compressed displayed quotient at least `4m+2` |
| Circuit depth | Unrestricted; displayed OR aggregation may be a chain or tree |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits only |
| Asymptotic quantifiers | Every `m>=1`, every pairwise-disjoint family of the stated sign type, every nonconstant disjoint base, and every pair of distinct nonconstant base residuals for quotient counting |
| Regime | Worst-case exact upper bound and representation audit; not an exact circuit lower bound, SAT lower bound, or terminal result |

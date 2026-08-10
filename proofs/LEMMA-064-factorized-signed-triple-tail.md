# LEMMA-064 — local factorization gives a four-gate signed-triple extension

**Label: PROVED**

## Statement

Under the hypotheses and notation of LEMMA-062,

`C(F)<=K+4m`.

The corresponding standalone conjunction `W=AND_i Q_i` has
`C(W)<=4m-1`. Under any two restrictions giving distinct nonconstant base
residuals, the displayed base-extension circuit has at least `5m` active
semantic joint-quotient classes in its signed tail. If the displayed circuit
is minimum, its signed loss is at most `K-m`.

Together with LEMMA-062,

`K+3m<=C(F)<=K+4m`.

## Factorization

Every permitted clause has one positive literal `p_i` and two negative
literals on variables `u_i,v_i`. Exactly,

`Q_i=p_i OR NOT(u_i AND v_i)`.

Use one AND, one NOT, and one OR per clause. This costs `3m`. Conjoining the
clauses uses `m-1` gates in the standalone predicate, giving `4m-1`.
Conjoining them successively above a size-`K` circuit for `H` uses `m` gates,
giving `K+4m`.

## Displayed quotient count

For every clause, the functions `u_i AND v_i`, its complement, and `Q_i`
are active, distinct, and distinguished across clauses by their disjoint
essential supports. They give `3m` row-independent classes.

Under base row `e`, conjunction-tail gate `j` computes

`H_e AND Q_1 AND ... AND Q_j`.

The `2m` row-tail functions are distinct across rows and prefix lengths and
cannot collide with clause-local functions. Hence the displayed circuit has
at least `5m` tail classes. Its size minus this count is `K-m`.

## Boundary

The `K+3m` restriction lower bound does not prove the displayed circuit
minimum. Up to `m` gates and the associated semantic classes can disappear
under global minimization. GATE-004Z records exactly this remaining issue.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits, disjoint signed width-three clauses, local Boolean factorization, and exact semantic joint quotients |
| Uniform/non-uniform | Uniform factorized tail; fully non-uniform base and minimizing circuit |
| Circuit size | Standalone upper `4m-1`; base-extension upper `K+4m`; combined bracket `K+3m<=C(F)<=K+4m`; displayed quotient at least `5m` |
| Circuit depth | Unrestricted; displayed conjunction tail may have linear depth |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits only |
| Asymptotic quantifiers | Every finite nonconstant base, every `m>=1`, every disjoint fresh family of the two stated sign types, and every pair of distinct nonconstant base residuals for quotient counting |
| Regime | Worst-case exact upper bound and displayed-quotient theorem; minimum-circuit loss, SAT lower bounds, and the terminal statement remain open |

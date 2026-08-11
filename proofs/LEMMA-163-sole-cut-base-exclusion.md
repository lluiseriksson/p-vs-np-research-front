# LEMMA-163 — the sole-cut upstream side contains no base variable

**Label: PROVED**

In LEMMA-160's sole-cut one-bit factorization of

`J_j=H AND W_j`,

no essential base variable lies in the upstream variable set `X`.
Consequently the upstream formula depends only on the `X` half of the unique
cut implication clause. Neutralizing that clause makes the duplicated bit
`z` constant and destroys the unique cycle.

## Residual-count proof

Suppose an essential base variable lies in `X`. Fix all other `X`-base
variables so that its two values give distinct residual base functions of the
`Y`-base variables; call them `A` and `B`. Such a fixing exists by
essentiality, and at least one of `A,B` is nonzero.

Let `c` be the nonconstant residual literal contributed by the `Y` half of
the cut implication clause. The `X` half has one value that forces the clause
true and another that leaves `c`. Varying independently the essential base
bit and this cut-clause half produces the four `Y` residuals

`A`, `B`, `A AND c`, `B AND c`,

all multiplied by the common product of the `j-1` `Y`-whole clauses.

At least three of the displayed functions are distinct:

- if one of `A,B` is zero and the other, say `B`, is nonzero, then
  `0`, `B`, and `B AND c` are distinct because `c` is a fresh variable;
- if both are nonzero and distinct, then `A`, `A AND c`, and `B` are
  distinct. In particular `B` cannot equal `A AND c`, because `B` is
  independent of the fresh variable of `c` while `A AND c` depends on it.

Fixing the other whole clauses true preserves these distinctions. But a
factorization through one bit `z(X)` permits at most two residual functions of
`Y`, a contradiction. Hence no essential base variable is upstream.

LEMMA-160 already excludes upstream whole tail clauses in the sole-cut case.
The only upstream tail input is therefore the `X` half of the cut clause.
After the full neutral restriction of that clause, every upstream input is
constant, so `z` is constant. Both downstream occurrences of `z` propagate
to constants and the unique undirected cycle disappears.

## Model card

| Field | Value |
|---|---|
| Computational model | One-bit factorizations of unicyclic base–implication circuits and Boolean residual functions |
| Uniform/non-uniform | Every individual non-uniform sole-cut factorization; uniform disjoint tail |
| Circuit size | No direct gate bound; consequence removes the unique cycle under the cut-clause neutral restriction |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted with one cycle in the parent |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and residual-function cardinality only |
| Asymptotic quantifiers | Every `j>=2`, every essential nonconstant base, and every sole-cut LEMMA-160 factorization |
| Regime | Exact worst-case base-exclusion theorem; not a higher-rank circuit theorem, SAT lower bound, or terminal result |

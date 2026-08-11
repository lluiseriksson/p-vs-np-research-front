# LEMMA-165 — general one-bit tail dichotomy for `J_j`

**Label: PROVED**

For any nonconstant one-bit factorization

`J_j(X,Y)=F(z(X),Y)`,

where `z` is computed by a formula whose inputs have no bypass to the output,
the implication-tail partition has either:

1. no cut clause; or
2. exactly one cut clause and no `X`-whole clause.

In the sole-cut case, no essential base input belongs to `X`.

## Proof

The zero/one-cut dichotomy is the residual-function argument of LEMMA-160 and
uses no downstream topology: fix the `X` part of a satisfying base assignment.
Two cut clauses give four distinct nonzero `Y` residuals; one cut plus one
`X`-whole clause gives zero plus two distinct nonzero residuals. A one-bit
interface permits at most two.

The sole-cut base exclusion is LEMMA-163. Its proof likewise uses only the
factorization: an essential upstream base bit and the upstream half of the cut
clause give at least three residuals `A,B,A AND c,B AND c`.

## Model card

| Field | Value |
|---|---|
| Computational model | Arbitrary one-bit functional factorizations of a base conjoined with disjoint implication clauses |
| Uniform/non-uniform | Every individual non-uniform factorization; uniform tail family |
| Circuit size | No gate bound; exact zero/one-cut structural classification |
| Circuit depth | Unrestricted formulas for the interface bit and unrestricted downstream computation |
| Fan-in | Interface formula uses AND/OR two and NOT one; downstream fan-in unrestricted only as inherited from the Boolean circuit basis |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and residual-function cardinality only |
| Asymptotic quantifiers | Every `j>=2`, every essential nonconstant base, and every nonconstant one-bit no-bypass factorization |
| Regime | Exact worst-case interface theorem; not resource pruning, a SAT lower bound, or terminal result |

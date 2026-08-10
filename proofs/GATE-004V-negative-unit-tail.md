# GATE-004V-NEGATIVE-UNIT-TAIL — complement sharing restores a fresh signed tail

**Label: NO-GO**

## Falsifiable route attempted

Attempt: exploit the polarity sharing isolated by LEMMA-054. Choose an
eligible base with `C(NOT H)=C(H)-1`, conjoin more than `K` common fresh
negative unit literals, and invoke LEMMA-055's exact size and quotient count
to force negative diagonal loss.

## Failure

LEMMA-052 says that the balanced outer product is coordinate-dense. For every
raw outer coordinate `z_i`, some product member has `z_i=0` and another has
`z_i=1`. Consequently neither `z_i` nor `NOT z_i` is common to the product.
There is not even one common negative unit literal, so the exact
complement-exposed tail cannot be attached while preserving agreement on all
GATE-004V witnesses.

## Scope and next attack

This closes only unit signed literals. Width-at-least-two mixed signed clauses
can be common despite coordinate density, and their exact minimum cost may
interact with both base polarity and overlap. Those are the next predicate
classes; GATE-004V remains `EXPLORATORY`.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact balanced slot-product witnesses and globally minimum unrestricted circuits with a complement-exposed base and fresh negative-unit conjunction tail |
| Uniform/non-uniform | Uniform witness product; fully non-uniform eligible base and attempted coordinate selection |
| Circuit size | LEMMA-055 would give exact `K+m` and loss at most `K-m-2`, but coordinate density forces the common-tail count `m=0` |
| Circuit depth | Unrestricted; the candidate exact tail may use a linear OR chain and final NOT |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits and finite coordinate incidence only |
| Asymptotic quantifiers | Every `rho>=7,s>=1`, every outer coordinate, and every complement-exposed nonconstant base; the common negative-unit count is exactly zero |
| Regime | Worst-case exact method no-go for unit signed predicates; mixed signed clauses, GATE-004V, and P versus NP remain open |

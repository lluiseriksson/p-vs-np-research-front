# GATE-004BU — align one clause with one common cycle coordinate

**Label: EXPLORATORY**

Assume GATE-004BT at residual rank at least two. Use LEMMA-174 to identify both
primary cofactors with the same residual cycle space `V`.

## Falsifiable theorem

There is a tail clause `i` and a nonzero `v in V` such that neutralizing `i`
kills `v` in both primary codes, unless some parent NOT already becomes the
same constant in both codes.

Either alternative proves GATE-004BT. GATE-004BT-CYCLE-SPACE-ONLY shows that
the dimension and separate existence of loss pairs do not suffice. The proof
must use the actual common directed paths, Boolean gate functions, or exact
minimum-circuit exchange to align the clause labels.

## Model card

| Field | Value |
|---|---|
| Computational model | One common minimum two-excess circuit and its two equal-rank primary cofactors |
| Uniform/non-uniform | Every individual non-uniform remaining parent; uniform symmetric tail |
| Circuit size | Exact parent `N+r=j+2`; one common cycle or NOT loss gives target `N+r<=j+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; primary source fanout two |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | One identified residual cycle space over `F_2` plus Boolean restriction semantics |
| Asymptotic quantifiers | Every operational GATE-004BT parent with residual cycle rank at least two |
| Regime | Exact worst-case sufficient subgate for GATE-004BT; not a SAT lower bound or terminal result |

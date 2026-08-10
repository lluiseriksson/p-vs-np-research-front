# LEMMA-058 — standalone implication conjunction: exact at one and two pairs

**Label: PROVED**

## Statement

For pairwise distinct raw inputs `a_i,b_i`, define

`W_m=AND_{i=1}^m (a_i OR NOT b_i)`.

In unrestricted fan-in-two AND/OR, fan-in-one NOT circuits,

`2m-1+ceil(log_2(m+1)) <= C(W_m) <= 3m-1`.

Consequently

`C(W_1)=2` and `C(W_2)=5`.

For `m>=3`, these two generic measures leave the explicit gap

`m-ceil(log_2(m+1))`.

## Upper bound

Each implication uses one NOT and one OR gate. Conjoining the `m` clause
outputs uses `m-1` AND gates, for total `3m-1`.

## Binary-gate lower bound

Every one of the `2m` inputs is essential. For `a_i`, set `b_i=1`, satisfy
all other clauses, and toggle `a_i`. For `b_i`, set `a_i=0`, satisfy all other
clauses, and toggle `b_i`.

In the output cone of a fan-in-two circuit depending on `2m` raw inputs, at
least `2m-1` binary gates are needed: each binary gate can merge at most two
previously disconnected input components, while NOT gates merge none.

## NOT-gate lower bound

Start at the all-zero assignment, where `W_m=1`. For `i=1,...,m`, first raise
`b_i` from zero to one, making `W_m=0`, and then raise `a_i` from zero to one,
restoring `W_m=1`. This is an increasing input chain with exactly `m`
`1`-to-`0` decreases.

Markov's inversion-complexity theorem therefore requires at least

`ceil(log_2(m+1))`

NOT gates. Adding the binary- and unary-gate lower bounds gives the stated
total lower bound.

For `m=1`, it equals the upper bound `2`; for `m=2`, it equals the upper bound
`5`. QED.

## GATE-004W consequence

The standalone clause predicate has the displayed exact size for the first
two nontrivial cases. For growing `m`, essential-input connectivity plus
inversion complexity alone does not certify `3m-1`, and it says still less
about additive composition with an arbitrary base or quotient survival.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits and Markov inversion complexity |
| Uniform/non-uniform | Fully non-uniform finite circuit size; uniform implication family |
| Circuit size | Between `2m-1+ceil(log_2(m+1))` and `3m-1`; exact 2 at `m=1` and 5 at `m=2` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean lattice chains only; no algebraic circuit model |
| Asymptotic quantifiers | Every integer `m>=1`; exact specializations at `m=1,2` |
| Regime | Worst-case exact total-function bounds; not an additive base theorem or SAT lower bound |

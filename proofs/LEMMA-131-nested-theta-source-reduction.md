# LEMMA-131 — fixing the first nested theta source leaves at most one cycle

**Label: PROVED**

Consider a nested-split theta circuit computing either polarity of `W_m`.
Let its unique core source have attached formula `A(X)` with output bit `z`
and `h` NOT gates, and let the whole circuit have `q` NOT gates. Then:

- if the `X` partition cuts no clause, `q>=m`;
- if it cuts one clause, `q-h>=m-1`, hence `q>=m-1`.

## Residual topology

The binary core source has degree two and lies internally on one of the three
theta paths. Deleting that source and its two incident core edges breaks one
independent cycle. After fixing an attained value of `z`, constant propagation
and pruning therefore leave a circuit of cycle rank at most one, containing
at most the `q-h` NOT gates outside `A`.

Every input in `X` reaches the output only through `z`, so the bipolar
one-bit dichotomy LEMMA-121 applies.

## Cofactor costs

If no clause is cut, let `a+b=m` be the whole clauses in `X` and outside it.
The source formula needs `h>=a`. Fixing `z` to the code for satisfied
`X`-clauses leaves the selected polarity of `W_b` in the residual circuit.
LEMMA-119 applies if its cycle rank is zero and LEMMA-123 if it is one, giving
`q-h>=b`. Thus `q>=m`.

If one clause is cut, there is no `X`-whole clause. The attained source value
that forces the cut clause to true leaves the selected polarity of `W_{m-1}`.
The residual formula/unicyclic lower bound gives `q-h>=m-1`.

## Model card

| Field | Value |
|---|---|
| Computational model | Nested-source theta circuits, one-bit source restrictions, and residual cycle rank at most one |
| Uniform/non-uniform | Every individual non-uniform nested theta circuit for either polarity of `W_m` |
| Circuit size | NOT lower `m` in the uncut source partition and `m-1` downstream in the cut case |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Theta cycle rank, Boolean cofactors, and formula/unicyclic inversion |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=2`, and every nested theta orientation |
| Regime | Exact source-restriction theorem; not a general bicyclic or terminal lower bound |

# LEMMA-175 — one surviving NOT mixes arbitrarily many tail blocks

**Label: PROVED**

For every `m>=1`, let

`U_m=u_1 OR ... OR u_m`

and define

`g_m=NOT(v OR (x AND U_m))`,

where `v` is a further free tail variable. Then

`g_m|_{x=0}=NOT v`

and

`g_m|_{x=1}=NOT(v OR U_m)`.

The same physical NOT remains nonconstant in both primary codes, while its
second cofactor depends essentially on every one of the `m` variables
`u_i`. Nevertheless only the final AND, OR, and NOT gates depend on `x`; the
entire `U_m` tree is selector-independent.

## Proof

Direct substitution gives the two cofactors. Setting all variables except
`u_i` to zero shows essential dependence on every `u_i` at `x=1`. The OR tree
for `U_m` is independent of `x`, and only the three displayed gates above it
have selector-dependent functions.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit non-uniform AND/OR/NOT formula gadget under a primary selector cofactor |
| Uniform/non-uniform | Uniform gadget family in `m`; no minimum-parent realization claim |
| Circuit size | One NOT, one selector AND, one final OR, and an `m-1` gate selector-independent OR tree |
| Circuit depth | Unrestricted OR-tree depth plus three |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and essential dependence only |
| Asymptotic quantifiers | Every `m>=1` |
| Regime | Exact semantic compression witness; not an exact-parent counterexample, SAT lower bound, or terminal result |

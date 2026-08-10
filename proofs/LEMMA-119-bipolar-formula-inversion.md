# LEMMA-119 — both polarities of the fixed-sign product need one formula NOT per block

**Label: PROVED**

For every `m>=1` and fixed `p>=1`, both `W_m` and `NOT W_m` have formula
inversion complexity exactly `m` over binary AND/OR and unary NOT.

## Decreases of `W_m`

LEMMA-109 already proves `d(W_m)=m`, so Morizumi's formula theorem gives
`I_F(W_m)=m`.

## Decreases of the complement

Along an increasing chain of input assignments, one clause

`NOT u_i OR v_{i,1} OR ... OR v_{i,p}`

can change from zero to one at most once: that change occurs only when its
first positive variable is raised after `u_i` has made the clause false.
Every `0->1` transition of the conjunction `W_m` requires at least one clause
to make its unique `0->1` transition. Hence `W_m` has at most `m` increases,
so `NOT W_m` has at most `m` decreases.

The bound is attained. Start with all variables zero. For each block `i` in
turn, first raise `u_i`, making `W_m` fall from one to zero, and then raise
`v_{i,1}`, making it rise from zero to one. This increasing chain has `m`
increases of `W_m`, hence `m` decreases of its complement. Therefore
`d(NOT W_m)=m`, and Morizumi gives `I_F(NOT W_m)=m`.

## Model card

| Field | Value |
|---|---|
| Computational model | Fan-out-one AND/OR/NOT formulas for both output polarities of the fixed-sign clause product |
| Uniform/non-uniform | Uniform function family; exact non-uniform formula inversion count |
| Circuit size | Exactly `m` NOT occurrences for either polarity; binary size unrestricted |
| Circuit depth | Unrestricted formula depth |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean-lattice increasing chains only |
| Asymptotic quantifiers | Every fixed `p>=1` and every `m>=1` |
| Regime | Exact worst-case formula inversion theorem; not an unrestricted circuit-size or terminal result |

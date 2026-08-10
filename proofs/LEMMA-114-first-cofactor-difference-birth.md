# LEMMA-114 — first cofactor-difference dependence is born at a binary gate

**Label: PROVED**

Fix a clause index `i`. For every node `g` of a circuit computing `W_m`, let
`g_empty` and `g_i` be the Boolean functions of the unassigned `u` variables
obtained under `alpha_empty` and `alpha_{ {i} }`, and define

`Delta_i(g) = g_empty XOR g_i`.

There exists an internal node `b_i` for which `Delta_i(b_i)` depends
essentially on `u_i`, while no earlier node in a topological order has that
property. Every such first node is a binary AND or OR gate; it cannot be a
NOT gate.

## Proof

The two restrictions differ only on the primary input `v_{i,1}`. At that
input the two constants are one and zero, so its difference is constant one.
At every other positive input the difference is zero, and at every `u` input
the two restricted functions are identical, so the difference is again zero.
No primary-input difference depends on `u_i`.

At the output, LEMMA-112 gives

`R_empty=1` and `R_{ {i} }=NOT u_i`.

Their XOR is `u_i`, which depends essentially on `u_i`. A first internal node
with this property therefore exists in every topological ordering.

If that node were a NOT gate with predecessor `a`, then

`Delta_i(NOT a) = (NOT a_empty) XOR (NOT a_i)
                = a_empty XOR a_i
                = Delta_i(a)`.

The predecessor would already have the property, contradicting firstness.
The basis contains only binary AND/OR gates besides NOT, so every first node
is binary.

The conclusion is deliberately only a localization theorem. A single binary
gate may in principle be first for several indices; no distinct-gate charge
is asserted.

## Model card

| Field | Value |
|---|---|
| Computational model | Node cofactor profiles in unrestricted AND/OR/NOT circuits for the fixed-sign clause product |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform pair of canonical restrictions per clause index |
| Circuit size | No size lower bound; existence and gate type of a first dependence-birth node |
| Circuit depth | Unrestricted finite DAG; firstness is relative to any topological order |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean functions with XOR used only to compare two cofactors |
| Asymptotic quantifiers | Every fixed `p>=1`, every `m>=1`, every clause index `i`, and every circuit computing `W_m` |
| Regime | Exact worst-case structural localization; not an additive charge, SAT lower bound, or terminal result |

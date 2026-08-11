# LEMMA-148 — an exposed common collision mask factors with linear saving

**Label: PROVED**

Let `B` be a nonempty set of `b` indices, let `R` be any Boolean function
independent of the fresh pairs `(t_i,u_i)`, and define

`M_B=AND_{i in B} ((t_i OR R) OR NOT u_i)`.

Then

`M_B = R OR AND_{i in B}(t_i OR NOT u_i)`.

If `R` is already available, the displayed clause-local circuit on the left
uses `4b-1` gates, whereas the factored circuit on the right uses `3b` gates.
Thus the factorization saves exactly `b-1` gates.

## Proof

Associativity gives

`(t_i OR R) OR NOT u_i = R OR (t_i OR NOT u_i)`.

Distributivity of one common disjunct over a conjunction gives the functional
identity. In the unfactored module, each index uses one NOT for `u_i`, one OR
for `t_i OR R`, and one OR to form its clause; a binary AND tree uses `b-1`
more gates. The total is `3b+(b-1)=4b-1`.

In the factored module, each index uses one NOT and one OR to form
`t_i OR NOT u_i`, their AND tree uses `b-1` gates, and one final OR introduces
`R`. The total is `2b+(b-1)+1=3b`. The difference is `b-1`.

Consequently, a minimum circuit cannot contain the unfactored module for
`b>=2` as an exposed subgraph whose internal outputs have no uses outside the
module and whose single module output is the only connection to the rest of
the circuit: replacing it preserves the computed function and reduces size.

## Scope boundary

The theorem is a local exchange, not a normal-form theorem. A gate whose two
selected cofactors equal `t_i` need not globally equal `t_i OR R(X)`, masks
need not be common, and the relevant gates may have nonlocal fanout. None of
those missing facts follows from cofactor equality.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted Boolean circuits with an exposed clause-local submodule |
| Uniform/non-uniform | Fully non-uniform finite identity and circuit rewrite |
| Circuit size | Exact rewrite from `4b-1` to `3b` gates with `R` already available; saving `b-1` |
| Circuit depth | Unrestricted; binary AND trees may have arbitrary shape |
| Fan-in | AND/OR two; NOT one; fanout unrestricted outside the stated exposed-module premise |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean distributivity only |
| Asymptotic quantifiers | Every `b>=1`, every Boolean mask `R`, and every fresh disjoint implication-input family |
| Regime | Exact local worst-case exchange; not a normal form, quotient lower bound, SAT lower bound, or terminal result |

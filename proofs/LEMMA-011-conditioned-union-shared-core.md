# LEMMA-011 — distinct conditioned branches need not have additive complexity

**Label: PROVED**

## Statement

Let `G(z)` be any nonzero Boolean function on at least one input and define

`H_0(t,z)=G(z) AND NOT(t)`,

`H_1(t,z)=G(z) AND t`,

and

`F(s,t,z)=G(z) AND (s XNOR t)`.

Then the two `s`-cofactors of `F` are `H_0,H_1`; they are distinct and
disjoint; and `H_0 OR H_1=G`. Nevertheless:

1. `S(F)<=S(G)+6`;
2. the pair `(H_0,H_1)` has a shared two-output circuit of size at most
   `S(G)+3`; and
3. if `S_2` denotes minimum shared two-output size, then
   `S(F)-S_2(H_0,H_1)<=7`.

Thus conditioned branches being distinct, disjoint, and jointly exhaustive do
not generically imply a superconstant direct-sum surplus or substantial joint
restriction loss.

## Model card

| Field | Value |
|---|---|
| Computational model | Unrestricted acyclic single- and two-output Boolean circuits; coordinate cofactors |
| Uniform/non-uniform | Fully non-uniform circuit complexity |
| Circuit size | Parent overhead at most six; parent-to-minimum-pair gap at most seven |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; XNOR is expanded into the Boolean basis |
| Asymptotic quantifiers | Every positive-arity nonzero Boolean function `G` |
| Regime | Worst-case exact total Boolean functions; no promise or distribution |

## Proof

Compute `s XOR t` with four gates, negate it, and AND with `G`, proving
`S(F)<=S(G)+6`. Fixing `s=0` or `s=1` gives the displayed conditioned
branches. They cannot both be one on the same `(t,z)`, and their OR is `G`.
They are distinct because `G` is nonzero and the value of `t` selects which is
one.

A shared circuit for the pair computes `G`, `NOT(t)`, and the two final AND
gates, so it has size at most `S(G)+3`. Conversely, ORing the two outputs of
any shared pair circuit computes `G` with one extra gate. Therefore

`S_2(H_0,H_1)>=S(G)-1`.

Combining this with the upper bound on `S(F)` gives
`S(F)-S_2(H_0,H_1)<=7`. QED.

## Scope

ENC-007 gives the analogous union identity for the two conditioned SAT
residuals. LEMMA-011 proves that this output-level identity, even strengthened
by distinctness and disjointness, cannot by itself establish the joint
compression required by GATE-004G. SAT-specific internal sharing must be
controlled separately.

# LEMMA-056 — balanced slots retain linearly many common implications

**Label: PROVED**

## Statement

For every `rho>=7`, the length-`4rho` balanced slot option set contains at
least `2rho-4` pairwise coordinate-disjoint mixed clauses of the form

`z_i OR NOT z_j`

that are one on every option. Consequently the `s`-slot product contains at
least

`m=(2rho-4)s`

pairwise variable-disjoint common mixed clauses.

Moreover:

1. no negative-negative two-clause is common to the product; and
2. every common mixed two-clause has both coordinates in one slot.

## Within-slot construction

Partition a slot into its `rho` aligned four-bit chunks. In chunk `k`, use
the two disjoint candidates

`z_{4k+3} OR NOT z_{4k}`

and

`z_{4k+2} OR NOT z_{4k+1}`.

Every ENC-020 short option is assembled from all-one chunks and aligned
chunks of its four neutral blocks. The complete four-bit alphabet is

`1111, 0110, 1001, 0011, 0001, 0010`.

Direct inspection shows that every word in this six-word alphabet satisfies
both displayed clauses: none has `(bit 3,bit 0)=(0,1)` or
`(bit 2,bit 1)=(0,1)`.

The long option `A_rho` begins with `0110` and has exactly six one bits.
Thus its first chunk satisfies both candidates. Every candidate it falsifies
requires a one in a distinct coordinate of one of the remaining disjoint
pairs. Only four one bits remain outside the first chunk, so at most four of
the `2rho` candidates are invalidated. At least `2rho-4` candidates are common
to every short option and to `A_rho`. Their coordinate pairs are disjoint.

Copying the construction independently into all `s` slots proves the product
count.

## Remaining binary-clause classification

The all-one option occurs in every slot. Hence the all-one product member
falsifies every clause with two negative literals, proving item 1.

For item 2, take a mixed clause whose two coordinates lie in distinct slots.
Coordinate density supplies an option in the first slot falsifying its first
literal and an option in the second slot falsifying its second literal.
Product independence combines those options, falsifying the clause. Thus any
common mixed two-clause is confined to one slot. QED.

## Scale in GATE-004V

Here `P=4rho s`, so

`m=P/2-4s`.

With `s=floor((R-1)/8)` and the GATE-004V parameters, `P=Theta(n)` and
`s=Theta(R)`. The common implication packing is therefore `Theta(n)` for the
small fixed context exponent, unlike the positive-clause packing bound
`6s=Theta(R)`. This is a circuit-method threat, not a proved counterexample:
an exact minimum-circuit and quotient theorem for the implication tail is
still required.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact balanced Boolean slot products and raw-coordinate signed width-two clauses |
| Uniform/non-uniform | Uniform explicit clause construction and witness product; no circuit chosen |
| Circuit size | No lower bound; at least `(2rho-4)s=P/2-4s` disjoint common implications |
| Circuit depth | Irrelevant to the combinatorial theorem; later circuits unrestricted |
| Fan-in | Each clause is a fan-in-two OR with one negated literal; ambient NOT fan-in one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence only |
| Asymptotic quantifiers | Every `rho>=7`, every `s>=1`, every pair of distinct slots for the cross-slot exclusion, and the explicit GATE-004V asymptotic parameter choice |
| Regime | Worst-case exact witness-family theorem; not a circuit lower bound or a GATE-004V counterexample |

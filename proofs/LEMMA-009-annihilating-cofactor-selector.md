# LEMMA-009 — an adjacent annihilating cofactor need not remove the hard core

**Label: PROVED**

## Statement

Let `G(z)` be any nonzero Boolean function on at least one input and define

`F(s,z)=s AND G(z)`.

Then `s` is essential, `F(1,z)=G(z)`, `F(0,z)=0`, and

`S(F)-S(G) <= 1`

for unrestricted fan-in-two AND/OR, fan-in-one NOT circuits. Consequently, the
existence of a constant-zero cofactor adjacent to a hard residual does not
generically force any substantial gate loss when the hard cofactor is selected.

## Model card

| Field | Value |
|---|---|
| Computational model | General acyclic Boolean circuits and one-bit coordinate restrictions |
| Uniform/non-uniform | Fully non-uniform circuit complexity |
| Circuit size | Exact minimum gate count; hard-cofactor size gap at most one |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every positive-arity nonzero Boolean function `G` |
| Regime | Worst-case exact total Boolean functions; no promise or distribution |

## Proof

Append one AND gate to a minimum circuit for `G`, giving
`S(F)<=S(G)+1`. Since `G` is nonzero, choose `z` with `G(z)=1`; changing `s`
then changes `F`, so `s` is essential. The two displayed cofactors follow
immediately.

Restrict any minimum circuit for `F` by `s=1` and normalize it. The resulting
circuit computes `G` and therefore has at least `S(G)` gates. It can have lost
at most `S(F)-S(G)<=1` gate even though the other cofactor is constant zero.
QED.

## Scope

ENC-005 gives a two-bit SAT-gamma analogue of the hard/zero cofactor pair.
LEMMA-009 does not model SAT itself; it proves that proximity to an
annihilating parser state and selector essentiality alone cannot establish
GATE-004F.

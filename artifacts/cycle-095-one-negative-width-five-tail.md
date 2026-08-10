# Cycle 095 one-negative width-five tail

## Fixed-sign packing

**Label: PROVED**

LEMMA-108 strengthens the LEMMA-076 obstruction: every distant quintuple has
an absent assignment with exactly four zeros, hence a common clause with four
positive literals and one negative literal. The packing has
`s*floor(N/5)=Theta(P)` disjoint clauses in the three-block slot product.

## Exact cost bracket

**Label: PROVED**

LEMMA-107 proves `K+5m<=C(F)<=K+6m` for a nonconstant base conjoined with the
disjoint fixed-sign tail. The displayed upper circuit has `7m` diagonal tail
classes, conditionally giving loss at most `K-m` if it is minimum.

## Gate and failed method

**Label: NO-GO**

GATE-004AG isolates exact minimality or representation-independent quotient
survival as the falsifiable next gate. Essential-variable restrictions reach
only `K+5m`, missing the required certificate by exactly `m`; the
restriction-only route is therefore closed. GATE-004AG and GATE-004AE remain
`EXPLORATORY`, and no unrestricted circuit or terminal progress is claimed.

# Cycle 105 unicyclic-quintet exclusion audit

## Structural proof

**Label: PROVED**

LEMMA-119 proves formula inversion complexity `m` for both polarities of
`W_m`. LEMMA-120 turns every unicyclic circuit into an upstream one-bit
formula and a downstream formula. LEMMA-121 classifies every one-bit variable
partition of the disjoint clause product.

Together with LEMMA-118, these facts exclude a unicyclic three-NOT circuit for
`W_5`: a cut clause forces four downstream NOTs, while an uncut partition
forces five total formula NOTs. GATE-004AM is therefore `PROVED`.

## Hall consequence

**Label: PROVED**

LEMMA-122 closes dependency-cone Hall inequalities for all subset sizes one
through five. Size six is the next open local gate.

## Independent-review boundary

**Label: EXPLORATORY**

An attempted Fable High adversarial consultation returned an organization
403 before model execution and supplied no mathematical evidence. The proof
was instead decomposed into independently auditable local lemmas and checked
by the repository audit. No formal proof-assistant certification, SAT lower
bound, or terminal claim is made.

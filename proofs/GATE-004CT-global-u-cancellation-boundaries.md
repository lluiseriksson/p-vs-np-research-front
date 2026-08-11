# GATE-004CT — classify globally `u`-cancelling boundaries

**Label: EXPLORATORY**

Assume the unresolved `Q=0` endpoint. By LEMMA-199, every direct boundary
`b!=n` cancels `u` globally despite receiving the `u`-sensitive signal `h`.

## Falsifiable theorem

Every such boundary belongs to one of two exhaustive classes and yields the
corresponding outcome:

1. its other input is globally `u`-insensitive; the two rowwise mask
   identities factor through a common base/`t` realization and give a
   same-size strict extremal descent or private certificate;
2. its other input is `u`-sensitive; the two incoming sensitivity routes
   counter-cancel and their first reconvergence creates a named cycle whose
   satisfying pruning requires a third deletion or removes a non-bridge edge.

The proof must preserve all four cofactors and account for essential base
outputs such as `y AND NOT x` in GATE-004CS-SEMANTIC-PRIVATE-ONLY. Semantic
independence of the boundary output is not itself a cost certificate.

LEMMA-200 now gives the exact rowwise identities for both aligned masks and
counterflows. A nonminimal local counterflow realizes them on both rows, so
reconvergence existence alone is `NO-GO`. GATE-004CU is the active minimum-
cost counterflow branch; the all-aligned two-row mask branch remains separate.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted plateau at `W=1`, size-three carrier, and zero handoff potential |
| Uniform/non-uniform | Every finite non-uniform operational `Q=0` tuple |
| Circuit size | Parent `K+2`; same-size descent, third deletion, private certificate, or forbidden cycle loss |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; every physical boundary input and fanout audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean identities and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical minimum size-three parent with `Q=0` |
| Regime | Exact worst-case zero-handoff boundary gate; not a SAT lower bound or terminal result |

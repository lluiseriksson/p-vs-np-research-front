# GATE-004BV — expose one uniformly neutral tail resource

**Label: EXPLORATORY**

Assume the common minimum parent of GATE-004BU.

## Falsifiable theorem

Some tail clause `i` admits, without increasing circuit size or `N+r`, a
minimum representation in which either:

1. a NOT-containing subgraph depending on clause `i` becomes the same
   constant under its neutral restriction for both primary codes; or
2. an exposed common cycle path containing the clause interface is deleted in
   both codes.

Either exposed form proves GATE-004BT/BU. GATE-004BU-SIGNATURE-COUNT-ONLY
shows that the form cannot be inferred by counting mixed signatures or
selector-dependent gates. It must follow from a size-preserving normal-form
exchange, exact minimality, or the disjoint implication semantics.

LEMMA-153 shows that size preservation already fixes `N+r`. An unnamed
exchange supplies no proof of exposure, as recorded by
GATE-004BV-UNSPECIFIED-EXCHANGE-ONLY. LEMMA-176 and GATE-004BW replace that
schema with the independently defined selector-minimal representation.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted two-excess implication circuits under size-preserving Boolean and graph exchanges |
| Uniform/non-uniform | Existential minimum representation for every non-uniform GATE-004BU parent; uniform tail |
| Circuit size | Exchange preserves minimum size and `N+r`; exposed neutralization loses at least one resource |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean gate identities and common cycle space over `F_2` |
| Asymptotic quantifiers | Every operational GATE-004BU instance |
| Regime | Exact worst-case sufficient normal-form subgate; not a SAT lower bound or terminal result |

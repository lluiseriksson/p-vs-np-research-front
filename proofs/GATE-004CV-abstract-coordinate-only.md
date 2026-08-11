# GATE-004CV-ABSTRACT-COORDINATE-ONLY — coordinate alignment is automatic

**Label: NO-GO**

GATE-004CV cannot distinguish counterflow by comparing only the abstract
cycle-space images of `gamma_b`. LEMMA-202 proves that every satisfying-minor
map `rho_s` is an isomorphism. The transition isomorphism
`rho_t o rho_s^{-1}` aligns the images of every parent coordinate
automatically.

Nor do exact two-gate loss and survival force a resource conflict. The
two-subdivision witness in LEMMA-202 has the same rank before and after two
vertices are contracted, preserves the marked cycle, and deletes no
non-bridge edge. This is a graph witness, not a Boolean plateau circuit.

Therefore an argument must retain data discarded by the abstract cycle
space: which parent edges are contracted, which gates disappear, and the
four-code Boolean signature transported along each arm. Abstract coordinate
identity, dimension, or edge count alone cannot yield factoring.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact-plateau cycle-space quotients plus a finite subdivision witness |
| Uniform/non-uniform | Every finite non-uniform plateau tuple for the isomorphism statement; one graph family for the witness |
| Circuit size | Parent `K+2`; witness has exactly two added subdivision vertices |
| Circuit depth | Unrestricted |
| Fan-in | Circuit application AND/OR two and NOT one; graph witness fan-in independent |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Cycle spaces and transition isomorphisms over `F_2` |
| Asymptotic quantifiers | Every parent coordinate and every ordered pair of satisfying codes |
| Regime | Abstract-coordinate-only no-go; not a minimum Boolean counterexample, SAT lower bound, or terminal result |

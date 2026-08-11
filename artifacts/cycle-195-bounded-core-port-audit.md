# Cycle 195 — bounded-core port audit

**Label: PROVED**

LEMMA-233 constructs a fixed three-gate marked cyclic core with `m` external
ports for every `m`. Selector slices make each port parent-live and show that
neither incoming signal is a free replacement.

Therefore GATE-004DV-BOUNDED-CORE-ENUMERATION-ONLY is `NO-GO` (NG-171): core
size four/six does not make external attachments finite. GATE-004DW asks for a
complete semantic/physical port quotient or a distinct minimum-cost payment
per inequivalent port type.

## Classification

- LEMMA-233: `PROVED`
- GATE-004DV-BOUNDED-CORE-ENUMERATION-ONLY: `NO-GO`
- GATE-004DW: `EXPLORATORY`

`verification/bounded_core_unbounded_ports_audit.py` checks core rank, gate
counts, all assignments through `m=6`, and the two input-substitution
witnesses. The uniform statement has the displayed construction. Fable was
not invoked; independent certification and terminal implications are not
claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Uniform constant-free AND/OR single-output family with fixed marked cyclic core and external ports |
| Uniform/non-uniform | Every finite diagnostic `m>=1`; exhaustive checks through `m=6` |
| Circuit size | `3m+4`; marked core size three and port count `m` |
| Circuit depth | Unrestricted output-tree depth |
| Fan-in | AND/OR two; NOT unused; core gate fanout `m+1` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean functions, selectors, and cycle rank over `F_2` |
| Asymptotic quantifiers | Every `m>=1`, assignment, port, and displayed substitution |
| Regime | Exact unbounded-port theorem and core-only no-go; not a SAT lower bound or terminal result |

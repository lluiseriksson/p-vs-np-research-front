# Cycle 199 — antichain reconvergence audit

**Label: PROVED**

LEMMA-241 extracts from any `k`-vertex reachability antichain with a common
sink a rooted unary/binary tree having exactly `k-1` binary reconvergence
vertices. Unlike LEMMA-215, the statement uses physical reachability rather
than essential independent source functions.

LEMMA-242 shows that the count is tight but not yet a payment: all `k-1`
merges can be parent-live and resist both input-wire substitutions. Counting
the reconvergences as free hosts is therefore NG-175. GATE-004EA retains the
complete physical tree and asks for independent seals, injective loss/origin
charges, uncrossing, descent, or a surviving four-code contradiction.

## Classification

- LEMMA-241: `PROVED`
- LEMMA-242: `PROVED`
- GATE-004DZ-RECONVERGENCE-COUNT-AS-PAYMENT: `NO-GO`
- GATE-004DZ: `EXPLORATORY`
- GATE-004EA: `EXPLORATORY`

`verification/antichain_reconvergence_audit.py` checks the tight comb family
through `k=7`. The general tree count and parent-rigidity claims use the direct
proofs. Fable was not invoked; independent certification, minimum endpoint
realizability, and terminal implications are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Fan-in-two physical DAG antichain trees and constant-free AND/OR parent-live diagnostics |
| Uniform/non-uniform | Every finite common-sink DAG for LEMMA-241; every finite diagnostic `k>=2` for LEMMA-242 |
| Circuit size | Exactly `k-1` extracted/tight binary reconvergences; no host count inferred |
| Circuit depth | Unrestricted; diagnostic comb depth `k` |
| Fan-in | At most two; circuit AND/OR two and NOT unused in the diagnostic; fanout unrestricted in the theorem |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed reachability trees and exact Boolean functions; endpoint cycle spaces over `F_2` remain open |
| Asymptotic quantifiers | Every finite common-sink antichain; every `k>=2`, merge, and separating assignment in the diagnostic |
| Regime | Exact graph theorem and scoped physical no-go; not endpoint proof, SAT lower bound, or terminal result |

# Cycle 190 — one-sided mask/payment audit

**Label: PROVED**

LEMMA-225 proves that a one-sided support mask is an independent full-function
seal at an OR or AND cut gate. It closes the semantic branch without assuming
parent-output equality.

LEMMA-226 separates that certificate from physical accounting. A uniform
family has `m` actual retargeted hosts, `m` parent-live sealed cut
gates, and one shared mask. Hence GATE-004DQ-MASK-AS-EXTRA-HOST is `NO-GO`
(NG-166): the hosts count once; masks and seals do not become extra payments.
GATE-004DR asks for path-complete mask cuts on the real hosts or a physical
contradiction from a two-sided cancellation.

## Classification

- LEMMA-225: `PROVED`
- LEMMA-226: `PROVED`
- GATE-004DQ-MASK-AS-EXTRA-HOST: `NO-GO`
- GATE-004DR: `EXPLORATORY`

`verification/one_sided_mask_payment_audit.py` checks 262,144 one-base-bit
function triples and the uniform family for `m=1,...,5`. The general seal and
selector-slice liveness statements have human proofs. Fable was not invoked;
independent certification and terminal implications are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Paired unrestricted AND/OR/NOT cut interfaces plus a uniform shared-mask single-output family |
| Uniform/non-uniform | Every one-base-bit truth-table triple; every finite diagnostic `m>=1` |
| Circuit size | One cut gate; diagnostic old size `4m+2` with exactly `m` real hosts |
| Circuit depth | Unrestricted ambient depth; diagnostic final OR-tree depth arbitrary |
| Fan-in | AND/OR two; NOT one; diagnostic mask fanout `m` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors, selectors, and physical host deduplication |
| Asymptotic quantifiers | All 262,144 table triples; every `m>=1`, assignment, and seal index |
| Regime | Exact semantic seal plus payment-separation no-go; not a SAT lower bound or terminal result |

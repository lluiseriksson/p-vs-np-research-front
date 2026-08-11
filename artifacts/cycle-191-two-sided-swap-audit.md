# Cycle 191 — two-sided swap audit

**Label: PROVED**

LEMMA-227 exactly partitions a zero-defect binary gate into exclusive
one-sided masks and an overlap region where both changed inputs swap
`01<->10`. This is a complete pointwise classification.

GATE-004DR-TWO-SIDED-SWAP-ONLY is `NO-GO` (NG-167). A constant-free crossbar
is identity on `00,01,11`, swaps `(x,y)` on `10`, and preserves both
`x OR y` and `x AND y`. Function-preserving double-NOT and reconvergent
identity padding changes its physical ledger without changing this table, so
the table determines no named, deduplicable resource. GATE-004DS therefore
retains physical path provenance and exact minimum cost.

## Classification

- LEMMA-227: `PROVED`
- GATE-004DR-TWO-SIDED-SWAP-ONLY: `NO-GO`
- GATE-004DS: `EXPLORATORY`

`verification/two_sided_swap_audit.py` checks every local bit state for both
AND and OR and all 16 crossbar assignments. The general support partition has
the displayed human proof. Fable was not invoked; independent certification
and terminal implications are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Local paired binary interfaces plus one unrestricted constant-free AND/OR/NOT crossbar DAG |
| Uniform/non-uniform | Every local Boolean state; one finite non-uniform diagnostic circuit |
| Circuit size | One local gate; crossbar OR-output size ten versus one gate |
| Circuit depth | One local layer; crossbar depth at most six |
| Fan-in | AND/OR two; NOT one; shared crossbar control fanout |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean functions and analytical defects over `F_2` |
| Asymptotic quantifiers | Every local state and every crossbar assignment |
| Regime | Exact local classification and swap-only no-go; not a SAT lower bound or terminal result |

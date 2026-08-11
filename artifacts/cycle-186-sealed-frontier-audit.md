# Cycle 186 — sealed-frontier audit

**Label: PROVED**

LEMMA-220 formalizes the exact multi-consumer interface: a rewrite preserves
the parent once its complete forward changed region reaches an exterior
frontier whose functions are unchanged. Immediate consumers may change.

GATE-004DM-FIXED-RADIUS-CONSUMER-AUDIT-ONLY shows that sealing depth is
unbounded in general. GATE-004DN must derive a complete sealed region from
minimum endpoint structure or turn nonsealing into an exact contradiction.

## Classification

- LEMMA-220: `PROVED`
- GATE-004DM-FIXED-RADIUS-CONSUMER-AUDIT-ONLY: `NO-GO`
- GATE-004DN: `EXPLORATORY`

`verification/sealed_frontier_depth_audit.py` checks `m=1,...,8`. The general
topological induction is a human proof. Fable was not invoked; independent
certification and terminal implications are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Paired unrestricted AND/OR/NOT DAGs plus one uniform sealing-depth family |
| Uniform/non-uniform | Every supplied finite sealed interface; every diagnostic `m>=1` |
| Circuit size | Interface size unrestricted; diagnostic `m+4` |
| Circuit depth | Unrestricted; diagnostic linear in `m` |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean functions and DAG topological induction |
| Asymptotic quantifiers | Every finite interface; every `m>=1` and assignment |
| Regime | Exact interface theorem plus fixed-radius no-go; not a SAT lower bound or terminal result |

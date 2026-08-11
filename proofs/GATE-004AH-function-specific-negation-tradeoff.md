# GATE-004AH — function-specific binary/NOT tradeoff

**Label: PROVED**

## Falsifiable theorem

For the four-positive/one-negative product `W_m`, every pruned unrestricted
circuit with `B` binary gates and `N` NOT gates satisfies

`B+N>=6m-1`.

In particular, throughout the formerly unresolved range
`ceil(log_2(m+1))<=N<=m-1`, one has `B>=6m-1-N`.

## Proof

Put `t=B-5m+1`, the exact output-cone cycle rank. LEMMA-139 gives `N>=m`
when `t=0` and `N>=m-t+1` when `t>=1`. Therefore

`B+N = 5m-1+t+N >= 6m-1`.

LEMMA-140 matches this lower bound with the displayed circuit and proves
`C(W_m)=6m-1`. LEMMA-141 also supplies the witness form `N+t>=m` by full
dependency-cone Hall matching.

This closes only the standalone prerequisite to GATE-004AG. It does not prove
additivity over the canonical base or minimum-circuit quotient survival.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits for the fixed four-positive/one-negative read-once clause product; exact binary/NOT counts |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform function family |
| Circuit size | Proved `B+N>=6m-1`; exact standalone size `C(W_m)=6m-1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected output-cone cycle rank over `F_2` and Boolean cofactors |
| Asymptotic quantifiers | Every `m>=1` and every pruned circuit for `W_m` |
| Regime | Exact worst-case standalone-size theorem; not a base direct sum, SAT lower bound, or terminal result |

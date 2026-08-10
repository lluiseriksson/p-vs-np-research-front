# GATE-004Y-CLAUSEWISE-MINIMALITY — the six-class clausewise tail is minimum

**Label: NO-GO**

## Rejected route

Prove the clausewise `K+5m` construction in LEMMA-062 minimum, then use its
`6m` paired-row tail classes to obtain loss `K-m`.

## Failure

LEMMA-064 computes the same total function with at most `K+4m` gates by
factoring each clause as `p OR NOT(u AND v)`. For every `m>=1`,

`K+4m<K+5m`.

Therefore the clausewise circuit is not minimum throughout the asymptotic
regime and its six-classes-per-clause quotient cannot be promoted through a
minimality claim.

The surviving GATE-004Y asks whether a different minimum circuit has the
required representation-independent quotient surplus. The compressed
displayed circuit gives only `4m+2` tail/output classes and loss `K-1`, so it
does not supply that theorem or refute it.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted Boolean circuits, disjoint signed three-clause tails, global De Morgan sharing, and exact semantic joint quotients |
| Uniform/non-uniform | Uniform clause and compression family; fully non-uniform base and minimizing circuits |
| Circuit size | Clausewise cost `K+5m`; factorized upper bound `K+4m`; strict separation for every `m>=1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean circuits only |
| Asymptotic quantifiers | Every nonconstant disjoint base and every `m>=1` for the stated signed-clause family |
| Regime | Structural no-go for clausewise minimality only; representation-independent GATE-004Y, GATE-004X, and P versus NP remain open |

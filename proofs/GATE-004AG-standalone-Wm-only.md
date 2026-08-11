# GATE-004AG-STANDALONE-WM-ONLY — promote standalone exactness to base additivity

**Label: NO-GO**

LEMMA-140 proves the exact unrestricted size of the isolated tail function
`W_m`. It does not imply that for the canonical base `H`,

`C(H AND W_m)=C(H)+C(W_m)+1`,

because a minimum circuit for the conjunction may share gates across the base
and tail variables or compute a representation unrelated to either separate
minimum circuit. Restricting the base to a satisfying assignment recovers
only the standalone lower bound and does not charge the gates needed on other
base assignments. Likewise, standalone size contains no semantic-quotient
statement ensuring that tail classes survive minimization.

Therefore using LEMMA-140 as alternative 1 or 2 of GATE-004AG would assume the
missing direct sum or quotient theorem. This no-go does not refute GATE-004AG;
it isolates the next gate as base-tail additivity or quotient survival.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for an external base conjoined with the disjoint fixed-sign tail `W_m` |
| Uniform/non-uniform | Canonical uniform base/tail construction; fully non-uniform minimizing circuits |
| Circuit size | Standalone exact `C(W_m)=(p+2)m-1`; no proved additive lower for `C(H AND W_m)` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean circuits and semantic quotients; no algebraic circuit model |
| Asymptotic quantifiers | Every canonical base/tail instance in GATE-004AG and every minimum circuit for its conjunction |
| Regime | Structural no-go for standalone-to-direct-sum promotion; GATE-004AG remains open |

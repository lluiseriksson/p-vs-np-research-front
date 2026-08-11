# GATE-004BW-SELECTOR-MINIMALITY-ONLY — extremality forces a neutral loss

**Label: NO-GO**

## Attempt

Use only minimum total size and minimum selector-sensitivity count `S(C)` to
deduce that one of many tail-block neutralizations deletes a NOT or lowers
cycle rank.

## Failure

LEMMA-177 gives, for every `m`, an exact minimum circuit whose selector-
sensitivity count is also minimum, while all `m` singleton neutralizations
preserve `N+r=1`. The extremal invariant therefore supplies no loss without
additional semantic information about the tail blocks.

The witness blocks are single positive variables, not canonical implication
pairs. Hence this closes selector-minimality-only reasoning and does not
refute GATE-004BW. Any successful proof must use the implication truth table,
in which three pair assignments satisfy the clause and one falsifies it.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact minimum unrestricted AND/OR/NOT formula family under singleton tail restrictions |
| Uniform/non-uniform | Uniform explicit witnesses; selector lower bound covers all non-uniform representations |
| Circuit size | Exact `m+2`, exact selector minimum three, and unchanged `N+r=1` under every declared restriction |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted in the lower bound |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `m>=1` and all `m` singleton neutralizations |
| Regime | Structural no-go for selector-minimality alone; not a counterexample to the implication-tail gate, SAT lower bound, or terminal result |

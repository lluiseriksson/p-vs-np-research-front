# GATE-004L — labelwise survival imbalance

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n0` such that for
every `n>=n0` and every minimum circuit `C_n` for `SAT-gamma_n`, use the
GATE-004K prefix block and identifier set `J_n`. Let `P_n` be the number of
prefix-dependent parent labels. For each `j`, let `z_j` count dependent labels
whose two copies contribute no active residual function under
`R_{j,0},R_{j,1}`, and let `t_j` count labels whose copies contribute two
distinct active residual functions. Then

`sum_{j in J_n}(z_j-t_j) >= |J_n|(B P_n^eta+1)`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted SAT-gamma circuits; prefix-dependent parent labels; exact active residual functions under every conditioned pair |
| Uniform/non-uniform | Fully non-uniform circuit adversary; representative-free labelwise classification |
| Circuit size | Average disappeared-label count exceeds split-label count by a positive power of the dependent region, plus the final OR gate |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed `0<c<1` and `B,eta>0`; every sufficiently large `n`; every minimum circuit; all identifiers in the selected block |
| Regime | Worst-case exact total-language computation; malformed suffixes reject |

## Bridge

LEMMA-024 gives for every `j`

`P_n-|T_j|=z_j-t_j+kappa_j>=z_j-t_j`.

Thus GATE-004L implies GATE-004K with the same constants. All subsequent
bridges already recorded in the vertical map then apply.

## First attack boundary

A proof must charge every label that splits under a conditioned pair to a
different label that disappears, while leaving a polynomial reserve on
average. Raw sensitivity points in the opposite direction because it can
create two active residuals. Cross-label collisions are deliberately omitted
from the target; if a proof needs them, it must account for `kappa_j`
explicitly rather than treating them as automatic.

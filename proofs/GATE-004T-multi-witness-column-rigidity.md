# GATE-004T — multi-witness column rigidity

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n_0` such that for
every `n>=n_0`, put `L=floor(c log_2 n)`, `R=2^(L-2)`, and use the full
ENC-016 expanded prefix cube. Let `G:{0,1}^n->{0,1}` be any total Boolean
function and `C` any minimum unrestricted circuit for `G`. Assume:

1. the expanded output residuals have exactly the ENC-017 equality classes
   and multiplicities;
2. the diagonal pairs OR to one common suffix function and include the exact
   complete-assignment columns; and
3. for every ternary specification choosing, independently for each diagonal
   variable, allowed values `{0}`, `{1}`, or `{0,1}`, some suffix string makes
   the `2R` diagonal outputs indicate exactly which polarities are allowed.

If `q_s` is the exact semantic joint quotient size under diagonal context
`s`, then

`sum_s (|C|-q_s) >= R(B R^eta+1)`.

The theorem is falsified by any ambient minimum-circuit family satisfying all
three output-level premises with smaller loss.

## SAT bridge

ENC-017 proves premise 1 for exact SAT residuals. ENC-013 gives the common
diagonal union, ENC-009 gives the complete-assignment columns, and ENC-018
gives all `3^R` compact ternary columns when `c` is chosen small enough that
the `O(RL)` witness formulas and padding fit in the suffix. Thus GATE-004T
would imply GATE-004Q and then GATE-004 through LEMMA-014.

## Attack boundary

LEMMA-042 rules out any proof using only the static expanded-row equality
table. The first attack must use the simultaneous both-polarities value in a
ternary column. It will test whether a three-state suffix encoding can extend
the LEMMA-041 fresh-tail counterexample. If it can, the next gate must retain
SAT's explicit formula-composition maps rather than output columns alone.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits, exact expanded-row output incidence, compact multi-witness diagonal columns, and exact semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform circuit adversary; uniform explicit prefix family and ternary witness specification |
| Circuit size | Average diagonal parent-to-joint-quotient loss at least `B R^eta+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine prefix geometry over `F_2`; output-column closure is Boolean |
| Asymptotic quantifiers | Exists fixed sufficiently small `c>0` and `B,eta>0`; every sufficiently large `n`; every eligible `G`; every minimum circuit; all contexts and ternary specifications |
| Regime | Worst-case exact total-function computation; semantic column property, not a promise or distribution |


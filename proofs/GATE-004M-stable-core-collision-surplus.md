# GATE-004M — stable-core collision surplus

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n_0` such that for
every `n>=n_0` and every minimum circuit `C_n` for `SAT-gamma_n`, use the
conditioned prefix block and identifier set `J_n` from GATE-004K. For each
`j`, define `z_j,t_j,kappa_j` as in LEMMA-024 and let

`lambda_j=|A_j intersect T_j|`

be the number of active residual functions shared by a prefix-independent
parent label and a prefix-dependent parent label in the joint quotient for
`R_{j,0},R_{j,1}`. If `P_n` is the number of prefix-dependent parent labels,
then

`sum_{j in J_n}(z_j-t_j+kappa_j+lambda_j)`

`>= |J_n|(B P_n^eta+1)`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted SAT-gamma circuits; exact paired semantic quotients; dependent labels and the surviving prefix-independent core |
| Uniform/non-uniform | Fully non-uniform circuit adversary; uniform explicit conditioned-prefix family |
| Circuit size | Average collision-aware surplus at least `B P_n^eta+1`; sufficient for the logarithmic-step superlinear recurrence |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed `0<c<1` and `B,eta>0`; every sufficiently large `n`; every minimum circuit; average over all identifiers in the selected block |
| Regime | Worst-case exact total-language computation; malformed strings reject |

## Bridge

LEMMA-029 gives, for every `j`,

`S_n-q_j=alpha_j+z_j-t_j+kappa_j+lambda_j`

with `alpha_j>=0`. Therefore GATE-004M supplies the same average quotient loss
required upstream by GATE-004I. LEMMA-014 converts the `O(log n)` length step
into a fixed superlinear SAT circuit lower bound, GATE-004.

GATE-004M is strictly less conservative than GATE-004K and GATE-004L: it does
not throw away collisions between dependent traces and the stable suffix core.
Those older gates remain valid sufficient routes but are no longer the
smallest active brick.

## First attack and falsification boundary

The first candidate mechanism is that the mandatory split output from
LEMMA-027 might collide with a prefix-independent core function after each
conditioning. LEMMA-030 refutes this as an output-semantics-only implication:
distinct active cofactors can be realized by a circuit in which every gate is
prefix-dependent, making `lambda=0`. A surviving proof must quantitatively use
minimum SAT circuit structure across the full identifier block, not merely the
existence of the conditioned output pair.

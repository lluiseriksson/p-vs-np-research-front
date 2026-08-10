# GATE-004O — context-trace elimination across the parallel edge family

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n_0` such that for
every `n>=n_0` and every minimum circuit `C_n` for `SAT-gamma_n`, set
`L=floor(c log_2 n)` and use the ENC-014 row family. Fix polarity `b=1`, and
let `U_n` be the number of parent binary-gate labels in the context-dependent
trace top region certified by LEMMA-034. For each context `s`, let `q_s` be the
full semantic joint quotient size under the adjacent pair
`Q_{j(s),0},Q_{j(s),1}`. Then

`sum_s (|C_n|-q_s) >= 2^(L-2)(B U_n^eta+1)`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted SAT-gamma circuits, affine context traces, and exact joint quotients under a parallel family of adjacent complete prefix restrictions |
| Uniform/non-uniform | Fully non-uniform circuit adversary; uniform explicit context embedding and restriction family |
| Circuit size | Average parent-to-joint-quotient loss at least `B U_n^eta+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine parametrization over `F_2`; Boolean circuit computation |
| Asymptotic quantifiers | Exists fixed `0<c<1` and `B,eta>0`; every sufficiently large `n`; every minimum circuit; all `2^(L-2)` contexts |
| Regime | Worst-case exact total-language computation; malformed strings reject; no promise or distribution |

## Bridge

LEMMA-034 gives `U_n>=2^(L-2)=Omega(n^c)`. The displayed inequality therefore
provides a fixed positive-power average quotient loss over the exact
conditioned-SAT pairs. ENC-013 supplies the OR reconstruction of SAT on the
suffix, whose length drops by only `6L+13=O(log n)`. LEMMA-014 yields GATE-004.

## First attack boundary

LEMMA-033 blocks charging the common edge direction: all edge influence can
sit in a four-gate XOR shell around an arbitrary context function. The missing
theorem must instead show that completely fixing the affine context `s`
eliminates, merges, or makes input-equivalent a positive power of the actual
`U_n` trace region on average, after all split residuals are counted.

LEMMA-035 further blocks using only the size of that region and parent
minimality. Its globally minimum `m`-gate context chain has every gate
context-dependent, yet the two-context joint quotient has `2m-3` classes and
signed loss `3-m`. A proof must use the full SAT shattering relation across all
`2^(L-2)` contexts, not merely contextual dependence of individual gates.

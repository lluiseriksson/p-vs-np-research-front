# GATE-004G — joint quotient of conditioned SAT residuals

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `B>0`, `delta>0`, and `n0` such that for every
`n>=n0` and every minimum circuit `C_n` for `SAT-gamma_n`, form two restricted
copies under the equal-length ENC-007 prefixes `R_0,R_1`. Merge constants,
free inputs, and semantically identical residual gates both within and across
the copies, delete gates reaching neither output, and normalize constants as in
the multi-output form of LEMMA-005. The resulting joint two-output quotient
`J_n` must satisfy

`|J_n| <= |C_n|-B n^delta-1`.

Its two outputs are exactly `CSAT_0` and `CSAT_1` on suffix length `n-14`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted SAT-gamma circuits; two equal-length coordinate restrictions; shared two-output semantic quotient |
| Uniform/non-uniform | Fully non-uniform circuit adversary and existential semantic merging |
| Circuit size | Joint quotient plus one OR loses at least `B n^delta` relative to the parent minimum circuit |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | No verifier advice; all circuit choices are non-uniform by length |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed `B,delta`; every sufficiently large `n`; every minimum length-`n` circuit |
| Regime | Worst-case exact total-language computation; malformed suffixes reject |

## Bridge to GATE-004

ENC-007 proves that ORing the two outputs of `J_n` computes
`SAT-gamma_{n-14}`. Adding one OR gate gives

`S(n-14) <= |J_n|+1 <= S(n)-B n^delta`.

Hence

`S(n)>=S(n-14)+B n^delta`.

LEMMA-002 applies with `beta=0` and `A=14`, yielding
`S(n)=Omega(n^(1+delta))`, which is GATE-004. GATE-004G is nonterminal and
does not supply GATE-005 amplification.

## First audit

The conditioned union identity alone is insufficient. LEMMA-011 gives
distinct, disjoint branches whose OR is an arbitrary hard core, yet a minimum
parent can exceed the optimal shared pair by at most seven gates. This is
`GATE-004G-CONDITIONED-UNION — NO-GO` for a generic direct-sum inference.

The open theorem must therefore prove a SAT-specific restriction on internal
sharing between `CSAT_0` and `CSAT_1`, strong enough to compress both outputs
jointly below the single parent circuit by `Omega(n^delta)`. No such restriction
is assumed here.

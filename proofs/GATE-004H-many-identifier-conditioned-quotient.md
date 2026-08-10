# GATE-004H — choose among many conditioned identifiers

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<=1`, `B,delta>0`, and `n0` such that for
every `n>=n0` and every minimum circuit `C_n` for `SAT-gamma_n`, let

`ell(n)=max(1,floor(c log_2 n))`.

Among the identifiers

`2^(ell(n)-1) <= j < 2^ell(n)`

there is one for which the joint semantic quotient of the two ENC-008
restrictions `R_{j,0},R_{j,1}` has at most

`|C_n|-B n^delta-1`

gates after constant normalization.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted SAT-gamma circuits; polynomially many equal-length conditioned pairs; shared two-output semantic quotient |
| Uniform/non-uniform | Fully non-uniform circuit adversary and per-circuit identifier choice |
| Circuit size | Joint quotient plus final OR loses at least `B n^delta` relative to the parent |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | No verifier advice; identifier selection is non-uniform within the theorem |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed `c,B,delta`; every sufficiently large `n`; every minimum circuit; exists one identifier in the bit-length block |
| Regime | Worst-case exact total-language computation; malformed suffixes reject |

## Bridge to GATE-004

All candidate prefixes have length

`p(n)=4ell(n)+10=O(log n)`.

ENC-008 proves that ORing the selected quotient outputs computes
`SAT-gamma_{n-p(n)}`. Adding one OR gives

`S(n)>=S(n-p(n))+B n^delta`.

LEMMA-014 then yields `Omega(n^(1+delta)/log n)` circuit size and hence a
superlinear exponent, establishing GATE-004. GATE-004H is nonterminal and does
not supply exponent amplification.

## First attack boundary

The number of available identifiers is approximately `n^c`, but candidate
count alone is not a loss theorem. An averaging proof must define incidences of
split and disappeared parent labels across identifiers and show that their
signed surplus is positive for at least one `j`. The next cycle will formulate
that incidence matrix and test it against functions whose dependence on many
semantic variables is mediated by a shared core.

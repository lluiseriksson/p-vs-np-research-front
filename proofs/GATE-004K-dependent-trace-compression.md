# GATE-004K — conditioned compression of dependent traces

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n0` such that for
every `n>=n0` and every minimum circuit `C_n` for `SAT-gamma_n`, use the full
bit-length-`ell(n)` identifier block `J_n`, where

`ell(n)=max(1,floor(c log_2 n))`.

Let `P_n` be the number of parent gates whose semantic functions depend on the
common ENC-008 prefix block. For each `j in J_n`, let `T_j` be the set of
distinct active residual functions contributed by the two copies of those
`P_n` labels under `R_{j,0},R_{j,1}`. Then

`sum_{j in J_n}(P_n-|T_j|) >= |J_n|(B P_n^eta+1)`.

Equivalently, if `e_j` counts eliminated dependent occurrences and `h_j`
counts their duplicate-function surplus, the left side is

`sum_j(e_j+h_j-P_n)`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted SAT-gamma circuits; semantic prefix-dependent labels; exact residual traces under every conditioned pair |
| Uniform/non-uniform | Fully non-uniform circuit adversary and semantic trace classification |
| Circuit size | Average dependent-trace deficit at least a positive power of the dependent region, plus the final OR gate |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed `0<c<1` and `B,eta>0`; every sufficiently large `n`; every minimum circuit; all identifiers in the block |
| Regime | Worst-case exact total-language computation; malformed suffixes reject |

## Bridge

LEMMA-023 gives, for each identifier,

`|C_n|-q_j >= P_n-|T_j|`.

Therefore GATE-004K implies the aggregate loss in GATE-004J with the full
dependent set in place of its top subset. LEMMA-021 gives
`P_n>=|D_n|>=|J_n|=Omega(n^c)`, so the positive-power term also implies the
GATE-004J target after adjusting constants. The established chain then reaches
GATE-004I, GATE-004H, and the nonterminal GATE-004.

## First attack boundary

The theorem requires `|T_j|<P_n` by a polynomial margin on average. LEMMA-022
shows this cannot follow from the size of the ambient Boolean-function
universe. The next proof attempt must use relations imposed by one shared
minimum SAT circuit—topology, reuse, or exact SAT trace identities—to prove
elimination or duplication among its actual dependent residuals.

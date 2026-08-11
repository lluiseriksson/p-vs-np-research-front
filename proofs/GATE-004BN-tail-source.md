# GATE-004BN-TAIL-SOURCE — prune every source containing a whole clause

**Label: PROVED**

Assume GATE-004BN and let `a>=1` whole implication clauses feed the LEMMA-164
source. Then some neutral clause restriction leaves `N+r<=j+1`.

## Exact higher-rank cases

For `r>=2,d=2` or `r=2,d=3`, LEMMA-166 gives `p=a`. LEMMA-168 identifies
the source bit, up to polarity, with `B W_a`. Its upstream tree is a
variable-read-once formula. LEMMA-167 makes one NOT private to each upstream
pair. Neutralizing any such pair deletes that NOT, so the parent resource
drops from `j+2` to at most `j+1`.

## Rank-one slack case

Here `N=j+1`, and the inequalities in LEMMA-166 have one total slack unit.
Thus either

`p=a, q=b+1`

or

`p=a+1, q=b`,

where `q=N-p` is the downstream formula NOT count.

In the first case LEMMA-167 again prunes an upstream private NOT.

In the second case with `b>=1`, fix `z` to its satisfied code. The downstream
formula restricts to `R W_b` with at most `q=b` NOTs, while LEMMA-119 gives
the reverse bound. It is therefore an exact variable-read-once `b`-NOT
formula. LEMMA-167 supplies a formula for the neutral restriction of any
downstream pair with `b-1` NOTs. Combine it with the upstream formula and, if
the satisfied code is zero, one NOT on `z`. The reconstructed circuit has
resource at most

`(a+1)+(b-1)+1=j+1`.

If `b=0`, the zero-NOT downstream formula is monotone in `z`. It outputs the
nonzero residual only at the satisfied code, so that code must be one.
Combining the upstream formula directly with the zero-NOT residual breaks the
cycle and has resource `p=j+1`; neutralizing any upstream clause does not
increase it.

These cases exhaust every positive-upstream-tail source.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned two-excess implication circuits with a no-cut source containing at least one whole tail clause |
| Uniform/non-uniform | Every individual non-uniform parent in the stated source regime; uniform symmetric tail |
| Circuit size | Parent `N+r=j+2`; restricted or reconstructed target `N+r<=j+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted globally and one in source/residual formulas |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors, read-once tree geometry, and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `j>=2`, `sigma>=3`, and LEMMA-166 no-cut parent with `a>=1` |
| Regime | Exact worst-case subgate of GATE-004BN; base-only sources remain open; not a SAT lower bound or terminal result |

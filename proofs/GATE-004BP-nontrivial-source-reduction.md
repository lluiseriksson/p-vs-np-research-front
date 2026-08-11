# GATE-004BP-NONTRIVIAL-SOURCE — reduce to a primary base source

**Label: PROVED**

Any counterexample to GATE-004BN of minimum essential base arity has no
nontrivial base-only source formula. Consequently its LEMMA-164 source is a
primary base input with `p=0`.

## Proof

All already closed cases leave GATE-004BP, so suppose its source formula `A`
is base-only. LEMMA-166 gives `p=0` in the exact higher-rank cases and
`p<=1` in rank one. Compress `A` by LEMMA-170 and call the resulting base
`G`. The factor circuit for `G W_j` has resource at most `j+2-p`.

If its minimum resource is at most `j+1`, LEMMA-169 gives a circuit for
`G W_{j-1}` with resource at most `j`. Substituting `A` adds at most `p<=1`,
so the original restricted function has resource at most `j+1`.

The only remaining possibility has `p=0` and minimum compressed resource
exactly `j+2`. If its base parameter is at most two, the general upper bound
already gives resource at most `j+1` at `j-1`. If its parameter is at least
three, it is another two-excess instance. Rank zero, sole-cut, and
positive-tail sources are already closed by LEMMA-166 and
GATE-004BN-TAIL-SOURCE. Otherwise it is a GATE-004BP counterexample.

If `A` has at least two inputs, LEMMA-170 makes that counterexample's essential
base arity strictly smaller, contrary to minimal choice. Therefore `A` has
one input. Since `p=0`, LEMMA-170 makes it the primary input itself.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum-counterexample reduction for pruned two-excess implication circuits with base-only sources |
| Uniform/non-uniform | Fully non-uniform bases and circuits; uniform symmetric tail |
| Circuit size | Preserves the target `N+r<=j+1`; reduces essential base arity unless the source is primary |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean substitution and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every minimum-arity counterexample candidate with `j>=2` and `sigma>=3` |
| Regime | Exact worst-case reduction of GATE-004BP; the primary-source boundary remains open; not a SAT lower bound or terminal result |

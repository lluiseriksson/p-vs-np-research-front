# GATE-004BM-SOURCE-RANK-COUNTS-ONLY — infer pruning from equality data

**Label: NO-GO**

## Attempt

Use only LEMMA-166's source degree, parent/residual ranks, regional clause
counts, regional NOT lower bounds, and their equality/slack status to infer
that some neutral clause restriction lowers `N+r`.

## Countermodel to the inference

Fix `j>=2`. Take the abstract equality data

`r=2, d=2, a=0, b=j, p=0, N=j`.

The residual source rank is `r-d+1=1`; the downstream bound is exactly
`N-p=b`, and the total resource is `N+r=j+2`. Thus every numerical and
topological scalar constraint used in LEMMA-166 is met. Now attach a formal
resource set of size `j+2` and declare that every neutral single-clause
restriction retains every resource. Nothing in the listed scalar data
forbids that survival table.

Therefore source/rank equality data alone do not imply the required pruning.
This is an abstract countermodel to an inference scheme, not a realizable
minimum Boolean circuit and not a counterexample to GATE-004BM.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract source-degree/rank/NOT data plus clause-restriction survival tables |
| Uniform/non-uniform | Explicit finite abstraction; no circuit-realizability or uniformity claim |
| Circuit size | Formal resource total `j+2`, all retained under every declared one-clause restriction |
| Circuit depth | Not represented |
| Fan-in | Not represented; target circuit basis remains binary AND/OR and unary NOT |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Integer ranks, degrees, and finite resource sets only |
| Asymptotic quantifiers | Every integer `j>=2` in the abstract equality-data class |
| Regime | Structural no-go for source-rank-count-only pruning; does not refute GATE-004BM or any SAT lower bound |

# GATE-004AC — rigidity under width-three-sparse two-block slot products

**Label: EXPLORATORY**

Use the GATE-004X rows and core, the LEMMA-071 slots, and
`s=floor((R-1)/104)`. Prove fixed `c,B,eta>0` exist such that every
sufficiently large exact SAT-gamma witness and every minimum agreeing
unrestricted circuit satisfy

`sum_context (|C|-q_context) >= R(B R^eta+1)`.

LEMMA-071 gives packing at most `78s<=3(R-1)/4<=K`; the all-long option
retains the `6s` positive-clause bound, and earlier run thresholds remain
below `K`. Width at least four, overlapping, and nonclausal predicates remain.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits agreeing with SAT-gamma on expanded rows and width-three-sparse slot products; exact diagonal quotients |
| Uniform/non-uniform | Uniform witnesses; fully non-uniform circuit adversary |
| Circuit size | Polynomial average-loss target; known disjoint signed width-at-most-three packing below `K` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean circuits with inherited affine geometry over `F_2` |
| Asymptotic quantifiers | Fixed positive constants; all sufficiently large compatible lengths; every agreeing function and minimum circuit |
| Regime | Worst-case exact positive brick; not a circuit lower bound or terminal result |

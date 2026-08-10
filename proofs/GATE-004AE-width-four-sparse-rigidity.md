# GATE-004AE — width-four-sparse three-block rigidity

**Label: EXPLORATORY**

Choose the proved LEMMA-075/GATE-004AD three-block slot product with
`s=floor((R-1)/192)`. Since `142s < R-1 <= K`, prove that every
minimum unrestricted circuit agreeing with SAT-gamma on the canonical
expanded rows and these witnesses has polynomial positive average diagonal
quotient loss.

This is falsifiable. A common predicate tail with exact additive circuit cost
and enough representation-independent quotient classes, or a width-five
packing whose cost survives minimum-circuit compression, refutes the proposed
forcing mechanism. The first attack is the width-five clause ladder; overlap
and nonclausal predicates remain explicit parallel obligations.

Even a proof would establish only the next local rigidity brick. The recorded
GATE-004 and GATE-005 bridges would still be required before any terminal
claim.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted Boolean circuits agreeing with SAT-gamma on expanded rows and width-four-sparse slot products; exact diagonal quotients |
| Uniform/non-uniform | Uniform witnesses and parameters; fully non-uniform circuit adversary |
| Circuit size | Polynomial average-loss target; proved disjoint signed width-at-most-four packing below `K` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean circuits with affine prefix geometry over `F_2` |
| Asymptotic quantifiers | Fixed positive constants; all sufficiently large compatible lengths; every agreeing function and minimum circuit |
| Regime | Worst-case exact positive brick; not a circuit lower bound or terminal result |

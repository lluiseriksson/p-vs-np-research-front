# GATE-004AE-WIDTH4-ONLY — width-four sparsity controls all disjoint tails

**Label: NO-GO**

LEMMA-076 proves that the three-block witness family retains
`floor(N/5)` disjoint common signed width-five clauses per sufficiently long
slot, even though LEMMA-075 bounds every such family through width four by a
constant. Therefore width-four sparsity alone cannot rule out the established
general-clause tail mechanism.

This does not prove negative diagonal loss: the exact additive cost and
representation-independent quotient survival of the signed width-five tail
remain unaudited. GATE-004AE may still use overlap, nonclausal structure, or
exact SAT interactions. The rejected inference is only that the width-four
matching bound controls all disjoint common predicates.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact three-block slot products and signed clause matching |
| Uniform/non-uniform | Uniform witnesses; no circuit selected |
| Circuit size | No lower bound; width-five common packing linear per slot |
| Circuit depth | Later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every sufficiently large slot with `floor(N/5)>=68` |
| Regime | Width-threshold method no-go only; GATE-004AE and P versus NP remain open |

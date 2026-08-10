# GATE-004AB-ENC022-ALPHABET-ONLY — the ten-block alphabet suffices

**Label: NO-GO**

LEMMA-069 proves that the ten ENC-022 blocks, even with every pair of
nonoverlapping placements and `A_rho`, retain `rho` disjoint common aligned
signed triples. Two blocks do not enrich one aligned chunk. Thus this fixed
alphabet cannot prove GATE-004AB. LEMMA-070 shows that identifier-10/12
contexts repair this particular defect; arbitrary nonaligned triples remain.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact two-block neutral contexts and signed-triple incidence |
| Uniform/non-uniform | Uniform ten-block alphabet; no circuit selected |
| Circuit size | No lower bound; surviving packing `rho` per slot |
| Circuit depth | Unrestricted later circuits |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence |
| Asymptotic quantifiers | Every `rho>=8` |
| Regime | Alphabet-specific witness no-go; GATE-004AB and P versus NP remain open |

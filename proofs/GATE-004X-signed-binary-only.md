# GATE-004X-SIGNED-BINARY-ONLY — signed-binary sparsity suffices

**Label: NO-GO**

## Rejected method

Infer that the enhanced GATE-004X slot products have no linear disjoint
common signed-clause tail merely because LEMMA-060 puts every disjoint common
signed-binary family below the base floor.

## Failure

LEMMA-061 explicitly constructs `rho` pairwise variable-disjoint common
signed width-three clauses in every slot, hence `rho*s=P/4` in the product.
The signed-binary packing remains at most `18s`; the two facts coexist. Thus
binary sparsity does not control the next clause width and cannot by itself
justify GATE-004X rigidity.

This does not falsify GATE-004X. The signed triples become an actual circuit
counterexample only if their exact minimum cost and semantic quotient
survival are established. LEMMA-062 leaves a `2m`-gate gap, and GATE-004Y
records the missing theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact enhanced slot products and signed raw-coordinate clause packings; later unrestricted Boolean circuits |
| Uniform/non-uniform | Uniform witness family and explicit clauses; no minimizing circuit selected |
| Circuit size | Signed-binary matching at most `18s`, while signed width-three matching is at least `rho*s=P/4`; no circuit lower bound follows |
| Circuit depth | Irrelevant to the incidence no-go; later circuits unrestricted |
| Fan-in | Clauses binarized with OR fan-in two; NOT fan-in one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence only |
| Asymptotic quantifiers | Every `rho>=13,s>=1`; separation between the two packing measures grows with `rho` |
| Regime | Structural method no-go only; GATE-004X, every unrestricted SAT lower bound, and P versus NP remain open |

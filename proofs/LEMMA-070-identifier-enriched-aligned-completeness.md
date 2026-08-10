# LEMMA-070 — identifiers ten and twelve complete interior aligned triples

**Label: PROVED**

Add all aligned placements of `01 T_10` and `01 T_12` to the ENC-022 option
family. Both blocks have length 24; their final four-bit chunks are `1010`
and `1100`. Translating the final chunk to aligned slot chunk `k` is possible
for every `k>=5`. Together with the six patterns from LEMMA-069, every such
triple realizes all eight patterns. Hence only the first five aligned triples
can support a common signed clause.

The reference certificate is `identifier_enriched_complete_aligned_triples`.
Nonaligned local and intermediate-span triples remain open.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact neutral contexts, aligned translations, and three-bit pattern incidence |
| Uniform/non-uniform | Uniform finite enriched alphabet; no circuit selected |
| Circuit size | No lower bound; full patterns on `rho-5` aligned triples |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | Encoded/circuit AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence only |
| Asymptotic quantifiers | Every `rho>=6` and aligned chunk index `5<=k<rho` |
| Regime | Exact partial witness repair; not a general matching or circuit result |

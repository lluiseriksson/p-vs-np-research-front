# GATE-004DK-SIX-UNCHARGED-LOSSES-ONLY — the carrier consumes the six-budget

**Label: NO-GO**

Treating all six positions in the three satisfying loss sets as uncharged
resources is invalid at the size-three endpoint. LEMMA-218 shows that `{g,h}`
already occupies two loss sets in the AND→OR orientation and one loss set in
the OR→AND orientation. After deduplication and carrier charge, at most two or
four physical gates remain, respectively.

Therefore a pruning-only injection for the aligned circuit deficit requires
`D_b^DAG<=2` in the first orientation or `D_b^DAG<=4` in the second. Even
these are upper caps, not guaranteed available resources. This no-go does not
exclude external joint savings, private/non-bridge gates, or potential
descent; it excludes a six-unit uncharged pruning ledger.

## Model card

| Field | Value |
|---|---|
| Computational model | Size-three minimum unrestricted AND/OR/NOT plateau with exact physical loss sets |
| Uniform/non-uniform | Every finite non-uniform hypothetical endpoint in either carrier orientation |
| Circuit size | Six raw loss positions reduce to at most two or four uncharged distinct gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Physical loss-set union and carrier-charge deduplication |
| Asymptotic quantifiers | Every endpoint loss triple and both LEMMA-193 orientations |
| Regime | Six-uncharged-losses accounting no-go; not an endpoint counterexample, SAT lower bound, or terminal result |

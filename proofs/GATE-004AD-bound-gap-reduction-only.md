# GATE-004AD-BOUND-GAP-REDUCTION-ONLY — truncate every large gap at one block length

**Label: NO-GO**

The proposed proof step was to infer, from four-alignment and a maximum block
length `B` alone, that all gaps at least `B` reduce to `{B,...,B+3}` while
preserving nonoverlap. LEMMA-101 gives an exact length-eight counterexample.

LEMMA-102 proves the safe geometry-only replacement `{2B,...,2B+3}`. For the
LEMMA-075 alphabet (`B=68`), the corrected quartet domain has gaps through 139
and `4*139^3=10,742,476` types. The existing `4*71^3` certificate proves only
its audited subdomain. Therefore LEMMA-075 and GATE-004AD return to
`EXPLORATORY` until the corrected domain or a stronger SAT-specific normal
form is proved.

This no-go concerns the finite-reduction method, not the truth or falsity of
GATE-004AD and not any circuit lower bound.

## Model card

| Field | Value |
|---|---|
| Computational model | Aligned bounded neutral-block contexts and quartet zero-mask incidence |
| Uniform/non-uniform | Uniform geometric proof method; later circuits not reached |
| Circuit size | No lower bound |
| Circuit depth | Later circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | The claimed all-gap reduction is refuted; the specific 92-identifier alphabet remains open outside the audited subdomain |
| Regime | Structural proof-method no-go; no SAT or terminal conclusion |

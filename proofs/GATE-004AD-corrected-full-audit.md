# GATE-004AD-CORRECTED-FULL-AUDIT — cover the safe quartet domain

**Label: PROVED**

For the 92 identifiers in `LENGTH68_REPAIR_IDENTIFIERS`, every
ordinary nonzero quartet mask 1 through 14 is realized by at most three
nonoverlapping four-aligned neutral blocks on every safely reduced type

`(68+r, 68+r+g1, 68+r+g1+g2, 68+r+g1+g2+g3)`, where
`r in {0,1,2,3}` and each gap obeys the phase cap of its left coordinate from
LEMMA-103: `(135,134,133,132)`.

LEMMA-106 proves all types with a gap at least 72 analytically, and the
historical `4*71^3` certificate proves every remaining type. Thus the theorem
is closed without executing the larger phase-sharded production sweep.

`verification/corrected_quartet_shards.py` fixes the production parameters and
splits the domain into 534 one-first-gap shards of 17,622–18,021 types. Every
shard seals its parameters, alphabet hash, checked count, failure count, and
first counterexamples. The merger rejects incomplete, overlapping, gapped,
tampered, or differently configured inputs and accepts a universality
certificate only when all 9,515,749 types are covered with zero failures.

The production sweep is deliberately retired rather than executed on Windows.
The shard contract remains an independent reproducibility option. A typical
shard command is

`python verification/corrected_quartet_shards.py run 0 1 2`

and the merger takes the complete list of shard JSON paths after `merge`.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact three-block SAT-gamma neutral contexts and four-coordinate zero-mask incidence |
| Uniform/non-uniform | Uniform fixed 92-identifier alphabet, placements, shard partition, and parameters; no circuit selected |
| Circuit size | No lower bound; `142s` disjoint common-clause packing consequence in LEMMA-075 |
| Circuit depth | Fixed blocks bounded; later circuits unrestricted |
| Fan-in | Encoded AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and modulo-four translation |
| Asymptotic quantifiers | Every one of the 9,515,749 phase-reduced types, hence every sufficiently interior quartet by LEMMA-103 |
| Regime | Exact witness-construction theorem closed analytically plus the smaller historical certificate; not a circuit lower bound or terminal result |

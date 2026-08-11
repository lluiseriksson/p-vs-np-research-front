# GATE-004DU — contraction-aware swap-support transport

**Label: EXPLORATORY**

LEMMA-230 and NG-169 show that a surviving provenance coordinate need not
have one literal parent edge uncontracted in all three satisfying minors.
GATE-004DT must therefore use the complete contraction maps rather than a
common-edge pivot.

## Falsifiable theorem

For every common-origin swap cycle at the refined endpoint, use its exact
parent edge support and the three labeled contraction maps to prove one of:

1. an explicit contraction-invariant uncrossing yields a size-nonincreasing
   rewrite and strict `W,Q,R_0` descent;
2. some support segment outside the relevant contracted pair supplies a real,
   previously uncharged host or non-bridge deletion in the code where it is
   needed; or
3. the three contracted pairs cannot cover the marked swap support under the
   exact two-gate loss identities and four-code path signatures.

For the distinct-origin branch, prove a genuine matching into distinct
retargetable hosts after global deduplication; origin identity alone is not a
payment. Literal support intersection, abstract cycle-space alignment, and
raw counts of swap gates are inadmissible substitutes.

The theorem is falsified by a refined minimum endpoint with positive aligned
deficit whose marked cycle supports are fully covered by rank-neutral
contractions as in LEMMA-230, whose distinct origins admit no host matching,
and which has no contraction-invariant exchange or potential descent.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with marked swap cycles and three exact contraction maps |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; only explicit exchanges or matched real hosts pay residual `D_b^DAG` |
| Circuit depth | Unrestricted; marked cycle paths and contracted segments unbounded |
| Fan-in | AND/OR two; NOT one; fanout unrestricted; every edge support, contraction, origin, and host audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code path signatures, literal edge supports, contraction maps, potentials, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, refined endpoint, swap cycle, satisfying contraction map, and distinct-origin branch |
| Regime | Exact worst-case contraction-aware support gate; not a SAT lower bound or terminal result |

## Cycle-194 audit

LEMMA-231 proves that oriented loss unions cannot fully cover marked supports
larger than four in AND→OR or six in OR→AND. LEMMA-232 makes those thresholds
sharp for abstract loss sets, so long-support pigeonhole alone is NG-170.
GATE-004DV replaces this route with a semantics-preserving reduction and
classification of the bounded residual cores. GATE-004DU remains
`EXPLORATORY`.

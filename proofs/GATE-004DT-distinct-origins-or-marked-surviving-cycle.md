# GATE-004DT — pay distinct origins or exploit marked surviving support

**Label: EXPLORATORY**

LEMMA-228 gives the physical provenance dichotomy when both defect routes
coexist in one parent DAG. LEMMA-229 and NG-168 show that a common-origin
cycle survives all satisfying minors and cannot be charged as a lost cycle.

## Falsifiable theorem

For every overlap swap remaining after GATE-004DS, prove one of:

1. **distinct-origin branch:** the two marked origins are distinct, previously
   uncharged, actually retargetable hosts or external payments, with complete
   path cuts and no shared physical gate counted twice; or
2. **common-origin branch:** retain the exact old-parent edge support of the
   surviving cycle and construct a size-nonincreasing uncrossing that frees a
   real host or strictly decreases `W,Q,R_0`, without calling the cycle lost;
   or
3. a named satisfying loss or non-bridge deletion outside that surviving
   coordinate supplies the missing payment.

If the two defect routes do not coexist in one physical parent DAG, first
replace union-graph provenance by an explicit compatible path certificate or
charge the structural retargeting that prevents it. All origins, paths,
supports, contractions, and prior charges must be globally deduplicated.

The theorem is falsified by a refined minimum endpoint with positive aligned
deficit whose distinct origins are unavailable or previously charged, whose
common-origin cycles have no cost-reducing marked-support exchange, and whose
remaining provenance exists only across incompatible old/new edges.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with compatible physical defect paths and marked surviving cycle support |
| Uniform/non-uniform | Every finite non-uniform operational residual endpoint tuple |
| Circuit size | Parent `K+2`; only distinct uncharged origins or explicit exchanges pay residual `D_b^DAG` |
| Circuit depth | Unrestricted; provenance paths and marked cycle support unbounded |
| Fan-in | AND/OR two; NOT one; fanout unrestricted; every origin, shared prefix, path, and contraction audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code defects, physical DAG paths, marked cycle supports, potentials, and cycle spaces over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, refined endpoint, overlap swap, provenance pair, and residual branch |
| Regime | Exact worst-case physical-provenance payment gate; not a SAT lower bound or terminal result |

## Cycle-193 audit

LEMMA-230 shows that a surviving parent coordinate can have no literal edge
left uncontracted in all three satisfying minors. Selecting a common edge from
survival alone is NG-169. GATE-004DU replaces that route with the full labeled
contraction maps and a separate matching obligation for distinct origins.
GATE-004DT remains `EXPLORATORY`.

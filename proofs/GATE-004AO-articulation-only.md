# GATE-004AO-ARTICULATION-ONLY — repeat one-bit articulation factorization

**Label: NO-GO**

The one-bit articulation method used in LEMMA-126 cannot address the remaining
theta core. After suppressing degree-two paths, a theta graph consists of two
branch vertices joined by three internally disjoint paths. Removing either
single branch vertex leaves the core connected; no articulation isolates a
leaf cycle block whose variables reach the output through one bit.

Therefore the exact hypothesis needed by LEMMA-121's articulated factorization
is absent. Treating either branch vertex as a one-bit cut without proving that
all relevant input paths pass through it would silently discard one or more
theta branches and is invalid.

This is a topology-method no-go only. GATE-004AO was subsequently proved by
orientation-stratum analysis; articulation-only reuse remains invalid.

## Model card

| Field | Value |
|---|---|
| Computational model | Theta 2-cores of pruned bicyclic Boolean circuits and articulation-based factorizations |
| Uniform/non-uniform | Every individual non-uniform theta-core candidate |
| Circuit size | No additional lower bound; one-vertex factorization does not apply |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected vertex connectivity only |
| Asymptotic quantifiers | Every theta-core candidate in GATE-004AO |
| Regime | Structural no-go for articulation-only reuse; two-vertex interface remains open |

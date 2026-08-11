# GATE-004BE-STRATUM-COUNTS-ONLY — infer pruning from `(q,rho)` alone

**Label: NO-GO**

LEMMA-158 determines the possible residual pairs `(q,rho)`, but a pair of
integers contains no clause-to-resource incidence or restriction-survival
data.

Formally, take a resource set `R` of size `m+1` and assign to every neutral
single-clause restriction the same survival set `R`. This abstract survival
table realizes the sole numerical premise `|R|=m+1` and loses no resource
under any clause. It can be decorated with any one of LEMMA-158's allowed
count pairs, because those pairs constrain only the total partition into NOT
and cycle resources, not the survival map.

This is not a Boolean circuit, does not claim realizability, and does not
refute GATE-004BE. It proves only that the one-excess integer classification
cannot imply pruning without at least one additional topological or semantic
relation between clauses and resources.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract resource sets and single-clause survival tables |
| Uniform/non-uniform | Explicit finite abstraction; no circuit-realizability or uniformity claim |
| Circuit size | Exactly `m+1` abstract resources, all retained by every one-clause restriction |
| Circuit depth | Not represented |
| Fan-in | Not represented; target circuit basis remains binary AND/OR and unary NOT |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite sets and integer resource partitions only |
| Asymptotic quantifiers | Every `m>=1` in the abstract survival-table class |
| Regime | Structural no-go for stratum-count-only pruning; GATE-004BE/BD were later proved using LEMMA-164/165, while GATE-004BA/AZ/AY/AX/AW/AV/AU/AG/AE remain open |

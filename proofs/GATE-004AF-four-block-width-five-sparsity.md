# GATE-004AF — four-block sparsity through signed width five

**Label: EXPLORATORY**

Allow up to four nonoverlapping translated universally neutral blocks per slot
option, retain the all-one and `A_rho` options, and seek fixed constants
`L,c_5` such that every disjoint family of non-tautological common signed
clauses of width at most five has at most `c_5` members per slot.

Four blocks can realize every pattern with at most four prescribed zeros on
distant quintuples, while `A_rho` supplies the all-zero pattern away from six
positions. The first attack is a five-coordinate finite translation
certificate, using the LEMMA-075 alphabet as a baseline and an exact
interval-DP falsifier. A translation-stable missing pattern gives a linear
packing and rejects the chosen alphabet; complete universality proves only
the witness theorem and opens a new rigidity gate.

LEMMA-077 carries out the baseline audit and finds a stable mask-16 failure on
offsets `{0,4,7,9,10}`. Thus the LEMMA-075 alphabet is `NO-GO` for this gate.
The next attack must enrich the fixed alphabet and preserve the resulting
larger block-length bound in the five-coordinate reduction.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact four-block neutral contexts, one long option, signed clauses through width five, and matching |
| Uniform/non-uniform | Uniform finite alphabet and placements; later circuits fully non-uniform |
| Circuit size | No lower bound; target constant-per-slot matching through width five |
| Circuit depth | Fixed blocks bounded; long option may have linear depth; later circuits unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence and translation |
| Asymptotic quantifiers | Exists fixed `L,c_5`; every sufficiently large slot; every disjoint width-at-most-five common family |
| Regime | Exact witness-construction gate; not a circuit lower bound or terminal result |

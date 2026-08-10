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

Identifiers 1,089 and 1,098 repair that representative at the same length
bound, but LEMMA-078 finds a new mask-8 obstruction and 1,787 failures in the
gap-at-most-20 audit. This two-identifier specialization is also `NO-GO`.

LEMMA-079 replaces ad hoc patches by an exact strength-five covering basis on
the fourteen free identifier bits. It reduces the local failure count from
1,787 to 497, but LEMMA-080 finds a fixed-token/gamma-boundary mask-16
obstruction. The next enrichment must cover complete-block phases, not merely
free binary projections.

LEMMA-081 extends the covering basis across every identifier length and proves
behavioral completeness for all five-coordinate projections. LEMMA-082 then
shows that the obstruction survives the literal complete identifier range
1 through 32,767. Therefore every length-at-most-68 specialization is
`NO-GO`; the next construction must use block length at least 72.

LEMMA-083 extends the complete obstruction through length 72. LEMMA-084 then
finds the first repair at length 76, using identifier 98,370. The next finite
audit must use bound 76 and must not infer global universality from that one
repaired quintuple.

LEMMA-085 shows that the single repair retains a shifted mask-16 obstruction
and 494 local failures. LEMMA-086 supplies 2,873 behaviorally complete
representatives for the full length-76 alphabet; its complete audit is the
next operational task.

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

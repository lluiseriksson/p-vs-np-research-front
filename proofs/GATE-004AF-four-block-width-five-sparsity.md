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

LEMMA-087 replaces representative materialization by an exact symbolic oracle.
Its exhaustive local audit finds 195 failures for the complete length-76
alphabet, and LEMMA-088 turns one into a translated packing. Every
length-at-most-76 specialization is therefore `NO-GO`; the next repair must
use block length at least 80.

LEMMA-089 extends the complete obstruction through length 80. LEMMA-090 gives
an explicit length-84 repair using identifier 278,594, so the next exact gate
is the complete length-84 local type audit. A repaired representative is not
being promoted to global width-five universality.

LEMMA-091 completes that audit and finds 122 failures. One mask-8 failure
translates to an `N/24-O(1)` common packing, so every length-at-most-84
specialization is `NO-GO`. The next repair must use block length at least 88.

LEMMA-092 supplies that first local repair explicitly with identifier 526,344.
The complete length-88 type audit is the next operational gate; no global
coverage is inferred from the repaired representative.

LEMMA-093's complete length-88 audit retains 111 failures and an
`N/24-O(1)` packing. LEMMA-094 then observes that the same translated
obstruction survives the exact complete alphabets through lengths 92 and 96.
Thus all length-at-most-96 specializations are `NO-GO`. LEMMA-095 gives a
length-100 local repair; the complete length-100 audit is next.

LEMMA-096 completes that audit and finds 46 failures. One mask-8 failure
translates to an `N/28-O(1)` packing, so every length-at-most-100
specialization is `NO-GO`. LEMMA-097 gives the first length-104 local repair;
the complete length-104 type audit is next.

LEMMA-098 completes that audit and retains 44 failures. LEMMA-099 follows the
resulting mask-16 obstruction through the complete length-108 and length-112
alphabets, retaining an `N/28-O(1)` packing. Every length-at-most-112
specialization is `NO-GO`. LEMMA-100 gives the first length-116 local repair;
the complete length-116 audit is next.

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

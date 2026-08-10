# GATE-004U — syntax-linked DNF witness rigidity

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n_0` such that for
every `n>=n_0`, put `L=floor(c log_2 n)`, `R=2^(L-2)`, and use the full
ENC-016 expanded prefix cube `X_L` of length `p=6L+13`.

Let `D_{L,n}` be the explicit set of length-`n-p` suffix strings obtained as
follows:

1. encode complete or partial assignment conjunctions over all ENC-016
   primary and auxiliary identifiers;
2. combine any nonempty list of them by the exact binary OR formula token;
3. require the unpadded formula to fit; and
4. use ENC-010's identifier-1-fresh padding together with outer double-NOT
   padding or any one/two-block ENC-022 neutral placement to reach length
   exactly `n-p`.

Let `G:{0,1}^n->{0,1}` be any total Boolean function satisfying

`G(r,y)=SAT-gamma_n(r,y)`

for every `r in X_L` and every `y in D_{L,n}`. For every minimum unrestricted
circuit `C` for `G`, let `q_s` be its exact semantic joint quotient size under
the two diagonal rows for context `s`. Then

`sum_s (|C|-q_s) >= R(B R^eta+1)`.

The statement is falsifiable by any total-function family matching SAT on all
specified bit-level DNF witnesses but violating the loss inequality.

## SAT bridge

Exact `SAT-gamma_n` satisfies the agreement premise by definition. The
conclusion is the GATE-004Q loss bound, so ENC-013 and LEMMA-014 yield the
first superlinear unrestricted SAT circuit lower bound GATE-004.

## Attack boundary

LEMMA-043 shows that the abstract output-column set carries no forcing power.
ENC-019 and LEMMA-044 close the first syntax-linked attempt as well: witnesses
sharing a growing common outer padding block lie in a fixed raw-coordinate
face, and those coordinates become an exact-minimum fresh tail.

ENC-020 completes the raw padding-density task: for each DNF and every large
four-divisible padding budget, an `O(n)` family of exact neutral encodings
varies every outer raw coordinate. LEMMA-045 blocks any LEMMA-044 tail made
from raw coordinate literals.

The next audit is strictly harder. Characterize low-complexity non-coordinate
predicates that equal one on every dense encoding, beginning with the regular
language recognizing the ENC-020 contexts, and determine whether conjoining
such a predicate has any exact additive minimum-circuit cost. LEMMA-037 cannot
be invoked because those predicates are not fresh inputs. Full GATE-004U
remains open.

ENC-021 and LEMMA-046 close that first non-coordinate audit. Half-block-
separated OR clauses are all one on ENC-020, and successive restrictions prove
their conjunction has exact additive cost. The resulting minimum circuit has
loss at most `K-P/2`, so ENC-020-only forcing is `NO-GO`.

The next syntax-design constraint is pairwise zero coverage: on any large
candidate padding region and for every coordinate pair, some required witness
must set both bits to zero. This blocks the particular positive two-literal
clauses above but is not assumed sufficient. Full GATE-004U remains open
because its complete DNF set may already supply interactions absent from the
single-block ENC-020 subfamily.

ENC-022 and LEMMA-047 meet that constraint up to four root-token pairs whose
matching number is only two. They therefore eliminate every growing disjoint
positive two-clause tail of the LEMMA-046 form once the required witness set
includes all one/two-block placements. The active audit now moves to
overlapping clauses, higher-width CNF predicates, and interactions already
present in the complete DNF suffix set. No pairwise-coverage statement is
treated as sufficient for loss.

ENC-023 and LEMMA-048 show that this repair is width-specific. Any context
with at most two localized blocks satisfies a linear family of distant
width-three clauses, whose exact minimum circuit again has loss at most
`K-P/3`. Thus one/two-block forcing alone is `NO-GO`. The next construction
target is triple-zero coverage; the structural audit simultaneously asks
whether allowing an unbounded block count merely moves the obstruction to a
growing-width common predicate.

ENC-024 and LEMMA-049 replace that iterative concern by a quantitative
theorem. For `b(P)` zero blocks of maximum length `D(P)`, put
`m=floor(P/(b(P)+1))`. Whenever `m>K(P),D(P)`, an exact width-`b+1` clause
tail gives negative loss. Every fixed block count and every sparse growing
regime satisfying those inequalities is therefore `NO-GO`.

The next audit no longer adds a fixed number of blocks. It must analyze a
sufficiently dense unbounded-block family or use the full variation of DNF
core lengths and syntax so that no common outer predicate remains. Full
GATE-004U remains open.

ENC-025 and LEMMA-050 show that dense block count alone also fails for a fixed
finite alphabet. A maximum zero run `rho(P)` leaves a width-`rho+1` window
tail with loss at most `K-floor(P/(rho+1))`. The ten-block alphabet has
`rho=7` under arbitrary concatenation. The next construction must permit zero
runs of order at least `P/K`, or abandon the common outer/core split by using
the full variation of DNF syntax. Neither escape is assumed sufficient.

ENC-026 and LEMMA-051 realize the long-run escape exactly: a power-of-two
identifier gives a neutral length-`4rho` block with a run of `rho` zeros and
sweeps interior windows. A single block nevertheless triggers LEMMA-049, so
single-long-block forcing is `NO-GO`. The next audit must combine long runs
and sufficiently many independently placed blocks so that both
`floor(P/(b+1))<D` and `floor(P/(rho+1))<=K` hold, without losing coordinate
density or exact syntax agreement.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for total functions agreeing with SAT-gamma on the full expanded prefix cube at explicit padded DNF suffix encodings; exact diagonal semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform circuit adversary; uniform explicit prefix, assignment, OR-composition, and padding maps |
| Circuit size | Average diagonal parent-to-joint-quotient loss at least `B R^eta+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine prefix geometry over `F_2`; suffix witnesses use exact Boolean formula syntax |
| Asymptotic quantifiers | Exists fixed sufficiently small `c>0` and `B,eta>0`; every sufficiently large `n`; every eligible total `G`; every minimum circuit; all expanded rows and fitting padded DNF witnesses |
| Regime | Worst-case exact agreement on an explicit total-language subset; no promise or distribution in the ambient function |

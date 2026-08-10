# GATE-004R — radius-two SAT neighborhood rigidity

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n_0` such that the
following holds for every `n>=n_0`. Put `L=floor(c log_2 n)`, let `A_L` be the
ENC-014 affine set of length-`p=6L+13` prefix rows, and let `N_2(A_L)` be its
closed Hamming-distance-two neighborhood in `{0,1}^p`.

Let `G:{0,1}^n->{0,1}` be any total Boolean function satisfying

`G(r,y)=SAT-gamma_n(r,y)`

for every `r in N_2(A_L)` and every suffix `y in {0,1}^{n-p}`. For every
minimum unrestricted circuit `C` for `G`, let `q_s` be the exact semantic
joint quotient size under the two ENC-014 base rows for context `s`. Then,
with `R=2^(L-2)`,

`sum_s (|C|-q_s) >= R(B R^eta+1)`.

This is stronger than GATE-004Q because it allows arbitrary behavior outside
the radius-two cylinder. It is falsifiable by any total-function family that
agrees exactly with SAT-gamma on that cylinder but violates the inequality.

## Bridge

Take `G=SAT-gamma_n`. The agreement premise is immediate, and the conclusion
is exactly the GATE-004Q loss inequality. ENC-013 and LEMMA-014 then give the
same first superlinear unrestricted SAT circuit lower bound GATE-004.

## Attack plan

LEMMA-040 proves that merely copying the simplified ENC-015 radius-one
relation schema is insufficient. GATE-004R instead requires exact equality of
the residual functions on every suffix, including all malformed suffixes and
all overlaps among distance-two prefix mutations.

The first audit is syntactic: classify pairs of independently flipped
occurrences, determine which rows collide between neighboring base contexts,
and record their exact parser/formula semantics. Any claimed forcing step must
survive the LEMMA-040 fresh-tail construction and use a proved radius-two
compatibility not already present in the radius-one lookup table.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for total functions agreeing exactly with SAT-gamma on the radius-two ENC-014 prefix cylinder; exact semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform circuit adversary; uniform explicit neighborhood and restriction family |
| Circuit size | Average parent-to-joint-quotient loss at least `B R^eta+1`, with `R=2^(L-2)` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Hamming neighborhoods and affine prefix geometry over `F_2`; computation remains Boolean |
| Asymptotic quantifiers | Exists fixed `0<c<1` and `B,eta>0`; every sufficiently large `n`; every eligible total `G`; every minimum circuit; all contexts and all suffixes in the local-agreement premise |
| Regime | Worst-case exact total-function agreement with total SAT-gamma; no promise or distribution |


# Cycle 134 — higher-rank one-excess closure

**Label: PROVED**

## Result

LEMMA-164 finds a no-bypass formula source at a core vertex of degree at
least two and proves that fixing its attained bit lowers cycle rank by at
least one. LEMMA-165 extends the zero/one-cut residual dichotomy and the
sole-cut base exclusion to every such one-bit tail factorization.

Their combination proves GATE-004BL for all parent ranks `r>=2`. Together
with the rank-zero exclusion and the previously closed rank-one case, this
proves GATE-004BE. Iterating its neutral restriction proves the near-maximal
localization theorem GATE-004BD.

## Audit boundary

This is an exact theorem only for the canonical disjoint-implication family
and resource excess one. It is not a SAT circuit lower bound and supplies no
terminal implication to `P != NP` or `P = NP`.

GATE-004BM is opened at resource excess two. The degree-two no-cut source can
meet the current accounting with equality, so a new equality classification
or a second structural reduction is required.

## Classification

- LEMMA-164: `PROVED`
- LEMMA-165: `PROVED`
- GATE-004BL: `PROVED`
- GATE-004BE: `PROVED`
- GATE-004BD: `PROVED`
- GATE-004BM: `EXPLORATORY`

# GATE-004V-DISJOINT-POSITIVE-CLAUSES — an exact clause tail falsifies rigidity

**Label: NO-GO**

## Falsifiable counterexample route attempted

Attempt: find more than `K` pairwise variable-disjoint positive clauses that
are one on the full balanced slot product, conjoin them to the canonical DNF
base, and invoke LEMMA-048 to obtain a globally minimum circuit with certified
loss at most `K-m<0`.

The route is falsifiable as a method by an upper bound `m<=K` for every such
common clause family.

## Failure

LEMMA-053 uses the all-long product member, which has exactly `6s` one bits,
to prove `m<=6s` for every disjoint common positive-clause family. With

`s=floor((R-1)/8)` and `K>=R-1`,

`m<=6s<=3(R-1)/4<=K`.

Thus the exact LEMMA-048 inequality cannot certify negative loss in this
route. Clause width, nonlocal placement, and irregular geometry do not change
the packing bound.

## Scope and next attack

This is a method no-go, not evidence for GATE-004V. It does not cover clauses
with negated literals, overlapping positive clauses, arbitrary slot-membership
predicates, or extra quotient classes beyond the LEMMA-048 certificate. The
next audit starts with signed disjoint clauses and asks whether their NOT-gate
cost admits any exact additive identity comparable to LEMMA-048.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for a canonical base conjoined with pairwise variable-disjoint positive clauses common to the balanced slot product; exact semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform clause adversary and base minimum circuit; uniform product witness and packing bound |
| Circuit size | Common clause count `m<=6s<=K`; the established loss certificate `K-m` cannot be negative |
| Circuit depth | Unrestricted; clause implementation may use OR chains and the extension an AND chain |
| Fan-in | AND/OR two; NOT one available but unused in positive clauses |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite set packing only |
| Asymptotic quantifiers | Every sufficiently large `R`, `s=floor((R-1)/8)`, every clause width, and every disjoint positive-clause family common to all balanced witnesses |
| Regime | Worst-case exact no-go for one counterexample certificate; GATE-004V and P versus NP remain open |

# LEMMA-188 — the three satisfying minors have a large physical overlap

**Label: PROVED**

Assume a minimum two-gate plateau parent `C` of size `K+2`, and fix one valid
minimum pruning for each satisfying code `s in {00,01,11}`. Let `E_s` be the
set of parent gates eliminated by that pruning and `S_s` the set of parent
gates that survive as physical vertices modulo incident contractions. Then

1. `|E_s|=2`, and both members are binary;
2. for distinct satisfying codes `s,s'`,
   `|S_s intersect S_s'| >= K-2`;
3. `|S_00 intersect S_01 intersect S_11| >= K-4`; and
4. every parent NOT gate belongs to the three-way intersection.

The lower bounds are understood as vacuous when their right side is negative.

## Proof

LEMMA-178 gives `|E_s|=2` and says no eliminated gate is a NOT. Since the
parent has `K+2` gates,

`|S_s intersect S_s'|=(K+2)-|E_s union E_s'| >= (K+2)-4=K-2`.

Likewise the union of the three two-element eliminated sets has size at most
six, so

`|S_00 intersect S_01 intersect S_11| >= (K+2)-6=K-4`.

Preservation of every NOT under every satisfying restriction gives part 4.
The lemma aligns physical parent vertices only; a surviving gate may compute
different base functions under different codes.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT plateau parent with three fixed minimum pruning maps |
| Uniform/non-uniform | Every individual finite non-uniform plateau parent and pruning triple |
| Circuit size | Parent `K+2`; pairwise survivor overlap at least `K-2`; triple overlap at least `K-4` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite set intersection plus rank-neutral contraction bookkeeping |
| Asymptotic quantifiers | Every nonconstant finite base, hypothetical minimum plateau parent, and valid satisfying pruning triple |
| Regime | Exact worst-case physical-overlap theorem; not semantic alignment, SAT lower bound, or terminal result |

# Cycle 200 — shared-seal cut capacity

**Label: PROVED**

LEMMA-243 proves that an irredundant cut of the selected reconvergence tree
partitions its antichain leaves into nonempty blocks, one per physical cut
gate. Leaf coverage is therefore not physical capacity.

LEMMA-244 realizes the extreme: cyclically retarget `k` independent terms so
every proper comb prefix changes, the total OR is invariant, and one unchanged
NOT gate is the only available equal nonoutput seal after the changed comb.
Charging that seal once per covered branch is NG-176. GATE-004EB now separates
large physical cut capacity from a heavy block whose whole pre-seal region
must be replaced, uncrossed, charged, or shown contradictory.

## Classification

- LEMMA-243: `PROVED`
- LEMMA-244: `PROVED`
- GATE-004EA-SHARED-SEAL-LEAF-MULTIPLICITY: `NO-GO`
- GATE-004EA: `EXPLORATORY`
- GATE-004EB: `EXPLORATORY`

`verification/shared_seal_cut_audit.py` checks every irredundant cut of comb
trees through six leaves and the cyclic function identities through `k=8`.
The general claims use the direct proofs. Fable was not invoked; independent
certification, minimum endpoint realizability, and terminal implications are
not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Rooted physical cut trees and named constant-free AND/OR/NOT cyclic-retargeting pairs |
| Uniform/non-uniform | Every finite irredundant tree cut; every finite diagnostic pair `k>=3` |
| Circuit size | Cut capacity equals physical cut count; diagnostic covers `k` branches with one equal seal |
| Circuit depth | Unrestricted; diagnostic comb depth linear in `k` |
| Fan-in | Application AND/OR two and NOT one; tree fanout toward root one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean functions, cut partitions, and endpoint cycle spaces over `F_2` remain open |
| Asymptotic quantifiers | Every finite tree/cut and every diagnostic `k>=3`, prefix, branch, and assignment |
| Regime | Exact cut theorem and scoped no-go; not endpoint proof, SAT lower bound, or terminal result |

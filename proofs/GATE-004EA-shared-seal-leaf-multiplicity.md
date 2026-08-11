# GATE-004EA-SHARED-SEAL-LEAF-MULTIPLICITY — one cut gate counts once

**Label: NO-GO**

Scope: count one independently equal cut gate once for every antichain branch
whose path it seals, thereby turning leaf coverage into multiple physical
hosts or payments.

LEMMA-243 proves the exact accounting: an irredundant tree cut partitions the
selected leaves into blocks, one block per physical cut vertex. A vertex whose
block contains many leaves still appears once in the cut. LEMMA-244 realizes
the extreme case for arbitrary `k`: all retargeted comb paths have one
available structurally unchanged equal nonoutput seal.

This is NG-176. The diagnostic parent is nonminimal, so an operational
endpoint may force additional seals, make the heavy pre-seal region jointly
replaceable, expose distinct losses/origins, or yield descent. It refutes only
repeatedly charging a shared seal from the number of leaves it covers.

## Model card

| Field | Value |
|---|---|
| Computational model | Rooted physical cut trees and constant-free named AND/OR/NOT cyclic-retargeting circuit pairs |
| Uniform/non-uniform | Every finite irredundant tree cut; uniform diagnostic pairs for every `k>=3` |
| Circuit size | `k` covered leaves but one available equal nonoutput seal in the diagnostic |
| Circuit depth | Unrestricted theorem; diagnostic comb depth linear in `k` |
| Fan-in | Tree application and circuit AND/OR at most two; NOT one; fanout unrestricted in theorem |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean functions, physical cut partitions, and named structural changes |
| Asymptotic quantifiers | Every `k>=3`, cut block, changed comb prefix, and retargeting path |
| Regime | Shared-seal-multiplicity no-go; not an endpoint counterexample, SAT lower bound, or terminal result |

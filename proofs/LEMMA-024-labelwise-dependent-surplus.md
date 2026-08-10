# LEMMA-024 — labelwise dependent-trace surplus

**Label: PROVED**

## Statement

Use the setting of LEMMA-023. For each prefix-dependent parent label `v`, let
`B_v` be the set of distinct active residual functions contributed by its two
restricted copies, before merging functions belonging to different parent
labels. Put `s_v=|B_v| in {0,1,2}` and define

`z=|{v:s_v=0}|`,

`t=|{v:s_v=2}|`.

Let `T=union_v B_v` and define the cross-label collision surplus

`kappa=sum_v |B_v|-|T|>=0`.

Then

`P-|T|=z-t+kappa`.

Consequently,

`S-q>=z-t+kappa>=z-t`.

## Model card

| Field | Value |
|---|---|
| Computational model | One acyclic Boolean parent circuit; two complete prefix restrictions; active residual functions grouped by prefix-dependent parent label |
| Uniform/non-uniform | Fully non-uniform semantic trace classification; no representative assignment |
| Circuit size | Exact identity `P-|T|=z-t+kappa` and lower bound `S-q>=z-t+kappa` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one in the intended application |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite set union and integer counting only |
| Asymptotic quantifiers | Every finite parent circuit, designated prefix block, and pair of complete prefix restrictions |
| Regime | Worst-case exact multi-output circuit computation |

## Proof

Among the `P` dependent labels, `z` contribute zero within-label classes, `t`
contribute two, and the remaining `P-z-t` contribute one. Therefore

`sum_v |B_v|=0z+2t+(P-z-t)=P-z+t`.

By the definition of `kappa`,

`|T|=P-z+t-kappa`,

which rearranges to the identity. LEMMA-023 gives `S-q>=P-|T|`, and
`kappa>=0` because the size of a union is at most the sum of the set sizes.
QED.

## Scope

Prefix dependence by itself favors neither side. A label may split into two
active functions and contribute `-1`; cross-label collisions may compensate,
but are not automatic. GATE-004L asks for a SAT-specific positive average of
the conservative representative-free score `z-t`.

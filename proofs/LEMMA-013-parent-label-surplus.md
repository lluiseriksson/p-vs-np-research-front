# LEMMA-013 — parent-label surplus normal form

**Label: PROVED**

## Statement

Let an `S`-gate parent circuit be restricted in two ways and semantically
quotiented jointly. After removing constants, free-input residuals, and dead
gates, let the `q_J` surviving gates represent the equivalence classes of
active residual gate functions across the two copies.

For each surviving class, choose one original parent-gate label appearing in
that class. For parent label `v`, let `r_v` be the number of classes assigned
to it. Then `r_v in {0,1,2}`. Define

`d = |{v:r_v=0}|`,

`t = |{v:r_v=2}|`.

Then

`S-q_J = d-t`.

Consequently `q_J<=S-L` iff `d>=t+L`. A parent gate whose two residual
functions are identical can never contribute to `t`; every split label counted
by `t` must have different residual functions under the two restrictions.

## Model card

| Field | Value |
|---|---|
| Computational model | Two restricted copies of an acyclic Boolean circuit; exact semantic quotient and residual-function classes |
| Uniform/non-uniform | Fully non-uniform semantic classification; representative choice arbitrary but fixed |
| Circuit size | Exact identity `S-q_J=d-t` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one in the intended application |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Integer counting only; no algebraic computation model |
| Asymptotic quantifiers | Every finite parent circuit, every two restrictions, every representative assignment |
| Regime | Worst-case exact multi-output circuit computation |

## Proof

Every residual class contains at least one of the two copies of some parent
gate. Assigning a class to a label appearing in it is therefore possible. A
parent label has only two copies, so it can occur in, and be assigned, at most
two distinct classes. Hence `r_v in {0,1,2}`.

There are `d` labels assigned zero classes, `t` assigned two, and
`S-d-t` assigned one. Since each surviving class is assigned exactly once,

`q_J = sum_v r_v = 0*d+2t+(S-d-t)=S-d+t`.

Rearranging gives the identity and the threshold equivalence. If the two
residual functions of label `v` are identical, its two copies belong to at
most one active equivalence class; therefore `r_v<=1` and it cannot be counted
by `t`. QED.

## Interpretation

One represented class per parent label is the zero baseline. A disappeared
label (`r_v=0`) contributes one unit of genuine compression; a label whose two
copies survive as separately represented classes (`r_v=2`) cancels one such
unit. Cross-label collisions can change which label represents a class, but
the signed total `d-t` is independent of the bookkeeping because it always
equals `S-q_J`.

For GATE-004G the exact target is

`d-t >= B n^delta+1`.

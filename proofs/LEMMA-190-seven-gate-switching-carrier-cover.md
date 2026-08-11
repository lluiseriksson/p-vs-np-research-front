# LEMMA-190 — at `W=1` the switching carrier has at most seven gates

**Label: PROVED**

Assume the active branch and an extremal tuple with `W=1`. Let

`H=H_{01,11}`

be the canonical Boolean-difference carrier from LEMMA-187, and let `n=NOT h`
be the earliest switching mixed NOT. Then

`2 <= |H| <= 7`.

Moreover every gate of `H` other than `n` belongs to

`E_00 union E_01 union E_11`,

where each `E_s` is the two-element binary deletion set for code `s`. If
`|H|=7`, the three sets are pairwise disjoint, every one of their six members
lies in `H`, and their union is exactly `H minus {n}`.

## Proof

The gate `n` lies in `H` because `n_01!=n_11`. Since negation is injective,
its input satisfies `h_01!=h_11`, so the binary gate `h` also lies in `H` and
is distinct from `n`. This gives the lower bound two.

At `W=1`, `n` is the unique satisfying-signature-misaligned gate in the
three-way common backbone. Every other member of `H` is also misaligned, so it
must lie outside that backbone. By LEMMA-188, the complement of the common
backbone is precisely the union of the three two-element eliminated sets.
That union has size at most six, proving `|H|-1<=6`.

If equality holds, all six available deletion incidences must cover six
distinct members of `H minus {n}`. Hence no deletion lies outside `H`, no gate
is deleted under two codes, and the three pairs are disjoint.

The lemma does not classify which directed carrier topologies or Boolean
cofactor labels realize these incidence patterns.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted switching plateau parent at `W=1` with three pruning maps |
| Uniform/non-uniform | Every individual finite non-uniform operational tuple at the stated floor case |
| Circuit size | Canonical `01/11` carrier has between two and seven gates; equality rigidly uses all six deletion slots |
| Circuit depth | Unrestricted ambient circuit; carrier depth at most its seven vertices |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean-difference carrier plus finite set-cover counting |
| Asymptotic quantifiers | Every active `W=1` extremal parent and every associated satisfying pruning triple |
| Regime | Exact worst-case bounded-carrier theorem; not a topology classification, SAT lower bound, or terminal result |

# LEMMA-189 — the switching branch forces common-backbone misalignment

**Label: PROVED**

For a plateau parent `C`, let

`M(C)=#{g : not (g_00=g_01=g_11)}`,

where `g` ranges over parent gates. For any triple of satisfying minimum
prunings, let `W` be the number of such gates that survive all three prunings.
Then

`max(0,M(C)-6) <= W <= M(C)`.

In the active satisfying-signature switching branch of LEMMA-180,

`W>=1`

for every pruning triple.

## Proof

Let `E_00,E_01,E_11` be the two-element eliminated sets from LEMMA-188. The
common physical backbone is the complement of their union. At most six parent
gates lie outside it. Intersecting the `M(C)` misaligned gates with that
backbone therefore removes at most six of them, giving the displayed bounds.

In the switching branch, choose the earliest mixed NOT `n` from LEMMA-180.
By definition `n_01!=n_11`, so `n` is satisfying-signature misaligned.
LEMMA-178 preserves every parent NOT under each satisfying restriction;
hence `n` belongs to the three-way physical backbone for every pruning triple
and contributes one to `W`.

This proves a positive floor only. It supplies no rewrite lowering `W`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted switching-branch plateau parent with three minimum pruning maps |
| Uniform/non-uniform | Every individual finite non-uniform operational parent and pruning triple |
| Circuit size | At most six misaligned gates can be excluded from the common backbone; `W>=1` in the switching branch |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite set counting and Boolean cofactor inequality |
| Asymptotic quantifiers | Every active switching plateau parent and every valid triple of satisfying minimum prunings |
| Regime | Exact worst-case misalignment floor; not a descent theorem, SAT lower bound, or terminal result |

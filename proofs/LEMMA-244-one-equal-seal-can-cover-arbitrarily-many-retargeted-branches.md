# LEMMA-244 — one equal seal can cover arbitrarily many retargeted branches

**Label: PROVED**

For every `k>=3` there is a pair of finite constant-free named AND/OR/NOT
circuits with `k` independent parent-live term gates and a cyclically
retargeted comb such that:

1. every proper named comb prefix has different old/new Boolean functions;
2. the final structurally changed comb gate has equal old/new function;
3. the first structurally unchanged downstream gate is independently equal;
4. that one gate is a path-complete nonoutput cut for every retargeting-to-
   output path; and
5. it is the only structurally unchanged nonoutput gate available on those
   paths after the changed comb.

Thus one independently equal physical seal can cover arbitrarily many changed
branches while retaining cut capacity one.

## Construction

Use raw pairs `(x_i,y_i)` and a raw signal `w`, and put

```text
p_i = x_i AND y_i.
```

Both circuits use named comb gates `r_2,...,r_k`. The old circuit feeds them
in order `(p_1,p_2,...,p_k)`; the new circuit uses the cyclic order
`(p_2,p_3,...,p_k,p_1)`. In each circuit the first comb gate ORs its first two
terms and every later `r_j` ORs `r_{j-1}` with the next term. Finally both use

```text
s = NOT r_k,
F = s AND w.
```

The named gates `p_i,s,F` have the same operations and incoming vertices in
both circuits. Every `r_j` belongs to the structural-change set because its
incoming term attachment differs.

## Proof

For `2<=j<k`, old `r_j` is the OR of `{p_1,...,p_j}`, while new `r_j` is the
OR of `{p_2,...,p_{j+1}}`. Set `p_1=1` and all other terms zero; the old prefix
is one and the new prefix zero. These term values are realizable with the
independent raw pairs. At `j=k`, both functions are the OR of all `k` terms.

Although `r_k` has equal functions, it remains structurally changed and so
cannot itself be the LEMMA-222 cut. The next gate `s` has the same named input
and operation in both circuits, and equality of `r_k` independently proves
equality of `s`. Every path from a changed `r_j` to `F` passes through `s`,
while `s` is neither changed nor the output. After the changed comb, the only
nonoutput named gate is `s`; the next gate is the output `F`. Hence `{s}` is
the unique available structurally unchanged nonoutput cut in that suffix.

Every term is parent-live: with `w=1`, make one `p_i=1` and all other terms
zero; changing that term flips `F` from one to zero. The construction is
deliberately nonminimal and is not a plateau endpoint.

## Model card

| Field | Value |
|---|---|
| Computational model | Pair of finite constant-free named AND/OR/NOT DAGs with cyclic comb retargeting and one common equal seal |
| Uniform/non-uniform | Uniform construction for every `k>=3`; each circuit pair finite and non-uniform |
| Circuit size | `k` common term gates, `k-1` structurally changed comb gates, one seal, and one output gate |
| Circuit depth | Comb depth linear in `k` |
| Fan-in | AND/OR two; NOT one; fanout one in the displayed comb and seal suffix |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean prefix functions, named structural changes, and directed cuts |
| Asymptotic quantifiers | Every `k>=3`, proper prefix, term, retargeting path, and raw assignment |
| Regime | Exact shared-seal diagnostic; not minimum endpoint realizability, SAT lower bound, or terminal result |

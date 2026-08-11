# LEMMA-231 — oriented loss unions leave common support gates above 4 or 6

**Label: PROVED**

At the size-three switching endpoint, let `X` be any finite set of physical
binary gates on a marked swap-cycle support, and let
`L_00,L_01,L_11` be the exact physical gate-loss sets of the satisfying
minors. Then:

```text
|X minus (L_00 union L_01 union L_11)| >= |X|-4   in AND→OR,
|X minus (L_00 union L_01 union L_11)| >= |X|-6   in OR→AND.
```

Every gate on the left is a named physical gate present in all three minors.
Consequently, a marked support of more than four physical gates in AND→OR, or
more than six in OR→AND, cannot be fully covered by satisfying losses.

## Proof

In AND→OR, LEMMA-193 gives `L_00=L_01={g,h}` and `|L_11|=2`, so the complete
union has cardinality at most four. In OR→AND,
`L_11={g,h}` and both remaining loss sets have size two, so the union has
cardinality at most six. Intersecting either union with `X` cannot increase
its size. Subtract from `|X|`.

This is a survival statement for physical gate identities, not for incident
literal edges: contractions adjacent to a surviving gate may change its edge
representative. Nor does common survival make the gate a free host or prove a
potential descent.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined size-three minimum unrestricted AND/OR/NOT plateau with exact physical satisfying-loss sets and a marked gate support |
| Uniform/non-uniform | Every finite non-uniform hypothetical endpoint and every finite marked physical gate set |
| Circuit size | Parent `K+2`; exact two-gate loss sets; total oriented union at most four or six |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Physical gate-set unions; cycle interpretation over `F_2` is external to the count |
| Asymptotic quantifiers | Every nonconstant base, endpoint, orientation, and finite marked support `X` |
| Regime | Exact worst-case common-gate threshold; not common-edge survival, host availability, SAT lower bound, or terminal result |

# LEMMA-221 — the canonical difference frontier is an a posteriori output test

**Label: PROVED**

Let `C` and `C'` be finite acyclic AND/OR/NOT circuits on the same raw inputs,
with the same named output `o`. They may differ in gate operations and incoming
edges. Let

```text
Delta = {v : the Boolean function at v differs between C and C'}.
```

Use the union of the two directed edge sets and define the exterior boundary

```text
S_Delta = {s notin Delta : some edge d -> s has d in Delta}.
```

Then every member of `S_Delta` is functionally sealed, by definition, and

```text
o notin Delta  iff  C and C' compute the same parent function.
```

Consequently, when the parent is preserved, the full semantic difference
region has a sealed exterior boundary (possibly empty). When it is not
preserved, the output itself belongs to the difference region.

## Proof

Membership outside `Delta` means exact equality of the two Boolean gate
functions. Hence every `s in S_Delta` is sealed. The named output belongs to
`Delta` exactly when its two computed Boolean functions differ, which proves
the displayed equivalence.

If every structural change is confined to a set `R`, every member of `Delta`
is forward reachable from `R` in the union graph. Indeed, take an earliest
counterexample in a topological order of `C`. It is not in `R`, so its
operation and incoming vertices agree in both circuits. Any changed
predecessor would be an earlier counterexample: if it were reachable from
`R`, so would the current gate. Thus all predecessor functions agree, forcing
the current function to agree, a contradiction.
Thus `Delta` is the canonical complete forward semantic change region.

This is only an a posteriori characterization. Constructing `Delta`, proving
that `o` is outside it, or declaring its exterior boundary sealed can require
the very parent-function equality that a host rewrite is intended to prove.
Moreover, `Delta` omits any structurally retargeted gate whose function happens
to remain equal, so it need not satisfy LEMMA-220's physical-region premise.
The lemma supplies no independent seal certificate and no size payment.

## Model card

| Field | Value |
|---|---|
| Computational model | Pair of finite constant-free unrestricted AND/OR/NOT DAGs with named corresponding vertices and output |
| Uniform/non-uniform | Every finite non-uniform circuit pair; optional structural-change set contains every changed operation or incoming list |
| Circuit size | Arbitrary finite sizes on a common named vertex set; no cost conclusion |
| Circuit depth | Unrestricted finite acyclic depth |
| Fan-in | AND/OR two; NOT one; fanout unrestricted; union of old and new edges used for the boundary |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean gate functions and finite DAG reachability |
| Asymptotic quantifiers | Every finite circuit pair, every vertex, and every supplied structural-change set |
| Regime | Exact worst-case semantic characterization; not an independent certificate, SAT lower bound, or terminal result |

# LEMMA-222 — an independently equal structural cut preserves the output

**Label: PROVED**

Let `C,C'` be finite acyclic AND/OR/NOT circuits on the same raw inputs and
named gate set, with common output `o`. Let `R` contain every gate whose
operation or incoming-vertex list differs between the two circuits. Let `S`
be disjoint from `R union {o}` and suppose:

1. every directed path from a gate in `R` to `o` in the union of the two edge
   sets contains a vertex of `S`; and
2. every `s in S` computes the same Boolean function in `C` and `C'`.

Then `C` and `C'` compute the same output function.

## Proof

Let `U` be the gates from which `o` is reachable in the union graph along a
path containing no vertex of `S`. The cut hypothesis gives `U cap R=empty`.
For every `v in U`, its operation and incoming list therefore agree in `C`
and `C'`.

Induct over `U` in a topological order of `C`. An input of `v` is either a raw
input, a member of `S`, or another member of `U`: in the last case prepend its
edge to the `S`-avoiding path from `v` to `o`. Raw inputs agree by convention,
members of `S` agree by hypothesis, and earlier members of `U` agree by
induction. Applying the same operation at `v` proves equality. Since `o in U`,
the two output functions agree.

The lemma is noncircular only when item 2 is established independently of the
output equality. It asserts neither existence nor physical payment for `S`.

## Model card

| Field | Value |
|---|---|
| Computational model | Pair of finite constant-free unrestricted AND/OR/NOT DAGs with a structural-change set and directed vertex cut |
| Uniform/non-uniform | Every finite non-uniform circuit pair satisfying the stated cut premises |
| Circuit size | Same arbitrary finite named gate set; no size or saving conclusion |
| Circuit depth | Unrestricted finite acyclic depth; union graph need not be acyclic |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and both edge sets audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean gate functions, directed reachability, and topological induction |
| Asymptotic quantifiers | Every finite circuit pair, complete structural-change set, cut, raw assignment, and output |
| Regime | Exact worst-case sufficient interface; not cut existence, SAT lower bound, or terminal result |

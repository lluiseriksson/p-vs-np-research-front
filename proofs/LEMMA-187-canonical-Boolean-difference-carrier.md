# LEMMA-187 — Boolean-difference carriers are canonical

**Label: PROVED**

Fix an AND/OR/NOT DAG `C` and two restrictions `alpha,beta` of the same raw
inputs. For every gate `g`, let `g_alpha,g_beta` be the resulting Boolean
functions of the unrestricted inputs. Define the **difference carrier**
`H_{alpha,beta}` to contain exactly the noninput gates satisfying

`g_alpha != g_beta`,

together with edges between such gates and source markers for raw inputs on
which `alpha,beta` differ.

Then:

1. every gate in the carrier has a directed carrier path from a differing raw
   source;
2. if the output cofactors are equal, every carrier-to-output path has a first
   gate outside the carrier; and
3. every such first boundary gate is binary.

The carrier and its boundary are determined by gate functions, independently
of any constant-propagation or contraction order.

## Proof

If a noninput gate has different cofactors, at least one predecessor has
different cofactors. Otherwise applying the same gate operation to equal
predecessor functions would give equal outputs. Repeating this argument
backwards in the finite DAG reaches a raw input fixed differently by the two
restrictions, proving part 1.

When the output cofactors agree, the output is outside the carrier. Every path
from a carrier gate to the output therefore crosses a first boundary gate.
Its path predecessor has unequal cofactors and the boundary gate has equal
cofactors. A NOT cannot perform this transition because negation is injective
on Boolean functions. Hence the boundary gate is AND or OR.

No pruning choices enter the definition or proof. The lemma does not say that
carrier gates must be deleted after either restriction.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite unrestricted AND/OR/NOT DAG under two fixed input restrictions |
| Uniform/non-uniform | Every individual finite non-uniform circuit and restriction pair |
| Circuit size | No bound; exact canonical carrier and binary-boundary statement |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Equality and symmetric difference of Boolean cofactor functions |
| Asymptotic quantifiers | Every finite circuit, every pair of restrictions, and every carrier-to-output path |
| Regime | Exact worst-case support theorem; not an elimination lower bound, SAT lower bound, or terminal result |

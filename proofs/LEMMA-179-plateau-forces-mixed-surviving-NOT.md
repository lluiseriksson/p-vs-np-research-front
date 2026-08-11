# LEMMA-179 — a two-gate plateau forces a mixed surviving NOT

**Label: PROVED**

Assume the notation and two-gate equality `C(F)=C(A)+2` of LEMMA-178. Every
minimum parent contains a NOT gate `n=NOT h` whose function depends
essentially on `u`, and every such gate has these properties:

1. `n` survives as a nonconstant gate under each satisfying pair code
   `00`, `01`, and `11`;
2. `n` depends essentially on base variables as well as on the fresh pair;
3. its input `h` is a pair-sensitive binary gate, not a raw input or a NOT;
4. neither input wire of `h` comes directly from raw `u` or raw `t`; and
5. at least one predecessor gate of `h` is itself pair-sensitive.

Thus the negative `u` polarity in any plateau is mixed into the base before
the surviving NOT. A pure `NOT u` attachment is impossible.

## A pair-sensitive NOT is necessary

If every NOT-gate function were independent of `u`, then the input of each
NOT would also be independent of `u`, because negation is injective. Treating
all such NOT outputs and all other `u`-independent signals as auxiliary
inputs, the remaining AND/OR circuit would be monotone nondecreasing in raw
`u`. This contradicts the restriction `A=1,t=0`, under which `F` decreases
from one to zero as `u` changes from zero to one.

## Equality forces survival and mixing

LEMMA-178 proves that every satisfying restriction preserves the total NOT
count. Restriction and pruning create no new NOT gates, so no parent NOT is
deleted. In particular every `u`-sensitive NOT `n` survives all three codes
and is nonconstant in each pruned output cone.

It cannot depend only on `u,t`, because fixing a full pair code would make it
constant. Hence it also depends on the base. Its input `h` is pair-sensitive.
It is not raw `u` or `t`, and it is not a base input. It cannot be another
NOT gate: replacing `NOT(NOT k)` by `k` at all uses of `n` would delete `n`
from a minimum circuit. Therefore `h` is binary.

If one input of `h` were raw `u`, then an AND gate would be constant at the
codes with `u=0`, while an OR gate would be constant at code `11`. If one
input were raw `t`, AND would be constant at `00`, while OR would be constant
at `01` and `11`. In each case `n` would also be constant, contradicting its
survival. Thus both inputs of `h` are internal or base signals. Since `h`
depends on the pair, at least one internal predecessor gate is pair-sensitive.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT circuits at an exact two-gate fresh-implication plateau |
| Uniform/non-uniform | Every finite non-uniform nonconstant base and every minimum plateau parent |
| Circuit size | Parent `C(F)=C(A)+2`; every NOT preserved under all three satisfying restrictions |
| Circuit depth | Unrestricted; proved mixed path has at least one internal predecessor before a binary-to-NOT edge |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean monotonicity, cofactors, and restriction survival; no algebraic computation |
| Asymptotic quantifiers | Every nonconstant finite `A`, every fresh implication pair, every minimum plateau circuit, and every `u`-sensitive NOT in it |
| Regime | Exact equality-case polarity localization; not an exclusion of the plateau, SAT lower bound, or terminal result |

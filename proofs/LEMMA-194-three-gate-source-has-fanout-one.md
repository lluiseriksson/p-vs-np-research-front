# LEMMA-194 — the source gate of a three-gate carrier has fanout one

**Label: PROVED**

Under LEMMA-193, the carrier source gate `g` has exactly one physical consumer
in the parent output cone: `h`.

## Proof

In the AND→OR case, satisfying codes `00,01` fix `g=0` and already eliminate
exactly `g,h`. Let `b!=h` be any additional direct consumer of `g`. If `b` is
AND, the fixed zero makes it constant; if OR, it becomes its other input; if
NOT, it becomes constant one. Constant propagation therefore eliminates `b`
in addition to `g,h`, contradicting the exact two-gate loss of LEMMA-178.

In the OR→AND case, code `11` fixes `g=1`. An AND consumer becomes its other
input, an OR consumer becomes constant one, and a NOT consumer becomes zero.
Again every additional consumer is eliminated and would be a third loss.

The edge `g->h` exists by LEMMA-193, so the fanout is exactly one. The lemma
does not bound the fanout of `h` or `n`.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT plateau with a three-gate alternating switching carrier |
| Uniform/non-uniform | Every finite non-uniform hypothetical parent in the size-three case |
| Circuit size | Parent `K+2`; neutral code has exact deletion set `{g,h}`; a third consumer is forbidden |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; `g` fanout exactly one, other fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Constant propagation and exact gate-loss counting |
| Asymptotic quantifiers | Every nonconstant base and hypothetical minimum size-three-carrier parent |
| Regime | Exact worst-case fanout localization; not private-cone existence, plateau exclusion, SAT lower bound, or terminal result |

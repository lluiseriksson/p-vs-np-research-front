# LEMMA-101 — a length bound alone does not justify the `B..B+3` gap reduction

**Label: PROVED**

For four-aligned binary blocks of maximum length `B`, replacing every selected-
coordinate gap at least `B` by its congruent representative in
`{B,B+1,B+2,B+3}` need not preserve the masks obtainable by nonoverlapping
blocks.

Take `B=8` and the two length-eight blocks

`A=01111111`, `C=11111110`.

Every placement starts at a multiple of four. On the selected coordinates
`(8,23)`, place `A` at 8 and `C` at 16. Their half-open intervals `[8,16)` and
`[16,24)` are nonoverlapping and their union has zero mask 3. The gap is 15.

The congruent representative in `{8,9,10,11}` is 11, giving coordinates
`(8,19)`. To zero coordinate 8, the only relevant aligned placement is `A` at
8. To zero coordinate 19, the only relevant aligned placement is `C` at 12.
The intervals `[8,16)` and `[12,20)` overlap. Neither block has another aligned
placement zeroing either selected coordinate, and no single block zeros both.
Thus mask 3 is absent after the proposed reduction.

`verification/gap_reduction.py` enumerates these two finite placement systems
independently of the SAT-specific auditors. This lemma refutes only the stated
geometric reduction rule. It does not prove that any particular SAT neutral
alphabet lacks a witness on an untested type.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite aligned binary interval placements and zero-mask union |
| Uniform/non-uniform | One explicit finite alphabet; no circuit selected |
| Circuit size | No circuit claim |
| Circuit depth | Irrelevant |
| Fan-in | Irrelevant to the interval counterexample |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite Boolean incidence only |
| Asymptotic quantifiers | Universal reduction claim falsified by one exact instance with `B=8` |
| Regime | Structural counterexample to a proof step; not a SAT lower bound or terminal result |

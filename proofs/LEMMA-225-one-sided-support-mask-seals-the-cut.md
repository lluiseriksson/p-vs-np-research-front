# LEMMA-225 — a one-sided support mask independently seals the cut

**Label: PROVED**

Let `A,A',B` be Boolean functions of fresh inputs `(u,t)` and any base tuple
`x`. Assume `B` is unchanged and

```text
A_00=A'_00,  A_01=A'_01,  A_11=A'_11.
```

Write `d=A_10 xor A'_10`. Then:

1. `A OR B = A' OR B` on all four codes if and only if
   `d AND NOT B_10=0`;
2. `A AND B = A' AND B` on all four codes if and only if
   `d AND B_10=0`.

These are independent full-function certificates for the OR or AND output;
they use the named cofactors and do not assume equality at the parent output.

## Proof

The three satisfying output cofactors agree because `A=A'` there and `B` is
common. LEMMA-224 gives the code-`10` OR defect as
`d AND NOT B_10` and the AND defect as `d AND B_10`. The full functions agree
exactly when this remaining cofactor defect is zero. LEMMA-223 then gives
equality on all four codes.

The mask is a semantic certificate, not an extra physical resource. The lemma
does not make the output gate or the gate computing `B` freely retargetable.

## Model card

| Field | Value |
|---|---|
| Computational model | Paired unrestricted AND/OR/NOT cut interfaces with one changed and one common input function |
| Uniform/non-uniform | Every finite non-uniform function triple satisfying the three-code premise |
| Circuit size | One binary cut gate; no host-count or size conclusion |
| Circuit depth | One local layer inside unrestricted ambient depth |
| Fan-in | AND/OR two; NOT one allowed in the ambient functions; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors and analytical difference over `F_2` |
| Asymptotic quantifiers | Every base arity, every assignment, every function triple, and both binary orientations |
| Regime | Exact worst-case independent seal certificate; not a physical payment, SAT lower bound, or terminal result |

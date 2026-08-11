# GATE-004CN — exclude the alternating three-gate carrier

**Label: EXPLORATORY**

Use the exact alternatives of LEMMA-193. In the AND→OR case both `00` and
`01` spend their entire deletion budget on the same physical pair `{g,h}`;
in the OR→AND case `11` spends its entire budget there.

## Falsifiable theorem

For every such minimum parent, either:

1. all live exits from `g,h` permit a function- and size-preserving uncrossing
   that lowers the extremal carrier/fanout potential;
2. some downstream consumer becomes constant or an identity in a neutral
   satisfying code, forcing a third binary deletion;
3. a shared exit yields the LEMMA-183 private certificate or deletion of a
   non-bridge edge of `gamma`; or
4. the deletion maps for the neutral code(s) and the remaining satisfying code
   cannot realize the full cofactor equality `F_00=F_01=F_11=A`.

The audit must include every fanout edge of both `g` and `h`. The local gadgets
in GATE-004CM-SIZE-THREE-LOCAL-ONLY show that the carrier chain itself is not
enough.

LEMMA-194 now proves `fanout(g)=1`: every extra consumer would exceed the
neutral deletion budget. A nonconstant aligned boundary shows that `h` can
still be shared, so source fanout one alone is `NO-GO`. GATE-004CO is the
active classification of all such shared exits from `h`.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted switching plateau parent at `W=1` with a three-gate alternating carrier |
| Uniform/non-uniform | Every finite non-uniform operational size-three tuple and valid pruning triple |
| Circuit size | Parent `K+2`; specified neutral codes already delete exactly `g,h` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; every fanout exit audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and every hypothetical minimum size-three-carrier parent |
| Regime | Exact worst-case size-three exclusion gate; not a SAT lower bound or terminal result |

# GATE-004CO — classify shared exits from `h`

**Label: EXPLORATORY**

By LEMMA-194, `g` is private to `h`. Every additional live exit from `h`
beyond `n` must reach a first binary `01/11` equal-cofactor boundary, because
the carrier has only `g,h,n`.

## Falsifiable theorem

For every minimum size-three-carrier parent, either:

1. `h` has no exit beyond `n` and the resulting two-gate predecessor cone
   gives a size-preserving extremal descent or LEMMA-183 certificate;
2. some first shared boundary is eliminated in a neutral code, forcing a third
   gate loss;
3. every surviving shared boundary is an aligned mask whose complete cofactor
   identities permit an uncrossing of `g,h` without increasing size; or
4. two shared routes create a cycle for which a satisfying pruning must delete
   a non-bridge edge.

The proof must cover nonconstant aligned masks such as
`(u AND x OR y) AND NOT x`, which survives the neutral contraction. Counting
the number of exits without their Boolean labels is insufficient.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted plateau at `W=1` with three-gate alternating carrier and all shared `h` exits |
| Uniform/non-uniform | Every finite non-uniform operational size-three tuple |
| Circuit size | Parent `K+2`; neutral deletion budget exhausted by `g,h` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; `g` fanout one, `h` fanout unrestricted and audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean mask identities and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical minimum size-three-carrier parent |
| Regime | Exact worst-case shared-boundary gate; not a SAT lower bound or terminal result |

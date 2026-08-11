# LEMMA-193 — a three-gate switching carrier alternates AND and OR

**Label: PROVED**

Assume a hypothetical minimum two-gate implication plateau in the switching
branch and `H_{01,11}={g,h,n}`, where `n=NOT h` is the earliest
`u`-sensitive NOT. Then the carrier has the directed chain

`u -> g -> h -> n`,

the gates `g,h` are binary, and exactly one of these forms holds, up to input
order:

1. `g=u AND p`, `h=g OR q`; then `E_00=E_01={g,h}`.
2. `g=u OR p`, `h=g AND q`; then `E_11={g,h}`.

Here `p,q` have equal `01/11` cofactors. In each displayed neutral code, `n`
survives rewired to `NOT q_s`, and no other parent gate is eliminated.

## Proof

LEMMA-187 gives a carrier path from the only differing raw source `u` to
`h`. With exactly one carrier gate before `h`, this path is `u->g->h`.
The gate `g` cannot be a NOT, since it is `u`-sensitive and precedes the
earliest such NOT `n`; hence it is binary. Minimality excludes an idempotent
duplicate-input gate, so its other input `p` is outside the carrier and is
`01/11`-aligned. Likewise `h` is binary by LEMMA-179, receives `g`, and its
other effective input `q` is aligned.

If `g=u AND p`, then at `u=0` it is constant zero. Were `h` also AND, `h`
would be zero and `n` one, contradicting LEMMA-179's nonconstant survival of
`n` under satisfying codes `00,01`. Thus `h` is OR and constant propagation
contracts `h` to `q` in both codes, deleting `g,h` and rewiring `n` to
`NOT q_s`.

If `g=u OR p`, then at `u=1` it is constant one. Were `h` also OR, `h` would
be one and `n` zero under satisfying code `11`, the same contradiction. Thus
`h` is AND, and code `11` contracts `h` to `q_11` after deleting `g`.

LEMMA-178 says every satisfying pruning loses exactly two binary gates. The
two forced losses are already `g,h`, so the displayed eliminated sets are
exact and no other parent gate disappears in those codes.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT two-gate plateau with a three-gate `01/11` switching carrier |
| Uniform/non-uniform | Every finite non-uniform hypothetical parent in this carrier-size case |
| Circuit size | Parent `K+2`; neutral satisfying codes delete exactly the two carrier binary gates `g,h` |
| Circuit depth | Unrestricted; carrier chain has three noninput vertices |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors, constant propagation, and exact gate-loss counting |
| Asymptotic quantifiers | Every nonconstant base and every hypothetical minimum switching parent with carrier size three |
| Regime | Exact worst-case topology and deletion classification; not exclusion of this case, SAT lower bound, or terminal result |

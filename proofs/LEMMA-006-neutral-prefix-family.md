# LEMMA-006 — exact neutral-prefix family

**Label: PROVED**

## Statement

For every integer `k>=0`, SAT-gamma has `k+1` distinct fixed prefixes
`P_{k,l}`, `0<=l<=k`, each of length `12k`, such that for every binary string
`y`:

`P_{k,l} y` is valid iff `y` is valid,

and, when valid, the two strings have the same satisfiability value. Moreover,

`Hamming(P_{k,l},P_{k,j}) = 6|l-j|`.

After reading `P_{k,l}`, the prefix parser has `6(k-l)` pending NOT frames and
`l` pending AND frames whose left child is the fixed tautology `T`; the only
unread obligation is one complete formula occupying the entire suffix.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact SAT-gamma prefix parser and coordinate restrictions |
| Uniform/non-uniform | Uniform construction of every prefix; later circuit choice may be non-uniform |
| Circuit size | No circuit-size conclusion |
| Circuit depth | Unrestricted in later circuit application |
| Fan-in | Encoded formula AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every `k>=0`, every `0<=l,j<=k`, and every binary suffix `y` |
| Regime | Exact total-language validity and satisfiability; malformed suffixes reject |

## Proof

Let `U=1111`, the encoding of two pending NOT nodes, and let `W=01T`, the
prefix for an AND node whose first child is the ten-bit tautology `T`. Thus
`|U|=4` and `|W|=12`. Define

`P_{k,l}=U^{3(k-l)} W^l`.

Its length is `12(k-l)+12l=12k`. Applying the pending frames to a suffix `y`
gives `3(k-l)` double negations outside `l` nested conjunctions with `T`.
ENC-003 therefore proves the validity and satisfiability identities. It also
gives the displayed parser stack: every copy of `U` contributes two pending
NOT frames, and every copy of `W` contributes one pending AND right-child
obligation after its complete left child.

For adjacent indices, remove the common prefix and suffix. The comparison is
between `U^3`, twelve one bits, and `W`. The word `W=01T` contains exactly six
zero bits, so their Hamming distance is six. For indices differing by `r`, the
same aligned comparison occurs in `r` disjoint twelve-bit blocks, giving
distance `6r`. In particular all prefixes are distinct. QED.

## Scope

Every member induces exactly the same output residual `SAT-gamma_m`. The lemma
does not identify, count, or constrain residual functions at internal gates of
an arbitrary circuit computing the slice.

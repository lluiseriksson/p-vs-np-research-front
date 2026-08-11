# LEMMA-198 — every handoff is a bisensitive neutral survivor

**Label: PROVED**

In a hypothetical minimum size-three-carrier plateau, every direct handoff
`b` depends essentially on both fresh inputs `u,t` and survives as a physical
nonconstant gate in every neutral satisfying pruning identified by LEMMA-193.
Consequently those prunings contain at least the two distinct pair-sensitive
survivors `n,b`.

## Proof

By definition, `b_01=b_11` and `b_00!=b_10`. The latter inequality makes `b`
essentially `u`-dependent. If `b` were independent of `t`, then
`b_00=b_01` and `b_10=b_11`; together with `b_01=b_11` this would give
`b_00=b_10`, a contradiction. Thus `b` also depends essentially on `t`.

LEMMA-193 proves that each neutral satisfying pruning has exact eliminated
set `{g,h}`. Since `b` is a distinct direct consumer outside the carrier, it
is not eliminated. A minimum circuit for the nonconstant base contains no
constant physical gate after propagation, so `b` survives nonconstantly.
LEMMA-179 separately preserves the pair-sensitive NOT `n`, and `b!=n`.

The lemma does not bound the number of handoffs or show that either survivor
can be removed.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT plateau with size-three switching carrier and direct handoffs |
| Uniform/non-uniform | Every finite non-uniform hypothetical parent in this case |
| Circuit size | Parent `K+2`; neutral deletions exactly `{g,h}`; at least two pair-sensitive survivors when a handoff exists |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; handoff fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors and physical survivor sets |
| Asymptotic quantifiers | Every nonconstant base, hypothetical minimum size-three parent, and direct handoff |
| Regime | Exact worst-case sensitivity/survival theorem; not a handoff bound, plateau exclusion, SAT lower bound, or terminal result |

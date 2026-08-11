# LEMMA-199 — at zero handoffs, `n` is the unique `u`-sensitive child of `h`

**Label: PROVED**

Assume the hypothetical minimum size-three-carrier plateau and handoff
potential `Q=0`. Then every direct consumer of `h` other than `n` is globally
independent of raw `u`. Consequently `n` is the unique direct consumer of `h`
whose gate function depends essentially on `u`.

## Proof

Any direct consumer `b!=n` lies outside `H_{01,11}`, because that carrier is
exactly `{g,h,n}`. Hence `b_01=b_11`. Since `Q=0`, no such boundary is a
handoff, so it also lies outside `H_{00,10}` and `b_00=b_10`.

For each fixed value of `t`, the two `u` cofactors are therefore equal. Thus
the Boolean gate function of `b` is independent of `u`. In contrast,
switching gives `n_01!=n_11`, so `n` depends essentially on `u` and is the
unique sensitive child.

The conclusion is semantic. It does not say that the other consumers or the
physical edges from `h` can be removed.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT plateau with size-three switching carrier and zero direct handoffs |
| Uniform/non-uniform | Every finite non-uniform hypothetical parent in the `Q=0` case |
| Circuit size | Parent `K+2`; no new gate-count conclusion |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; `n` is the unique `u`-sensitive child of `h` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactor equality |
| Asymptotic quantifiers | Every nonconstant base and hypothetical minimum size-three parent with `Q=0` |
| Regime | Exact worst-case semantic-fanout theorem; not physical privacy, plateau exclusion, SAT lower bound, or terminal result |

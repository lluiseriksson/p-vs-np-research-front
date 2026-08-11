# GATE-004CS — descend the handoff potential

**Label: EXPLORATORY**

Among minimum size-three-carrier parents at the previous extremal potentials,
minimize `Q`, the number of direct handoffs from `h`. LEMMA-198 makes every
handoff a bisensitive neutral survivor; handoff count alone is unavailable.

## Falsifiable theorem

For every extremal parent with `Q>0`, one of the following holds:

1. a four-code-preserving, same-size rewrite strictly lowers `Q` without
   increasing earlier potentials;
2. the first handoff has a private realization certificate;
3. its neutral survival forces a third binary deletion after all consumers are
   propagated; or
4. its cross-carrier reconvergence forces deletion of a non-bridge edge.

If descent reaches `Q=0`, every direct `h` boundary is aligned on both rows;
that zero-handoff branch must then be analyzed separately. The rewrite must
use minimum cost, not handoff multiplicity or the output table alone.

LEMMA-199 now proves that `n` is the unique `u`-sensitive child at `Q=0`.
Semantic privacy alone is `NO-GO` because an essential base boundary can still
consume `h`. GATE-004CT is the active aligned-mask versus counterflow
classification for this endpoint; descent for `Q>0` remains open.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically extremal minimum unrestricted plateau at `W=1` with size-three carrier |
| Uniform/non-uniform | Every finite non-uniform operational tuple |
| Circuit size | Parent `K+2`; same-size strict `Q` descent or exact contradiction |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; handoff fanout preserved by rewrites |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean signatures, finite potential, and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical extremal minimum size-three parent |
| Regime | Exact worst-case handoff-potential gate; not a SAT lower bound or terminal result |

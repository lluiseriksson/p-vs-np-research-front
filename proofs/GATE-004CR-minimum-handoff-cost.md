# GATE-004CR — charge a cross-carrier handoff in a minimum parent

**Label: EXPLORATORY**

Call a direct boundary `b` a **handoff** when it lies outside `H_{01,11}` but
inside `H_{00,10}`. LEMMA-197 shows that handoffs are compatible with the full
output table in nonminimal circuits.

## Falsifiable theorem

For every minimum size-three-carrier plateau parent containing a handoff,
one of the following holds:

1. the handoff subcone contains removable tautological or duplicate structure,
   yielding a strict size reduction;
2. its neutral-code survival requires a third binary elimination;
3. the first handoff admits a LEMMA-183 private replacement at no greater cost;
4. the `01/11` carrier handing off into the `00/10` carrier creates a named
   reconvergence cycle whose satisfying pruning deletes a non-bridge edge; or
5. all handoffs are absent, reducing GATE-004CQ to boundaries aligned on both
   rows.

The proof must use minimum cost or minor structure. The complete signature
table alone is ruled out by GATE-004CQ-FOUR-CODE-SIGNATURES-ONLY.

LEMMA-198 shows that every handoff is a bisensitive neutral survivor. A
uniform redundant exact-table family has arbitrarily many such handoffs, so
counting them is `NO-GO`. GATE-004CS is the active lexicographic handoff-
potential descent, with a separate zero-handoff branch if descent succeeds.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted plateau at `W=1` with size-three carrier and cross-carrier handoffs |
| Uniform/non-uniform | Every finite non-uniform operational tuple |
| Circuit size | Parent `K+2`; exact two-binary-loss satisfying minors |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; handoff fanout and reconvergence audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four-code Boolean signatures and cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base and hypothetical minimum size-three-carrier parent |
| Regime | Exact worst-case minimum-handoff gate; not a SAT lower bound or terminal result |

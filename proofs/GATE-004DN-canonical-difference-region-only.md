# GATE-004DN-CANONICAL-DIFFERENCE-REGION-ONLY — the canonical seal is circular

**Label: NO-GO**

Scope: after proposing a host rewrite, define its region to be all gates whose
Boolean functions differ, take the first unchanged exterior gates as a sealed
frontier, and use that frontier to prove that the parent is unchanged.

LEMMA-221 shows the circularity exactly. The canonical region excludes the
output if and only if the old and new parent functions are already equal. Its
boundary gates are called unchanged only because their complete Boolean
functions have already been compared. Thus this construction is a valid
a posteriori audit of a separately proved rewrite, but cannot itself supply
the missing parent-preservation proof. It may also omit a physically
retargeted vertex whose function happens to remain equal, so it is not
automatically a valid physical replacement region for LEMMA-220.

The obstruction is logical, not computational: even an unlimited semantic
oracle used to build the canonical region would answer the target equality at
the output as part of the same computation. It does not refute a frontier cut
whose equality is derived independently from local four-code identities,
pruning maps, or an explicit replacement expression.

## Model card

| Field | Value |
|---|---|
| Computational model | Paired finite constant-free unrestricted AND/OR/NOT DAGs under a proposed host rewrite |
| Uniform/non-uniform | Every finite non-uniform circuit pair |
| Circuit size | Arbitrary finite size; no host-saving inference |
| Circuit depth | Unrestricted finite acyclic depth |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and all old/new exits included |
| Randomness | None |
| Advice | None |
| Oracle access | None in the target; the no-go persists even with semantic equality queries |
| Field/algebraic model | Exact Boolean functions and forward difference regions |
| Asymptotic quantifiers | Every proposed rewrite and its complete semantic difference set |
| Regime | Circular-certification no-go; not an endpoint counterexample, SAT lower bound, or terminal result |

# GATE-004DV-BOUNDED-CORE-ENUMERATION-ONLY — ports remain unbounded

**Label: NO-GO**

Scope: after LEMMA-231 bounds a fully covered marked support by four or six
gates, enumerate only that induced core and treat the number and semantics of
external attachments as automatically finite or irrelevant.

LEMMA-233 gives a fixed three-gate marked cyclic core with `m` exterior ports
for every `m`. Each port has an unmasked selector slice and neither incoming
signal can replace it without changing the parent. Hence bounded core size
does not bound fanout, port count, downstream contexts, or replacement cost.

The family is nonminimal and not an endpoint. It does not refute a theorem
that quotients semantically equivalent ports or charges inequivalent ones by
minimum cost. It refutes finite core-only enumeration without such a theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Uniform constant-free unrestricted AND/OR marked-core family with selector-isolated exterior ports |
| Uniform/non-uniform | Every `m>=1`; each diagnostic circuit finite and non-uniform |
| Circuit size | `3m+4`; core size three and port count `m` |
| Circuit depth | Unrestricted output-tree depth |
| Fan-in | AND/OR two; NOT unused; marked core fanout unbounded with `m` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean interfaces and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `m>=1`, assignment, and port index |
| Regime | Core-only-enumeration no-go; not endpoint counterexample, SAT lower bound, or terminal result |

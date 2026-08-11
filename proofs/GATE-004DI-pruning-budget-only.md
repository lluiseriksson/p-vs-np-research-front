# GATE-004DI-PRUNING-BUDGET-ONLY — satisfying losses cannot pay unbounded deficit

**Label: NO-GO**

The three exact satisfying-pruning loss sets cannot by themselves pay an
arbitrary private formula deficit. LEMMA-216 caps their deduplicated physical
union at six gates, before subtracting carrier losses or other prior charges.
Therefore every proposed injection of `D_b` distinct deficit units solely into
these loss sets requires `D_b<=6`.

The NG-158 local family has `D_b=n-2`, unbounded with `n`, while retaining the
same exact comparable boundary identities and a one-gate minimum joint
cofactor saving. It is nonminimal and is not an exact plateau, so it does not
show that an endpoint can have `D_b>6`. It shows that local cofactor semantics,
fanout, reachability, and joint-saving data do not supply the missing bound.

Hence pruning-only accounting is closed unless one first proves a genuine
minimum-endpoint theorem bounding `D_b` by the uncharged union size. No loss
may be counted once per minor when it is the same physical gate.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact-plateau unrestricted AND/OR/NOT loss-set accounting plus the explicit nonminimal NG-158 family |
| Uniform/non-uniform | Every finite endpoint for the six-gate cap; every `n>=3` for the diagnostic family |
| Circuit size | Three exact two-gate loss sets give at most six distinct resources; diagnostic deficit `n-2` |
| Circuit depth | Unrestricted endpoint; diagnostic family depth linear in `n` |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Physical set union, exact Boolean cofactors, and joint circuit size |
| Asymptotic quantifiers | Every triple of exact loss sets and every diagnostic `n>=3` |
| Regime | Pruning-budget-only no-go; not an endpoint counterexample, SAT lower bound, or terminal result |

# GATE-004CW-SEMANTIC-ERASURE-ONLY — an abstract signal is not a free DAG rewrite

**Label: NO-GO**

LEMMA-204 specifies a function `r^dagger` that erases the `00/10`
counterflow at one edge while preserving the boundary truth table. It does not
provide a same-size AND/OR/NOT realization.

Computing `r_00 AND r_10` or `r_00 OR r_10` from a circuit for `r` may require
duplicating cofactor cones and adding selectors. Moreover `r` can have other
consumers whose functions must remain unchanged. Replacing `r` globally can
damage those consumers, while replacing only the edge into `b` can require a
private copy of the entire realization. No bound on that cost follows from
the cofactor identity.

This is the same circuit-versus-function distinction enforced elsewhere in
the repository, now on the only possible counterflow row. A valid descent
must exhibit an AND/OR/NOT DAG rewrite, pay for duplication from gates that
are provably freed, or derive an exact satisfying-code resource loss.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT DAG audited against an abstract counterflow-edge substitution |
| Uniform/non-uniform | Every finite non-uniform endpoint parent; no uniform rewrite asserted |
| Circuit size | No size bound follows; cofactor duplication and selector cost are uncontrolled |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and explicitly audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean cofactors and lattice meet/join only |
| Asymptotic quantifiers | Every proposed use of LEMMA-204 without an explicit basis-level realization |
| Regime | Semantic-erasure-only no-go; not a minimum counterexample, SAT lower bound, or terminal result |

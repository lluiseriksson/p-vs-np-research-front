# GATE-003 — Quantifier-stable unrestricted lower-bound family

**Label: EXPLORATORY**

## Falsifiable theorem

There exist a uniformly indexed family `(L_j)`, one uniform nondeterministic
verifier, and unary-polynomial-time computable exponents `a(j), b(j)` satisfying
every hypothesis of GATE-002, including

`limsup_j b(j)/a(j) = infinity`,

for unrestricted, unbounded-depth, fan-in-two Boolean circuits without advice
or oracles on the verifier side.

The full model card is recorded as `GATE-003` in
`verification/claims.json` and `docs/vertical-map.md`.

## Initial attack

The first candidate input is the Murray-Williams fixed-exponent NP transfer.
Substitution gives ratio `epsilon/(c j^3)`, so it fails the gate
quantitatively. Medium-uniform diagonalization also fails because it restricts
the circuit generator rather than arbitrary non-uniform circuits.

The next brick is to audit every exponent loss in the easy-witness transfer and
determine whether any premise/conclusion parameter regime can make the ratio
unbounded without assuming a terminal separation. A negative result must name
the precise inequality that forces a bounded ratio; a positive result must
retain general circuits and one effective verifier family.

No proof is currently claimed.

# GATE-003 — Quantifier-stable unrestricted lower-bound family

**Label: NO-GO** (as an intermediate decomposition; the theorem itself remains open)

## Falsifiable theorem

There exist a uniformly indexed family `(L_j)`, one uniform nondeterministic
verifier, and unary-polynomial-time computable exponents `a(j), b(j)` satisfying
every hypothesis of GATE-002, including

`limsup_j b(j)/a(j) = infinity`,

for unrestricted, unbounded-depth, fan-in-two Boolean circuits without advice
or oracles on the verifier side.

The full model card is recorded as `GATE-003` in
`verification/claims.json` and `docs/vertical-map.md`.

## Equivalence audit

The family statement is equivalent to `NP notsubseteq P/poly`.

Forward direction: GATE-002 constructs one `L* in NP` outside `P/poly` from
any family satisfying this gate.

Reverse direction: assume one language `L in NP` is outside `P/poly`. Fix one
NP verifier for `L` with exponent `a0`. For every `j`, set

`L_j=L`, `a(j)=a0`, and `b(j)=j`.

One uniform verifier ignores the tag `j` and verifies `L`; the exponent
functions are unary-polynomial-time computable; and `L notin P/poly` implies
`L` has no `O(n^j)` circuit family for every fixed `j`. Hence
`b(j)/a(j)=j/a0` is unbounded and all GATE-003 hypotheses hold.

Thus GATE-003 does not break the terminal-sufficient theorem into a smaller
obligation. Treating it as the “smallest attackable brick” would be circular
progress accounting.

## Attempt through the known fixed-exponent family

The first candidate input is the Murray-Williams fixed-exponent NP transfer.
Substitution gives ratio `epsilon/(c j^3)`, so it fails the gate
quantitatively. Medium-uniform diagonalization also fails because it restricts
the circuit generator rather than arbitrary non-uniform circuits.

Murray-Williams Lemma 4.1 requires, for `s(n)=n^k`, a time bound large enough
to dominate a triple composition of the circuit-size function, yielding
`n^Omega(k^3)` verifier time in the fixed-exponent specialization. Their
Theorem 1.1 records the consequence as time exponent `c k^4/epsilon` versus
circuit exponent `k`.

Reindexing `k=h(j)` changes the ratio to
`epsilon/(c h(j)^3)` and cannot make it unbounded. Standard polynomial padding
by `N=n^q` divides both the verifier exponent and transferable circuit exponent
by `q`, preserving their ratio (or decreasing it once linear-time floors are
included). Therefore neither reindexing nor padding repairs the known family.

## Exact no-go

GATE-003 is rejected as an intermediate gate because it is equivalent to the
terminal-sufficient non-uniform separation. The reparameterization subroute is
also closed for the audited Murray-Williams family. This does not show the
separation false and does not rule out a genuinely new lower-bound mechanism.

## Next gate

GATE-004 asks for a first same-language, unrestricted superlinear circuit lower
bound for SAT. It is not terminal-sufficient, but unlike GATE-003 it would be a
strictly new lower bound rather than a restatement of `NP notsubseteq P/poly`.

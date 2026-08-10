# Structural barrier and failure-mode audit

**Overall label: PROVED** as a source-grounded audit of known barrier theorems;
it is not a proof of either terminal outcome.

Canonical model fields for the named claims are in
[`verification/claims.json`](../verification/claims.json). Each entry below
states the design constraint imposed on this programme.

## Relativization — B-REL

Baker, Gill, and Solovay constructed recursive oracles `A` and `B` with
`P^A = NP^A` and `P^B != NP^B`. Therefore a proof schema that relativizes
uniformly to every oracle cannot settle the unrelativized question.

Design constraint: every terminal route must identify a step that fails for
arbitrary oracle gates and explain the concrete, non-black-box structure it
uses. An oracle separation alone is `NO-GO` as a terminal result.

## Natural proofs — B-NAT

Razborov and Rudich formalized properties that are constructive and large and
showed, under an appropriate strong pseudorandom-function assumption, that such
properties cannot be useful against polynomial-size general circuits.

Design constraint: a general circuit lower-bound property must document exactly
which of constructivity, largeness, or usefulness it avoids, or which
cryptographic assumption it refutes. “Non-natural” is not itself evidence of
correctness. The barrier is conditional and is not a universal ban on circuit
lower bounds.

## Algebrization — B-ALG

Aaronson and Wigderson exhibited oracle/low-degree-extension worlds showing that
many arithmetization-based techniques still cannot resolve central separations.
The 2026 Chen-Hu-Ren audit strengthens the warning for general-circuit lower
bounds and records that known superpolynomial general-circuit lower bounds for
larger classes remain algebrizing.

Design constraint: any arithmetized route must be tested after adjoining both
oracle access and low-degree extensions. The terminal step must expose why its
argument does not survive that transformation.

## Diagonalization limitations — B-DIAG

Plain machine enumeration plus simulation naturally produces hierarchy
separations at a larger resource bound. It does not keep the diagonal language
inside `NP` while defeating every polynomial-time machine. Moreover, any fully
relativizing form is blocked by B-REL.

Design constraint: a diagonal route must account for simulation overhead,
membership of the diagonal language, uniform enumeration, and all quantifier
orders. “The language disagrees with machine `M_i`” is insufficient unless the
language remains in the promised class under one fixed verifier exponent.

## General-circuit lower-bound obstacles — B-CIRCUIT

Counting proves that almost all Boolean functions need large circuits, but it
does not make an NP function explicit. Restricted lower bounds for `AC0`,
`ACC0`, formulas, monotone circuits, or threshold subclasses do not transfer to
unrestricted fan-in-two, unbounded-depth Boolean circuits. The current explicit
unrestricted-circuit record remains linear (`3.1n-o(n)` for affine dispersers),
and the generic constant-substitution gate-elimination framework has a proved
linear ceiling. As of
this audit, even a superlinear lower bound for an explicit Boolean function and
a superpolynomial lower bound for an explicit NEXP function against general
circuits remain open; a fortiori no superlinear SAT lower bound is known.

Design constraint: every restriction on gates, depth, size, uniformity, or input
distribution is part of the theorem name and model card. Dropping it requires a
separate proved lifting theorem.

## Uniform versus non-uniform complexity — B-UNI

Uniform polynomial time is contained in non-uniform polynomial-size circuits,
so `SAT notin P/poly` is terminal-sufficient. The reverse inference is invalid:
a lower bound against P-uniform circuits can hold because circuit generation is
hard even when arbitrary non-uniform circuits remain possible. Santhanam and
Williams prove fixed-exponent lower bounds against medium-uniform circuits, not
`SAT notin P/poly`.

Design constraint: the generator, advice length, circuit family, and whether the
language may depend on the size exponent are explicit in every statement.

## Reduction and quantifier traps — B-RED

NP-completeness transfers algorithms through polynomial-time reductions. A
circuit lower bound transfers only after the reduction's length and circuit-size
blow-ups are bounded in the correct direction. It is invalid to infer

`exists L in NP, forall k: L notin SIZE(n^k)`

from

`forall k, exists L_k in NP: L_k notin SIZE(n^k)`.

Padding a family into one language also consumes lower-bound exponent. GATE-002
makes the exact ratio loss explicit.

Design constraint: all reductions record source length, target length,
uniformity, gate overhead, promise preservation, and the order of asymptotic
quantifiers. A reduction that assumes the desired separation is circular.

## Surrogate domains — B-SURR

Proof-complexity, communication-complexity, algebraic-complexity, oracle, and
restricted-circuit results are valuable but logically separate. For example, a
lower bound for one proof system rules out only algorithms whose correctness and
runtime are captured by that system.

Design constraint: no surrogate receives terminal credit until a proved bridge
with a complete model card reaches T-UNIFORM or constructs a qualifying uniform
SAT algorithm.

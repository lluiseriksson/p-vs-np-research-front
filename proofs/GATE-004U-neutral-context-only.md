# GATE-004U-NEUTRAL-CONTEXT-ONLY — dense neutral contexts force loss

**Label: NO-GO**

## Falsifiable theorem attempted

Fix the GATE-004U expanded prefix cube and first equalize all compact DNF
witnesses to a common inner suffix length using ENC-010. For every sufficiently
large four-divisible outer budget `P`, replace each core by every ENC-020
neutral placement of outer length `P`.

Attempted claim: exact agreement with SAT-gamma at all of those syntax-linked,
coordinate-dense witnesses forces positive polynomial average diagonal
parent-to-joint-quotient loss in every minimum unrestricted circuit.

This is falsifiable by any total-function family agreeing at every specified
row and suffix string while admitting a minimum circuit with nonpositive
average diagonal loss.

## Counterexample

Put `m=P/2` and pair coordinate `i` with `i+m`. Define

`W_P(z)=AND_{i=0}^{m-1}(z_i OR z_{i+m})`.

The pair distance is at least 16. Every ENC-020 context is all ones or has all
zeros confined to one inserted block of length at most 16, so `W_P=1` on the
entire family. This is a non-coordinate common predicate: ENC-020 still takes
both bit values at every individual coordinate.

Let `H(r,u)` be the polynomial-size total core recognizer/evaluator from the
LEMMA-044 application. On canonical compact DNF cores it returns their exact
SAT feasibility under the expanded row condition; outside that set it is
defined as zero. Its diagonal residuals are distinct and nonconstant. Put

`G(r,z,u)=H(r,u) AND W_P(z)`.

The function agrees with SAT-gamma at every witness in the attempted theorem.
LEMMA-046 proves that, writing `K=C(H)`, the displayed circuit is globally
minimum with exact size `K+P`. Its `m` clause functions and `2m` row-specific
AND-prefix functions yield at least `3m` joint-quotient classes for every
diagonal pair. Hence each loss is at most

`K+P-3P/2=K-P/2`.

The explicit parser/evaluator gives `K=poly(R,L,t)`. Choosing the fixed
context exponent `c>0` below the reciprocal of that polynomial degree makes
`K=o(P)` while `P=Theta(n)`. Thus the loss is negative at infinitely many
compatible lengths, falsifying the attempted theorem.

## Structural conclusion

Coordinate density is only a one-wise property. It eliminates common
literals but does not eliminate common clauses. A witness family capable of
blocking this counterexample must at least have pairwise zero coverage on any
large candidate padding region: for every proposed pair of coordinates, some
witness must set both to zero. This necessary condition is not sufficient for
GATE-004U, but it is the next concrete syntax-design audit.

Full GATE-004U remains open because its full suffix set includes other padding
forms and near-boundary cores not accepted by `W_P`.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits agreeing with exact SAT-gamma on common-inner-length DNF cores under every ENC-020 outer context; exact diagonal semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform circuit adversary and base minimum circuit; uniform DNF core maps, neutral contexts, and coordinate pairing |
| Circuit size | Counterexample size exactly `K+P`; quotient at least `3P/2`; loss at most `K-P/2<0` asymptotically |
| Circuit depth | Unrestricted base; one layer of pairwise OR gates and an unrestricted sequential AND tail |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Infinitely many compatible lengths, every four-divisible `P>=32`, all compact DNF cores and all their ENC-020 placements, and sufficiently small fixed `c>0` |
| Regime | Worst-case exact total-function counterexample to an ENC-020-only forcing theorem; not a lower bound and not a counterexample to full GATE-004U |

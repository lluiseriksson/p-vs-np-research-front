# LEMMA-005 — semantic restriction quotient

**Label: PROVED**

## Statement

Let `C` be an acyclic Boolean circuit and let `rho` fix any subset of its input
coordinates. There is a circuit for the restricted output function obtained by
the following semantic quotient:

1. replace gates whose residual functions are constant or equal to a free
   input;
2. whenever two gates have identical residual functions, redirect uses of the
   later gate to an earlier gate with that function; and
3. delete gates that no longer reach the output.

The quotient uses at most one reachable gate for each distinct nonconstant
residual gate function that is not already a free input. If free constants are
not part of the circuit basis, at most three gates suffice to generate both
constants whenever at least one free input remains.

## Model card

| Field | Value |
|---|---|
| Computational model | Acyclic Boolean circuits under coordinate restrictions and exact semantic equivalence |
| Uniform/non-uniform | Existential non-uniform quotient; no efficient equivalence test asserted |
| Circuit size | One gate per surviving residual-function class, plus at most three constant-generator gates |
| Circuit depth | Unrestricted and may decrease under redirection |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Every finite acyclic circuit and every coordinate restriction |
| Regime | Worst-case exact total Boolean function computation |

## Proof

Process gates in a topological order. A gate whose residual function is a
constant or a free input can have every outgoing edge redirected to that
source. If a gate has the same residual function as an earlier gate, redirect
its outgoing edges to the earlier gate. The earlier gate cannot depend on the
later one, so redirection creates no cycle. Each redirection preserves the
Boolean function carried by every affected edge and therefore preserves the
output function. After processing, remove gates with no path to the output.

At most one processed gate remains for each residual-function class. Constant
sources are free in the restricted representation; in the original
constant-free basis, the three-gate construction from LEMMA-004 generates zero
and one from any remaining free input. QED.

This quotient is semantic and need not be computable efficiently. Its role is
to make the exact missing mathematical property in GATE-004D auditable.

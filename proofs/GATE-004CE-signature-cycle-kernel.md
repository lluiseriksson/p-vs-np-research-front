# GATE-004CE — force a signature-cycle kernel

**Label: EXPLORATORY**

Assume the shared-exit branch of GATE-004CD and no private-cone certificate
from LEMMA-183. Let `d,c` be the two distinct first cancellation fronts from
LEMMA-184, let `gamma` be their reconvergence cycle coordinate, and let
`rho_ab` be the cycle-space map induced by restriction to pair code `ab`,
pruning, and contraction.

## Falsifiable theorem

The edgewise Boolean differences on the two arms, together with

`F_00=F_01=F_11=A` and `F_10=0`,

force at least one of the following.

1. `rho_ab(gamma)=0` for some satisfying code
   `ab in {00,01,11}`.
2. One arm contains an admissible private realization certificate satisfying
   LEMMA-183.

Alternative 1 contradicts the injectivity supplied by LEMMA-174 under the
rank equality of LEMMA-178. Alternative 2 contradicts extremality. Hence a
proof excludes the shared-exit branch and, with the private case, the
one-sided mask.

A proof must identify the actual edge set of `gamma` and show why the Boolean
four-code signatures put that coordinate in a specific restriction kernel.
Merely exhibiting reconvergence is invalid by
GATE-004CD-CYCLE-EXISTENCE-ONLY.

LEMMA-185 makes the minimum-parent obligation quantitative: every satisfying
minor loses exactly two binary gates through rank-neutral operations.
GATE-004CE-FOUR-CODE-SIGNATURES-ONLY gives an exact-table witness showing that
the four cofactors and local signatures alone do not create a kernel.
GATE-004CF isolates the remaining task as a three-elimination lower bound or a
forced noncontractible edge within the exact two-gate budget.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically extremal minimum unrestricted plateau DAG with two signature-cancellation fronts |
| Uniform/non-uniform | Every individual non-uniform operational shared-exit parent; uniform fresh implication pair |
| Circuit size | Same-size private descent or one satisfying restriction loses a cycle coordinate |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean symmetric-difference flow and cycle-space maps over `F_2` |
| Asymptotic quantifiers | Every operational GATE-004CD shared-exit parent and all four pair codes |
| Regime | Exact worst-case signature-kernel gate; not a SAT lower bound or terminal result |

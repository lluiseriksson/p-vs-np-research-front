# GATE-004BC — one neutral clause prunes one NOT

**Label: EXPLORATORY**

Let `j>=2`, and let `C` be a variable-read-once formula computing

`J_j=H AND AND_{i=1}^j(t_i OR NOT u_i)`

with exactly `j` NOT gates. Assume every NOT survives every satisfying-base
restriction, as guaranteed for the maximal-deficit formulas of LEMMA-155.

## Falsifiable theorem

Prove that some clause index `i` has the following property: after the neutral
restriction

`(u_i,t_i)=(0,1)`,

constant propagation and pruning leave a formula for the remaining
`J_{j-1}` with at most `j-1` NOT gates.

A formula satisfying the premises for which all `j` neutral clause
restrictions retain all `j` NOT gates falsifies the theorem.

## Sufficiency for GATE-004BB

At maximal deficit, LEMMA-155 supplies such a formula at `j=m`. If GATE-004BC
removes one NOT, the restricted rank-zero circuit has `N+r<=j-1`. LEMMA-153
and its lower bound `mu_{j-1}>=j-1` force equality and

`Delta_{j-1}=sigma`.

The resulting formula is again an endpoint minimum formula satisfying
LEMMA-155. Repeating until `j=min(m,K+sigma)` proves GATE-004BB. Clause
symmetry identifies any surviving subset with the canonical prefix.

LEMMA-156 supplies exact state-potential rigidity on every canonical clause
chain. The remaining step must upgrade zero-slack potential accounting to
syntactic pruning or a semantic formula exchange.

## Model card

| Field | Value |
|---|---|
| Computational model | Variable-read-once AND/OR/NOT formulas for base conjoined with disjoint implication clauses, under neutral restrictions |
| Uniform/non-uniform | Every individual non-uniform equality-stratum formula; symmetric uniform clause family |
| Circuit size | Premise exactly `j` NOTs and rank zero; target a restricted formula with at most `j-1` NOTs and rank zero |
| Circuit depth | Unrestricted read-once formula depth |
| Fan-in | AND/OR two; NOT one; fanout one in the output cone |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restrictions, formula trees, and integer NOT-state potential |
| Asymptotic quantifiers | Every `j>=2` in every compatible maximal-deficit descent stratum |
| Regime | Falsifiable worst-case sufficient subgate for GATE-004BB; not full GATE-004BA, a SAT lower bound, or a terminal result |

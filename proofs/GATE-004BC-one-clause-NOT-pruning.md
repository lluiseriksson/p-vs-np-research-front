# GATE-004BC — one neutral clause prunes one NOT

**Label: PROVED**

Let `j>=2`, and let `C` be a variable-read-once formula computing

`J_j=H AND AND_{i=1}^j(t_i OR NOT u_i)`

with exactly `j` NOT gates. Assume every NOT survives every satisfying-base
restriction, as guaranteed for the maximal-deficit formulas of LEMMA-155.

## Theorem

Every clause index `i` has the following property: after the neutral
restriction

`(u_i,t_i)=(0,1)`,

constant propagation and pruning leave a formula for the remaining
`J_{j-1}` with at most `j-1` NOT gates.

LEMMA-157 proves the stronger statement that every clause works. After De
Morgan normalization, minterm co-occurrence forces each implication pair to
be its own canonical OR subtree. Opposite polarities require one private NOT
inside every such subtree. Since the formula has exactly `j` NOT gates, these
private gates exhaust the count. Neutralizing a pair deletes its unique NOT.

## Sufficiency for GATE-004BB

At maximal deficit, LEMMA-155 supplies such a formula at `j=m`. If GATE-004BC
removes one NOT, the restricted rank-zero circuit has `N+r<=j-1`. LEMMA-153
and its lower bound `mu_{j-1}>=j-1` force equality and

`Delta_{j-1}=sigma`.

The resulting formula is again an endpoint minimum formula satisfying
LEMMA-155. Repeating until `j=min(m,K+sigma)` proves GATE-004BB. Clause
symmetry identifies any surviving subset with the canonical prefix.

LEMMA-156 supplies compatible exact state-potential rigidity, but the proof
of pruning uses the stronger read-once wiring and polarity structure from
LEMMA-157 rather than scalar potential alone.

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
| Regime | Exact worst-case sufficient subgate closing GATE-004BB; not intermediate-deficit GATE-004BA, a SAT lower bound, or a terminal result |

# GATE-004AH — function-specific binary/NOT tradeoff

**Label: EXPLORATORY**

## Falsifiable theorem

For the four-positive/one-negative product `W_m`, let a pruned unrestricted
circuit contain `B` binary gates and `N` NOT gates. Prove that throughout the
only unresolved inversion range

`ceil(log_2(m+1)) <= N <= m-1`,

one has

`B >= 6m-1-N`.

The theorem is falsified by one explicit circuit in this range violating the
inequality.

Essential-input connectivity already gives `B>=5m-1`. If `N>=m`, that bound
alone gives total size at least `6m-1`; if `N` is below the displayed range,
Markov rules the circuit out. Thus GATE-004AH would prove
`C(W_m)=6m-1`, settling the standalone prerequisite to the displayed-
minimality branch of GATE-004AG. It would not by itself prove additivity over
the canonical base or minimum-circuit quotient survival.

LEMMA-111 currently gives only the cycle-rank consequence

`B >= 5m-1+ceil(log_2(m/N))`,

which is far below `6m-1-N` across the middle range. A successful proof must
use the clause-indexed distribution of the negative variables, not only total
decrease or generic graph topology.

GATE-004AI rewrites the target with output-cone cycle rank
`t=B-5m+1`: prove `N+t>=m` by injecting clause indices into NOT gates or
independent cycle coordinates. LEMMA-113 shows that raw output cofactor
transitions cannot supply distinct witnesses; an internal bounded-reuse
theorem remains missing.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted Boolean circuits for the fixed four-positive/one-negative read-once clause product; exact binary/NOT gate counts |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform function family |
| Circuit size | Target tradeoff `B+N>=6m-1` in the unresolved NOT range; current cycle-rank lower is weaker |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean circuits and restrictions only |
| Asymptotic quantifiers | Every `m>=5` and every pruned circuit with `ceil(log2(m+1))<=N<=m-1` |
| Regime | Exact worst-case standalone-size gate; not a base direct sum, SAT lower bound, or terminal result |

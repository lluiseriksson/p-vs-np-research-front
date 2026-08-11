# Cycle 178 — private-reservoir audit

**Label: PROVED**

LEMMA-212 generalizes the paid two-gate rewrite to an aligned formula of any
finite size. A closed set of `m-1` strict noncarrier ancestors of the counted
boundary hosts the non-root gates, while the boundary vertex hosts the formula
root.
The closure and nondescendant conditions preserve all exterior functions and
acyclicity. New reservoir functions are independent of both fresh inputs, so
size and earlier potentials do not increase; at equality the boundary leaves
`R_0`.

GATE-004DE-FANOUT-ONE-PRIVATE-BUDGET-ONLY records the precise limitation. A
29-gate single-output extension of the cycle-177 witness gives every proper
counterflow ancestor a live escape. Although `r` itself has fanout one to `b`,
the greatest `b`-private reservoir is only `{r}`. The unchanged boundary
output `xyz OR w` needs at least three formula gates over the independent base
pool and therefore two non-root host vertices.

## Classification

- LEMMA-212: `PROVED`
- GATE-004DE-FANOUT-ONE-PRIVATE-BUDGET-ONLY: `NO-GO`
- GATE-004DF: `EXPLORATORY`

GATE-004DF now asks minimum joint cost to pay the exact private-reservoir
deficit, or to resolve absence of an aligned formula, raw/shared inputs, and
incomparable erasure. No SAT lower bound or terminal implication is claimed.

## Review boundary

`verification/private_reservoir_budget_audit.py` checks all 64 assignments of
the base witness, the cofactor identities, essential dependence, and the
consumer-closure fixed point. Liveness of selector-isolated terms and the
LEMMA-212 exchange proof remain human arguments. Fable and `fable-bridge` were
not invoked. No independent mathematical certification or formal verification
is claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Refined unrestricted AND/OR/NOT endpoint plus one explicit finite single-output nonminimal witness |
| Uniform/non-uniform | Every endpoint with the aligned-formula/private-reservoir certificate; one fixed finite witness for the no-go |
| Circuit size | `m` physical vertices are repurposed with no increase; witness has 29 gates and makes no minimum claim |
| Circuit depth | Unrestricted target; constant witness depth |
| Fan-in | AND/OR two; NOT one; reservoir excludes distinguished carriers and is consumer-closed toward `b`; witness `r` has fanout one, with live escapes at `g,i,j,k` and a live complement of `h` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean identities, formula leaf bounds, physical rewiring, and consumer-closure fixed point |
| Asymptotic quantifiers | Every qualifying finite endpoint certificate; all 64 base assignments and every strict ancestor of the witness boundary |
| Regime | Exact sufficient exchange plus private-budget no-go; not a SAT lower bound or terminal result |

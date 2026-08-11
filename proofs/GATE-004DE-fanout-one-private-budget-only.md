# GATE-004DE-FANOUT-ONE-PRIVATE-BUDGET-ONLY — fanout one does not pay a deep formula

**Label: NO-GO**

Fanout one of the counterflow output does not force the private reservoir
needed by LEMMA-212. The following single-output finite DAG has a comparable
fanout-one counterflow input at `b`, but its greatest `b`-private ancestor set
has only one gate while the unchanged boundary function requires at least
three formula gates over its independent base signals.

## Witness

For raw inputs `u,t,x,y,z,w`, let

```text
nt = NOT t
a  = u AND w
c  = x OR a       d = y OR a
e  = c AND d      f = z OR a
h  = e AND f      = xyz OR uw
g  = u AND x      i = g AND y
j  = i AND z      k = j AND nt
r  = w OR k       = w OR uxyz NOT t
b  = h OR r       = xyz OR w.
```

Add `n = NOT h`. For each `v` in `{g,i,j,k}`, add an escape
`s_v = v OR p_v` with a fresh raw input `p_v`. Finally give each of
`b,n,s_g,s_i,s_j,s_k` a fresh selector, AND the signal with its selector, and
combine the six terms with a five-gate binary OR tree. This is a 29-gate
single-output circuit. Selecting one term and clearing the other selectors
shows that each displayed escape is semantically live.

The `r` cofactors are

```text
r_00 = w,  r_10 = w OR xyz,  r_01 = r_11 = w,
```

so the row-zero defect is comparable, and `r` has exactly one consumer, `b`.
Before `b`, the globally `u`-independent base pool contains
`x,y,z,w,t,nt`. The target `xyz OR w` depends essentially on all four of
`x,y,z,w`. A constant-free formula with at most two gates has at most three
leaf occurrences and therefore cannot compute the target from that pool.

Call a set `E` of strict gate ancestors of `b` *admissibly `b`-private* when it
excludes the distinguished carrier `h` and every edge leaving `E` targets
`E union {b}`. The greatest such set here is `{r}`. The
edge `h -> n` removes the whole `h` cone from every private set. Each of
`g,i,j,k` has a live escape edge, which removes the counterflow chain below
`r`; fixed-point propagation also removes `nt`. Thus the available reservoir
has size one, whereas a three-gate formula needs two private vertices under
LEMMA-212.

The selector tree lies downstream of the named escapes and is not an ancestor
of `b`, so it cannot be counted in this reservoir. The witness is deliberately
nonminimal. It does not refute a theorem using minimum joint cost, exact
satisfying-pruning losses, or another source of physical payment. It refutes
only the inference from output fanout one to sufficient private budget.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit single-output constant-free unrestricted AND/OR/NOT DAG with live escape consumers |
| Uniform/non-uniform | One uniform finite witness schema with fixed fresh escape and selector inputs; no minimum-parent claim |
| Circuit size | 29 gates: 13 base gates, one `NOT h`, four escapes, six selector ANDs, and five output ORs |
| Circuit depth | Constant finite depth; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; `r` has fanout one to `b`; `g,i,j,k` have live escapes and `h` has the live complement consumer |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean identities, essential-variable counting, distinguished-carrier exclusion, and directed consumer-closure fixed point |
| Asymptotic quantifiers | Every assignment to all displayed raw inputs and selectors; every at-most-two-gate formula over the independent base pool |
| Regime | Fanout-one-to-private-budget no-go; not a minimum counterexample, SAT lower bound, or terminal result |

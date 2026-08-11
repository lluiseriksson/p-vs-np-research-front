# GATE-004DM-FIXED-RADIUS-CONSUMER-AUDIT-ONLY — sealing depth is unbounded

**Label: NO-GO**

No fixed number of consumer layers suffices to decide whether a host rewrite
preserves the parent. For every `m>=1`, define

```text
e   = v OR x,
c_1 = e AND z_1,
c_i = c_(i-1) AND z_i,
n   = NOT c_m,
a   = c_m OR n,
F   = y AND a = y.
```

Replace `e` by its `v=0` cofactor wire `x`. On the assignment
`v=1,x=0,z_1=...=z_m=1`, the function changes at every `c_i` and at `n`.
It first becomes equal again at `a`, because both old and new versions compute
`c_m OR NOT c_m=1`; the nonconstant parent `F=y` is preserved. The first seal
is therefore beyond an arbitrarily long changed chain.

Every witness is deliberately redundant and nonminimal. It does not refute a
minimum-endpoint theorem forcing a short seal, a pruning contradiction, or a
global changed-region certificate. It refutes consumer auditing truncated at
any fixed radius independent of the circuit.

## Model card

| Field | Value |
|---|---|
| Computational model | Uniform family of finite single-output constant-free unrestricted AND/OR/NOT DAGs |
| Uniform/non-uniform | Uniform construction for every `m>=1`; each member finite and non-uniform |
| Circuit size | `m+4` gates; changed chain length `m` before the tautological seal |
| Circuit depth | Linear in `m` |
| Fan-in | AND/OR two; NOT one; fanout two at `c_m`, otherwise one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean functions and forward changed-region reachability |
| Asymptotic quantifiers | Every `m>=1` and every assignment to displayed inputs |
| Regime | Fixed-radius-interface no-go; not a minimum endpoint, SAT lower bound, or terminal result |

# GATE-004DR-TWO-SIDED-SWAP-ONLY — a functional swap is not a resource

**Label: NO-GO**

Scope: at the common support of two incoming code-`10` defects, use only the
`01<->10` function table from LEMMA-227 to name and charge a satisfying loss,
non-bridge deletion, cycle coordinate, free host, or strict potential descent.

Use raw inputs `u,t,x,y` and the constant-free crossbar

```text
n   = NOT t,
q   = u AND n,
r   = NOT q,
p_x = r AND x,    q_y = q AND y,
A   = p_x OR q_y,
p_y = r AND y,    q_x = q AND x,
B   = p_y OR q_x.
```

At `00,01,11`, `q=0` and `(A,B)=(x,y)`. At `10`, `q=1` and
`(A,B)=(y,x)`. Hence the two input defects have identical support
`q AND (x xor y)` and swap on that support. Nevertheless

```text
A OR B = x OR y,
A AND B = x AND y
```

on all four codes. The displayed OR-output circuit has ten gates and depth at
most six; replacing the crossbar by `x OR y` gives the same nonconstant parent
with one gate.

The same interface admits arbitrarily different physical realizations. A wire
may be padded by double NOTs, changing physical gate identities and counts, or
by the constant-free identity

```text
I_r(z) = (z AND r) OR (z AND NOT r) = z
```

with fresh `r`, adding reconvergent undirected cycle structure without changing
any interface function. Iterating these paddings preserves the crossbar swap
table and the symmetric output while changing the candidate physical ledger.
Therefore the table alone determines no named, deduplicable physical resource.

The crossbar and paddings are highly nonminimal. They do not refute an
endpoint-minimality theorem that uses the actual marked paths to prove an
existential saving or loss. They refute only table-to-resource attribution
without physical provenance, minimum cost, and exact pruning maps.

## Model card

| Field | Value |
|---|---|
| Computational model | Finite single-output constant-free unrestricted AND/OR/NOT crossbar DAG and its one-gate replacement |
| Uniform/non-uniform | One finite non-uniform diagnostic circuit; exact for every assignment |
| Circuit size | Crossbar OR-output size ten versus one-gate replacement; no endpoint claim |
| Circuit depth | At most six |
| Fan-in | AND/OR two; NOT one; crossbar control and complement have shared fanout |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean functions and analytical defect supports over `F_2` |
| Asymptotic quantifiers | Every assignment to `u,t,x,y`; both symmetric binary outputs |
| Regime | Two-sided-swap-only no-go; not a minimum endpoint, SAT lower bound, or terminal result |

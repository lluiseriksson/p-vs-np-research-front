# LEMMA-239 — zero-overhead coordinate gates can form an arbitrary chain

**Label: PROVED**

For every `m>=1`, take admissible raw signals `A={a,z_1,...,z_m}` and define

```text
p_i = a AND z_1 AND ... AND z_i,
N_m = (p_1,...,p_m).
```

The exact multi-output AND/OR/NOT complexity of `N_m` is `m`, so its minimum
overhead `h=C_A(N_m)-q_A(N_m)` is zero. Nevertheless it has a minimum
realization whose coordinate dependency graph is the full directed chain

```text
p_1 -> p_2 -> ... -> p_m.
```

Every `p_i` is a designated vector output, while every `p_i` with `i<m` is
also an input to the next coordinate gate.

## Proof

Set `p_0=a`, and compute `p_i=p_{i-1} AND z_i` for `1<=i<=m`. This uses `m`
gates and has the displayed dependency path. The coordinate functions are
pairwise distinct: if `i<j`, set `a,z_1,...,z_i` to one and `z_{i+1}` to zero;
then `p_i=1` and `p_j=0`. None is an admissible input projection. Therefore
`q_A(N_m)=m`, and LEMMA-236 proves that the construction is minimum.

In this physical realization, deleting or retargeting a proper-prefix gate
without repairing its outgoing edge destroys the definitions of all later
coordinates. Also neither input of `p_i=p_{i-1} AND z_i` computes `p_i`:
assignments with `(p_{i-1},z_i)=(1,0)` and `(0,1)` separate the two input
functions from the output. Thus zero overhead does not imply a set of
mutually non-reachable or wire-replaceable coordinate gates.

Adjoining two fresh code inputs and repeating every coordinate on all four
codes preserves the proof. The vector is a diagnostic, not a minimum plateau
endpoint.

## Model card

| Field | Value |
|---|---|
| Computational model | Constant-free multi-output unrestricted AND/OR/NOT DAG for nested conjunction coordinates |
| Uniform/non-uniform | Uniform construction for every `m>=1`; each instance finite and non-uniform |
| Circuit size | Exact cost `m`, coordinate count `q=m`, and minimum overhead `h=0` |
| Circuit depth | Exact displayed chain depth `m`; other minimum realizations not classified |
| Fan-in | AND two; OR/NOT unused; fanout at most two when output designation is counted separately |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean coordinate functions and physical DAG reachability |
| Asymptotic quantifiers | Every `m>=1`, coordinate pair, displayed gate, and separating assignment |
| Regime | Exact zero-overhead chain witness; not uniqueness, endpoint realizability, SAT lower bound, or terminal result |

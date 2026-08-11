# GATE-004DF-ESCAPE-COUNT-ONLY — a constant frontier can block unbounded deficit

**Label: NO-GO**

Counting escape-frontier edges cannot pay the private-reservoir deficit
one-for-one. For every `n>=3`, the following single-output nonminimal circuit
has boundary function requiring `n` formula gates, maximum private reservoir
one, and only three frontier exits, independent of `n`.

## Family

Let `X = x_1 AND ... AND x_n`. Compute `a=u AND w`, every
`c_i=x_i OR a`, and their binary AND chain ending at the distinguished gate
`h`. Then `h=X OR uw`. Independently compute the chain

```text
q_1 = u AND x_1,
q_i = q_(i-1) AND x_i,
k   = q_n AND NOT t,
r   = w OR k,
b   = h OR r = X OR w.
```

Add the live carrier consumer `nh=NOT h` and the one noncarrier escape
`s=k OR p`. Selector-isolate `b,nh,s` with three AND gates and a two-gate OR
tree to obtain one output. This circuit has `3n+11` gates. Each isolated term
is live by setting its selector to one and the other two to zero.

Among eligible strict ancestors of `b`, the only private gate is `r`. The edge
`k -> s` puts `k` on the escape frontier and reverse reachability removes the
entire `q` chain and `NOT t`. Excluding distinguished `h` leaves exactly two
carrier-frontier edges into it; reverse reachability removes its independent
construction cone. LEMMA-213 therefore gives `rho_b=1` from a frontier of
three edges.

Before `b`, the globally `u`-independent available signals are raw inputs,
`NOT t`, and signals outside the `b`-ancestor cone; none compresses two of the
essential variables below. Apart from `NOT t`, every gate in the displayed
`h` and counterflow cones is `u`-sensitive. The target `X OR w` depends
essentially on the `n+1` variables `x_1,...,x_n,w`. A constant-free
`m`-gate formula over the available independent pool has at most `m+1` leaf
occurrences, each carrying at most one
of those essential variables, so it needs `m>=n`; the displayed AND chain
followed by OR uses exactly `n` gates. Hence `A_b=n-1` and `D_b=n-2`, which is
unbounded although the frontier has three exits and only one noncarrier live
escape.

Every family member is nonminimal and does not refute a semantic charge on an
escape region, a pruning loss, or a minimum-cost injection using more than raw
frontier cardinality. It refutes only a one-unit-per-frontier-edge argument.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit uniform family of finite single-output constant-free unrestricted AND/OR/NOT DAGs |
| Uniform/non-uniform | Uniform construction for every `n>=3`; each member is a finite non-uniform witness and makes no minimum claim |
| Circuit size | Exactly `3n+11` gates; target formula size exactly `n`; private deficit `D_b=n-2` |
| Circuit depth | Linear in `n`; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; one noncarrier escape edge, two edges into excluded carrier `h`, and `r` fanout one to `b` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean identities, formula leaf counting, and directed reverse reachability |
| Asymptotic quantifiers | Every integer `n>=3`, every assignment to all raw inputs and selectors, and every constant-free formula for `X OR w` |
| Regime | Escape-cardinality-only no-go; not a minimum counterexample, SAT lower bound, or terminal result |

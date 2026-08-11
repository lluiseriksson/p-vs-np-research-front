# GATE-004DG-ENTRY-COUNT-ONLY — one masked entry can hide unbounded deficit

**Label: NO-GO**

The number of gates directly consuming raw `u` in a jointly masked escape
region does not lower-bound the private deficit. For every `n>=3`, reuse the
cycle-179 carrier construction with `X=AND_i x_i`,

```text
h = X OR uw,
q_1 = u AND x_1,
q_i = q_(i-1) AND x_i,
k = q_n AND NOT t,
r = w OR k,
b = h OR r = X OR w.
```

Take `S={q_1,...,q_n,k,r}` with outputs `{k,r}`. Raw `u` enters `S` only at
`q_1`, so `d=1`. Add the live secondary consumer `c=u AND k`. The larger
cofactor selected at the OR boundary is `sigma=1`. Replacing
`k` by `k|_{u=1}=X AND NOT t` preserves `c`, because

```text
u AND (X AND NOT t) = k.
```

Replacing `r` by `r|_{u=1}=w OR (X AND NOT t)` also preserves `b`, since
`h OR r|_{u=1}=X OR w`. Thus the entire two-output region satisfies
LEMMA-214 and specialization saves exactly the one entry gate `q_1`; the
remaining `q` chain is the AND chain for `X`.

Add `nh=NOT h` and selector-isolate `b,nh,c` into one output. The maximum
admissible private reservoir at `b` is still `{r}`: the live edge `k -> c`
removes the whole `q` chain by reverse reachability, while the two inputs of
excluded carrier `h` remove its construction cone. As in NG-156, the exact
independent formula size of `X OR w` is `n`, so `D_b=n-2`.

Hence a canonical jointly masked frontier region can have entry payment one
and unbounded private deficit. The family is nonminimal—LEMMA-214 itself makes
that explicit—and does not refute a lower bound on the full joint cofactor
circuit saving. It refutes raw entry multiplicity alone.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit uniform family of finite single-output constant-free unrestricted AND/OR/NOT DAGs with a marked two-output region |
| Uniform/non-uniform | Uniform construction for every `n>=3`; every member finite, non-uniform, nonminimal |
| Circuit size | `3n+11` gates; marked specialization saves exactly one gate while `D_b=n-2` |
| Circuit depth | Linear in `n`; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; one raw-`u` entry in `S`, outputs `k,r`, and live consumers `c,b` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean cofactors, joint DAG specialization, formula leaf counting, and reachability |
| Asymptotic quantifiers | Every `n>=3`, every assignment to raw inputs and selectors, and the selected cofactor `sigma=1` |
| Regime | Entry-count-only no-go; not a minimum counterexample, SAT lower bound, or terminal result |

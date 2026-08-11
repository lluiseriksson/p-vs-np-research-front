# GATE-004DH-JOINT-SAVING-ONLY — exact joint saving can remain one

**Label: NO-GO**

The full minimum joint cofactor-circuit saving of one canonical masked escape
region need not cover its private deficit. In the NG-157 family, the marked
region

```text
S = {q_1,...,q_n,k,r}
```

has `|S|=n+2` and selected `u=1` cofactor vector

```text
(k_1,r_1) = (X AND NOT t, w OR (X AND NOT t)).
```

Using the already available independent signal `NOT t`, an AND chain for `X`
uses `n-1` gates, the final AND produces `k_1`, and one OR produces `r_1`.
Thus the vector has a joint circuit of `n+1` gates with `k_1` exposed as an
intermediate output.

This size is minimum. The second output `r_1` depends essentially on the
`n+2` available source signals `x_1,...,x_n,NOT t,w`. LEMMA-215 requires at
least `n+1` binary gates in its cone. Therefore

```text
J_1(S,{k,r}) = (n+2) - (n+1) = 1.
```

The boundary target still has exact independent formula size `n`, private
reservoir size one, and `D_b=n-2`. Hence `J_1<D_b` for every `n>=4`, with an
unbounded gap. All masked-consumer and single-output identities from NG-157
remain exact.

Every member is nonminimal precisely because the one-gate specialization
saving exists. The family does not refute a theorem that uses global minimum
endpoint structure to force another region, a pruning loss, or a coupling
between boundary formula cost and all available joint savings. It refutes the
local joint-saving quantity alone.

## Model card

| Field | Value |
|---|---|
| Computational model | Uniform family of finite single-output constant-free unrestricted AND/OR/NOT DAGs with one marked two-output region |
| Uniform/non-uniform | Every `n>=3`; each family member finite, non-uniform, and nonminimal |
| Circuit size | Marked region `n+2`; exact selected joint cofactor circuit `n+1`; `J_1=1`; `D_b=n-2` |
| Circuit depth | Linear in `n`; ambient target unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and both cofactor outputs exposed |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean cofactors, essential-source arity lower bound, and shared DAG realization |
| Asymptotic quantifiers | Every `n>=3`, every assignment, and every constant-free joint circuit over the stated available sources |
| Regime | Local-joint-saving-only no-go; not a minimum counterexample, SAT lower bound, or terminal result |

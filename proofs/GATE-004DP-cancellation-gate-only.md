# GATE-004DP-CANCELLATION-GATE-ONLY — a first cancellation is not a payment

**Label: NO-GO**

Scope: find the first binary gate whose code-`10` output defect is zero and
count that gate automatically as a free host, satisfying loss, non-bridge, or
strict potential descent.

Use raw inputs `u,t,x,y` and define the old circuit fragment

```text
n = NOT t,
q = u AND n,
a = x OR q,
m = NOT x,
c = a OR m,
F = y AND c = y.
```

Replace the changed signal `a=x OR (u AND NOT t)` by `a'=x`. Its defect is
`u AND NOT t AND NOT x`. The common second input `m=NOT x` equals one on the
defect support, so LEMMA-224 proves that the OR gate `c` kills the defect.
Indeed both old and new `c` are the constant-one function, and the nonconstant
parent remains `F=y`.

This names a genuine first one-sided cancellation but does not make `c` an
independent payment: it is a redundant tautological gate in a deliberately
nonminimal circuit. The family does not refute an endpoint-minimality theorem
that converts the mask and changed cone into an explicit saving. It refutes
only the inference from the local event alone.

## Model card

| Field | Value |
|---|---|
| Computational model | Paired finite single-output constant-free unrestricted AND/OR/NOT DAG fragments |
| Uniform/non-uniform | One finite non-uniform diagnostic interface; exact for every assignment |
| Circuit size | Old diagnostic six gates; replacement removes the three-gate code-10 defect source; no endpoint claim |
| Circuit depth | At most five |
| Fan-in | AND/OR two; NOT one; fanout one in the displayed fragment |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean functions and analytical `F_2` defect support |
| Asymptotic quantifiers | Every assignment to `u,t,x,y` |
| Regime | First-cancellation-only no-go; not a minimum endpoint, SAT lower bound, or terminal result |

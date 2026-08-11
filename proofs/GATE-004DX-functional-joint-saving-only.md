# GATE-004DX-FUNCTIONAL-JOINT-SAVING-ONLY — joint minimization need not save

**Label: NO-GO**

Scope: infer from multi-output sharing alone that replacing a deduplicated
physical port region by a minimum shared DAG for its complete vector always
releases at least one gate.

LEMMA-236 gives only the unavoidable coordinate-output cost. LEMMA-237
exhibits, for every `m>=1`, an exterior region of `m` gates computing
`(a AND z_i)_i` whose exact additional shared-DAG cost is also `m`. Adjoining
two code inputs and using the same vector on all four codes does not create a
saving. Thus the purely functional deficit `|U|-C_A(P)` can be zero for
unbounded vector length.

This is NG-173. It does not refute GATE-004DX's endpoint-sensitive alternatives:
the LEMMA-233 parent is nonminimal, and an actual plateau endpoint may force a
distinct loss/origin payment, positive overhead, potential descent, or a
four-code contradiction. It refutes only a universal strict-saving inference
from joint minimization or vector length itself.

## Model card

| Field | Value |
|---|---|
| Computational model | Constant-free multi-output unrestricted AND/OR/NOT DAG for the LEMMA-237 diagonal diagnostic |
| Uniform/non-uniform | Uniform vector family for every `m>=1`; each instance finite and non-uniform |
| Circuit size | Deduplicated exterior region `|U|=m` and exact additional joint cost `C_A(P)=m` |
| Circuit depth | Unrestricted lower bound; depth-one exterior construction after the supplied signal |
| Fan-in | AND/OR two; NOT one; fanout and multi-output sharing unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean vector functions and a code-independent four-row extension |
| Asymptotic quantifiers | Every `m>=1`, every coordinate, and every realizing shared DAG |
| Regime | Functional-joint-saving-only no-go; not an endpoint counterexample, SAT lower bound, or terminal result |

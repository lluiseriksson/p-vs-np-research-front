# GATE-004DY-ZERO-OVERHEAD-AS-INDEPENDENT-HOSTS — coordinates can be nested

**Label: NO-GO**

Scope: in the `e=0,h=0` branch, count every coordinate-source gate as a
mutually independent physical host merely because LEMMA-236 leaves no
auxiliary-only gates.

LEMMA-238 says exactly what zero overhead provides: a coordinate straight-line
ordering. LEMMA-239 shows that this ordering may be a full chain of arbitrary
length. In its minimum `m`-gate realization, every proper-prefix coordinate
gate feeds later coordinate gates, and neither of its two inputs is a wire
replacement. Hence coordinate designation does not imply physical
independence, safe retargetability, or a parent-preserving payment.

This is NG-174. The witness is a diagnostic vector, not an operational
endpoint. It does not rule out payments obtained from a reachability
antichain, independently sealed downstream regions, satisfying losses,
marked origins, or a contradiction along a long endpoint chain.

## Model card

| Field | Value |
|---|---|
| Computational model | Constant-free multi-output unrestricted AND/OR/NOT zero-overhead coordinate DAGs |
| Uniform/non-uniform | Uniform nested-vector family for every `m>=1`; each instance finite and non-uniform |
| Circuit size | Exact `C_A(P)=q_A(P)=m`, with all `m` coordinate gates on one dependency chain |
| Circuit depth | Displayed minimum realization depth `m` |
| Fan-in | AND two; OR/NOT unused; physical gate dependencies and output designations explicit |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean vector functions and DAG reachability |
| Asymptotic quantifiers | Every `m>=1`, every proper-prefix coordinate gate, and every displayed dependency edge |
| Regime | Zero-overhead-independent-host no-go; not an endpoint counterexample, SAT lower bound, or terminal result |

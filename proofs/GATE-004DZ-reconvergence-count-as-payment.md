# GATE-004DZ-RECONVERGENCE-COUNT-AS-PAYMENT — merges need seals

**Label: NO-GO**

Scope: after selecting a width-`k` coordinate antichain, count the `k-1`
binary reconvergence gates forced by LEMMA-241 as free, distinct physical
payments solely because they exist downstream.

LEMMA-242 makes the count tight while every forced merge remains parent-live
and neither merge input can replace it. Removing or retargeting such a gate
without a parent-preserving repair changes the output. Therefore distinct
physical identity and exact reconvergence cardinality do not establish host
availability.

This is NG-175. The witness is nonminimal and not an operational endpoint, so
minimum endpoint identities may still supply independently equal cuts,
satisfying losses, marked origins, contraction resources, or potential
descent. Each such payment must be proved rather than inferred from the
reconvergence count.

## Model card

| Field | Value |
|---|---|
| Computational model | Constant-free single-output AND/OR antichain-reconvergence diagnostics |
| Uniform/non-uniform | Uniform family for every `k>=2`; each circuit finite and non-uniform |
| Circuit size | Exactly `k-1` forced merge gates, all parent-live in the displayed circuit |
| Circuit depth | Unrestricted in the theorem; diagnostic comb depth `k` |
| Fan-in | AND/OR two; NOT unused; fanout one in the displayed region |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean functions and directed reconvergence trees |
| Asymptotic quantifiers | Every `k>=2`, every displayed merge, and both input-substitution tests |
| Regime | Reconvergence-count-only no-go; not an endpoint counterexample, SAT lower bound, or terminal result |

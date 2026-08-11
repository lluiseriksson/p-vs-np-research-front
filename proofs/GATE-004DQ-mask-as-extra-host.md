# GATE-004DQ-MASK-AS-EXTRA-HOST — a seal is not a second host

**Label: NO-GO**

Scope: after a one-sided mask certifies equality at a cut gate, count the mask
or the cut gate as an additional physical host beyond the gate actually
retargeted upstream.

LEMMA-226 gives a uniform obstruction. For every `m`, the `m` changed gates
`a_i` are independently sealed at `c_i`, but all seals share one mask signal
`b`. Each `c_i` has an unmasked selector slice, and neither incoming signal
can replace it without changing the parent. It cannot be treated as free
without another certified rewrite. The original rewrite therefore certifies
the `m` actual hosts `a_i`, not
`2m` hosts from also counting the seals, and the one shared `b` cannot be
charged `m` times.

The family is nonminimal and does not refute a separate minimum-cost exchange
that happens to free a mask or cut gate. It refutes only automatic or repeated
payment from the semantic seal certificate.

## Model card

| Field | Value |
|---|---|
| Computational model | Uniform paired single-output constant-free unrestricted AND/OR/NOT host-rewrite family |
| Uniform/non-uniform | Every `m>=1`; each circuit finite and non-uniform |
| Circuit size | Old size `4m+2`; `m` real upstream hosts, `m` parent-live seals, and one shared mask signal |
| Circuit depth | Unrestricted final OR-tree depth; constant host-to-seal depth |
| Fan-in | AND/OR two; NOT one; shared mask fanout `m` |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean functions and physical host deduplication |
| Asymptotic quantifiers | Every `m>=1`, every assignment, and every seal index |
| Regime | Seal-as-extra-payment no-go; not an endpoint counterexample, SAT lower bound, or terminal result |

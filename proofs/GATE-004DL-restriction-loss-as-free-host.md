# GATE-004DL-RESTRICTION-LOSS-AS-FREE-HOST — deletion is not expendability

**Label: NO-GO**

Membership in a satisfying-pruning loss set does not make a physical gate
available for parent-level repurposing. LEMMA-219 gives, already at `m=2`, a
single-output circuit where exactly two binary gates are lost under one
restriction but replacing them by the restricted wires changes the parent
function.

The witness is nonminimal and not an implication plateau. It therefore does
not refute an endpoint theorem deriving additional masking, privacy, or a
joint multi-output replacement. It refutes the unproved step from

```text
e in L_alpha
```

to “`e` is a free host”. A valid charge must name every unrestricted consumer
and prove that the complete replacement interface preserves the parent across
all four pair codes. The orientation-specific caps `2/4` remain caps on
restriction losses, not counts of automatically expendable gates.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact physical restriction accounting plus an explicit single-output AND/OR witness family |
| Uniform/non-uniform | Every loss-set inference under audit; one uniform family for every `m>=1` |
| Circuit size | Diagnostic `4m-1`; `m=2` gives an exact two-gate restriction loss with no free parent substitution |
| Circuit depth | Unrestricted; diagnostic OR-tree depth arbitrary |
| Fan-in | AND/OR two; NOT one allowed; fanout unrestricted in target |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restriction, physical consumers, and exact parent-function comparison |
| Asymptotic quantifiers | Every `m>=1`, every diagnostic assignment, and every proposed loss-to-host inference |
| Regime | Restriction-loss-as-free-host no-go; not an endpoint counterexample, SAT lower bound, or terminal result |

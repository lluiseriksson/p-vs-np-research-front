# GATE-004CU-CYCLE-EXISTENCE-ONLY — existence is not cycle loss

**Label: NO-GO**

LEMMA-201 names a genuine cycle coordinate `gamma_b` at every counterflow
boundary. That fact alone cannot discharge GATE-004CU. LEMMA-185 requires
every satisfying restriction to preserve the full parent cycle rank, and
LEMMA-174 makes the cycle-space map injective modulo contraction. Therefore
`gamma_b` survives all three satisfying minors as a nonzero coordinate.

The inference

`counterflow reconvergence -> a satisfying minor kills its cycle`

is consequently unavailable without an additional theorem that forces a
non-bridge deletion, rules out the necessary contraction, or proves an
independent resource conflict. The nonminimal gadget in
GATE-004CT-COUNTERFLOW-LOCAL-ONLY separately shows that exact Boolean
cancellation is locally compatible with such reconvergence. Neither fact is
a plateau counterexample.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT plateau endpoint and its satisfying restriction minors |
| Uniform/non-uniform | Every finite non-uniform hypothetical endpoint parent; local witness remains nonminimal |
| Circuit size | Parent `K+2`; exactly two binary losses in every satisfying minor |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Cycle-space quotient maps over `F_2` |
| Asymptotic quantifiers | Every counterflow boundary and every satisfying code in `{00,01,11}` |
| Regime | Cycle-existence-only no-go; not a counterexample, SAT lower bound, or terminal result |

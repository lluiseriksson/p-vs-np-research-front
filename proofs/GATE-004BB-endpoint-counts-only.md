# GATE-004BB-ENDPOINT-COUNTS-ONLY — infer localization from rank and NOT counts alone

**Label: NO-GO**

LEMMA-155 yields three endpoint facts: cycle rank zero, exactly `m` NOT
gates, and survival of all `m` NOT gates under every satisfying base
restriction. Those facts alone do not imply survival after setting an
unrelated clause signal to one.

For an explicit witness to the missing semantic information, let `x` be a
base bit and let `q_1,...,q_m` be abstract clause signals. The formula

`F(x,q)=x AND AND_{i=1}^m NOT q_i`

has cycle rank zero and exactly `m` displayed NOT gates. All `m` survive the
base restriction `x=1`. Yet fixing any single `q_j=1` makes the output
constant zero, so constant propagation removes every other displayed NOT as
well. Thus the tuple

`(rank zero, m NOTs, full survival under a base restriction)`

does not encode the polarity or restriction behavior needed for prefix
localization.

This witness is deliberately not `J_m` and is not claimed to be a minimum
formula for its function. It therefore does not refute GATE-004BB. It closes
only an argument that discards the target function and minimum-circuit
equality after invoking LEMMA-155. A successful proof must use the exact
one-negative implication clauses together with minimality or an equality-case
exchange theorem.

## Model card

| Field | Value |
|---|---|
| Computational model | Explicit fanout-one AND/OR/NOT formulas under base and clause-signal restrictions |
| Uniform/non-uniform | Explicit non-uniform witness family; no minimum-circuit or canonical-function claim |
| Circuit size | Exactly `m` displayed NOT gates and cycle rank zero; no minimum-size assertion |
| Circuit depth | Unrestricted binary conjunction-tree depth |
| Fan-in | AND two; NOT one; formula fanout one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean restriction semantics only |
| Asymptotic quantifiers | Every `m>=1` |
| Regime | Structural no-go for endpoint-count-only inference; GATE-004BB/BA/AZ/AY/AX/AW/AV/AU/AG/AE remain open |
